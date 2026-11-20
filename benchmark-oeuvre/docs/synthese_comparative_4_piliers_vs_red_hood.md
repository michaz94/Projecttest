# Synthèse comparative — Poids du Visuel/Dessin vs Monde/Univers, Personnages et Intrigue : *Fullmetal Alchemist*, *Hunter × Hunter*, *Jujutsu Kaisen*, *One Piece* face à *The Hunters Guild: Red Hood*

**Date** : 2 octobre 2026  
**Fichiers JSON constitués et sauvegardés dans `/home/user/benchmark_4_piliers/`** :
1. `goodreads_tomes_1_2_5_series.json` — **11 volumes, 311 critiques textuelles intégrales** extraites du JSON `__NEXT_DATA__` de Goodreads (Tomes 1 et 2 de *Fullmetal Alchemist*, *Hunter × Hunter*, *Jujutsu Kaisen*, *One Piece*, et Tomes 1, 2 et 3 de *Red Hood*).
2. `mal_reviews_5_series.json` — **240 critiques intégrales** extraites de MyAnimeList (60 *Fullmetal Alchemist*, 40 *Hunter × Hunter*, 60 *Jujutsu Kaisen*, 60 *One Piece*, 20 *Red Hood*) avec métadonnées (`review_id`, `author`, `date`, `verdict`, `is_preliminary`, `rating_10`, `tags`, `text`).
3. `reddit_jjk_2018_ch1_18.json` — **7 fils `[DISC]` (164 commentaires, 88 comptes uniques)** de `r/manga` publiés entre mars et juillet 2018 sur les chapitres 1 à 18 de *Jujutsu Kaisen* (comparés aux **18 fils `[DISC]` / 4 432 commentaires / 1 382 comptes uniques** de *Red Hood*).

---

## 1. Vue d'ensemble : notes moyennes et volumes d'évaluation (Goodreads Tomes 1–2 & MyAnimeList)

| Série | Tome 1 Goodreads (Note /5 & votes) | Tome 2 Goodreads (Note /5 & votes) | Évolution T1 → T2 | Critiques T1+T2 extraites | Verdict MAL sur l'échantillon extrait (`N = 240`) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Fullmetal Alchemist** | **4,54 / 5** *(198 634 votes)* | **4,51 / 5** *(23 057 votes)* | **-0,03 pt** *(stable)* | 60 *(30 + 30)* | **95,0 % Recommended** *(57 Rec / 1 Mix / 2 NotRec sur 60)* |
| **Hunter × Hunter** | **4,53 / 5** *(70 744 votes)* | **4,42 / 5** *(7 561 votes)* | **-0,11 pt** *(solide)* | 60 *(30 + 30)* | **90,0 % Recommended** *(36 Rec / 4 Mix / 0 NotRec sur 40)* |
| **Jujutsu Kaisen** | **4,49 / 5** *(73 124 votes)* | **4,46 / 5** *(38 692 votes)* | **-0,03 pt** *(stable)* | 60 *(30 + 30)* | **70,0 % Rec en 2019–2020** *(7/10)* vs **30,0 % au global** *(biais post-fin 2024 : 18 Rec / 21 Mix / 21 NotRec)* |
| **One Piece** | **4,49 / 5** *(194 014 votes)* | **4,36 / 5** *(34 869 votes)* | **-0,13 pt** *(solide)* | 60 *(30 + 30)* | **61,7 % Recommended** *(37 Rec / 11 Mix / 12 NotRec sur 60)* |
| **Red Hood** *(benchmark)* | **3,62 / 5** *(439 votes)* | **3,48 / 5** *(232 votes)* *(T3 : **3,29**)* | **-0,14 pt** *(puis -0,19 pt au T3)* | 71 *(30 + 22 + 19)* | **45,0 % Recommended** *(9 Rec / 7 Mix / 4 NotRec sur 20)* |

---

## 2. Couche 1 — Ce qui attire les lecteurs dès le Tome 1 et le Tome 2 (Goodreads JSON, `N = 311`)

