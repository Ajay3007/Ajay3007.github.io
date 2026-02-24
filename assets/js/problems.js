// assets/js/problems.js
document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("problems-tbody");
    if (!tableBody || !window.dsaProblems) return;

    const searchInput = document.getElementById("filter-search");
    const diffFilter = document.getElementById("filter-difficulty");
    const topicFilter = document.getElementById("filter-topic");
    const statusFilter = document.getElementById("filter-status");

    // The single source of truth array defined cleanly in problems.md via Liquid
    const problems = window.dsaProblems;

    function renderTable() {
        // Grab current filter values
        const query = searchInput.value.toLowerCase();
        const diff = diffFilter.value;
        const targetTopic = topicFilter.value;
        const status = statusFilter.value;

        // Apply filters
        const filtered = problems.filter(p => {
            const matchSearch = p.title.toLowerCase().includes(query) || (p.id || "").toString().includes(query);
            const matchDiff = diff === "all" || p.difficulty === diff;
            const matchTopic = targetTopic === "all" || (p.topics && p.topics.includes(targetTopic));
            
            let matchStatus = true;
            if (status === "solved") matchStatus = p.solved === true;
            if (status === "todo") matchStatus = p.solved !== true;

            return matchSearch && matchDiff && matchTopic && matchStatus;
        });

        // Clear existing rows
        tableBody.innerHTML = "";

        if (filtered.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="5" style="text-align: center; padding: 2rem; color: var(--light-text);">No problems found matching your criteria. Keep grinding! ☕️</td></tr>`;
            return;
        }

        // Build new rows
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
            let diffColor = "#64748b";
            let diffBg = "#f1f5f9";
            if (p.difficulty === "easy") { diffColor = "#10b981"; diffBg = "#dcfce7"; }
            if (p.difficulty === "medium") { diffColor = "#f59e0b"; diffBg = "#fef3c7"; }
            if (p.difficulty === "hard") { diffColor = "#ef4444"; diffBg = "#fee2e2"; }
            
            const diffHtml = `<span style="display: inline-block; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.8rem; font-weight: 600; color: ${diffColor}; background: ${diffBg}; text-transform: capitalize;">${p.difficulty}</span>`;

            // Topics mapping
            let topicsHtml = "";
            if (p.topics && p.topics.length > 0) {
                topicsHtml = p.topics.map(t => `<span style="display: inline-block; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.75rem; background: var(--bg-secondary); border: 1px solid var(--border-color); color: var(--light-text); margin-right: 0.25rem; margin-bottom: 0.25rem; white-space: nowrap;">${t.replace('-', ' ')}</span>`).join("");
            }

            // Solution & Approach Buttons
            let actionsHtml = `<div style="display: flex; gap: 0.5rem;">`;
            if (p.solution_url) {
                actionsHtml += `<a href="${p.solution_url}" title="View Solution" style="background: rgba(16, 185, 129, 0.1); color: #10b981; padding: 0.3rem 0.6rem; border-radius: 4px; text-decoration: none; font-size: 0.85rem; transition: background 0.2s;">💻 Code</a>`;
            }
            if (p.approach_url) {
                actionsHtml += `<a href="${p.approach_url}" title="Read Approach notes" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6; padding: 0.3rem 0.6rem; border-radius: 4px; text-decoration: none; font-size: 0.85rem; transition: background 0.2s;">📝 Notes</a>`;
            }
            if (!p.solution_url && !p.approach_url) {
                actionsHtml += `<span style="font-size: 0.85rem; color: var(--light-text); font-style: italic;">No notes yet</span>`;
            }
            actionsHtml += `</div>`;

            // Construct full row payload
            tr.innerHTML = `
                <td style="padding: 1rem; text-align: center;">${statusHtml}</td>
                <td style="padding: 1rem;">${titleHtml}</td>
                <td style="padding: 1rem;">${diffHtml}</td>
                <td style="padding: 1rem;">${topicsHtml}</td>
                <td style="padding: 1rem;">${actionsHtml}</td>
            `;

            tableBody.appendChild(tr);
        });
    }

    // Attach listeners
    [searchInput, diffFilter, topicFilter, statusFilter].forEach(el => {
        el.addEventListener("input", renderTable);
        el.addEventListener("change", renderTable); // for selects
    });

    // Handle global CSS styling for hover effects on dynamically generated rows
    const style = document.createElement("style");
    style.textContent = `
        .problem-row:hover {
            background-color: var(--bg-secondary) !important;
        }
        .problem-link:hover {
            color: #3b82f6 !important;
        }
        .problem-table-wrapper {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: var(--bg-color);
        }
        .problem-filter-input {
            padding: 0.6rem 1rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: var(--bg-color);
            color: var(--text-color);
            font-size: 0.95rem;
            outline: none;
            transition: border-color 0.2s;
        }
        .problem-filter-input:focus {
            border-color: #3b82f6;
        }
        @media (max-width: 768px) {
            #problems-table th, #problems-table td {
                padding: 0.75rem 0.5rem !important;
                font-size: 0.9rem;
            }
            .hide-mobile {
                display: none !important;
            }
        }
    `;
    document.head.appendChild(style);

    // Initial render
    renderTable();
});
