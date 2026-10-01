/*! Kambu Guide components.js v1.0 · 1 October 2026
 *
 * Progressive enhancement for Kambu guide pages. No dependencies, no globals
 * except window.KambuGuide. The page is complete without this file: tab
 * panels stack under their headings, galleries scroll natively and
 * accordions are native <details>. This script only upgrades them.
 *
 *   [data-kg-tabs]        horizontal or vertical (.kg-tabs--vertical) tabs
 *   [data-kg-gallery]     arrows, counter, keyboard, lightbox
 *   [data-kg-spy]         marks the nav link for the section in view
 *   [data-kg-progress]    reading-progress bar (put it inside .site-header)
 *   [data-kg-anchors]     adds copy-link anchors to h2[id] inside it
 *   [data-kg-totop]       on <body>: floating back-to-top on small screens
 *
 * Analytics: every interaction dispatches a `kg:track` CustomEvent on
 * document and, when window.dataLayer exists, pushes the same object
 * (event names follow kambu-semantic-content-architect).
 */
(function () {
  'use strict';
  if (window.KambuGuide) return;

  var doc = document;
  var root = doc.documentElement;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ICON = {
    prev: '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5L7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    next: '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5L13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    close: '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 5l10 10M15 5L5 15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    up: '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M4.5 12.5L10 7l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
  };

  /* ---------- helpers ---------- */
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }
  function track(name, detail) {
    var data = { event: name };
    for (var k in detail) if (Object.prototype.hasOwnProperty.call(detail, k)) data[k] = detail[k];
    try { doc.dispatchEvent(new CustomEvent('kg:track', { detail: data })); } catch (e) { /* old browser */ }
    if (Array.isArray(window.dataLayer)) window.dataLayer.push(data);
  }
  function once(el, key) { if (el.getAttribute('data-kg-ready-' + key)) return false; el.setAttribute('data-kg-ready-' + key, ''); return true; }
  function headerOffset() {
    var h = doc.querySelector('.site-header');
    return h ? h.getBoundingClientRect().height : 0;
  }
  var toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = doc.createElement('div');
      toastEl.className = 'kg-toast'; toastEl.setAttribute('role', 'status'); toastEl.setAttribute('aria-live', 'polite');
      doc.body.appendChild(toastEl);
    }
    toastEl.textContent = msg; toastEl.classList.add('is-visible');
    clearTimeout(toastTimer); toastTimer = setTimeout(function () { toastEl.classList.remove('is-visible'); }, 2200);
  }

  /* ======================================================================
     Tabs (WAI-ARIA tabs pattern, automatic activation)
     Markup: .kg-tabs[data-kg-tabs] > .kg-tabs__list[hidden] > button[data-kg-tab="panel-id"]
             panels: section.kg-tabs__panel#panel-id (each with its own heading)
     ====================================================================== */
  var tabSets = [];
  function initTabs(set) {
    if (!once(set, 'tabs')) return;
    var vertical = set.classList.contains('kg-tabs--vertical');
    var list = set.querySelector('.kg-tabs__list');
    if (!list) return;
    var tabs = $$('[data-kg-tab]', list);
    var panels = tabs.map(function (t) { return doc.getElementById(t.getAttribute('data-kg-tab')); });
    if (!tabs.length || panels.some(function (p) { return !p; })) return;

    var groupLabel = set.getAttribute('data-kg-label') || '';
    list.setAttribute('role', 'tablist');
    if (groupLabel && !list.hasAttribute('aria-label')) list.setAttribute('aria-label', groupLabel);
    if (vertical) list.setAttribute('aria-orientation', 'vertical');
    tabs.forEach(function (tab, i) {
      var panel = panels[i];
      if (!tab.id) tab.id = panel.id + '-tab';
      tab.setAttribute('type', 'button');
      tab.setAttribute('role', 'tab');
      tab.setAttribute('aria-controls', panel.id);
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tab.id);
      panel.setAttribute('tabindex', '0');
      tab.addEventListener('click', function () { select(i, true); });
      tab.addEventListener('keydown', onKey);
    });

    function select(i, byUser, focus) {
      tabs.forEach(function (t, j) {
        var on = j === i;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.setAttribute('tabindex', on ? '0' : '-1');
        panels[j].classList.toggle('is-active', on);
      });
      if (focus) tabs[i].focus();
      if (byUser) {
        // keep the chosen tab visible in a scrolling strip
        if (tabs[i].scrollIntoView) tabs[i].scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: reduceMotion ? 'auto' : 'smooth' });
        track('tab_select', { group: groupLabel || set.id || '', tab: (tabs[i].querySelector('.kg-tabs__label') || tabs[i]).textContent.trim() });
      }
    }
    function onKey(e) {
      var i = tabs.indexOf(e.currentTarget), n = tabs.length, to = null;
      var back = vertical ? ['ArrowUp', 'ArrowLeft'] : ['ArrowLeft'];
      var fwd = vertical ? ['ArrowDown', 'ArrowRight'] : ['ArrowRight'];
      if (fwd.indexOf(e.key) > -1) to = (i + 1) % n;
      else if (back.indexOf(e.key) > -1) to = (i - 1 + n) % n;
      else if (e.key === 'Home') to = 0;
      else if (e.key === 'End') to = n - 1;
      if (to === null) return;
      e.preventDefault();
      select(to, true, true);
    }

    var start = tabs.findIndex(function (t) { return t.getAttribute('aria-selected') === 'true' || t.hasAttribute('data-kg-default'); });
    select(start < 0 ? 0 : start, false);
    list.hidden = false;
    set.classList.add('is-enhanced');
    tabSets.push({ panels: panels, select: select });
  }

  /* Open whatever hides a deep-linked element: a closed <details> or an
     inactive tab panel. Runs on load and on every hashchange. */
  function revealHash(scroll) {
    var id = decodeURIComponent((location.hash || '').slice(1));
    if (!id) return;
    var el = doc.getElementById(id);
    if (!el) return;
    var node = el;
    while (node && node !== doc.body) {
      if (node.tagName === 'DETAILS' && !node.open) node.open = true;
      if (node.classList && node.classList.contains('kg-tabs__panel')) {
        tabSets.forEach(function (s) { var i = s.panels.indexOf(node); if (i > -1) s.select(i, false); });
      }
      node = node.parentElement;
    }
    if (scroll) el.scrollIntoView({ block: 'start', behavior: 'auto' });
  }

  /* ======================================================================
     Gallery + lightbox
     Markup: figure.kg-gallery[data-kg-gallery] > .kg-gallery__viewport > ul.kg-gallery__track > li.kg-gallery__slide
             each slide: figure > a.kg-gallery__open[href=large.webp] > img + figcaption
             controls: .kg-gallery__controls[hidden] with [data-kg-prev] [data-kg-next] .kg-gallery__count
     ====================================================================== */
  function initGallery(g) {
    if (!once(g, 'gallery')) return;
    var viewport = g.querySelector('.kg-gallery__viewport');
    var slides = $$('.kg-gallery__slide', g);
    if (!viewport || !slides.length) return;
    var controls = g.querySelector('.kg-gallery__controls');
    var prev = g.querySelector('[data-kg-prev]');
    var next = g.querySelector('[data-kg-next]');
    var count = g.querySelector('.kg-gallery__count');
    var dotsWrap = g.querySelector('.kg-gallery__dots');
    var label = g.getAttribute('aria-label') || 'Gallery';
    var index = 0, dots = [];

    g.setAttribute('aria-roledescription', 'carousel');
    slides.forEach(function (s, i) {
      s.setAttribute('role', 'group');
      s.setAttribute('aria-roledescription', 'slide');
      s.setAttribute('aria-label', (i + 1) + ' of ' + slides.length);
    });
    if (prev) prev.innerHTML = ICON.prev;
    if (next) next.innerHTML = ICON.next;
    if (dotsWrap) {
      slides.forEach(function () { var d = doc.createElement('span'); dotsWrap.appendChild(d); dots.push(d); });
      dotsWrap.hidden = false;
    }
    if (controls) controls.hidden = slides.length < 2;

    function offsetOf(i) { return slides[i].offsetLeft - slides[0].offsetLeft; }
    function go(i, byUser) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      viewport.scrollTo({ left: offsetOf(i), behavior: reduceMotion ? 'auto' : 'smooth' });
      setIndex(i);
      if (byUser) track('gallery_nav', { gallery: label, index: i + 1 });
    }
    function setIndex(i) {
      index = i;
      if (count) count.textContent = (i + 1) + ' / ' + slides.length;
      if (prev) prev.setAttribute('aria-disabled', i === 0 ? 'true' : 'false');
      if (next) next.setAttribute('aria-disabled', i === slides.length - 1 ? 'true' : 'false');
      dots.forEach(function (d, j) { d.classList.toggle('is-active', j === i); });
    }
    var ticking = false;
    viewport.addEventListener('scroll', function () {
      if (ticking) return; ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        var x = viewport.scrollLeft, best = 0, bestD = Infinity;
        slides.forEach(function (s, i) { var d = Math.abs(offsetOf(i) - x); if (d < bestD) { bestD = d; best = i; } });
        if (best !== index) setIndex(best);
      });
    }, { passive: true });
    if (prev) prev.addEventListener('click', function () { if (index > 0) go(index - 1, true); });
    if (next) next.addEventListener('click', function () { if (index < slides.length - 1) go(index + 1, true); });
    viewport.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(index - 1, true); }
      else if (e.key === 'ArrowRight') { e.preventDefault(); go(index + 1, true); }
    });
    setIndex(0);

    // Lightbox: opens on the slide's link; without JS the link opens the image
    var items = slides.map(function (s) {
      var a = s.querySelector('.kg-gallery__open');
      var img = s.querySelector('img');
      var cap = s.querySelector('figcaption');
      return { a: a, src: a ? a.getAttribute('href') : (img && img.currentSrc), alt: img ? img.alt : '', caption: cap ? cap.innerHTML : '' };
    });
    items.forEach(function (it, i) {
      if (!it.a || typeof HTMLDialogElement !== 'function') return;
      it.a.setAttribute('aria-haspopup', 'dialog');
      it.a.addEventListener('click', function (e) {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return; // let "open in new tab" work
        e.preventDefault();
        Lightbox.open(items, i, label, function (j) { go(j, false); });
      });
    });
  }

  var Lightbox = (function () {
    var dlg, img, cap, cnt, items, idx, onMove, lastFocus, label, touchX = null;
    function build() {
      dlg = doc.createElement('dialog');
      dlg.className = 'kg-lightbox';
      dlg.innerHTML =
        '<figure class="kg-lightbox__frame"><img class="kg-lightbox__img" alt=""><figcaption class="kg-lightbox__caption"></figcaption></figure>' +
        '<div class="kg-lightbox__bar">' +
        '<span class="kg-gallery__count" aria-live="polite"></span>' +
        '<button type="button" class="kg-iconbtn" data-lb="prev" aria-label="Previous image">' + ICON.prev + '</button>' +
        '<button type="button" class="kg-iconbtn" data-lb="next" aria-label="Next image">' + ICON.next + '</button>' +
        '<button type="button" class="kg-iconbtn" data-lb="close" aria-label="Close image viewer">' + ICON.close + '</button>' +
        '</div>';
      doc.body.appendChild(dlg);
      img = dlg.querySelector('img'); cap = dlg.querySelector('figcaption'); cnt = dlg.querySelector('.kg-gallery__count');
      dlg.addEventListener('click', function (e) {
        var b = e.target.closest ? e.target.closest('[data-lb]') : null;
        if (b) { var a = b.getAttribute('data-lb'); if (a === 'close') dlg.close(); else move(a === 'next' ? 1 : -1); return; }
        if (e.target === dlg) dlg.close(); // backdrop
      });
      dlg.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); move(1); }
        else if (e.key === 'ArrowLeft') { e.preventDefault(); move(-1); }
      });
      dlg.addEventListener('touchstart', function (e) { touchX = e.touches[0].clientX; }, { passive: true });
      dlg.addEventListener('touchend', function (e) {
        if (touchX === null) return;
        var dx = e.changedTouches[0].clientX - touchX; touchX = null;
        if (Math.abs(dx) > 50) move(dx < 0 ? 1 : -1);
      });
      dlg.addEventListener('close', function () {
        root.classList.remove('kg-lock');
        if (onMove) onMove(idx);
        if (lastFocus && lastFocus.focus) lastFocus.focus();
      });
    }
    function show() {
      var it = items[idx];
      img.src = it.src; img.alt = it.alt;
      cap.innerHTML = it.caption;
      cnt.textContent = (idx + 1) + ' / ' + items.length;
      dlg.querySelector('[data-lb="prev"]').setAttribute('aria-disabled', idx === 0 ? 'true' : 'false');
      dlg.querySelector('[data-lb="next"]').setAttribute('aria-disabled', idx === items.length - 1 ? 'true' : 'false');
      dlg.setAttribute('aria-label', label + ', image ' + (idx + 1) + ' of ' + items.length);
    }
    function move(d) {
      var j = idx + d;
      if (j < 0 || j >= items.length) return;
      idx = j; show();
      track('gallery_nav', { gallery: label, index: idx + 1, view: 'lightbox' });
    }
    return {
      open: function (list, i, galleryLabel, cb) {
        if (!dlg) build();
        items = list; idx = i; onMove = cb; label = galleryLabel; lastFocus = doc.activeElement;
        show();
        root.classList.add('kg-lock');
        dlg.showModal();
        dlg.querySelector('[data-lb="close"]').focus();
        track('gallery_open', { gallery: label, index: i + 1 });
      }
    };
  })();

  /* ======================================================================
     Scroll-linked: active section in nav, reading progress, scroll depth,
     floating back-to-top. One rAF-throttled listener.
     ====================================================================== */
  var spies = [], progress = null, progressTarget = null, depthsSent = {}, toTop = null;
  function initSpy(nav) {
    if (!once(nav, 'spy')) return;
    var items = $$('a[href^="#"]', nav).map(function (a) {
      return { a: a, el: doc.getElementById(decodeURIComponent(a.getAttribute('href').slice(1))) };
    }).filter(function (x) { return x.el; });
    items.sort(function (x, y) { return x.el.compareDocumentPosition(y.el) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1; });
    spies.push(items);
  }
  function onScroll() {
    var line = headerOffset() + window.innerHeight * 0.25;
    spies.forEach(function (items) {
      var active = null;
      items.forEach(function (it) { if (it.el.getBoundingClientRect().top <= line) active = it; });
      items.forEach(function (it) {
        if (it === active) it.a.setAttribute('aria-current', 'true'); else it.a.removeAttribute('aria-current');
      });
    });
    if (progress && progressTarget) {
      var r = progressTarget.getBoundingClientRect();
      var total = r.height - window.innerHeight + headerOffset();
      var p = total > 0 ? Math.min(1, Math.max(0, (headerOffset() - r.top) / total)) : 0;
      progress.style.setProperty('--kg-p', p.toFixed(4));
      [25, 50, 75, 90].forEach(function (d) {
        if (!depthsSent[d] && p * 100 >= d) { depthsSent[d] = true; track('scroll_depth_' + d, {}); }
      });
    }
    if (toTop) toTop.classList.toggle('is-visible', window.scrollY > window.innerHeight * 1.5);
  }
  var scrollQueued = false;
  function queueScroll() {
    if (scrollQueued) return; scrollQueued = true;
    requestAnimationFrame(function () { scrollQueued = false; onScroll(); });
  }

  /* ======================================================================
     Heading anchors with copy-to-clipboard
     ====================================================================== */
  function initAnchors(scope) {
    if (!once(scope, 'anchors')) return;
    $$('h2[id]', scope).forEach(function (h) {
      if (h.querySelector('.kg-anchor') || h.closest('.planning-card, .contents, .kg-tabs__panel, summary')) return;
      var a = doc.createElement('a');
      a.className = 'kg-anchor';
      a.href = '#' + h.id;
      a.setAttribute('aria-label', 'Copy link to section: ' + h.textContent.trim());
      a.textContent = '#';
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var url = location.href.split('#')[0] + '#' + h.id;
        if (history.replaceState) history.replaceState(null, '', '#' + h.id);
        var done = function () { toast('Link to this section copied'); };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(done, function () { toast('Section link is in the address bar'); });
        } else { toast('Section link is in the address bar'); }
        track('copy_section_link', { section: h.id });
      });
      h.appendChild(a);
    });
  }

  /* ======================================================================
     Init
     ====================================================================== */
  function init(ctx) {
    ctx = ctx || doc;
    $$('[data-kg-tabs]', ctx).forEach(initTabs);
    $$('[data-kg-gallery]', ctx).forEach(initGallery);
    $$('[data-kg-spy]', ctx).forEach(initSpy);
    $$('[data-kg-anchors]', ctx).forEach(initAnchors);

    var bar = doc.querySelector('[data-kg-progress]');
    if (bar && !progress) {
      progress = bar;
      progressTarget = doc.querySelector(bar.getAttribute('data-kg-progress') || '#article') || doc.querySelector('main');
      bar.hidden = false;
    }
    if (doc.body.hasAttribute('data-kg-totop') && !toTop) {
      toTop = doc.createElement('a');
      toTop.href = '#top';
      toTop.className = 'kg-iconbtn kg-totop';
      toTop.setAttribute('aria-label', 'Back to top');
      toTop.innerHTML = ICON.up;
      doc.body.appendChild(toTop);
    }

    // disclosure analytics (toggle does not bubble, so capture it)
    if (once(root, 'toggle')) {
      doc.addEventListener('toggle', function (e) {
        var d = e.target;
        if (d.tagName === 'DETAILS' && d.open) {
          var s = d.querySelector('summary');
          track('disclosure_open', { id: d.id || '', label: s ? s.textContent.trim().slice(0, 80) : '' });
        }
      }, true);
      window.addEventListener('scroll', queueScroll, { passive: true });
      window.addEventListener('resize', queueScroll);
      window.addEventListener('hashchange', function () { revealHash(true); });
    }
    revealHash(!!location.hash);
    onScroll();
  }

  window.KambuGuide = { init: init, track: track, version: '1.0' };
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', function () { init(); });
  else init();
})();
