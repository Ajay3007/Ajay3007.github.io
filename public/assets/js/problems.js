// assets/js/problems.js
document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("problems-tbody");
    if (!tableBody || !window.dsaProblems) return;

    const searchInput  = document.getElementById("filter-search");
    const diffFilter   = document.getElementById("filter-difficulty");
    const topicFilter  = document.getElementById("filter-topic");
    const statusFilter = document.getElementById("filter-status");
    const topicBanner  = document.getElementById("topic-page-banner");
    const paginationEl = document.getElementById("pagination-controls");
    const progressBar  = document.getElementById("my-progress-bar");

    const problems  = window.dsaProblems;
    const PAGE_SIZE = 25;
    let   currentPage = 1;

    // ── localStorage helpers ─────────────────────────────────────────────────
    const LS_KEY = "dsa_my_solved";

    function getMySolved() {
        try {
            return new Set(JSON.parse(localStorage.getItem(LS_KEY) || "[]"));
        } catch { return new Set(); }
    }

    function setMySolved(set) {
        try {
            localStorage.setItem(LS_KEY, JSON.stringify([...set]));
        } catch { /* localStorage unavailable */ }
    }

    function toggleMySolved(id) {
        const solved = getMySolved();
        if (solved.has(id)) solved.delete(id);
        else                 solved.add(id);
        setMySolved(solved);
        return solved.has(id);
    }

    // ── Personal progress bar ─────────────────────────────────────────────────
    function updateProgressBar() {
        if (!progressBar) return;
        const solved  = getMySolved();
        const count   = solved.size;
        const total   = problems.length;
        const pct     = total > 0 ? Math.round((count / total) * 100) : 0;
        const easy    = problems.filter(p => p.difficulty === "easy"   && solved.has(String(p.id))).length;
        const medium  = problems.filter(p => p.difficulty === "medium" && solved.has(String(p.id))).length;
        const hard    = problems.filter(p => p.difficulty === "hard"   && solved.has(String(p.id))).length;

        progressBar.innerHTML = `
            <div class="my-progress-header">
                <span class="my-progress-label">🏆 My Progress</span>
                <span class="my-progress-count"><strong>${count}</strong> / ${total} solved &nbsp;·&nbsp; ${pct}%</span>
                <button id="reset-progress-btn" title="Reset all my progress" class="my-progress-reset">↺ Reset</button>
            </div>
            <div class="my-progress-track">
                <div class="my-progress-fill" style="width:${pct}%"></div>
            </div>
            <div class="my-progress-breakdown">
                <span class="my-pb-easy">🟢 ${easy} Easy</span>
                <span class="my-pb-medium">🟡 ${medium} Medium</span>
                <span class="my-pb-hard">🔴 ${hard} Hard</span>
            </div>
        `;

        document.getElementById("reset-progress-btn")?.addEventListener("click", () => {
            if (confirm(`Reset all your personal progress? (${count} solved problems will be cleared)`)) {
                setMySolved(new Set());
                updateProgressBar();
                renderTable();
            }
        });
    }

    // ── Map of topic slugs → dedicated learning pages ────────────────────────
    const topicPages = {
        'arrays':              '/learning/dsa/arrays/arrays-problems/',
        'strings':             '/learning/dsa/strings/strings-problems/',
        'linked-list':         '/learning/dsa/linked-list/linked-list-problems/',
        'tree':                '/learning/dsa/tree/tree-problems/',
        'stacks':              '/learning/dsa/stacks/stacks-problems/',
        'searching-sorting':   '/learning/dsa/searching-sorting/searching-sorting-problems/',
        'graphs':              '/learning/dsa/graphs/graphs-problems/',
        'recursion':           '/learning/dsa/recursion/recursion-problems/',
        'binary-search':       '/learning/dsa/binary-search/binary-search-problems/',
        'backtracking':        '/learning/dsa/backtracking/backtracking-problems/',
        'dynamic-programming': '/learning/dsa/dynamic-programming/dynamic-programming-problems/',
        'queues':              '/learning/dsa/queues/queues-problems/',
        'hashing':             '/learning/dsa/hashing/hashing-problems/',
        'heaps':               '/learning/dsa/heaps/heaps-problems/',
        'greedy':              '/learning/dsa/greedy/greedy-problems/',
        'bit-manipulation':    '/learning/dsa/bit-manipulation/bit-manipulation-problems/',
        'intervals':           '/learning/dsa/intervals/intervals-problems/',
    };

    // ── Auto-populate Topics dropdown ─────────────────────────────────────────
    if (topicFilter && problems) {
        const uniqueTopics = new Set();
        problems.forEach(p => {
            if (p.topics && Array.isArray(p.topics)) p.topics.forEach(t => uniqueTopics.add(t));
        });
        Array.from(uniqueTopics).sort().forEach(topicStr => {
            const option = document.createElement("option");
            option.value = topicStr;
            option.textContent = topicStr.split('-')
                .map(w => w.charAt(0).toUpperCase() + w.slice(1))
                .join(' ');
            topicFilter.appendChild(option);
        });
    }

    // ── Topic-page banner ─────────────────────────────────────────────────────
    function updateTopicBanner(selectedTopic) {
        if (!topicBanner) return;
        const pageUrl = topicPages[selectedTopic];
        if (selectedTopic !== "all" && pageUrl) {
            const prettyName = selectedTopic.split('-')
                .map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            topicBanner.style.display = "block";
            topicBanner.innerHTML = `📚 Viewing <strong>${prettyName}</strong> problems &mdash; <a href="${pageUrl}">Open dedicated ${prettyName} page →</a>`;
        } else {
            topicBanner.style.display = "none";
            topicBanner.innerHTML = "";
        }
    }

    // ── Filter helper ─────────────────────────────────────────────────────────
    function getFiltered() {
        const query       = searchInput.value.toLowerCase();
        const diff        = diffFilter.value;
        const targetTopic = topicFilter.value;
        const status      = statusFilter.value;
        const mySolved    = getMySolved();

        return problems.filter(p => {
            const matchSearch = p.title.toLowerCase().includes(query) ||
                                (p.id || "").toString().includes(query);
            const matchDiff   = diff === "all" || p.difficulty === diff;
            const matchTopic  = targetTopic === "all" ||
                                (p.topics && p.topics.includes(targetTopic));
            let   matchStatus = true;
            const isMySolved  = mySolved.has(String(p.id));
            if (status === "solved")    matchStatus = p.solved === true;
            if (status === "todo")      matchStatus = p.solved !== true;
            if (status === "my-solved") matchStatus = isMySolved;
            if (status === "my-todo")   matchStatus = !isMySolved;
            return matchSearch && matchDiff && matchTopic && matchStatus;
        });
    }

    // ── Row builder ───────────────────────────────────────────────────────────
    function buildRow(p) {
        const tr = document.createElement("tr");
        tr.className = "problem-row";
        tr.dataset.problemId = p.id;

        const mySolved   = getMySolved();
        const isPersonal = mySolved.has(String(p.id));

        // Personal checkbox
        const checkHtml = `
            <label class="my-check-wrap" title="${isPersonal ? 'Mark as unsolved' : 'Mark as solved'}">
                <input type="checkbox" class="my-solved-cb" data-id="${p.id}" ${isPersonal ? 'checked' : ''}>
                <span class="my-check-box ${isPersonal ? 'checked' : ''}"></span>
            </label>`;

        // Author solved badge (from YAML)
        const authorBadge = p.solved
            ? `<span class="author-badge solved" title="Editorial solved">✅</span>`
            : `<span class="author-badge unsolved" title="Not solved in editorial">⭕️</span>`;

        const statusHtml = `<div class="status-cell">${checkHtml}${authorBadge}</div>`;

        // Title
        const titleHtml = p.problem_url
            ? `<a href="${p.problem_url}" target="_blank" rel="noopener noreferrer" class="problem-link">${p.id}. ${p.title}</a>`
            : `<span class="problem-link-plain">${p.id}. ${p.title}</span>`;

        // Difficulty badge
        let diffClass = "diff-badge";
        if (p.difficulty === "easy")   diffClass += " diff-easy";
        if (p.difficulty === "medium") diffClass += " diff-medium";
        if (p.difficulty === "hard")   diffClass += " diff-hard";
        const diffHtml = `<span class="${diffClass}">${p.difficulty}</span>`;

        // Topic tags
        let topicsHtml = "";
        if (p.topics && p.topics.length > 0) {
            topicsHtml = p.topics.map(t => {
                const pretty = t.replace(/-/g, ' ');
                const dest   = topicPages[t];
                if (dest) {
                    return `<a href="${dest}" class="topic-tag topic-tag-link" title="View ${pretty} page">${pretty}</a>`;
                }
                return `<button onclick="(function(){var s=document.getElementById('filter-topic');if(s){s.value='${t}';s.dispatchEvent(new Event('change'));}})();return false;" class="topic-tag">${pretty}</button>`;
            }).join("");
        }

        // Action buttons
        let actionsHtml = `<div class="action-btns">`;
        if (p.approach_url) {
            let text = "📖 Editorial", cls = "action-btn editorial";
            if (p.approach_url.endsWith('.pdf'))              { text = "📝 PDF Notes"; cls = "action-btn pdf"; }
            else if (p.approach_url.includes('leetcode.com')) { text = "🔗 Approach";  cls = "action-btn approach"; }
            actionsHtml += `<a href="${p.approach_url}" target="_blank" rel="noopener noreferrer" class="${cls}">${text}</a>`;
        }
        if (p.solution_url) {
            let text = "💻 Code", cls = "action-btn code";
            if (p.solution_url.match(/\.(cpp|c|java|py|js)$/i))  text = "💻 Raw Code";
            else if (p.solution_url.includes('leetcode.com'))      { text = "🔗 Solution"; cls = "action-btn solution"; }
            actionsHtml += `<a href="${p.solution_url}" target="_blank" rel="noopener noreferrer" class="${cls}">${text}</a>`;
        }
        if (!p.solution_url && !p.approach_url) {
            actionsHtml += `<span class="no-notes">No notes yet</span>`;
        }
        actionsHtml += `</div>`;

        if (isPersonal) tr.classList.add("my-solved-row");

        tr.innerHTML = `
            <td class="td-status">${statusHtml}</td>
            <td class="td-title">${titleHtml}</td>
            <td class="td-diff">${diffHtml}</td>
            <td class="td-topics">${topicsHtml}</td>
            <td class="td-actions">${actionsHtml}</td>
        `;

        // Checkbox event
        tr.querySelector(".my-solved-cb").addEventListener("change", (e) => {
            const nowSolved = toggleMySolved(String(p.id));
            const box  = e.target.nextElementSibling;
            const wrap = e.target.closest("label");
            box.classList.toggle("checked", nowSolved);
            wrap.title = nowSolved ? "Mark as unsolved" : "Mark as solved";
            tr.classList.toggle("my-solved-row", nowSolved);
            updateProgressBar();
            // If filtering by my-solved/my-todo, re-render so row disappears/appears correctly
            const sv = statusFilter.value;
            if (sv === "my-solved" || sv === "my-todo") { currentPage = 1; renderTable(); }
        });

        return tr;
    }

    // ── Pagination controls renderer ──────────────────────────────────────────
    function renderPagination(total) {
        if (!paginationEl) return;
        const totalPages = Math.ceil(total / PAGE_SIZE);

        if (totalPages <= 1) { paginationEl.innerHTML = ""; return; }

        const start = (currentPage - 1) * PAGE_SIZE + 1;
        const end   = Math.min(currentPage * PAGE_SIZE, total);

        paginationEl.innerHTML = `
            <div class="pagination-row">
                <button id="pg-prev" class="pg-btn" ${currentPage === 1 ? 'disabled' : ''}>← Prev</button>
                <span class="pg-info">
                    Page <strong>${currentPage}</strong> of <strong>${totalPages}</strong>
                    <span class="pg-range">(${start}–${end} of ${total})</span>
                </span>
                <button id="pg-next" class="pg-btn" ${currentPage === totalPages ? 'disabled' : ''}>Next →</button>
            </div>
        `;
        document.getElementById("pg-prev").addEventListener("click", () => {
            if (currentPage > 1) { currentPage--; renderTable(); }
        });
        document.getElementById("pg-next").addEventListener("click", () => {
            if (currentPage < totalPages) { currentPage++; renderTable(); }
        });
    }

    // ── Main render ───────────────────────────────────────────────────────────
    function renderTable() {
        const filtered = getFiltered();
        updateTopicBanner(topicFilter.value);
        tableBody.innerHTML = "";

        if (filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:2rem;color:var(--light-text);">No problems found matching your criteria. Keep grinding! ☕️</td></tr>`;
            renderPagination(0);
            return;
        }

        const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
        if (currentPage > totalPages) currentPage = totalPages;

        const pageStart = (currentPage - 1) * PAGE_SIZE;
        const pageItems = filtered.slice(pageStart, pageStart + PAGE_SIZE);
        pageItems.forEach(p => tableBody.appendChild(buildRow(p)));
        renderPagination(filtered.length);
    }

    // ── Filter listeners (reset to page 1) ────────────────────────────────────
    [searchInput, diffFilter, topicFilter, statusFilter].forEach(el => {
        el.addEventListener("input",  () => { currentPage = 1; renderTable(); });
        el.addEventListener("change", () => { currentPage = 1; renderTable(); });
    });

    // ── Inject component styles ───────────────────────────────────────────────
    const style = document.createElement("style");
    style.textContent = `
        /* ── Row states ── */
        .problem-row { border-bottom: 1px solid var(--border-color); transition: background 0.15s; }
        .problem-row:hover { background-color: var(--bg-secondary) !important; }
        .my-solved-row { background: rgba(16,185,129,0.05) !important; }
        .my-solved-row:hover { background: rgba(16,185,129,0.10) !important; }

        /* ── Table cells ── */
        .td-status  { padding: 0.9rem 1rem; text-align: center; white-space: nowrap; }
        .td-title   { padding: 0.9rem 1rem; }
        .td-diff    { padding: 0.9rem 1rem; }
        .td-topics  { padding: 0.9rem 1rem; }
        .td-actions { padding: 0.9rem 1rem; }

        /* ── Status cell ── */
        .status-cell { display: flex; flex-direction: column; align-items: center; gap: 0.3rem; }
        .author-badge { font-size: 1.1rem; }

        /* ── Personal checkbox ── */
        .my-check-wrap { display: flex; align-items: center; justify-content: center; cursor: pointer; }
        .my-check-wrap input[type="checkbox"] { display: none; }
        .my-check-box {
            width: 20px; height: 20px; border-radius: 5px;
            border: 2px solid var(--border-color);
            background: var(--bg-color);
            display: flex; align-items: center; justify-content: center;
            transition: all 0.2s; flex-shrink: 0;
        }
        .my-check-box.checked {
            background: #10b981; border-color: #10b981;
        }
        .my-check-box.checked::after { content: "✓"; color: #fff; font-size: 13px; font-weight: 800; line-height: 1; }
        .my-check-wrap:hover .my-check-box:not(.checked) { border-color: #10b981; background: rgba(16,185,129,0.1); }

        /* ── Links & badges ── */
        .problem-link { color: var(--text-color); font-weight: 600; text-decoration: none; }
        .problem-link:hover { color: #3b82f6; }
        .problem-link-plain { font-weight: 600; color: var(--text-color); }
        .diff-badge { display: inline-block; padding: 0.22rem 0.55rem; border-radius: 4px; font-size: 0.8rem; font-weight: 700; text-transform: capitalize; }
        .diff-easy   { color: #10b981; background: #dcfce7; }
        .diff-medium { color: #f59e0b; background: #fef3c7; }
        .diff-hard   { color: #ef4444; background: #fee2e2; }

        /* ── Topic tags ── */
        .topic-tag {
            display: inline-block; padding: 0.15rem 0.4rem; border-radius: 4px;
            font-size: 0.75rem; font-weight: 600; white-space: nowrap;
            margin-right: 0.25rem; margin-bottom: 0.25rem;
            background: rgba(102,126,234,0.08); border: 1px solid rgba(102,126,234,0.25);
            color: #667eea; cursor: pointer; transition: background 0.15s;
            text-decoration: none;
        }
        .topic-tag:hover { background: rgba(102,126,234,0.18); }
        .topic-tag-link { /* inherits topic-tag */ }

        /* ── Action buttons ── */
        .action-btns { display: flex; gap: 0.5rem; flex-wrap: wrap; }
        .action-btn {
            padding: 0.28rem 0.6rem; border-radius: 4px; text-decoration: none;
            font-size: 0.83rem; white-space: nowrap; transition: opacity 0.15s; font-weight: 500;
        }
        .action-btn:hover { opacity: 0.8; }
        .action-btn.editorial { background: rgba(59,130,246,0.1);  color: #3b82f6; }
        .action-btn.pdf       { background: rgba(139,92,246,0.1);  color: #8b5cf6; }
        .action-btn.approach  { background: rgba(99,102,241,0.1);  color: #6366f1; }
        .action-btn.code      { background: rgba(16,185,129,0.1);  color: #10b981; }
        .action-btn.solution  { background: rgba(5,150,105,0.1);   color: #059669; }
        .no-notes { font-size: 0.85rem; color: var(--light-text); font-style: italic; }

        /* ── Progress bar widget ── */
        .my-progress-header {
            display: flex; align-items: center; gap: 0.75rem;
            margin-bottom: 0.5rem; flex-wrap: wrap;
        }
        .my-progress-label { font-weight: 700; font-size: 0.95rem; color: var(--text-color); }
        .my-progress-count { font-size: 0.92rem; color: var(--light-text); margin-left: auto; }
        .my-progress-reset {
            padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.8rem; cursor: pointer;
            border: 1px solid var(--border-color); background: var(--bg-color);
            color: var(--light-text); transition: color 0.2s, border-color 0.2s;
        }
        .my-progress-reset:hover { color: #ef4444; border-color: #ef4444; }
        .my-progress-track {
            height: 10px; border-radius: 10px; background: var(--bg-secondary);
            overflow: hidden; margin-bottom: 0.45rem;
        }
        .my-progress-fill {
            height: 100%; border-radius: 10px;
            background: linear-gradient(90deg, #10b981, #3b82f6);
            transition: width 0.4s ease;
            min-width: ${0}%;
        }
        .my-progress-breakdown { font-size: 0.82rem; display: flex; gap: 1rem; color: var(--light-text); }
        .my-pb-easy   { color: #10b981; }
        .my-pb-medium { color: #f59e0b; }
        .my-pb-hard   { color: #ef4444; }

        /* ── Pagination ── */
        .pagination-row {
            display: flex; align-items: center; justify-content: center;
            gap: 1rem; margin-top: 1.25rem; flex-wrap: wrap;
        }
        .pg-btn {
            padding: 0.45rem 1.1rem; border-radius: 6px;
            border: 1px solid var(--border-color); background: var(--card-bg);
            color: var(--text-color); font-size: 0.9rem; font-weight: 600;
            cursor: pointer; transition: background 0.2s, color 0.2s, border-color 0.2s;
        }
        .pg-btn:hover:not(:disabled) { background: var(--secondary-color); color: #fff; border-color: var(--secondary-color); }
        .pg-btn:disabled { opacity: 0.38; cursor: default; }
        .pg-info  { font-size: 0.92rem; color: var(--text-color); }
        .pg-range { margin-left: 0.4rem; color: var(--light-text); font-size: 0.85rem; }

        @media (max-width: 768px) {
            #problems-table th, #problems-table td { padding: 0.75rem 0.5rem !important; font-size: 0.9rem; }
            .hide-mobile { display: none !important; }
        }

        /* ── Print: hide interactive elements in problems table ── */
        @media print {
            .my-check-wrap, .my-progress-reset, .action-btn, #pagination-controls,
            .filters-bar, .topic-chips, #topic-page-banner, #my-progress-bar { display: none !important; }
            .my-progress-count { margin-left: 0; }
        }
    `;
    document.head.appendChild(style);

    // ── Init ──────────────────────────────────────────────────────────────────
    updateProgressBar();
    renderTable();
});
