/* Visionneuse d'images façon Fandom (lightbox) — autonome, sans réseau.
   Mobile (< 761 px) : plein écran noir, en-tête titre + ✕, légende en bas, bande de vignettes,
   toucher l'image = masquer/afficher l'interface, toucher à côté = fermer, geste rapide = image suivante, pincer / double-toucher = zoom.
   Ordinateur : barre du haut (titre, « Voir en taille réelle », légende, ✕), flèches, barre du bas
   (« 3 sur 15 » + carrousel), cadenas pour épingler les barres (sinon masquées après 3 s d'inactivité).
   Clavier : ← → Échap. Bouton Retour du téléphone : ferme la visionneuse.
   Une image dans un lien, ou avec data-nolightbox, n'ouvre pas la visionneuse. */
(function () {
  if (window.__fandomLightbox) return; window.__fandomLightbox = true;
  var D = document, H = D.documentElement;
  var ICON = {
    info: '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9.5"/><path d="M12 11v6"/><path d="M12 7.5h.01" stroke-width="2.8"/></svg>',
    x: '<svg class="flb-ic-d" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5 5 19"/></svg>',
    l: '<svg class="flb-ic-d" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
    r: '<svg class="flb-ic-d" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    /* tour 91 : icônes façon Atelier (index 7) pour le mobile — chevrons et croix trait 2.4 */
    lc: '<svg class="flb-ic-m" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>',
    rc: '<svg class="flb-ic-m" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
    xc: '<svg class="flb-ic-m" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
    cl: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m15 6-6 6 6 6"/></svg>',
    cr: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>',
    lockOpen: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 7.5-2"/></svg>',
    lock: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
  };

  /* ---------- quelles images ---------- */
  function eligible(img, needVisible) {
    if (!img || img.tagName !== 'IMG' || img.closest('.flb')) return false;
    if (img.hasAttribute('data-nolightbox') || img.closest('[data-nolightbox]')) return false;
    var a = img.closest('a[href]'); if (a && a.getAttribute('href') !== '#') return false;
    if (!img.currentSrc && !img.getAttribute('src')) return false;
    if (needVisible === false) return true;
    if (!img.offsetParent && getComputedStyle(img).position !== 'fixed') return false;
    var r = img.getBoundingClientRect(); return r.width >= 48 || r.height >= 48;
  }
  function groupFor(img) {
    var scope = img.closest('[data-lb-group]') || D;
    return Array.prototype.filter.call(scope.querySelectorAll('img'), function (i) { return eligible(i); });
  }
  function textOf(img) {
    var fig = img.closest('figure'), cap = '';
    if (fig) { var fc = fig.querySelector('figcaption'); if (fc) cap = fc.textContent.trim(); }
    if (!cap) { var gi = img.closest('.wikia-gallery-item, .lbx-gitem, .gallerybox'); /* légende de galerie (Fandom / MediaWiki) — tour 86 */
      if (gi) { var gc = gi.querySelector('.lightbox-caption, .lbx-gcap, .gallerytext'); if (gc) cap = gc.textContent.trim(); } }
    if (!cap) { var ib = img.closest('.infobox'); if (ib) { var ic = ib.querySelector('.ib-cap'); if (ic) cap = ic.textContent.trim(); } }
    if (!cap) cap = img.getAttribute('data-caption') || img.getAttribute('title') || '';
    var alt = (img.getAttribute('alt') || '').trim();
    var title = img.getAttribute('data-title') || (alt && alt.length <= 70 ? alt : '');
    if (!title) { var src0 = alt || cap, m = src0.match(/^(.{2,60}?)\s*[:—–.]\s/); if (m) title = m[1]; }
    if (!cap && alt && alt !== title) cap = alt;
    if (cap === title) cap = '';
    return { title: title, cap: cap, user: img.getAttribute('data-user') || '', desc: img.getAttribute('data-desc') || '' };
  }

  /* ---------- construction ---------- */
  var el, imgEl, view, strip, list = [], idx = 0, lastFocus = null, pushed = false, pinned = false, idleT = 0;
  var z = { s: 1, x: 0, y: 0 };
  function build() {
    el = D.createElement('div'); el.className = 'flb'; el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true');
    el.setAttribute('aria-label', "Visionneuse d'images"); el.tabIndex = -1; el.hidden = true;
    el.innerHTML =
      '<div class="flb-top"><div class="flb-tl"><div class="flb-t1"><span class="flb-title"></span>' +
      '<button type="button" class="flb-full">Voir en taille réelle</button></div><div class="flb-capd"></div></div>' +
      '<span class="flb-cnt-m"></span><button type="button" class="flb-info flb-info-top" aria-label="Informations sur l\u2019image">' + ICON.info + '</button><button type="button" class="flb-x" aria-label="Fermer">' + ICON.x + ICON.xc + '</button></div>' +
      '<div class="flb-stage"><div class="flb-view"><img class="flb-img" alt="" draggable="false"></div>' +
      '<button type="button" class="flb-arrow flb-prev" aria-label="Image précédente">' + ICON.l + ICON.lc + '</button>' +
      '<button type="button" class="flb-arrow flb-next" aria-label="Image suivante">' + ICON.r + ICON.rc + '</button></div>' +
      '<div class="flb-bot"><div class="flb-capm" role="button" tabindex="0" aria-label="Déplier la légende"></div>' +
      '<div class="flb-row"><div class="flb-cnt"></div><button type="button" class="flb-info flb-info-bot" aria-label="Informations sur l\u2019image">' + ICON.info + '</button></div><div class="flb-sw"><button type="button" class="flb-sl" aria-label="Vignettes précédentes">' + ICON.cl + '</button>' +
      '<div class="flb-strip" role="listbox" aria-label="Toutes les images"></div>' +
      '<button type="button" class="flb-sr" aria-label="Vignettes suivantes">' + ICON.cr + '</button>' +
      '<button type="button" class="flb-pin" aria-pressed="false" title="Épingler les barres">' + ICON.lockOpen + '</button></div></div>';
    D.body.appendChild(el);
    imgEl = el.querySelector('.flb-img'); view = el.querySelector('.flb-view'); strip = el.querySelector('.flb-strip');
    el.querySelector('.flb-x').onclick = function () { close(); };
    el.querySelector('.flb-prev').onclick = function (e) { e.stopPropagation(); go(idx - 1); };
    el.querySelector('.flb-next').onclick = function (e) { e.stopPropagation(); go(idx + 1); };
    el.querySelector('.flb-sl').onclick = function () { strip.scrollBy({ left: -strip.clientWidth * .8, behavior: 'smooth' }); };
    el.querySelector('.flb-sr').onclick = function () { strip.scrollBy({ left: strip.clientWidth * .8, behavior: 'smooth' }); };
    el.querySelector('.flb-full').onclick = function (e) { e.stopPropagation(); fullSize(); };
    var capm = el.querySelector('.flb-capm');
    capm.onclick = function (e) { e.stopPropagation(); capm.classList.toggle('open'); };
    capm.onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); capm.classList.toggle('open'); } };
    var pin = el.querySelector('.flb-pin');
    pin.onclick = function () { pinned = !pinned; pin.setAttribute('aria-pressed', pinned); pin.innerHTML = pinned ? ICON.lock : ICON.lockOpen; poke(); };
    strip.addEventListener('click', function (e) { var b = e.target.closest('.flb-th'); if (b) go(+b.dataset.i); });
    el.addEventListener('mousemove', poke, { passive: true });
    el.addEventListener('keydown', onKey);
    Array.prototype.forEach.call(el.querySelectorAll('.flb-info'), function (b) { b.onclick = function (e) { e.stopPropagation(); info(); }; });
    el.addEventListener('click', function (e) {
      var t = e.target;
      if (t.classList && (t.classList.contains('flb-top') || t.classList.contains('flb-tl') || t.classList.contains('flb-bot') || t.classList.contains('flb-sw') || t.classList.contains('flb-strip') || t.classList.contains('flb-cnt') || t.classList.contains('flb-stage') || t.classList.contains('flb-row'))) close();
    });
    gestures();
  }
  function isMobile() { return window.innerWidth < 761; }

  /* ---------- fenêtre « infos » (comme le bouton ⓘ de Fandom mobile) ---------- */
  function info() {
    closeInfo(); var t = textOf(list[idx]), d = D.createElement('div');
    d.className = 'flb-dlg';
    d.innerHTML = '<div class="flb-dlg-box" role="dialog" aria-modal="true" aria-label="Informations"><div class="flb-dlg-in">' +
      '<h3>' + esc(t.title || ('Image ' + (idx + 1))) + '</h3>' + (t.cap ? '<p>' + esc(t.cap) + '</p>' : '') +
      (t.desc ? '<p class="flb-dlg-desc">' + esc(t.desc) + '</p>' : '') + (t.user ? '<p class="flb-dlg-by">Ajoutée par ' + esc(t.user) + '</p>' : '') +
      (!t.cap && !t.desc && !t.user ? '<p class="flb-dlg-by">Aucune information supplémentaire.</p>' : '') +
      '</div><div class="flb-dlg-act"><button type="button">Fermer</button></div></div>';
    d.addEventListener('click', function (e) { e.stopPropagation(); if (e.target === d || e.target.closest('.flb-dlg-act button')) closeInfo(); });
    d.addEventListener('pointerdown', function (e) { e.stopPropagation(); });
    el.appendChild(d); d.querySelector('.flb-dlg-act button').focus();
  }
  function closeInfo() { var d = el && el.querySelector('.flb-dlg'); if (d) { d.remove(); return true; } return false; }

  /* ---------- ouverture / fermeture ---------- */
  function theme() {
    // clair ou sombre selon le fond de la page, couleur d'accent = couleur des liens
    var bg = getComputedStyle(D.body).backgroundColor, m = bg.match(/\d+(\.\d+)?/g) || [255, 255, 255];
    var a = m.length > 3 ? +m[3] : 1, lum = (0.299 * m[0] + 0.587 * m[1] + 0.114 * m[2]);
    el.classList.toggle('flb-dark', a > 0.1 && lum < 128);
    var link = D.querySelector('.mw-parser-output a[href]') || D.querySelector('main a[href]') || D.querySelector('article a[href]') || D.querySelector('a[href]'), acc = link ? getComputedStyle(link).color : '';
    var custom = D.body.getAttribute('data-lb-accent');
    el.style.setProperty('--flb-accent', custom || acc || '#00cdd0');
  }
  function open(group, start) {
    if (!el) build();
    list = group; idx = Math.max(0, list.indexOf(start));
    theme(); lastFocus = D.activeElement;
    strip.innerHTML = list.map(function (im, i) {
      var t = textOf(im);
      return '<button type="button" class="flb-th" role="option" data-i="' + i + '" aria-label="Image ' + (i + 1) + (t.title ? ' : ' + esc(t.title) : '') + '"><img src="' + esc(im.currentSrc || im.src) + '" alt="" loading="lazy" draggable="false"></button>';
    }).join('');
    el.classList.toggle('flb-single', list.length < 2);
    el.hidden = false; H.classList.add('flb-open');
    requestAnimationFrame(function () { el.classList.add('open'); });
    /* tour 93 : body[data-lb-nohistory] = la page gère elle-même le bouton retour (ex. l'Atelier et sa pile navPush) */
    if (!D.body.hasAttribute('data-lb-nohistory')) { try { history.pushState({ flb: 1 }, ''); pushed = true; } catch (e) { pushed = false; } }
    show(); el.focus({ preventScroll: true }); poke();
  }
  function close(fromPop, silent) {
    if (!el || el.hidden) return;
    closeInfo(); el.classList.remove('open', 'flb-ui-hidden', 'flb-idle'); el.hidden = true; H.classList.remove('flb-open');
    resetZoom(); clearTimeout(idleT);
    if (pushed && !fromPop) { pushed = false; try { history.back(); } catch (e) {} }
    pushed = false;
    if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
    /* tour 93 : prévient la page qu'on a fermé (✕, Échap, toucher le vide…) — pas envoyé si la page ferme elle-même (silent) */
    if (!silent) try { D.dispatchEvent(new CustomEvent('flb:close')); } catch (e) {}
  }
  window.addEventListener('popstate', function () { if (D.body.hasAttribute('data-lb-nohistory')) return; if (el && !el.hidden) { pushed = false; close(true); } });

  function go(i) {
    if (!list.length) return;
    idx = (i + list.length) % list.length; show();
  }
  function show() {
    var im = list[idx], t = textOf(im), src = im.currentSrc || im.src;
    resetZoom(); el.classList.remove('flb-natural');
    imgEl.classList.remove('in'); imgEl.onload = function () { imgEl.classList.add('in'); updateFull(); };
    imgEl.src = src; imgEl.alt = t.title || t.cap || ('Image ' + (idx + 1));
    if (imgEl.complete) { imgEl.classList.add('in'); updateFull(); }
    var title = t.title || ('Image ' + (idx + 1));
    el.querySelector('.flb-title').textContent = title;
    el.querySelector('.flb-capd').textContent = t.cap;
    var capm = el.querySelector('.flb-capm'); capm.textContent = t.cap; capm.classList.remove('open'); capm.hidden = !t.cap;
    el.querySelector('.flb-cnt').innerHTML = '<span class="flb-cnt-mob">' + (idx + 1) + ' / ' + list.length + '</span><span class="flb-cnt-desk"><b>' + (idx + 1) + '</b> sur <b>' + list.length + '</b></span>';
    el.querySelector('.flb-cnt-m').textContent = list.length > 1 ? (idx + 1) + ' / ' + list.length : '';
    Array.prototype.forEach.call(strip.children, function (b, i) {
      var on = i === idx; b.classList.toggle('on', on); b.setAttribute('aria-selected', on);
      if (on) { var l = b.offsetLeft - (strip.clientWidth - b.offsetWidth) / 2; strip.scrollTo({ left: l, behavior: 'smooth' }); }
    });
    [idx + 1, idx - 1].forEach(function (k) { var n = list[(k + list.length) % list.length]; if (n) { var p = new Image(); p.src = n.currentSrc || n.src; } });
  }
  function updateFull() {
    var b = el.querySelector('.flb-full'), r = imgEl.getBoundingClientRect();
    b.hidden = !(imgEl.naturalWidth > r.width / z.s + 2);
  }
  function fullSize() {
    if (z.s > 1) { resetZoom(); el.classList.remove('flb-natural'); return; }
    var r = imgEl.getBoundingClientRect(); if (!r.width) return;
    z.s = Math.min(8, imgEl.naturalWidth / r.width); z.x = 0; z.y = 0; apply(); el.classList.add('flb-natural');
  }

  /* ---------- barres masquées après inactivité (ordinateur) ---------- */
  function poke() {
    el.classList.remove('flb-idle'); clearTimeout(idleT);
    if (!pinned && !isMobile()) idleT = setTimeout(function () { el.classList.add('flb-idle'); }, 3000);
  }

  /* ---------- clavier ---------- */
  function onKey(e) {
    if (e.key === 'Escape') { e.preventDefault(); if (!closeInfo()) close(); }
    else if (el.querySelector('.flb-dlg')) { if (e.key !== 'Tab') return; }
    else if (e.key === 'ArrowRight') { e.preventDefault(); go(idx + 1); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); go(idx - 1); }
    else if (e.key === 'Tab') { // garder le focus dans la visionneuse
      var f = Array.prototype.filter.call(el.querySelectorAll('button,[tabindex="0"]'), function (b) { return !b.hidden && b.offsetParent; });
      if (!f.length) return; var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (D.activeElement === first || D.activeElement === el)) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && D.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    poke();
  }

  /* ---------- zoom, glisser, toucher ---------- */
  function apply() { imgEl.style.transform = 'translate(' + z.x + 'px,' + z.y + 'px) scale(' + z.s + ')'; el.classList.toggle('flb-zoomed', z.s > 1.01); }
  function resetZoom() { z.s = 1; z.x = 0; z.y = 0; if (imgEl) { imgEl.style.transform = ''; el.classList.remove('flb-zoomed'); } }
  function clampPan() {
    var r = view.getBoundingClientRect(), w = imgEl.offsetWidth * z.s, h = imgEl.offsetHeight * z.s;
    var mx = Math.max(0, (w - r.width) / 2), my = Math.max(0, (h - r.height) / 2);
    z.x = Math.max(-mx, Math.min(mx, z.x)); z.y = Math.max(-my, Math.min(my, z.y));
  }
  function zoomAt(cx, cy, ns) {
    var r = view.getBoundingClientRect(), ox = cx - (r.left + r.width / 2), oy = cy - (r.top + r.height / 2);
    var k = ns / z.s; z.x = ox - (ox - z.x) * k; z.y = oy - (oy - z.y) * k; z.s = ns;
    if (z.s <= 1.01) { resetZoom(); return; } clampPan(); apply();
  }
  function gestures() {
    var pts = {}, start = null, pinch = null, lastTap = 0, tapT = 0, moved = false;
    view.addEventListener('pointerdown', function (e) {
      if (e.target.closest('button')) return;
      view.setPointerCapture(e.pointerId); pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      var ids = Object.keys(pts);
      if (ids.length === 1) { start = { x: e.clientX, y: e.clientY, zx: z.x, zy: z.y, t: Date.now() }; moved = false; }
      if (ids.length === 2) {
        var a = pts[ids[0]], b = pts[ids[1]];
        pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), s: z.s, cx: (a.x + b.x) / 2, cy: (a.y + b.y) / 2 };
      }
    });
    view.addEventListener('pointermove', function (e) {
      if (!pts[e.pointerId]) return; pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      var ids = Object.keys(pts);
      if (ids.length === 2 && pinch) {
        var a = pts[ids[0]], b = pts[ids[1]], d = Math.hypot(a.x - b.x, a.y - b.y);
        zoomAt(pinch.cx, pinch.cy, Math.max(1, Math.min(6, pinch.s * d / pinch.d))); moved = true; return;
      }
      if (!start) return;
      var dx = e.clientX - start.x, dy = e.clientY - start.y;
      if (Math.abs(dx) > 8 || Math.abs(dy) > 8) moved = true;
      if (z.s > 1.01) { z.x = start.zx + dx; z.y = start.zy + dy; clampPan(); apply(); }
    });
    function end(e) {
      if (!pts[e.pointerId]) return; delete pts[e.pointerId];
      if (Object.keys(pts).length) { start = null; return; }
      if (pinch) { pinch = null; start = null; return; }
      if (!start) return;
      var dx = e.clientX - start.x, dy = e.clientY - start.y, s = start; start = null;
      if (z.s <= 1.01 && moved) {
        // l'image ne suit plus le doigt : un geste rapide gauche/droite change seulement d'image
        if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) { go(idx + (dx < 0 ? 1 : -1)); }
        return;
      }
      if (moved) return;
      // toucher / clic : dans le vide (hors de l'image) = fermer tout de suite
      var r = imgEl.getBoundingClientRect();
      var onImg = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
      if (!onImg && z.s <= 1.01) { clearTimeout(tapT); lastTap = 0; close(); return; }
      var now = Date.now();
      if (now - lastTap < 300) { // double toucher = zoom
        clearTimeout(tapT); lastTap = 0;
        if (z.s > 1.01) { resetZoom(); el.classList.remove('flb-natural'); } else zoomAt(e.clientX, e.clientY, 2.5);
        return;
      }
      lastTap = now;
      tapT = setTimeout(function () { if (isMobile()) el.classList.toggle('flb-ui-hidden'); }, 300);
    }
    view.addEventListener('pointerup', end); view.addEventListener('pointercancel', end);
    view.addEventListener('dblclick', function (e) { e.preventDefault(); });
    view.addEventListener('wheel', function (e) { e.preventDefault(); if (e.ctrlKey || z.s > 1.01) zoomAt(e.clientX, e.clientY, Math.max(1, Math.min(6, z.s * (e.deltaY < 0 ? 1.15 : 0.87)))); }, { passive: false });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ---------- déclencheurs ---------- */
  /* tour 92 : body[data-lb-manual] = la page ouvre elle-même la visionneuse via window.FLB.open (ex. l'Atelier) */
  function manual() { return !!(D.body && D.body.hasAttribute('data-lb-manual')); }
  D.addEventListener('click', function (e) {
    if (manual()) return;
    var img = e.target.closest && e.target.closest('img');
    if (!img || !eligible(img)) return;
    e.preventDefault(); e.stopPropagation(); open(groupFor(img), img);
  }, true);
  D.addEventListener('keydown', function (e) {
    if (manual()) return;
    var img = e.target; if ((e.key === 'Enter' || e.key === ' ') && img && img.tagName === 'IMG' && eligible(img)) { e.preventDefault(); open(groupFor(img), img); }
  });
  function mark(root) {
    if (manual()) return;
    Array.prototype.forEach.call((root || D).querySelectorAll('img'), function (i) {
      if (i.closest('.flb') || i.dataset.lbMarked) return;
      if (!eligible(i, false) && !i.hasAttribute('data-img')) return;
      if (i.closest('a[href]:not([href="#"])') || i.hasAttribute('data-nolightbox')) return;
      i.dataset.lbMarked = '1'; i.classList.add('flb-able'); i.tabIndex = 0; i.setAttribute('role', 'button');
      if (!i.getAttribute('aria-label')) i.setAttribute('aria-label', 'Agrandir l\u2019image' + (i.alt ? ' : ' + i.alt : ''));
    });
  }
  /* tour 92 : API publique — FLB.open(img) ouvre le groupe de l'image ; FLB.open([img, ...], imgDeDépart) ouvre une liste
     (les images peuvent être créées à la volée : new Image() + data-title / data-caption) ; FLB.close() ferme */
  window.FLB = {
    open: function (a, start) {
      if (Array.isArray(a)) { if (a.length) open(a, start && a.indexOf(start) >= 0 ? start : a[0]); }
      else if (a && a.tagName === 'IMG') open(groupFor(a).indexOf(a) >= 0 ? groupFor(a) : [a], a);
    },
    close: function (silent) { close(false, !!silent); },
    isOpen: function () { return !!(el && !el.hidden); }
  };
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', function () { mark(); }); else mark();
})();
