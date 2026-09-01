/* Command palette (redesign Phase 6).
   Cmd/Ctrl+K (or "/") opens a keyboard-driven search over /search.json.
   Progressive enhancement: if fetch/JSON is unavailable the trigger no-ops. */
(function () {
  'use strict';

  var el = document.getElementById('cmdk');
  if (!el) return;
  var input = document.getElementById('cmdk-input');
  var results = document.getElementById('cmdk-results');
  var searchUrl = el.getAttribute('data-search') || '/search.json';

  var data = null;     // loaded index (array)
  var loading = false;
  var items = [];       // current visible result objects
  var sel = -1;         // selected index
  var lastFocus = null;

  // Show "Ctrl K" instead of the Command symbol on non-Apple platforms.
  var isApple = /Mac|iPhone|iPad|iPod/.test(navigator.platform || '');
  if (!isApple) {
    var kbds = document.querySelectorAll('.search-trigger-kbd');
    for (var q = 0; q < kbds.length; q++) kbds[q].textContent = 'Ctrl K';
  }

  function open() {
    if (!el.hidden) return;
    lastFocus = document.activeElement;
    el.hidden = false;
    document.body.classList.add('cmdk-open');
    input.value = '';
    render([]);
    input.focus();
    if (!data && !loading) load();
  }

  function close() {
    if (el.hidden) return;
    el.hidden = true;
    document.body.classList.remove('cmdk-open');
    sel = -1;
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function load() {
    loading = true;
    fetch(searchUrl)
      .then(function (r) { return r.json(); })
      .then(function (d) {
        data = Array.isArray(d) ? d : [];
        loading = false;
        if (input.value) search(input.value);
      })
      .catch(function () { loading = false; });
  }

  function search(qraw) {
    var q = (qraw || '').trim().toLowerCase();
    if (!q) { render([]); return; }
    if (!data) { render([]); return; } // still loading
    var scored = [];
    for (var i = 0; i < data.length; i++) {
      var it = data[i];
      var title = (it.title || '').toLowerCase();
      var cat = (it.category || '').toLowerCase();
      var content = (it.content || '').toLowerCase();
      var score = 0;
      if (title.indexOf(q) === 0) score = 100;
      else if (title.indexOf(q) !== -1) score = 60;
      else if (cat.indexOf(q) !== -1) score = 25;
      else if (content.indexOf(q) !== -1) score = 10;
      if (score) scored.push({ it: it, s: score });
    }
    scored.sort(function (a, b) { return b.s - a.s; });
    var out = [];
    for (var k = 0; k < scored.length && k < 20; k++) out.push(scored[k].it);
    render(out);
  }

  function render(list) {
    items = list;
    results.innerHTML = '';
    if (!list.length) {
      if (input.value.trim()) {
        var li0 = document.createElement('li');
        li0.className = 'cmdk-empty';
        li0.textContent = data ? 'No results' : 'Loading…';
        results.appendChild(li0);
      }
      sel = -1;
      return;
    }
    for (var i = 0; i < list.length; i++) {
      var it = list[i];
      var li = document.createElement('li');
      li.className = 'cmdk-item';
      li.setAttribute('role', 'option');
      var t = document.createElement('span');
      t.className = 'cmdk-item-title';
      t.textContent = it.title || it.url;
      var c = document.createElement('span');
      c.className = 'cmdk-item-cat';
      c.textContent = it.category || '';
      li.appendChild(t);
      li.appendChild(c);
      (function (url) { li.addEventListener('click', function () { go(url); }); })(it.url);
      (function (idx) { li.addEventListener('mousemove', function () { if (sel !== idx) { sel = idx; highlight(); } }); })(i);
      results.appendChild(li);
    }
    sel = 0;
    highlight();
  }

  function highlight() {
    var lis = results.querySelectorAll('.cmdk-item');
    for (var i = 0; i < lis.length; i++) lis[i].classList.toggle('active', i === sel);
    if (sel >= 0 && lis[sel]) lis[sel].scrollIntoView({ block: 'nearest' });
  }

  function move(delta) {
    var n = items.length;
    if (!n) return;
    sel = (sel + delta + n) % n;
    highlight();
  }

  function go(url) {
    if (!url) return;
    close();
    window.location.href = url;
  }

  input.addEventListener('input', function () { search(input.value); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter') { e.preventDefault(); if (items[sel]) go(items[sel].url); }
    else if (e.key === 'Escape') { e.preventDefault(); close(); }
  });

  el.addEventListener('click', function (e) {
    if (e.target.hasAttribute('data-cmdk-close')) close();
  });

  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      if (el.hidden) open(); else close();
    } else if (e.key === 'Escape' && !el.hidden) {
      close();
    } else if (e.key === '/' && el.hidden) {
      var tag = (e.target && e.target.tagName) || '';
      if (!/^(INPUT|TEXTAREA|SELECT)$/.test(tag) && !(e.target && e.target.isContentEditable)) {
        e.preventDefault();
        open();
      }
    }
  });

  var triggers = document.querySelectorAll('[data-cmdk-open]');
  for (var t = 0; t < triggers.length; t++) triggers[t].addEventListener('click', open);
})();