### 2.1. Tableau comparatif sur le Tome 1 seul (`30 critiques par série`, ensemble complet vs sous-ensemble anglophone)

| Série (Tome 1 Goodreads) | Visuel / Dessin / Designs *(Total)* | ...dont **Éloge pur** vs **Réserve/Critique** | Monde / Univers / Système de pouvoir | Personnages / Duo / Trio | Histoire / Rythme / Émotion / Action | Mentionne l'Anime | Part du Visuel sur le sous-ensemble 100 % anglophone |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Red Hood — Tome 1** (`id=60433200`) | **56,7 %** *(17/30)* | **46,7 %** éloge *(14)* / **10,0 %** critique *(3)* | **63,3 %** *(19/30)* | **63,3 %** *(19/30)* | **66,7 %** *(20/30)* | **3,3 %** *(1/30)* | **58,6 %** *(17/29)* |
| **Fullmetal Alchemist — Tome 1** (`id=870`) | **30,0 %** *(9/30)* | **30,0 %** éloge *(9)* / **0,0 %** réserve *(0)* | **70,0 %** *(21/30)* | **73,3 %** *(22/30)* | **63,3 %** *(19/30)* | **30,0 %** *(9/30)* | **36,4 %** *(8/22)* |
| **One Piece — Tome 1** (`id=1237398`) | **26,7 %** *(8/30)* | **23,3 %** éloge *(7)* / **3,3 %** réserve *(1)* | **53,3 %** *(16/30)* | **60,0 %** *(18/30)* | **70,0 %** *(21/30)* | **33,3 %** *(10/30)* | **28,0 %** *(7/25)* |
| **Hunter × Hunter — Tome 1** (`id=18249913`) | **23,3 %** *(7/30)* | **23,3 %** éloge *(7)* / **0,0 %** réserve *(0)* | **33,3 %** *(10/30)* | **56,7 %** *(17/30)* | **50,0 %** *(15/30)* | **33,3 %** *(10/30)* | **29,2 %** *(7/24)* |
| **Jujutsu Kaisen — Tome 1** (`id=44451887`) | **16,7 %** *(5/30)* | **16,7 %** éloge *(5)* / **0,0 %** réserve *(0)* | **40,0 %** *(12/30)* | **70,0 %** *(21/30)* | **50,0 %** *(15/30)* | **33,3 %** *(10/30)* | **17,9 %** *(5/28)* |

### 2.2. Cumul Tomes 1 + 2 sur Goodreads

| Série (Tomes 1 + 2 cumulés) | Visuel / Dessin *(Total)* | Monde / Univers / Système | Personnages / Duo / Trio | Histoire / Rythme / Émotion | Mentionne l'Anime |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Red Hood (T1+T2, `N = 52`)** | **40,4 %** *(21/52)* | **46,2 %** *(24/52)* | **53,8 %** *(28/52)* | **57,7 %** *(30/52)* | **3,8 %** *(2/52)* |
| **Fullmetal Alchemist (T1+T2, `N = 60`)** | **23,3 %** *(14/60)* | **60,0 %** *(36/60)* | **66,7 %** *(40/60)* | **61,7 %** *(37/60)* | **18,3 %** *(11/60)* |
| **One Piece (T1+T2, `N = 60`)** | **23,3 %** *(14/60)* | **35,0 %** *(21/60)* | **58,3 %** *(35/60)* | **65,0 %** *(39/60)* | **21,7 %** *(13/60)* |
| **Hunter × Hunter (T1+T2, `N = 60`)** | **21,7 %** *(13/60)* | **23,3 %** *(14/60)* | **61,7 %** *(37/60)* | **45,0 %** *(27/60)* | **25,0 %** *(15/60)* |
| **Jujutsu Kaisen (T1+T2, `N = 60`)** | **11,7 %** *(7/60)* | **36,7 %** *(22/60)* | **66,7 %** *(40/60)* | **41,7 %** *(25/60)* | **25,0 %** *(15/60)* |

---

