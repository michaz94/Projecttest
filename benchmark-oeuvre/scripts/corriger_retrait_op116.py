#!/usr/bin/env python3
"""Retrait de l'entrée « ONE PIECE 116 » du corpus (décision utilisateur du 27/09/2026).

Contexte : cette entrée Goodreads (4,68 / 59 notes) correspond à un chapitre de
l'édition originale (Glénat), pas à un tome relié ; elle n'a aucun équivalent
SensCritique (la série s'arrête au tome 115). Elle est retirée du corpus.

Le retrait modifie la population Goodreads (N) : tous les percentiles, rangs
décroissants, bandes et scores ajustés Goodreads sont recalculés à l'identique
de la méthode d'origine ; le côté SensCritique est inchangé.

  - percentile au rang moyen des ex æquo : P = 100 × (inférieurs + 0,5 × ex æquo) / N ;
  - rang décroissant moyen = (strictement mieux notés) + (ex æquo + 1) / 2 ;
  - score ajusté = (v × R + m × C) / (v + m), C = moyenne simple, m = médiane des votes.
"""
from __future__ import annotations

import csv
import json
import shutil
import statistics
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.formatting.formatting import ConditionalFormattingList
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Font

ROOT = Path("/home/user")
LIV = ROOT / "livrables"
BAK = ROOT / "work" / "backup_avant_retrait_op116"
BAK.mkdir(parents=True, exist_ok=True)

SERIE, POS, PLAT = "One Piece", "116", "Goodreads"
NOTE_CORRECTION = ("Retrait du 27/09/2026 : « ONE PIECE 116 » (Goodreads) était un chapitre de "
                   "l’édition originale, pas un tome relié ; aucune fiche SensCritique correspondante. "
                   "Percentiles, rangs et scores ajustés recalculés.")
LOG: list[str] = []
REMOVED_INFO: dict = {}


def backup(name: str) -> Path:
    src = LIV / name
    dst = BAK / name
    if not dst.exists():
        shutil.copy2(src, dst)
    return src


def band(p: float) -> str:
    return ("P99+" if p >= 99 else "P95–99" if p >= 95 else "P90–95" if p >= 90
            else "P75–90" if p >= 75 else "P50–75" if p >= 50 else "P25–50" if p >= 25
            else "Sous P25")


def midrank_stats(ratings: list[float]) -> dict:
    n = len(ratings)
    cnt = Counter(ratings)
    out = {}
    for v, eq in cnt.items():
        lo = sum(c for r, c in cnt.items() if r < v)
        hi = n - lo - eq
        p = 100 * (lo + 0.5 * eq) / n
        out[v] = {"lower": lo, "tied": eq, "higher": hi, "percentile": p,
                  "rank_mid": hi + (eq + 1) / 2,
                  "rank_range": f"{hi + 1}–{hi + eq}" if eq > 1 else str(hi + 1),
                  "band": band(p), "better_pct": 100 * hi / n}
    return out


def q7(vals, p):
    a = sorted(vals); k = (len(a) - 1) * p; lo = int(k); hi = min(lo + 1, len(a) - 1)
    return a[lo] + (k - lo) * (a[hi] - a[lo])


def is_target(r: dict) -> bool:
    return (r.get("platform") == PLAT and r.get("series") == SERIE
            and str(r.get("position")) == POS)


def params(rows):
    return (statistics.mean(float(r["rating"]) for r in rows),
            float(statistics.median(int(r["ratings_count"]) for r in rows)))


def ns(x):
    return repr(x) if isinstance(x, float) else str(x)


def read_csv(p):
    with p.open(encoding="utf-8-sig", newline="") as fh:
        rd = csv.DictReader(fh)
        return rd.fieldnames, list(rd)


def write_csv(p, cols, rows):
    with p.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def find_stat_row(ws, label="Goodreads"):
    for r in range(1, ws.max_row + 1):
        if ws.cell(r, 1).value == label and isinstance(ws.cell(r, 2).value, (int, float)):
            return r
    raise AssertionError("ligne de statistiques introuvable")


