/* Visionneuses d'images Fandom reconstituées, pour comparer dans les aperçus.
   Ordinateur : « f26 » (Fandom actuel, 2026), « oasis » (ancien Wikia, avant 2020), « mine » (lightbox.js).
   Mobile     : « fm25 » (Fandom mobile actuel, 2025), « mw » (ancienne appli mobile-wiki, avant 2021), « mine ».
   Code réécrit à partir des valeurs relevées dans le code Fandom (resultat/code-fandom/) : aucune ligne copiée.
   Choix mémorisé dans localStorage (si le navigateur l'autorise). */
(function () {
  'use strict';
  if (window.__lbxVisionneuses) return; window.__lbxVisionneuses = true;
  var D = document, H = D.documentElement, W = window;
  var PLAT = H.getAttribute('data-lb-platform') === 'mobile' ? 'mobile' : 'web';
  var ENG = PLAT === 'web'
    ? [['mine', 'La mienne (par défaut)'], ['f26', 'Fandom actuel (2026)'], ['oasis', 'Ancien Wikia « Oasis » (avant 2020)']]
    : [['mine', 'La mienne (par défaut)'], ['fm25', 'Fandom mobile actuel (2025)'], ['mw', 'Ancienne appli « mobile-wiki » (avant 2021)']];
  /* tour 92 : « la mienne » devient la visionneuse par défaut ; nouvelle clé pour ignorer les anciens choix mémorisés */
  var KEY = 'fandom-visionneuse-v2-' + PLAT, mode = ENG[0][0], arrowsExp = false;
  try { var s0 = localStorage.getItem(KEY); if (s0 && ENG.some(function (e) { return e[0] === s0; })) mode = s0; arrowsExp = localStorage.getItem(KEY + '-fleches') === '1'; } catch (e) {}
  var WIKI_URL = 'https://mon-wiki.fandom.com/fr/wiki/';
  var ARTICLE = "Titre de l'article";
  var TOUCH = ('ontouchstart' in W) || navigator.maxTouchPoints > 0;

  /* ---------------- icônes (dessinées ici, style « WDS ») ---------------- */
  var SV = function (w, p, extra) { return '<svg viewBox="0 0 24 24" width="' + w + '" height="' + w + '" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"' + (extra || '') + '>' + p + '</svg>'; };
  var IC = {
    x: function (w) { return SV(w || 18, '<path d="M5 5l14 14M19 5 5 19"/>'); },
    down: function (w) { return SV(w || 12, '<path d="m6 9 6 6 6-6"/>', ' stroke-width="2.6"'); },
    share: SV(14, '<circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="m8.2 10.8 7.6-4.4M8.2 13.2l7.6 4.4"/>'),
    q: SV(14, '<circle cx="12" cy="12" r="9.5"/><path d="M9.6 9.3a2.5 2.5 0 0 1 4.8.9c0 1.7-2.4 2.2-2.4 3.6"/><path d="M12 17.2h.01" stroke-width="2.6"/>'),
    lockOpen: SV(15, '<rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 7.5-2"/>'),
    lock: SV(15, '<rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
    link: SV(22, '<path d="M9.5 14.5 14.5 9.5"/><path d="M11 6.5l1.8-1.8a4 4 0 0 1 5.6 5.6L16.6 12M13 17.5l-1.8 1.8a4 4 0 0 1-5.6-5.6L7.4 12"/>'),
    info: SV(22, '<circle cx="12" cy="12" r="9.5"/><path d="M12 11v6"/><path d="M12 7.5h.01" stroke-width="2.8"/>'),
    left: SV(20, '<path d="m15 6-6 6 6 6"/>', ' stroke-width="2.4"'),
    right: SV(20, '<path d="m9 6 6 6-6 6"/>', ' stroke-width="2.4"')
  };
  /* Pictos d'origine de l'ancien Wikia (sprite-Lightbox, dépôt Wikia/app, GPL) — injectés par le script de build */
  var SPR = W.LBX_SPRITES || {};

  /* ---------------- utilitaires ---------------- */
  function mk(tag, cls, html) { var e = D.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  var probe;
  function rgb(c) {
    if (!probe) { probe = mk('i'); probe.style.display = 'none'; D.body.appendChild(probe); }
    probe.style.color = ''; probe.style.color = c;
    var m = getComputedStyle(probe).color.match(/[\d.]+/g) || [0, 0, 0]; return [+m[0], +m[1], +m[2]];
  }
  function mix(a, b, p) { return 'rgb(' + [0, 1, 2].map(function (k) { return Math.round(a[k] * p + b[k] * (1 - p)); }).join(',') + ')'; }
  function lum(c) { return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]; }
  function theme(el) {
    var src = D.getElementById('site') || H, cs = getComputedStyle(src);
    function v() { for (var i = 0; i < arguments.length; i++) { var x = cs.getPropertyValue(arguments[i]).trim(); if (x) return x; } return ''; }
    var page = v('--page', '--bg') || '#ffffff', text = v('--text') || '#3a3a3a', link = v('--link') || '#337800', border = v('--border') || '#cecece';
    var P = rgb(page), dark = lum(P) < 128, WH = [255, 255, 255], BK = [0, 0, 0];
    var body = v('--accent-rgb'); var B = body ? body.split(',').map(Number) : rgb(border);
    var st = el.style;
    st.setProperty('--p', page); st.setProperty('--t', text); st.setProperty('--l', link); st.setProperty('--b', border);
    st.setProperty('--prgb', P.join(',')); st.setProperty('--brgb', B.join(','));
    st.setProperty('--btn', link); st.setProperty('--shd', mix(P, BK, 0.5));
    /* boutons secondaires Oasis (skins/shared/color.scss) */
    var sbh = dark ? mix(WH, P, 0.08) : mix(P, WH, 0.94), sb = dark ? mix(WH, P, 0.03) : mix(P, BK, 0.9), sbb = dark ? mix(WH, P, 0.2) : mix(P, BK, 0.8);
    st.setProperty('--sbh', sbh); st.setProperty('--sb', sb); st.setProperty('--sbb', sbb);
    st.setProperty('--sbhd', mix(rgb(sbh), BK, 0.96)); st.setProperty('--sbd', mix(rgb(sb), BK, 0.96));
    return { dark: dark, link: link };
  }
  function toast(el, msg) {
    var t = el.querySelector('.lbx-toast'); if (!t) { t = mk('div', 'lbx-toast'); el.appendChild(t); }
    t.textContent = msg; t.hidden = false; clearTimeout(t._t); t._t = setTimeout(function () { t.hidden = true; }, 2600);
  }
  function openFull(el, src) {
    try {
      fetch(src).then(function (r) { return r.blob(); }).then(function (b) {
        var u = URL.createObjectURL(b), w = W.open(u, '_blank');
        if (!w) toast(el, "L'image seule s'ouvre dans un nouvel onglet — bloqué dans cet aperçu.");
      }).catch(function () { toast(el, "Impossible d'ouvrir l'image seule ici."); });
    } catch (e) { toast(el, "Impossible d'ouvrir l'image seule ici."); }
  }
  /* ?file= dans l'adresse (comme Fandom ordinateur). Silencieux si l'aperçu l'interdit. */
  function setFile(f) {
    try {
      var u = new URL(location.href);
      if (f) u.searchParams.set('file', f); else u.searchParams.delete('file');
      history.replaceState(history.state, '', u.toString());
    } catch (e) {}
  }

  /* ---------------- quelles images, quel groupe ---------------- */
  function eligible(img) {
    if (!img || img.tagName !== 'IMG') return false;
    if (img.closest('.lbx,.flb,[data-nolightbox]')) return false;
    if (!img.closest('.mw-parser-output')) return false;
    var a = img.closest('a[href]'); if (a && a.getAttribute('href') !== '#') return false;
    var r = img.getBoundingClientRect(); if (r.width && r.height) return r.width > 50 && r.height > 50;
    return (img.naturalWidth || 0) > 50;
  }
  function all() { return Array.prototype.filter.call(D.querySelectorAll('.mw-parser-output img'), function (i) { return !i.closest('.lbx,.flb,[data-nolightbox]') && !(i.closest('a[href]') && i.closest('a[href]').getAttribute('href') !== '#'); }); }
  function groupFor(img) {
    if (PLAT === 'web') return all();                                     /* ordinateur : toutes les images de la page */
    var g = img.closest('.lbx-gallery');                                  /* mobile : la galerie seulement */
    return g ? Array.prototype.slice.call(g.querySelectorAll('img')) : [img];
  }
  function info(img) {
    var fig = img.closest('figure,.lbx-gitem'), capEl = fig && fig.querySelector('figcaption,.lbx-gcap');
    return {
      src: img.getAttribute('data-full') || img.currentSrc || img.src,
      file: img.getAttribute('data-file') || 'Image',
      cap: (img.getAttribute('data-caption') || (capEl ? capEl.textContent : '') || '').trim(),
      user: img.getAttribute('data-user') || '', desc: img.getAttribute('data-desc') || '',
      gallery: !!img.closest('.lbx-gallery')
    };
  }

  /* ---------------- socle commun ---------------- */
  var cur = null; /* {eng, el, list, i, last} */
  function begin(eng, imgs, start) {
    if (cur) end();
    var list = imgs.map(info), el = eng.el || (eng.el = eng.build());
    if (!el.parentNode) D.body.appendChild(el);
    cur = { eng: eng, el: el, list: list, i: Math.max(0, imgs.indexOf(start)), last: D.activeElement };
    H.classList.add('lbx-open'); el.hidden = false;
    eng.open(cur);
    try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); }
  }
  function end() {
    if (!cur) return; var c = cur; cur = null;
    c.eng.close(c); c.el.hidden = true; H.classList.remove('lbx-open');
    if (c.last && c.last.focus) try { c.last.focus({ preventScroll: true }); } catch (e) {}
  }
  D.addEventListener('keydown', function (e) {
    if (!cur) return;
    if (e.key === 'Tab') { /* garder le focus dans la visionneuse */
      var f = Array.prototype.filter.call(cur.el.querySelectorAll('button,a[href],input,[tabindex="0"]'), function (x) { return x.offsetParent !== null; });
      if (!f.length) { e.preventDefault(); return; }
      var a = f.indexOf(D.activeElement);
      if (e.shiftKey && a <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && a === f.length - 1) { e.preventDefault(); f[0].focus(); }
      if (cur.eng.poke) cur.eng.poke(cur, e.target);
      return;
    }
    if (e.target && e.target.tagName === 'INPUT') { if (e.key === 'Escape') end(); return; }
    cur.eng.key(cur, e);
  }, true);

  /* =====================================================================
     1. FANDOM ORDINATEUR 2026 (ext.fandom.Lightbox + lightbox.css)
     ===================================================================== */
  function sharePanel(cls) {
    return '<div class="shp ' + (cls || '') + '"><button type="button" class="back">Retour</button><div class="content">' +
      '<div class="hero"><img alt=""></div><div class="form"><h1><a href="#" class="sh-file"></a></h1>' +
      '<label>Lien standard</label><input type="text" readonly class="sh-url">' +
      '<ul class="soc"><li><span style="background:#2e77f2" title="Facebook">f</span></li><li><span style="background:#4ba0eb" title="Twitter / X">X</span></li><li><span style="background:#ec5428" title="Reddit">r</span></li><li><span style="background:#38455b" title="Tumblr">t</span></li></ul></div>' +
      '<div class="bottom"><div><h2>E-mail</h2><label>L’envoyer par e-mail à un ami</label><input type="text" placeholder="Adresse e-mail de votre ami" disabled></div>' +
      '<div><h2>URL</h2><label>URL de la page du fichier</label><input type="text" readonly class="sh-furl"></div></div>' +
      '<p class="off">Aperçu hors ligne : les boutons de partage sont inactifs.</p></div></div>';
  }
  function fillShare(el, it) {
    el.querySelector('.shp .hero img').src = it.src;
    el.querySelector('.sh-file').textContent = it.file;
    el.querySelector('.sh-url').value = WIKI_URL + encodeURIComponent(ARTICLE.replace(/ /g, '_')) + '?file=' + encodeURIComponent(it.file);
    el.querySelector('.sh-furl').value = WIKI_URL + 'Fichier:' + encodeURIComponent(it.file);
  }
  function descHtml(it) { return (it.cap ? '<p><b>Légende :</b> ' + esc(it.cap) + '</p>' : '') + '<p><b>Description :</b> ' + esc(it.desc || '—') + '</p>'; }

  /* moteur « bureau » partagé entre 2026 et Oasis (même logique Lightbox.js, habillage différent) */
  function desktopEngine(K) {
    var E = { key: key };
    var hideT = 0, lastMove = 0, pinned = false, first = 0, shown = 1;
    function $(s) { return E.el.querySelector(s); }
    function showOverlay() { clearTimeout(hideT); E.el.classList.remove('oh'); }
    function hideOverlay(ms) { clearTimeout(hideT); if (pinned) return; hideT = setTimeout(function () { if (!pinned && !E.el.classList.contains('share')) E.el.classList.add('oh'); }, ms); }
    E.poke = function () { showOverlay(); hideOverlay(1200); };
    E.build = function () {
      var el = mk('div', 'lbx lbx-' + K.name); el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true');
      el.setAttribute('aria-label', "Visionneuse d'images"); el.tabIndex = -1; el.hidden = true;
      el.innerHTML = K.html();
      E.el = el;
      el.addEventListener('click', function (e) {
        var t = e.target;
        if (t === el || t.classList.contains(K.bo)) { end(); return; }
        if (t.closest('.' + K.x)) { end(); return; }
        var th = t.closest('li[data-i]'); if (th) { go(+th.getAttribute('data-i')); return; }
        if (t.closest('.' + K.prev)) { if (!t.closest('.dis')) go(cur.i - 1); return; }
        if (t.closest('.' + K.next)) { if (!t.closest('.dis')) go(cur.i + 1); return; }
        if (t.closest('.' + K.cprev)) { page(-1); return; }
        if (t.closest('.' + K.cnext)) { page(1); return; }
        if (t.closest('.' + K.pin)) { setPin(!pinned); return; }
        if (t.closest('.' + K.share)) { e.preventDefault(); fillShare(el, cur.list[cur.i]); el.classList.add('share'); showOverlay(); return; }
        if (t.closest('.shp .back')) { el.classList.remove('share'); hideOverlay(1200); return; }
        if (t.closest('.' + K.full)) { e.preventDefault(); openFull(el, cur.list[cur.i].src); return; }
        var dd = t.closest('.' + K.dd); if (dd && t.closest('button')) { dd.classList.toggle('open'); return; }
        if (!t.closest('.' + K.ddc)) Array.prototype.forEach.call(el.querySelectorAll('.' + K.dd + '.open'), function (d) { d.classList.remove('open'); });
        if (t.closest('a[href="#"]')) e.preventDefault();
      });
      /* souris : afficher, puis masquer 1,2 s après (sauf si la souris est sur une barre) ; sortie du cadre : 10 ms */
      var modal = el.querySelector('.' + K.modal);
      modal.addEventListener('mousemove', function (e) {
        var n = Date.now(); if (n - lastMove < 100) return; lastMove = n;
        showOverlay(); if (!e.target.closest('.' + K.head + ',.' + K.car)) hideOverlay(1200);
      });
      modal.addEventListener('mouseleave', function () { hideOverlay(10); });
      W.addEventListener('resize', function () { if (cur && cur.eng === E) carousel(); });
      return el;
    };
    function setPin(p) {
      pinned = p; E.el.classList.toggle('pinned', p);
      var b = $('.' + K.pin); b.classList.toggle('active', p);
      b.title = p ? 'Libérer les barres latérales' : 'Maintenir les barres latérales en place';
      K.pinIcon(b, p);
      if (p) showOverlay(); else hideOverlay(1200);
    }
    E.open = function (c) {
      var th = theme(E.el); E.el.classList.toggle('dark', th.dark); E.el.classList.toggle('light', !th.dark); E.el.classList.toggle('dk', th.dark);
      E.el.classList.remove('share', 'oh');
      $('.' + K.car + ' ul').innerHTML = c.list.map(function (it, i) { return '<li data-i="' + i + '" title="' + esc(it.cap || it.file) + '"><img src="' + esc(it.src) + '" alt=""></li>'; }).join('');
      first = 0;
      setPin(TOUCH ? true : pinned);           /* écran tactile : barres épinglées, jamais masquées… */
      $('.' + K.pin).hidden = TOUCH;            /* …et le cadenas est caché (pin.click().hide() dans les deux codes Fandom) */
      render(); showOverlay(); hideOverlay(3000);  /* ouverture : masquage après 3 s */
    };
    E.close = function () { clearTimeout(hideT); setFile(null); };
    function go(i) { if (i < 0 || i >= cur.list.length) return; cur.i = i; render(); }   /* pas de boucle */
    function render() {
      var c = cur, it = c.list[c.i];
      $('.' + K.media + ' img').src = it.src;
      $('.' + K.media + ' img').alt = it.file;
      K.header(E.el, it);
      $('.' + K.prev).classList.toggle('dis', c.i === 0);
      $('.' + K.next).classList.toggle('dis', c.i === c.list.length - 1);
      Array.prototype.forEach.call(E.el.querySelectorAll('li[data-i]'), function (li) { li.classList.toggle('on', +li.getAttribute('data-i') === c.i); });
      if (c.i < first || c.i >= first + shown) first = Math.max(0, Math.min(c.i, c.list.length - shown));
      carousel(); setFile(it.file);
    }
    function carousel() {
      var cc = $('.' + K.cc), n = cur.list.length;
      shown = Math.max(1, K.shown(cc.clientWidth));
      first = Math.max(0, Math.min(first, n - shown));
      cc.classList.toggle('scroll', n > shown);
      cc.querySelector('ul').style.transform = n > shown ? 'translateX(' + (-first * (K.item + K.gap)) + 'px)' : '';
      $('.' + K.cprev).classList.toggle('dis', first === 0);
      $('.' + K.cnext).classList.toggle('dis', first + shown >= n);
      $('.' + K.prog).innerHTML = '<b>' + (first + 1) + '-' + Math.min(n, first + shown) + '</b> de <b>' + n + '</b>';
    }
    function page(d) { first += d * shown; carousel(); }
    function key(c, e) {
      if (e.key === 'Escape') { e.preventDefault(); if (E.el.classList.contains('share')) E.el.classList.remove('share'); else end(); }
      else if (E.el.classList.contains('share')) return;
      else if (e.key === 'ArrowLeft') { e.preventDefault(); go(c.i - 1); }
      else if (e.key === 'ArrowRight') { e.preventDefault(); go(c.i + 1); }
    }
    return E;
  }

  var f26 = desktopEngine({
    name: 'f26', bo: 'f26-bo', modal: 'f26-modal', media: 'f26-media', head: 'f26-head', car: 'f26-car', x: 'f26-x',
    prev: 'f26-arr.prev', next: 'f26-arr.next', cprev: 'f26-ca.prev', cnext: 'f26-ca.next', pin: 'f26-pin', share: 'f26-share',
    full: 'f26-full', dd: 'f26-dd', ddc: 'f26-ddc', cc: 'f26-cc', prog: 'f26-prog', item: 70, gap: 26,
    shown: function (w) { return Math.round((w + 13) / 96); },   /* formule du Lightbox.js actuel */
    html: function () {
      return '<div class="f26-bo"></div><div class="f26-modal"><div class="f26-media"><img alt=""></div>' +
        '<header class="f26-head"><button type="button" class="f26-x" aria-label="Fermer">' + IC.x(18) + '</button>' +
        '<button type="button" class="f26-btn f26-share">' + IC.share + '<span>Partager</span></button>' +
        '<div class="f26-dd f26-more"><button type="button" class="f26-btn">' + IC.q + '<span>Plus d’informations</span></button><div class="f26-ddc"></div></div>' +
        '<div class="f26-dd left f26-tdd"><button type="button"><h1></h1></button><div class="f26-ddc"></div></div>' +
        '<a href="#" class="f26-full">Voir image en pleine taille</a><div class="f26-user"></div></header>' +
        '<div class="f26-arrows"><button type="button" class="f26-arr prev" aria-label="Précédente">' + IC.down(14) + '</button><button type="button" class="f26-arr next" aria-label="Suivante">' + IC.down(14) + '</button></div>' +
        '<div class="f26-car"><div class="f26-progw"><p class="f26-prog"></p><button type="button" class="f26-pin"></button></div>' +
        '<button type="button" class="f26-ca prev" aria-label="Vignettes précédentes">' + IC.down(18) + '</button><button type="button" class="f26-ca next" aria-label="Vignettes suivantes">' + IC.down(18) + '</button>' +
        '<div class="f26-cc"><ul></ul></div></div>' + sharePanel() + '</div>';
    },
    pinIcon: function (b, p) { b.innerHTML = p ? IC.lock : IC.lockOpen; },
    header: function (el, it) {
      el.querySelector('.f26-head h1').textContent = it.file;
      Array.prototype.forEach.call(el.querySelectorAll('.f26-ddc'), function (d) { d.innerHTML = descHtml(it); });
      el.querySelector('.f26-user').innerHTML = (it.cap ? '<p>' + esc(it.cap) + '</p>' : '') + '<span class="f26-av"></span>Ajoutée par <a href="#">' + esc(it.user || 'Utilisateur') + '</a> <span class="posted">Publiée sur <a href="#">' + esc(ARTICLE) + '</a></span>';
    }
  });

  /* =====================================================================
     2. ANCIEN WIKIA « OASIS » (extensions/wikia/Lightbox, dépôt Wikia/app)
     ===================================================================== */
  var oasis = desktopEngine({
    name: 'oasis', bo: 'oa-bo', modal: 'oa-modal', media: 'oa-media', head: 'oa-head', car: 'oa-car', x: 'oa-x',
    prev: 'oa-zone.prev', next: 'oa-zone.next', cprev: 'oa-ca.prev', cnext: 'oa-ca.next', pin: 'oa-pin', share: 'oa-share',
    full: 'oa-full', dd: 'oa-dd', ddc: 'oa-ddc', cc: 'oa-cc', prog: 'oa-prog', item: 90, gap: 8,
    shown: function () { return 9; },                            /* itemsShown = 9 dans l'ancien Lightbox.js */
    html: function () {
      var sp = function (n) { return SPR[n] ? ' style="background-image:url(' + SPR[n] + ')"' : ''; };
      return '<div class="oa-bo"></div><div class="oa-wrap"><div class="oa-modal">' +
        '<button type="button" class="oa-x wb" aria-label="Fermer">' + IC.x(12) + '</button>' +
        '<div class="oa-media"><img alt=""></div>' +
        '<header class="oa-head"><a href="#" class="wb oa-share">Partager</a>' +
        '<div class="oa-dd"><button type="button" class="wb">' + IC.q + '<span>Plus d’informations</span></button><div class="oa-ddc"></div></div>' +
        '<div class="oa-dd left"><button type="button"><h1></h1></button><div class="oa-ddc"></div></div>' +
        '<a href="#" class="oa-full">Voir image en pleine taille</a><div class="oa-user"></div></header>' +
        '<div class="oa-zone prev" role="button" aria-label="Précédente"><i' + sp('arrow_large_previous') + '></i></div>' +
        '<div class="oa-zone next" role="button" aria-label="Suivante"><i' + sp('arrow_large_next') + '></i></div>' +
        '<div class="oa-car"><button type="button" class="oa-pin"></button><p class="oa-prog"></p>' +
        '<div class="oa-cw"><button type="button" class="oa-ca prev wb" aria-label="Vignettes précédentes"></button><button type="button" class="oa-ca next wb" aria-label="Vignettes suivantes"></button>' +
        '<div class="oa-cc"><ul></ul></div></div></div>' + sharePanel() + '</div></div>';
    },
    pinIcon: function (b, p) {
      var dk = b.closest('.lbx').classList.contains('dk'), n = (p ? 'filmstrip_close_' : 'filmstrip_open_') + (dk ? 'white' : 'black');
      b.style.backgroundImage = SPR[n] ? 'url(' + SPR[n] + ')' : ''; if (!SPR[n]) b.innerHTML = p ? IC.lock : IC.lockOpen;
    },
    header: function (el, it) {
      el.querySelector('.oa-head h1').textContent = it.file;
      Array.prototype.forEach.call(el.querySelectorAll('.oa-ddc'), function (d) { d.innerHTML = descHtml(it); });
      el.querySelector('.oa-user').innerHTML = (it.cap ? '<p>' + esc(it.cap) + '</p>' : '') + '<span class="oa-av"></span>Ajoutée par <a href="#">' + esc(it.user || 'Utilisateur') + '</a> <span class="posted">Publiée sur <a href="#">' + esc(ARTICLE) + '</a></span>';
    }
  });

  /* =====================================================================
     3 et 4. MOBILE : Fandom mobile 2025 et ancienne appli mobile-wiki
     ===================================================================== */
  function mobileEngine(K) {
    var E = {}, z = { s: 1, x: 0, y: 0 }, ptrs = {}, g = null, lastTap = { t: 0, x: 0, y: 0 };
    function $(s) { return E.el.querySelector(s); }
    E.build = function () {
      var el = mk('div', 'lbx lbx-m lbx-' + K.name); el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true');
      el.setAttribute('aria-label', "Visionneuse d'images"); el.tabIndex = -1; el.hidden = true;
      el.innerHTML = '<div class="m-content"><img class="m-img" alt="" draggable="false"></div>' +
        '<div class="m-head"><div class="m-title"></div><button type="button" class="m-x" aria-label="Fermer">' + IC.x(24) + '</button></div>' +
        '<button type="button" class="m-arr prev" aria-label="Précédente">' + IC.left + '</button><button type="button" class="m-arr next" aria-label="Suivante">' + IC.right + '</button>' +
        '<div class="m-foot"><div class="m-info"><div class="m-left"><div class="m-cnt"></div><div class="m-cap" role="button" tabindex="0"></div></div>' +
        (K.actions ? '<div class="m-acts"><button type="button" class="m-act link" aria-label="Lien">' + IC.link + '</button><button type="button" class="m-act info" aria-label="Infos">' + IC.info + '</button></div>' : '') +
        '</div><div class="m-strip"></div></div>';
      E.el = el;
      el.addEventListener('click', function (e) {
        var t = e.target;
        if (t.closest('.m-x')) { end(); return; }
        if (t.closest('.m-dlg')) { if (t.closest('.acts button') || t.classList.contains('m-dlg')) t.closest('.m-dlg').remove(); return; }
        var th = t.closest('.m-th'); if (th) { go(+th.getAttribute('data-i')); return; }
        if (t.closest('.m-arr')) { var b = t.closest('.m-arr'); if (!b.disabled) go(cur.i + (b.classList.contains('next') ? 1 : -1)); return; }
        if (t.closest('.m-act.link')) { toast(el, 'Lien vers la page du fichier (inactif hors ligne).'); return; }
        if (t.closest('.m-act.info')) { dialog(); return; }
      });
      var ct = $('.m-content');
      ct.addEventListener('pointerdown', down); ct.addEventListener('pointermove', move);
      ct.addEventListener('pointerup', up); ct.addEventListener('pointercancel', up);
      $('.m-foot').addEventListener('pointerup', function (e) { if (e.target.closest('.m-cap')) { $('.m-cap').classList.toggle('open'); } });
      el.addEventListener('wheel', function (e) { e.preventDefault(); }, { passive: false });
      return el;
    };
    function dialog() {
      var it = cur.list[cur.i], d = mk('div', 'm-dlg');
      d.innerHTML = '<div role="dialog" aria-label="Infos"><h3>' + esc(it.file) + '</h3>' + (it.cap ? '<p>' + esc(it.cap) + '</p>' : '') +
        '<p>' + esc(it.desc || '') + '</p><p style="opacity:.8">Ajoutée par ' + esc(it.user || 'Utilisateur') + '</p><div class="acts"><button type="button">Fermer</button></div></div>';
      E.el.appendChild(d); d.querySelector('button').focus();
    }
    E.open = function (c) {
      var th = theme(E.el); E.el.style.setProperty('--acc', K.acc || th.link);
      E.gal = c.list.length > 1 && c.list[c.i].gallery;
      E.el.classList.remove('ui-hidden', 'in'); requestAnimationFrame(function () { E.el.classList.add('in'); });
      var strip = $('.m-strip');
      strip.innerHTML = E.gal ? c.list.map(function (it, i) { return '<button type="button" class="m-th" data-i="' + i + '" aria-label="Image ' + (i + 1) + '"><img src="' + esc(it.src) + '" alt=""></button>'; }).join('') : '';
      strip.hidden = !E.gal;
      var arrows = E.gal && K.arrows();
      Array.prototype.forEach.call(E.el.querySelectorAll('.m-arr'), function (b) { b.hidden = !arrows; });
      render();
    };
    E.close = function () { reset(); var d = E.el.querySelector('.m-dlg'); if (d) d.remove(); E.el.classList.remove('in'); };
    function go(i) {
      var n = cur.list.length; if (n < 2) return;
      if (K.loop) i = (i + n) % n; else if (i < 0 || i >= n) return;
      cur.i = i; render();
    }
    function render() {
      var c = cur, it = c.list[c.i];
      reset(); var img = $('.m-img'); img.src = it.src; img.alt = it.file;
      $('.m-cnt').textContent = E.gal ? (c.i + 1) + '/' + c.list.length : '';
      $('.m-cnt').hidden = !E.gal;
      var cap = $('.m-cap'); cap.textContent = it.cap; cap.classList.remove('open'); cap.hidden = !it.cap;
      var hasFoot = !!it.cap || E.gal || K.actions;
      $('.m-foot').hidden = !hasFoot; E.el.classList.toggle('has-grad', hasFoot && K.grad);
      Array.prototype.forEach.call(E.el.querySelectorAll('.m-th'), function (b) { var on = +b.getAttribute('data-i') === c.i; b.classList.toggle('on', on); if (on && b.scrollIntoView) b.scrollIntoView({ block: 'nearest', inline: 'center' }); });
      var p = $('.m-arr.prev'), nx = $('.m-arr.next');
      p.disabled = !K.loop && c.i === 0; nx.disabled = !K.loop && c.i === c.list.length - 1;
    }
    /* ---- zoom / gestes ---- */
    function apply(anim) { var im = $('.m-img'); im.style.transition = anim ? 'transform .25s' : ''; im.style.transform = z.s === 1 ? '' : 'scale(' + z.s + ') translate(' + z.x + 'px,' + z.y + 'px)'; }
    function reset() { z.s = 1; z.x = 0; z.y = 0; if (E.el) apply(false); }
    function clamp() {
      var im = $('.m-img'), w = im.offsetWidth, h = im.offsetHeight, vw = E.el.clientWidth, vh = E.el.clientHeight;
      var mx = Math.max(0, (w * z.s - vw) / 2 / z.s), my = Math.max(0, (h * z.s - vh) / 2 / z.s);
      z.x = Math.max(-mx, Math.min(mx, z.x)); z.y = Math.max(-my, Math.min(my, z.y));
    }
    function zoomAt(cx, cy, s) {
      var r = E.el.getBoundingClientRect(), ox = cx - r.left - r.width / 2, oy = cy - r.top - r.height / 2;
      var ns = Math.max(1, Math.min(K.max, s));
      z.x = z.x + ox / ns - ox / z.s; z.y = z.y + oy / ns - oy / z.s; z.s = ns; if (ns === 1) { z.x = 0; z.y = 0; } clamp();
    }
    function down(e) {
      ptrs[e.pointerId] = { x: e.clientX, y: e.clientY };
      try { e.target.setPointerCapture(e.pointerId); } catch (x) {}
      var ids = Object.keys(ptrs);
      if (ids.length === 1) g = { t: Date.now(), x0: e.clientX, y0: e.clientY, zx: z.x, zy: z.y, moved: false, pinch: false };
      else if (ids.length === 2 && g) { var a = ptrs[ids[0]], b = ptrs[ids[1]]; g.pinch = true; g.d0 = Math.hypot(a.x - b.x, a.y - b.y); g.s0 = z.s; g.moved = true; }
    }
    function move(e) {
      if (!ptrs[e.pointerId] || !g) return; ptrs[e.pointerId] = { x: e.clientX, y: e.clientY };
      var ids = Object.keys(ptrs);
      if (g.pinch && ids.length === 2) {
        var a = ptrs[ids[0]], b = ptrs[ids[1]], d = Math.hypot(a.x - b.x, a.y - b.y);
        zoomAt((a.x + b.x) / 2, (a.y + b.y) / 2, g.s0 * d / g.d0); apply(false); return;
      }
      var dx = e.clientX - g.x0, dy = e.clientY - g.y0;
      if (Math.abs(dx) > 10 || Math.abs(dy) > 10) g.moved = true;
      if (z.s > 1 && !g.pinch) { z.x = g.zx + dx / z.s; z.y = g.zy + dy / z.s; clamp(); apply(false); }
    }
    function up(e) {
      var p = ptrs[e.pointerId]; delete ptrs[e.pointerId]; if (!g || !p) return;
      if (Object.keys(ptrs).length) return;
      var dx = e.clientX - g.x0, dy = e.clientY - g.y0, dt = Date.now() - g.t, gg = g; g = null;
      if (gg.pinch) return;
      /* glisser (galerie seulement, et pas pendant un zoom) */
      if (E.gal && z.s === 1 && Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) && dt < 800) { go(cur.i + (dx < 0 ? 1 : -1)); return; }
      if (gg.moved) return;
      /* appui : afficher / masquer l'interface */
      E.el.classList.toggle('ui-hidden');
      /* double appui : zoom x3 (galerie : seulement dans le tiers central de l'écran) */
      var n = Date.now();
      if (n - lastTap.t < 300 && Math.hypot(e.clientX - lastTap.x, e.clientY - lastTap.y) < 30) {
        lastTap.t = 0;
        var w = E.el.clientWidth, inCenter = e.clientX > w / 3 && e.clientX < 2 * w / 3;
        if (!E.gal || inCenter) { if (z.s > 1) { z.s = 1; z.x = 0; z.y = 0; } else zoomAt(e.clientX, e.clientY, 3); apply(true); }
      } else lastTap = { t: n, x: e.clientX, y: e.clientY };
    }
    E.key = function (c, e) {
      if (e.key === 'Escape') { e.preventDefault(); var d = E.el.querySelector('.m-dlg'); if (d) d.remove(); else end(); }
      else if (E.gal && e.key === 'ArrowLeft') { e.preventDefault(); go(c.i - 1); }
      else if (E.gal && e.key === 'ArrowRight') { e.preventDefault(); go(c.i + 1); }
    };
    return E;
  }
  var fm25 = mobileEngine({ name: 'fm25', actions: true, loop: false, max: 5, grad: false, acc: null, arrows: function () { return arrowsExp; } });
  var mw = mobileEngine({ name: 'mw', actions: false, loop: true, max: 5, grad: true, acc: '#00d6d6', arrows: function () { return false; } });
  var ENGINES = { f26: f26, oasis: oasis, fm25: fm25, mw: mw };

  /* ---------------- aiguillage des clics ---------------- */
  function launch(img) {
    if (mode === 'mine') { if (W.FLB && W.FLB.open) W.FLB.open(img); return; }
    begin(ENGINES[mode], groupFor(img), img);
  }
  W.addEventListener('click', function (e) {
    if (cur) return;
    var img = e.target && e.target.closest && e.target.closest('img');
    if (!eligible(img) || mode === 'mine') return;   /* « la mienne » : lightbox.js s'en occupe */
    e.preventDefault(); e.stopImmediatePropagation(); launch(img);
  }, true);
  W.addEventListener('keydown', function (e) {
    if (cur || mode === 'mine') return;
    var t = e.target; if ((e.key === 'Enter' || e.key === ' ') && eligible(t)) { e.preventDefault(); e.stopImmediatePropagation(); launch(t); }
  }, true);

  /* ---------------- sélecteur(s) ---------------- */
  function syncUI() {
    Array.prototype.forEach.call(D.querySelectorAll('select[data-lbx-select]'), function (s) { s.value = mode; });
    Array.prototype.forEach.call(D.querySelectorAll('[data-lbx-arrows]'), function (lab) {
      lab.hidden = mode !== 'fm25'; var cb = lab.querySelector('input'); if (cb) cb.checked = arrowsExp;
    });
    Array.prototype.forEach.call(D.querySelectorAll('[data-lbx-desc]'), function (p) { p.innerHTML = DESC[mode] || ''; });
  }
  var DESC = {
    f26: 'Fenêtre posée sur la page (fond violet foncé), barre du haut : nom du fichier, « Voir image en pleine taille », « Ajoutée par », Partager, Plus d’informations. Barre du bas : « 1-6 de 6 », vignettes, cadenas. Les barres se masquent 3 s après l’ouverture, puis 1,2 s après chaque mouvement de souris. Pas de boucle.',
    oasis: 'Ancienne fenêtre Wikia de 1010 × 628 px, cadre épais, boutons en dégradé. Cliquer sur la moitié gauche ou droite de l’image = précédente / suivante. Mêmes délais de masquage.',
    mine: 'Ma visionneuse (tour 64) : zoom, plein écran, boucle, bouton Retour du téléphone.',
    fm25: 'Plein écran noir, ✕ en haut, légende fine en bas avec deux boutons (lien, infos), vignettes 44 px. Galerie seulement : glisser, compteur et vignettes ; l’image de l’infobox s’ouvre seule. Les flèches sont un test A/B de Fandom (case à cocher).',
    mw: 'Ancienne appli Ember : plein écran noir, dégradé sous la légende, vignettes à bord turquoise, glisser en boucle, double appui = zoom ×3, pincer jusqu’à ×5. Pas de bouton d’action.'
  };
  function initUI() {
    Array.prototype.forEach.call(D.querySelectorAll('select[data-lbx-select]'), function (s) {
      s.innerHTML = ENG.map(function (e) { return '<option value="' + e[0] + '">' + esc(e[1]) + '</option>'; }).join('');
      s.addEventListener('change', function () { mode = s.value; try { localStorage.setItem(KEY, mode); } catch (e) {} syncUI(); });
    });
    Array.prototype.forEach.call(D.querySelectorAll('[data-lbx-arrows] input'), function (cb) {
      cb.addEventListener('change', function () { arrowsExp = cb.checked; try { localStorage.setItem(KEY + '-fleches', arrowsExp ? '1' : '0'); } catch (e) {} syncUI(); });
    });
    syncUI();
    /* lien direct ?file=… (ordinateur) */
    try {
      var f = new URL(location.href).searchParams.get('file');
      if (f && PLAT === 'web' && mode !== 'mine') { var im = all().filter(function (i) { return i.getAttribute('data-file') === f; })[0]; if (im) launch(im); }
    } catch (e) {}
  }
  W.LBX = { open: function (img) { launch(img); }, close: end, mode: function () { return mode; }, set: function (m) { mode = m; syncUI(); } };
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', initUI); else initUI();
})();
