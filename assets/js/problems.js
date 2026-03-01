// assets/js/problems.js
document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("problems-tbody");
    if (!tableBody || !window.dsaProblems) return;

    const searchInput = document.getElementById("filter-search");
    const diffFilter = document.getElementById("filter-difficulty");
    const topicFilter = document.getElementById("filter-topic");
    const statusFilter = document.getElementById("filter-status");
    const topicBanner = document.getElementById("topic-page-banner");

    const problems = window.dsaProblems;

    // Map of topic slugs that have dedicated learning pages
    const topicPages = {
        'arrays':            '/learning/dsa/arrays/arrays-problems/',
        'strings':           '/learning/dsa/strings/strings-problems/',
        'linked-list':       '/learning/dsa/linked-list/linked-list-problems/',
        'tree':              '/learning/dsa/tree/tree-problems/',
        'stacks':            '/learning/dsa/stacks/stacks-problems/',
        'searching-sorting': '/learning/dsa/searching-sorting/searching-sorting-problems/',
        'graphs':            '/learning/dsa/graphs/graphs-problems/',
        'recursion':         '/learning/dsa/recursion/recursion-problems/',
        'binary-search':     '/learning/dsa/binary-search/binary-search-problems/',
    };

    // Dynamically auto-populate the Topics dropdown from the dataset
    if (topicFilter && problems) {
        const uniqueTopics = new Set();
        problems.forEach(p => {
            if (p.topics && Array.isArray(p.topics)) {
                p.topics.forEach(t => uniqueTopics.add(t));
            }
        });

        const sortedTopics = Array.from(uniqueTopics).sort();
        sortedTopics.forEach(topicStr => {
            const option = document.createElement("option");
            option.value = topicStr;
            const prettyLabel = topicStr.split('-')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                .join(' ');
            option.textContent = prettyLabel;
            topicFilter.appendChild(option);
        });
    }

    // Update topic-page banner when a topic filter is selected
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

    function renderTable() {
        const query = searchInput.value.toLowerCase();
        const diff = diffFilter.value;
        const targetTopic = topicFilter.value;
        const status = statusFilter.value;

        updateTopicBanner(targetTopic);

        const filtered = problems.filter(p => {
            const matchSearch = p.title.toLowerCase().includes(query) || (p.id || "").toString().includes(query);
            const matchDiff = diff === "all" || p.difficulty === diff;
            const matchTopic = targetTopic === "all" || (p.topics && p.topics.includes(targetTopic));

            let matchStatus = true;
            if (status === "solved") matchStatus = p.solved === true;
            if (status === "todo") matchStatus = p.solved !== true;

            return matchSearch && matchDiff && matchTopic && matchStatus;
        });

        tableBody.innerHTML = "";

        if (filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" style="text-align: center; padding: 2rem; color: var(--light-text);">No problems found matching your criteria. Keep grinding! ☕️</td></tr>`;
            return;
        }

        filtered.forEach(p => {
            const tr = document.createElement("tr");
            tr.className = "problem-row";
            tr.style.borderBottom = "1px solid var(--border-color)";
            tr.style.transition = "background 0.2s";

            // Status Icon
            const statusHtml = p.solved
                ? `<span title="Solved" style="color: #10b981; font-weight: bold;">✅</span>`
                : `<span title="Unsolved" style="color: #64748b; font-size: 1.2rem;">⭕️</span>`;

            // Title Link
            const titleHtml = p.problem_url
                ? `<a href="${p.problem_url}" target="_blank" rel="noopener noreferrer" style="color: var(--text-color); font-weight: 600; text-decoration: none;" class="problem-link">${p.id}. ${p.title}</a>`
                : `<span style="font-weight: 600; color: var(--text-color);">${p.id}. ${p.title}</span>`;

            // Difficulty Badge
            let diffColor = "#64748b", diffBg = "#f1f5f9";
            if (p.difficulty === "easy")   { diffColor = "#10b981"; diffBg = "#dcfce7"; }
            if (p.difficulty === "medium") { diffColor = "#f59e0b"; diffBg = "#fef3c7"; }
            if (p.difficulty === "hard")   { diffColor = "#ef4444"; diffBg = "#fee2e2"; }
            const diffHtml = `<span style="display:inline-block;padding:0.25rem 0.5rem;border-radius:4px;font-size:0.8rem;font-weight:600;color:${diffColor};background:${diffBg};text-transform:capitalize;">${p.difficulty}</span>`;

            // Topic tags — clickable: dedicated page if one exists, else filter in hub
            let topicsHtml = "";
            if (p.topics && p.topics.length > 0) {
                topicsHtml = p.topics.map(t => {
                    const pretty = t.replace(/-/g, ' ');
                    const dest = topicPages[t];
                    if (dest) {
                        return `<a href="${dest}" title="View ${pretty} problems page" style="display:inline-block;padding:0.15rem 0.4rem;border-radius:4px;font-size:0.75rem;background:rgba(102,126,234,0.08);border:1px solid rgba(102,126,234,0.25);color:#667eea;margin-right:0.25rem;margin-bottom:0.25rem;white-space:nowrap;text-decoration:none;font-weight:600;" onmouseover="this.style.background='rgba(102,126,234,0.18)'" onmouseout="this.style.background='rgba(102,126,234,0.08)'">${pretty}</a>`;
                    }
                    // No dedicated page — clicking filters the table by this topic
                    return `<button onclick="(function(){var s=document.getElementById('filter-topic');if(s){s.value='${t}';s.dispatchEvent(new Event('change'));}})();return false;" title="Filter by ${pretty}" style="display:inline-block;padding:0.15rem 0.4rem;border-radius:4px;font-size:0.75rem;background:var(--bg-secondary);border:1px solid var(--border-color);color:var(--light-text);margin-right:0.25rem;margin-bottom:0.25rem;white-space:nowrap;cursor:pointer;">${pretty}</button>`;
                }).join("");
            }

            // Action Buttons
            let actionsHtml = `<div style="display:flex;gap:0.5rem;flex-wrap:wrap;">`;
            if (p.approach_url) {
                let text = "📖 Editorial", color = "#3b82f6", bg = "rgba(59,130,246,0.1)";
                if (p.approach_url.endsWith('.pdf'))            { text = "📝 PDF Notes"; color = "#8b5cf6"; bg = "rgba(139,92,246,0.1)"; }
                else if (p.approach_url.includes('leetcode.com')) { text = "🔗 Approach";  color = "#6366f1"; bg = "rgba(99,102,241,0.1)"; }
                actionsHtml += `<a href="${p.approach_url}" target="_blank" rel="noopener noreferrer" style="background:${bg};color:${color};padding:0.3rem 0.6rem;border-radius:4px;text-decoration:none;font-size:0.85rem;transition:background 0.2s;white-space:nowrap;">${text}</a>`;
            }
            if (p.solution_url) {
                let text = "💻 Code", color = "#10b981", bg = "rgba(16,185,129,0.1)";
                if (p.solution_url.match(/\.(cpp|c|java|py|js)$/i)) { text = "💻 Raw Code"; }
                else if (p.solution_url.includes('leetcode.com'))    { text = "🔗 Solution"; color = "#059669"; bg = "rgba(5,150,105,0.1)"; }
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
            tableBody.appendChild(tr);
        });
    }

    [searchInput, diffFilter, topicFilter, statusFilter].forEach(el => {
        el.addEventListener("input", renderTable);
        el.addEventListener("change", renderTable);
    });

    const style = document.createElement("style");
    style.textContent = `
        .problem-row:hover { background-color: var(--bg-secondary) !important; }
        .problem-link:hover { color: #3b82f6 !important; }
        @media (max-width: 768px) {
            #problems-table th, #problems-table td { padding: 0.75rem 0.5rem !important; font-size: 0.9rem; }
            .hide-mobile { display: none !important; }
        }
    `;
    document.head.appendChild(style);

    renderTable();
});