def add_correction_row(ws):
    r = ws.max_row + 2
    ws.cell(r, 1, "Correction 27/09/2026").font = Font(bold=True)
    ws.cell(r, 2, NOTE_CORRECTION).alignment = Alignment(wrap_text=True, vertical="top")
    return r


def permute_sheet(ws, values_rows: list[list], ncols: int) -> int:
    """Réécrit toute la zone de données et efface les lignes résiduelles.

    Renvoie le numéro de la dernière ligne de données écrite.
    """
    old_max = ws.max_row
    for i, vals in enumerate(values_rows, start=2):
        for j in range(1, ncols + 1):
            ws.cell(i, j, vals[j - 1])
    new_max = 1 + len(values_rows)
    if old_max > new_max:
        ws.delete_rows(new_max + 1, old_max - new_max)
    return new_max


def snapshot_rows(ws, ncols):
    out = []
    for i in range(2, ws.max_row + 1):
        out.append([ws.cell(i, j).value for j in range(1, ncols + 1)])
    return out


def reset_cf(ws, ranges):
    ws.conditional_formatting = ConditionalFormattingList()
    for rng, lo in ranges:
        ws.conditional_formatting.add(
            rng, ColorScaleRule(start_type="num", start_value=lo, start_color="F8696B",
                                mid_type="num", mid_value=(lo + 100) / 2, mid_color="FFEB84",
                                end_type="num", end_value=100, end_color="63BE7B"))


# ===========================================================================
# 1) Percentiles bruts — 22/09
# ===========================================================================
def patch_tous_22():
    p = backup("percentiles_tous_corpus_principaux_2026-09-22.csv")
    cols, rows = read_csv(p)
    kept = [r for r in rows if not is_target(r)]
    removed = [r for r in rows if is_target(r)]
    assert len(removed) == 1
    REMOVED_INFO.update({k: removed[0][k] for k in ("title", "rating", "ratings_count",
                                                    "percentile_midrank", "raw_rank_mid")})
    gr = [r for r in kept if r["platform"] == "Goodreads"]
    sc = [r for r in kept if r["platform"] == "SensCritique"]
    c_gr, m_gr = params(gr)
    st = midrank_stats([float(r["rating"]) for r in gr])
    for r in gr:
        s = st[float(r["rating"])]
        r.update(reference_n=str(len(gr)), percentile_midrank=ns(s["percentile"]),
                 raw_rank_mid=ns(s["rank_mid"]), raw_rank_range=s["rank_range"])
    write_csv(p, cols, kept)
    LOG.append(f"[CSV brut 22/09] {len(rows)}→{len(kept)} lignes ; GR {len(gr)} (C={c_gr:.12f}, m={m_gr}) ; SC {len(sc)}")

    j = backup("percentiles_tous_corpus_principaux_2026-09-22.json")
    d = json.loads(j.read_text(encoding="utf8"))
    d["rows"] = [r for r in d["rows"] if not is_target(r)]
    for r in d["rows"]:
        if r["platform"] == "Goodreads":
            s = st[r["rating"]]
            r.update(reference_n=len(gr), percentile_midrank=s["percentile"],
                     raw_rank_mid=s["rank_mid"], raw_rank_range=s["rank_range"])
    gr_r = [float(r["rating"]) for r in gr]
    cand = {"N": len(gr), "n": len(gr), "C": c_gr, "m": m_gr, "min": min(gr_r), "max": max(gr_r),
            "mean": c_gr, "median": statistics.median(gr_r), "q1": q7(gr_r, .25), "q3": q7(gr_r, .75),
            "p90": q7(gr_r, .90), "p95": q7(gr_r, .95), "p99": q7(gr_r, .99),
            "total_votes": sum(int(r["ratings_count"]) for r in gr)}
    summ = d["summary"]["Goodreads"]
    summ.update({k: v for k, v in cand.items() if k in summ})
    j.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf8")
    LOG.append(f"[JSON brut 22/09] GR N={len(gr)} ; summary mis à jour ({sorted(set(cand) & set(summ))})")

    x = backup("Percentiles_tous_corpus_principaux_2026-09-22.xlsx")
    wb = load_workbook(x)
    ws = wb["Synthèse"]
    ws["B3"] = f"Goodreads N={len(gr)} ; SensCritique N={len(sc)}. Plateformes séparées, œuvres principales seulement."
    ws["B5"] = ("Corpus de référence au 20 septembre 2026 ; Tolkien et comptes directs indiqués relevés le "
                "22 septembre 2026. Retrait de « ONE PIECE 116 » (chapitre, pas un tome) le 27 septembre 2026.")
    r = find_stat_row(ws)
    for col, val in zip(range(2, 9), [len(gr), c_gr, m_gr, q7(gr_r, .50), q7(gr_r, .90), q7(gr_r, .95), max(gr_r)]):
        ws.cell(r, col, val)
    add_correction_row(ws)
    sh = wb["Goodreads"]
    tr = next(i for i in range(2, sh.max_row + 1)
              if sh.cell(i, 2).value == SERIE and str(sh.cell(i, 3).value) == POS)
    sh.delete_rows(tr, 1)
    for i in range(2, sh.max_row + 1):
        s = st[float(sh.cell(i, 5).value)]
        sh.cell(i, 7, s["percentile"]); sh.cell(i, 8, s["rank_range"])
    sh.auto_filter.ref = f"A1:I{sh.max_row}"
    reset_cf(sh, [(f"G2:G{sh.max_row}", 0)])
    wb.save(x)
    LOG.append(f"[XLSX brut 22/09] Synthèse (N,C,m,médiane,P90,P95,max) ; feuille Goodreads {sh.max_row - 1} lignes, P et rangs recalculés")


