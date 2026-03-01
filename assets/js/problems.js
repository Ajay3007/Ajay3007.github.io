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

    const problems  = window.dsaProblems;
    const PAGE_SIZE = 25;
    let   currentPage = 1;

    // Map of topic slugs that have dedicated learning pages
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

    // ── Auto-populate Topics dropdown ────────────────────────────────────────
    if (topicFilter && problems) {
        const uniqueTopics = new Set();
        problems.forEach(p => {
            if (p.topics && Array.isArray(p.topics)) {
                p.topics.forEach(t => uniqueTopics.add(t));
            }
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

    // ── Topic-page banner ────────────────────────────────────────────────────
    function updateTopicBanner(selectedTopic) {
        if (!topicBanner) return;
        const pageUrl = topicPages[selectedTopic];
        if (selectedTopic !== "all" && pageUrl) {
            const prettyName = selectedTopic.split('-')
                .map(w => w.charAt(0).toUpperCase() + w.slice(1))
                .join(' ');
            topicBanner.style.display = "block";
            topicBanner.innerHTML = `📚 Viewing <strong>${prettyName}</strong> problems &mdash; <a href="${pageUrl}">Open dedicated ${prettyName} page →</a>`;
        } else {
            topicBanner.style.display = "none";
            topicBanner.innerHTML = "";
        }
    }

    // ── Filter helper ────────────────────────────────────────────────────────
    function getFiltered() {
        const query       = searchInput.value.toLowerCase();
        const diff        = diffFilter.value;
        const targetTopic = topicFilter.value;
        const status      = statusFilter.value;

        return problems.filter(p => {
            const matchSearch = p.title.toLowerCase().includes(query) ||
                                (p.id || "").toString().includes(query);
            const matchDiff   = diff === "all" || p.difficulty === diff;
            const matchTopic  = targetTopic === "all" ||
                                (p.topics && p.topics.includes(targetTopic));
            let   matchStatus = true;
            if (status === "solved") matchStatus = p.solved === true;
            if (status === "todo")   matchStatus = p.solved !== true;
            return matchSearch && matchDiff && matchTopic && matchStatus;
        });
    }

    // ── Row builder ──────────────────────────────────────────────────────────
    function buildRow(p) {
        const tr = document.createElement("tr");
        tr.className = "problem-row";
        tr.style.borderBottom  = "1px solid var(--border-color)";
        tr.style.transition    = "background 0.2s";

        // Status
        const statusHtml = p.solved
            ? `<span title="Solved" style="color:#10b981;font-weight:bold;">✅</span>`
            : `<span title="Unsolved" style="color:#64748b;font-size:1.2rem;">⭕️</span>`;

        // Title
        const titleHtml = p.problem_url
            ? `<a href="${p.problem_url}" target="_blank" rel="noopener noreferrer" style="color:var(--text-color);font-weight:600;text-decoration:none;" class="problem-link">${p.id}. ${p.title}</a>`
            : `<span style="font-weight:600;color:var(--text-color);">${p.id}. ${p.title}</span>`;

        // Difficulty badge
        let diffColor = "#64748b", diffBg = "#f1f5f9";
        if (p.difficulty === "easy")   { diffColor = "#10b981"; diffBg = "#dcfce7"; }
        if (p.difficulty === "medium") { diffColor = "#f59e0b"; diffBg = "#fef3c7"; }
        if (p.difficulty === "hard")   { diffColor = "#ef4444"; diffBg = "#fee2e2"; }
        const diffHtml = `<span style="display:inline-block;padding:0.25rem 0.5rem;border-radius:4px;font-size:0.8rem;font-weight:600;color:${diffColor};background:${diffBg};text-transform:capitalize;">${p.difficulty}</span>`;

        // Topic tags
        let topicsHtml = "";
        if (p.topics && p.topics.length > 0) {
            topicsHtml = p.topics.map(t => {
                const pretty = t.replace(/-/g, ' ');
                const dest   = topicPages[t];
                if (dest) {
                    return `<a href="${dest}" title="View ${pretty} problems page" style="display:inline-block;padding:0.15rem 0.4rem;border-radius:4px;font-size:0.75rem;background:rgba(102,126,234,0.08);border:1px solid rgba(102,126,234,0.25);color:#667eea;margin-right:0.25rem;margin-bottom:0.25rem;white-space:nowrap;text-decoration:none;font-weight:600;" onmouseover="this.style.background='rgba(102,126,234,0.18)'" onmouseout="this.style.background='rgba(102,126,234,0.08)'">${pretty}</a>`;
                }
                return `<button onclick="(function(){var s=document.getElementById('filter-topic');if(s){s.value='${t}';s.dispatchEvent(new Event('change'));}})();return false;" title="Filter by ${pretty}" style="display:inline-block;padding:0.15rem 0.4rem;border-radius:4px;font-size:0.75rem;background:var(--bg-secondary);border:1px solid var(--border-color);color:var(--light-text);margin-right:0.25rem;margin-bottom:0.25rem;white-space:nowrap;cursor:pointer;">${pretty}</button>`;
            }).join("");
        }

        // Action buttons
        let actionsHtml = `<div style="display:flex;gap:0.5rem;flex-wrap:wrap;">`;
        if (p.approach_url) {
            let text = "📖 Editorial", color = "#3b82f6", bg = "rgba(59,130,246,0.1)";
            if (p.approach_url.endsWith('.pdf'))             { text = "📝 PDF Notes"; color = "#8b5cf6"; bg = "rgba(139,92,246,0.1)"; }
            else if (p.approach_url.includes('leetcode.com')){ text = "🔗 Approach";  color = "#6366f1"; bg = "rgba(99,102,241,0.1)"; }
            actionsHtml += `<a href="${p.approach_url}" target="_blank" rel="noopener noreferrer" style="background:${bg};color:${color};padding:0.3rem 0.6rem;border-radius:4px;text-decoration:none;font-size:0.85rem;transition:background 0.2s;white-space:nowrap;">${text}</a>`;
        }
        if (p.solution_url) {
            let text = "💻 Code", color = "#10b981", bg = "rgba(16,185,129,0.1)";
            if (p.solution_url.match(/\.(cpp|c|java|py|js)$/i))  { text = "💻 Raw Code"; }
            else if (p.solution_url.includes('leetcode.com'))     { text = "🔗 Solution"; color = "#059669"; bg = "rgba(5,150,105,0.1)"; }
            actionsHtml += `<a href="${p.solution_url}" target="_blank" rel="noopener noreferrer" style="background:${bg};color:${color};padding:0.3rem 0.6rem;border-radius:4px;text-decoration:none;font-size:0.85rem;transition:background 0.2s;white-space:nowrap;">${text}</a>`;
        }
        if (!p.solution_url && !p.approach_url) {
            actionsHtml += `<span style="font-size:0.85rem;color:var(--light-text);font-style:italic;">No notes yet</span>`;
        }
        actionsHtml += `</div>`;

        tr.innerHTML = `
            <td style="padding:1rem;text-align:center;">${statusHtml}</td>
            <td style="padding:1rem;">${titleHtml}</td>
            <td style="padding:1rem;">${diffHtml}</td>
            <td style="padding:1rem;">${topicsHtml}</td>
            <td style="padding:1rem;">${actionsHtml}</td>
        `;
        return tr;
    }

    // ── Pagination controls renderer ─────────────────────────────────────────
    function renderPagination(total) {
        if (!paginationEl) return;
        const totalPages = Math.ceil(total / PAGE_SIZE);

        if (totalPages <= 1) {
            paginationEl.innerHTML = "";
            return;
        }

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

    // ── Main render ──────────────────────────────────────────────────────────
    function renderTable() {
        const filtered = getFiltered();
        updateTopicBanner(topicFilter.value);

        tableBody.innerHTML = "";

        if (filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:2rem;color:var(--light-text);">No problems found matching your criteria. Keep grinding! ☕️</td></tr>`;
            renderPagination(0);
            return;
        }

        // Slice to current page window
        const totalPages  = Math.ceil(filtered.length / PAGE_SIZE);
        if (currentPage > totalPages) currentPage = totalPages;

        const pageStart = (currentPage - 1) * PAGE_SIZE;
        const pageEnd   = pageStart + PAGE_SIZE;
        const pageItems = filtered.slice(pageStart, pageEnd);

        pageItems.forEach(p => tableBody.appendChild(buildRow(p)));
        renderPagination(filtered.length);
    }

    // ── Filter listeners (reset to page 1) ───────────────────────────────────
    [searchInput, diffFilter, topicFilter, statusFilter].forEach(el => {
        el.addEventListener("input",  () => { currentPage = 1; renderTable(); });
        el.addEventListener("change", () => { currentPage = 1; renderTable(); });
    });

    // ── Styles ───────────────────────────────────────────────────────────────
    const style = document.createElement("style");
    style.textContent = `
        .problem-row:hover { background-color: var(--bg-secondary) !important; }
        .problem-link:hover { color: #3b82f6 !important; }

        /* Pagination */
        .pagination-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-top: 1.25rem;
            flex-wrap: wrap;
        }
        .pg-btn {
            padding: 0.45rem 1.1rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: var(--card-bg);
            color: var(--text-color);
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s, color 0.2s, border-color 0.2s;
        }
        .pg-btn:hover:not(:disabled) {
            background: var(--secondary-color);
            color: #fff;
            border-color: var(--secondary-color);
        }
        .pg-btn:disabled {
            opacity: 0.38;
            cursor: default;
        }
        .pg-info {
            font-size: 0.92rem;
            color: var(--text-color);
        }
        .pg-range {
            margin-left: 0.4rem;
            color: var(--light-text);
            font-size: 0.85rem;
        }

        @media (max-width: 768px) {
            #problems-table th, #problems-table td { padding: 0.75rem 0.5rem !important; font-size: 0.9rem; }
            .hide-mobile { display: none !important; }
        }
    `;
    document.head.appendChild(style);

    // Initial render
    renderTable();
});