## 3. Couche 2 — Analyse des 240 critiques MyAnimeList (`mal_reviews_5_series.json`) : biais de structure, poids de l'anime et réserves sur le dessin

| Série (Fiche Manga MAL) | Mentions du Dessin (`Art`) | ...dont **Positif pur** | ...dont **Réserve / Critique** *(brouillon, simple, confus)* | Part des mentions du dessin comportant une réserve | Monde / Univers / Système | Personnages | Histoire / Action | Mentionne l'Anime |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Red Hood** (`N = 20`) | **90,0 %** *(18/20)* | **70,0 %** *(14/20)* | **20,0 %** *(4/20)* | **22,2 %** *(4/18)* | **85,0 %** *(17/20)* | **95,0 %** *(19/20)* | **100,0 %** *(20/20)* | **10,0 %** *(2/20)* |
| **One Piece** (`N = 60`) | **75,0 %** *(45/60)* | **50,0 %** *(30/60)* | **25,0 %** *(15/60)* | **33,3 %** *(15/45)* | **78,3 %** *(47/60)* | **95,0 %** *(57/60)* | **100,0 %** *(60/60)* | **43,3 %** *(26/60)* |
| **Fullmetal Alchemist** (`N = 60`) | **66,7 %** *(40/60)* | **51,7 %** *(31/60)* | **15,0 %** *(9/60)* | **22,5 %** *(9/40)* | **81,7 %** *(49/60)* | **95,0 %** *(57/60)* | **100,0 %** *(60/60)* | **55,0 %** *(33/60)* |
| **Jujutsu Kaisen** (`N = 60`) | **60,0 %** *(36/60)* | **35,0 %** *(21/60)* | **25,0 %** *(15/60)* | **41,7 %** *(15/36)* | **73,3 %** *(44/60)* | **96,7 %** *(58/60)* | **100,0 %** *(60/60)* | **30,0 %** *(18/60)* |
| **Hunter × Hunter** (`N = 40`) | **55,0 %** *(22/40)* | **37,5 %** *(15/40)* | **17,5 %** *(7/40)* | **31,8 %** *(7/22)* | **70,0 %** *(28/40)* | **97,5 %** *(39/40)* | **100,0 %** *(40/40)* | **45,0 %** *(18/40)* |

---

## 4. Couche 3 — Réception hebdomadaire à chaud sur Reddit `r/manga` : *Jujutsu Kaisen* (Ch. 1–18, 2018) vs *Red Hood* (Ch. 1–18, 2021)

| Indicateur (`r/manga` — Chapitres 1 à 18) | *Jujutsu Kaisen* (mars–juillet 2018, `N = 164` comm. / `88` comptes) | *Red Hood* (juin–novembre 2021, `N = 4 432` comm. / `1 382` comptes) | *Red Hood* — Chapitre 1 seul (`N = 446` comm. / `185` top-level) |
| :--- | :---: | :---: | :---: |
| **Rang 1 des sujets discutés** | **Histoire / Action / Rythme : 22,6 %** *(37/164)* | **Visuel / Dessin / Designs : 16,2 %** *(717/4 432)* — **30,5 %** des comptes | **Visuel / Dessin / Designs : 31,6 %** *(141/446)* — **48,1 %** des top-level |
| **Personnages / Équipe / Antagonistes** | **20,7 %** *(34/164)* *(Yuji, Megumi, Gojo, Sukuna)* | *Subordonné au design de Grimm / Debonair / Crab* | *Grimm & loups-garous d'abord commentés sous l'angle visuel* |
| **Monde / Univers / Système de pouvoir** | **15,9 %** *(26/164)* *(Curses, Exorcisme, Territoires)* | **10,7 %** *(474/4 432)* — **20,7 %** des comptes | **23,3 %** *(104/446)* — **32,4 %** des top-level |
| **Visuel / Dessin / Découpage** | **12,2 %** *(20/164)* *(4e position)* | **16,2 %** *(717/4 432)* *(1re position)* | **31,6 %** *(141/446)* / **48,1 %** des top-level *(1re position)* |