# ===========================================================================
# 2) Percentiles bruts — 20/09
# ===========================================================================
def patch_tous_20():
    p = backup("percentiles_tous_corpus_principaux_2026-09-20.csv")
    cols, rows = read_csv(p)
    kept = [r for r in rows if not is_target(r)]
    assert len(rows) - len(kept) == 1
    gr = [r for r in kept if r["platform"] == "Goodreads"]
    sc = [r for r in kept if r["platform"] == "SensCritique"]
    st = midrank_stats([float(r["rating"]) for r in gr])
    for r in gr:
        s = st[float(r["rating"])]
        r.update(reference_n=str(len(gr)), percentile_midrank=ns(s["percentile"]),
                 percentile_band=s["band"], descending_rank_mid=ns(s["rank_mid"]),
                 descending_rank_range=s["rank_range"], strictly_lower=ns(s["lower"]),
                 tied=ns(s["tied"]), strictly_higher=ns(s["higher"]),
                 strictly_better_pct=ns(s["better_pct"]))
    write_csv(p, cols, kept)
    LOG.append(f"[CSV brut 20/09] {len(rows)}→{len(kept)} lignes ; GR {len(gr)} ; SC {len(sc)}")

    j = backup("percentiles_tous_corpus_principaux_2026-09-20.json")
    d = json.loads(j.read_text(encoding="utf8"))
    d["rows"] = [r for r in d["rows"] if not is_target(r)]
    for r in d["rows"]:
        if r["platform"] == "Goodreads":
            s = st[r["rating"]]
            r.update(reference_n=len(gr), percentile_midrank=s["percentile"], percentile_band=s["band"],
                     descending_rank_mid=s["rank_mid"], descending_rank_range=s["rank_range"],
                     strictly_lower=s["lower"], tied=s["tied"], strictly_higher=s["higher"],
                     strictly_better_pct=s["better_pct"])
    if isinstance(d.get("scope"), dict):
        d["scope"]["Goodreads"] = len(gr)
    os_ = d["summary"]["Goodreads"]
    gr_r = [float(r["rating"]) for r in gr]
    os_.update({k: v for k, v in {"n": len(gr), "min": min(gr_r), "max": max(gr_r), "mean": statistics.mean(gr_r),
                                  "median": statistics.median(gr_r), "q1": q7(gr_r, .25), "q3": q7(gr_r, .75),
                                  "p90": q7(gr_r, .90), "p95": q7(gr_r, .95), "p99": q7(gr_r, .99)}.items() if k in os_})
    j.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf8")
    LOG.append(f"[JSON brut 20/09] scope GR → {len(gr)} ; summary mis à jour")

    x = backup("Percentiles_tous_corpus_principaux_2026-09-20.xlsx")
    wb = load_workbook(x)
    ws = wb["Synthèse"]
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row):
        for c in row:
            if isinstance(c.value, str) and "561 tomes de manga" in c.value:
                c.value = c.value.replace("561 tomes de manga", "560 tomes de manga")
    r = find_stat_row(ws)
    for col, val in zip(range(2, 12), [len(gr), min(gr_r), q7(gr_r, .25), statistics.median(gr_r),
                                       q7(gr_r, .75), q7(gr_r, .90), q7(gr_r, .95), q7(gr_r, .99),
                                       max(gr_r), statistics.mean(gr_r)]):
        ws.cell(r, col, val)
    for rr in range(1, ws.max_row + 1):
        if ws.cell(rr, 1).value == "Goodreads" and ws.cell(rr, 2).value in (
                "Manga", "Fantasy — cycle principal", "Arthur — texte fondateur", "Web-serial"):
            ws.cell(rr, 3, sum(1 for z in gr if z["family"] == ws.cell(rr, 2).value))
    add_correction_row(ws)
    sh = wb["Goodreads"]
    tr = next(i for i in range(2, sh.max_row + 1)
              if sh.cell(i, 2).value == SERIE and str(sh.cell(i, 3).value) == POS)
    sh.delete_rows(tr, 1)
    for i in range(2, sh.max_row + 1):
        s = st[float(sh.cell(i, 5).value)]
        for col, key in ((7, "percentile"), (8, "band"), (9, "rank_mid"), (10, "rank_range"),
                         (11, "higher"), (12, "better_pct")):
            sh.cell(i, col, s[key])
        sh.cell(i, 13, len(gr))
    sh.auto_filter.ref = f"A1:N{sh.max_row}"
    reset_cf(sh, [(f"G2:G{sh.max_row}", 0)])
    wb.save(x)
    LOG.append(f"[XLSX brut 20/09] Synthèse recalculée + composition 560 mangas ; feuille Goodreads {sh.max_row - 1} lignes")


