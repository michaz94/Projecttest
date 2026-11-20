# Analyse lexicale du corpus Red Hood

`analyse_red_hood.py` compte la fréquence de thèmes dans les 4 432 commentaires
Reddit de Red Hood (18 chapitres) extraits de `posts_scores_commentaires.html`.

## Rejouer

```bash
curl -sL -o posts.html "https://raw.githubusercontent.com/michaz94/Projecttest/main/Benchmark%20Oeuvre/Red%20Hood/posts_scores_commentaires.html"
python3 -c "import re,json;h=open('posts.html',encoding='utf-8',errors='replace').read();m=re.search(r'<script[^>]*id=.data.[^>]*>(.*?)</script>',h,re.S);json.dump(json.loads(m.group(1)),open('data.json','w'))"
python3 analyse_red_hood.py
```

## Limites, à lire avant d'utiliser les chiffres

- **Appariement lexical, pas compréhension.** Un commentaire qui contient « slow »
  peut dire « ce n'est pas trop lent ». Le sens n'est pas évalué.
- **Commentateurs ≠ lecteurs.** Les gens qui commentent sur Reddit ne sont pas
  un échantillon du lectorat.
- **Une occurrence ≠ un avis.** Un thème peut être cité pour être contredit.
- **Fréquence ≠ cause.** Ce qui se dit souvent n'est pas ce qui fait décrocher.
- Les faux positifs ont été vérifiés manuellement pour le thème « annulation »
  (9 occurrences sur 10 authentiques dans un tirage aléatoire) ; pas pour les autres.
