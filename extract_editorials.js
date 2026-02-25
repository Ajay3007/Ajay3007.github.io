const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const problemsPath = '_data/problems.yml';
let problemsData = yaml.load(fs.readFileSync(problemsPath, 'utf8'));

const editorialsDir = '_editorials';
if (!fs.existsSync(editorialsDir)) fs.mkdirSync(editorialsDir);

let migratedCount = 0;

function parseAndExtract(prob, item, uri) {
    if (uri.endsWith('/')) uri = uri.slice(0, -1);
    let targetSlug = prob.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    let newEditorialPath = `/editorials/${targetSlug}/`;

    if (uri.includes('#')) {
        let [filePathStr, anchor] = uri.split('#');
        filePathStr = filePathStr.replace('/learning/', '_learning/');
        if (filePathStr.endsWith('/')) filePathStr = filePathStr.slice(0, -1);
        if (!filePathStr.endsWith('.md')) filePathStr += '.md';

        if (filePathStr.startsWith('/')) filePathStr = filePathStr.substring(1);

        let actualFile = null;
        let tryPaths = [
            filePathStr,
            filePathStr.replace('strings', 'Strings'),
            filePathStr.replace('searching-sorting', 'Searching-Sorting'),
            filePathStr.replace('arrays', 'Arrays')
        ];

        for (let tr of tryPaths) {
            if (fs.existsSync(tr)) { actualFile = tr; break; }
        }

        if (actualFile) {
            let mdContent = fs.readFileSync(actualFile, 'utf8');
            let lines = mdContent.split('\n');
            let startIndex = -1;
            let endIndex = -1;
            let headerLevel = 0;

            const searchAnchor = anchor.replace(/-/g, '').toLowerCase();

            for (let i = 0; i < lines.length; i++) {
                let line = lines[i];
                if (line.trim().startsWith('#')) {
                    let textPart = line.replace(/^#+\s*/, '').replace(/[^a-z0-9]/gi, '').toLowerCase();
                    if (textPart === searchAnchor || textPart.includes(searchAnchor)) {
                        startIndex = i;
                        headerLevel = line.match(/^#+/)[0].length;
                        break;
                    }
                }
            }

            if (startIndex !== -1) {
                for (let i = startIndex + 1; i < lines.length; i++) {
                    let line = lines[i];
                    if (line.trim().startsWith('#')) {
                        let currentLevel = line.match(/^#+/)[0].length;
                        if (currentLevel <= headerLevel) {
                            endIndex = i;
                            break;
                        }
                    }
                }
                if (endIndex === -1) endIndex = lines.length;

                let extractedLines = lines.slice(startIndex, endIndex);
                let newMdContent = lines.slice(0, startIndex).concat(lines.slice(endIndex)).join('\n');
                fs.writeFileSync(actualFile, newMdContent);

                const currentIsoDate = new Date().toISOString();
                let editorialContent = `---
layout: editorial
title: "${prob.title} Solution"
problem_id: "${prob.id || ''}"
date: ${currentIsoDate}
---

${extractedLines.slice(1).join('\n').trim()}
`;
                fs.writeFileSync(path.join(editorialsDir, targetSlug + '.md'), editorialContent);
                prob[item.key] = newEditorialPath;
                migratedCount++;
                console.log(`[Extracted Anchor] ${targetSlug}`);
            } else {
                console.log(`Failed to find anchor ${anchor} in ${actualFile}`);
            }
        } else {
            console.log(`File not found: ${filePathStr}`);
        }
    }
    else if (uri.includes('-solution') || uri.includes('leetcode-') || uri.includes('Leetcode-')) {
        let filePathStr = uri.replace('/learning/', '_learning/');
        if (!filePathStr.endsWith('.md')) {
            if (!filePathStr.endsWith('.cpp')) filePathStr += '.md';
        }

        if (filePathStr.startsWith('/')) filePathStr = filePathStr.substring(1);

        let actualFile = null;
        let tryPaths = [
            filePathStr,
            filePathStr.replace('strings', 'Strings'),
            filePathStr.replace('searching-sorting', 'Searching-Sorting')
        ];

        for (let tr of tryPaths) {
            if (fs.existsSync(tr)) { actualFile = tr; break; }
            if (fs.existsSync(tr + "/index.md")) { actualFile = tr + "/index.md"; break; }
        }

        if (actualFile) {
            let mdContent = fs.readFileSync(actualFile, 'utf8');
            let bodyOnly = actualFile.endsWith('.cpp') ? "```cpp\n" + mdContent + "\n```" : mdContent.replace(/^---[\s\S]*?---\n*/, '');

            const currentIsoDate = new Date().toISOString();
            let editorialContent = `---
layout: editorial
title: "${prob.title} Solution"
problem_id: "${prob.id || ''}"
date: ${currentIsoDate}
---

${bodyOnly}`;
            fs.writeFileSync(path.join(editorialsDir, targetSlug + '.md'), editorialContent);
            prob[item.key] = newEditorialPath;
            migratedCount++;
            console.log(`[Ported Standalone File] ${targetSlug}`);
        } else {
            console.log(`Standalone File not found for: ${filePathStr}`);
        }
    }
}

problemsData.problems.forEach(prob => {
    let urls = [];
    if (prob.approach_url && prob.approach_url.includes('/learning/dsa/') && !prob.approach_url.endsWith('.pdf')) {
        urls.push({ key: 'approach_url', url: prob.approach_url });
    }
    if (prob.solution_url && prob.solution_url.includes('/learning/dsa/') && !prob.solution_url.endsWith('.pdf')) {
        urls.push({ key: 'solution_url', url: prob.solution_url });
    }

    urls.forEach(item => {
        try {
            parseAndExtract(prob, item, item.url);
        } catch (e) {
            console.error(`Error on ${item.url}: ${e}`);
        }
    });
});

fs.writeFileSync(problemsPath, yaml.dump(problemsData, { indent: 2 }));
console.log(`\n✅ Successfully Migrated ${migratedCount} solutions into _editorials!`);