# ===========================================================================
# 3) Classement robuste — 22/09
# ===========================================================================
def patch_votes_22():
    p = backup("percentiles_avec_nombre_votes_2026-09-22.csv")
    cols, rows = read_csv(p)
    kept = [r for r in rows if not is_target(r)]
    gr = [r for r in kept if r["platform"] == "Goodreads"]
    sc = [r for r in kept if r["platform"] == "SensCritique"]
    c_gr, m_gr = params(gr)
    st = midrank_stats([float(r["rating"]) for r in gr])
    old = {id(r): (float(r["adjusted_rating"]), float(r["adjusted_percentile"])) for r in gr}
    adj = {id(r): (int(r["ratings_count"]) * float(r["rating"]) + m_gr * c_gr) / (int(r["ratings_count"]) + m_gr) for r in gr}
    ast = midrank_stats(list(adj.values()))
    for r in gr:
        s, a = st[float(r["rating"])], adj[id(r)]
        r.update(reference_n=str(len(gr)), percentile_midrank=ns(s["percentile"]),
                 raw_rank_mid=ns(s["rank_mid"]), raw_rank_range=s["rank_range"],
                 adjusted_rating=ns(a), adjusted_percentile=ns(ast[a]["percentile"]),
                 adjusted_rank_mid=ns(ast[a]["rank_mid"]), adjusted_rank_range=ast[a]["rank_range"])
    gr_sorted = sorted(gr, key=lambda r: (-adj[id(r)], -float(r["rating"]), r["series"], r["position"]))
    write_csv(p, cols, gr_sorted + sc)
    maxd = max(abs(adj[id(r)] - old[id(r)][0]) for r in gr)
    maxdp = max(abs(ast[adj[id(r)]]["percentile"] - old[id(r)][1]) for r in gr)
    LOG.append(f"[CSV robuste 22/09] {len(rows)}→{len(kept)} ; C={c_gr:.12f}, m={m_gr} ; "
               f"Δmax score={maxd:.2e}, Δmax P ajusté={maxdp:.4f} pts ; export retrié par score ajusté")

    j = backup("percentiles_avec_nombre_votes_2026-09-22.json")
    d = json.loads(j.read_text(encoding="utf8"))
    d["rows"] = [r for r in d["rows"] if not is_target(r)]
    for r in d["rows"]:
        if r["platform"] == "Goodreads":
            s = st[r["rating"]]
            a = (r["ratings_count"] * r["rating"] + m_gr * c_gr) / (r["ratings_count"] + m_gr)
            r.update(reference_n=len(gr), percentile_midrank=s["percentile"], raw_rank_mid=s["rank_mid"],
                     raw_rank_range=s["rank_range"], adjusted_rating=a,
                     adjusted_percentile=ast[a]["percentile"], adjusted_rank_mid=ast[a]["rank_mid"],
                     adjusted_rank_range=ast[a]["rank_range"])
    if isinstance(d.get("summary"), dict) and isinstance(d["summary"].get("Goodreads"), dict):
        sm = d["summary"]["Goodreads"]
        sm.update({k: v for k, v in {"N": len(gr), "n": len(gr), "C": c_gr, "m": m_gr,
                                     "total_votes": sum(int(r["ratings_count"]) for r in gr)}.items() if k in sm})
    j.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf8")
    LOG.append("[JSON robuste 22/09] lignes filtrées, score ajusté recalculé")

    x = backup("Percentiles_avec_nombre_de_votes_2026-09-22.xlsx")
    wb = load_workbook(x)
    ws = wb["Synthèse"]
    ws["B3"] = f"Goodreads N={len(gr)} ; SensCritique N={len(sc)}. Plateformes séparées, œuvres principales seulement."
    ws["B5"] = ("Corpus de référence au 20 septembre 2026 ; Tolkien et comptes directs indiqués relevés le "
                "22 septembre 2026. Retrait de « ONE PIECE 116 » (chapitre, pas un tome) le 27 septembre 2026.")
    r = find_stat_row(ws)
    gr_r = sorted(float(z["rating"]) for z in gr)
    for col, val in zip(range(2, 9), [len(gr), c_gr, m_gr, statistics.median(gr_r), q7(gr_r, .90), q7(gr_r, .95), max(gr_r)]):
        ws.cell(r, col, val)
    add_correction_row(ws)
    sh = wb["Goodreads"]
    rows_vals = snapshot_rows(sh, 12)
    tr = next(i for i, v in enumerate(rows_vals, start=2)
              if v[1] == SERIE and str(v[2]) == POS)
    rows_vals = [v for i, v in enumerate(rows_vals, start=2) if i != tr]
    for v in rows_vals:
        v[6] = (v[5] * v[4] + m_gr * c_gr) / (v[5] + m_gr)
    rows_vals.sort(key=lambda v: -v[6])
    for v in rows_vals:
        a = v[6]; s = st[float(v[4])]
        v[7] = ast[a]["percentile"]; v[8] = ast[a]["rank_range"]
        v[9] = s["percentile"]; v[10] = s["rank_range"]
    new_max = permute_sheet(sh, rows_vals, 12)
    sh.auto_filter.ref = f"A1:L{new_max}"
    reset_cf(sh, [(f"G2:G{new_max}", 0)])
    wb.save(x)
    LOG.append(f"[XLSX robuste 22/09] feuille Goodreads {len(rows_vals)} lignes retriées par score ajusté ; toutes colonnes recalculées")


# ===========================================================================
# 4) Classement robuste — 20/09
# ===========================================================================
def patch_votes_20():
    p = backup("percentiles_avec_nombre_votes_2026-09-20.csv")
    cols, rows = read_csv(p)
    kept = [r for r in rows if not is_target(r)]
    gr = [r for r in kept if r["platform"] == "Goodreads"]
    sc = [r for r in kept if r["platform"] == "SensCritique"]
    c_gr, m_gr = params(gr)
    st = midrank_stats([float(r["rating"]) for r in gr])
    total = sum(int(r["ratings_count"]) for r in gr)
    by_rating = Counter()
    for r in gr:
        by_rating[float(r["rating"])] += int(r["ratings_count"])
    adj = {id(r): (int(r["ratings_count"]) * float(r["rating"]) + m_gr * c_gr) / (int(r["ratings_count"]) + m_gr) for r in gr}
    ast = midrank_stats(list(adj.values()))
    for r in gr:
        s = st[float(r["rating"])]; a = adj[id(r)]
        lo = sum(c for v, c in by_rating.items() if v < float(r["rating"]))
        wp = 100 * (lo + 0.5 * by_rating[float(r["rating"])]) / total
        r.update(percentile_midrank=ns(s["percentile"]), weighted_percentile=ns(wp),
                 delta_weighted_vs_raw=ns(wp - s["percentile"]), adjusted_rating=ns(a),
                 adjusted_percentile=ns(ast[a]["percentile"]),
                 delta_adjusted_vs_raw=ns(ast[a]["percentile"] - s["percentile"]),
                 adjusted_rank_mid=ns(ast[a]["rank_mid"]), adjusted_rank_range=ast[a]["rank_range"])
    write_csv(p, cols, kept)
    LOG.append(f"[CSV robuste 20/09] {len(rows)}→{len(kept)} ; C={c_gr:.12f}, m={m_gr}, votes GR {total}")

    x = backup("Percentiles_avec_nombre_de_votes_2026-09-20.xlsx")
    wb = load_workbook(x)
    ws = wb["Synthèse"]
    r = find_stat_row(ws)

    def wq(q):
        cum = 0
        for z in sorted(gr, key=lambda z: float(z["rating"])):
            cum += int(z["ratings_count"])
            if cum >= q * total:
                return float(z["rating"])
    for col, val in zip(range(2, 11), [len(gr), total, c_gr,
                                       sum(float(z["rating"]) * int(z["ratings_count"]) for z in gr) / total,
                                       c_gr, m_gr, wq(.50), wq(.90), wq(.95)]):
        ws.cell(r, col, val)
    add_correction_row(ws)
    sh = wb["Goodreads"]
    rows_vals = snapshot_rows(sh, 14)
    tr = next(i for i, v in enumerate(rows_vals, start=2) if v[1] == SERIE and str(v[2]) == POS)
    rows_vals = [v for i, v in enumerate(rows_vals, start=2) if i != tr]
    for v in rows_vals:
        v[9] = (v[5] * v[4] + m_gr * c_gr) / (v[5] + m_gr)
    rows_vals.sort(key=lambda v: -v[9])
    for v in rows_vals:
        a = v[9]; R = float(v[4]); s = st[R]
        lo = sum(c for x, c in by_rating.items() if x < R)
        wp = 100 * (lo + 0.5 * by_rating[R]) / total
        v[6] = s["percentile"]; v[7] = wp; v[8] = wp - s["percentile"]
        v[10] = ast[a]["percentile"]; v[11] = ast[a]["percentile"] - s["percentile"]
        v[12] = ast[a]["rank_range"]
    new_max = permute_sheet(sh, rows_vals, 14)
    sh.auto_filter.ref = f"A1:N{new_max}"
    reset_cf(sh, [(f"G2:G{new_max}", 0), (f"H2:H{new_max}", 50), (f"K2:K{new_max}", 50)])
    wb.save(x)
    LOG.append(f"[XLSX robuste 20/09] feuille Goodreads {len(rows_vals)} lignes retriées ; quantiles pondérés et rangs ajustés recalculés")


if __name__ == "__main__":
    patch_tous_22()
    patch_tous_20()
    patch_votes_22()
    patch_votes_20()
    print("RETIRÉ :", json.dumps(REMOVED_INFO, ensure_ascii=False))
    print("\n".join(LOG))
