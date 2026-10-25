import csv
import json
import re
import time
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import requests
from bs4 import BeautifulSoup


BASE = "https://rule34.xxx/index.php"
SAVED_PAGES = 107
SAVED_TAGS = 2140
SAVED_LOWEST_COUNT = 31145
SAVED_CHARACTERS = [{'name': 'pokemon_(species)', 'count': 597707, 'type': 'Character ( edit )', 'character': True}, {'name': 'original_character', 'count': 562905, 'type': 'Character ( edit )', 'character': True}, {'name': 'pok&eacute;mon_(species)', 'count': 187517, 'type': 'Character ( edit )', 'character': True}, {'name': 'oc', 'count': 144292, 'type': 'Character ( edit )', 'character': True}, {'name': 'eeveelution', 'count': 85859, 'type': 'Character ( edit )', 'character': True}, {'name': 'fan_character', 'count': 82727, 'type': 'Character ( edit )', 'character': True}, {'name': 'character_request', 'count': 65923, 'type': 'Character ( edit )', 'character': True}, {'name': 'generation_1_pokemon', 'count': 59942, 'type': 'Character ( edit )', 'character': True}, {'name': 'nami_(one_piece)', 'count': 56885, 'type': 'Character ( edit )', 'character': True}, {'name': 'tifa_lockhart', 'count': 53420, 'type': 'Character ( edit )', 'character': True}, {'name': 'princess_peach', 'count': 50129, 'type': 'Character ( edit )', 'character': True}, {'name': 'legendary_pokemon', 'count': 49958, 'type': 'Character ( edit )', 'character': True}, {'name': 'robloxian', 'count': 49608, 'type': 'Character ( edit )', 'character': True}, {'name': 'generation_4_pokemon', 'count': 48446, 'type': 'Character ( edit )', 'character': True}, {'name': 'digimon_(species)', 'count': 47706, 'type': 'Character ( edit )', 'character': True}, {'name': 'rouge_the_bat', 'count': 45037, 'type': 'Character ( edit )', 'character': True}, {'name': 'hyuuga_hinata', 'count': 42866, 'type': 'Character ( edit )', 'character': True}, {'name': 'loona_(helluva_boss)', 'count': 42510, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'yorha_2b', 'count': 42454, 'type': 'Character ( edit )', 'character': True}, {'name': 'amy_rose', 'count': 41365, 'type': 'Character ( edit )', 'character': True}, {'name': 'gardevoir', 'count': 41237, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'hatsune_miku', 'count': 40842, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'chun-li', 'count': 40023, 'type': 'Character ( edit )', 'character': True}, {'name': 'raven_(dc)', 'count': 39582, 'type': 'Character ( edit )', 'character': True}, {'name': 'sakura_haruno', 'count': 39451, 'type': 'Character ( edit )', 'character': True}, {'name': 'tsunade', 'count': 39326, 'type': 'Character ( edit )', 'character': True}, {'name': 'princess_zelda', 'count': 39082, 'type': 'Character ( edit )', 'character': True}, {'name': 'lucario', 'count': 37568, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'sonic_the_hedgehog', 'count': 36970, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'samus_aran', 'count': 36750, 'type': 'Character ( edit )', 'character': True}, {'name': 'd.va', 'count': 35323, 'type': 'Character ( edit )', 'character': True}, {'name': 'uzumaki_naruto', 'count': 34994, 'type': 'Character ( edit )', 'character': True}, {'name': 'nico_robin', 'count': 34138, 'type': 'Character ( edit )', 'character': True}, {'name': 'makima_(chainsaw_man)', 'count': 33343, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'renamon', 'count': 33274, 'type': 'Character ( edit )', 'character': True}, {'name': 'ochako_uraraka', 'count': 33046, 'type': 'Character ( edit )', 'character': True}, {'name': 'generation_3_pokemon', 'count': 33044, 'type': 'Character ( edit )', 'character': True}, {'name': 'anon', 'count': 32955, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'link', 'count': 32889, 'type': 'Character ( edit )', 'character': True}, {'name': 'lara_croft', 'count': 32532, 'type': 'Character ( edit )', 'character': True}, {'name': 'mobian_(species)', 'count': 31722, 'type': 'Character, ambiguous ( edit )', 'character': True}, {'name': 'widowmaker', 'count': 31708, 'type': 'Character ( edit )', 'character': True}]

def parse_rows(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = None
    for candidate in soup.find_all('table'):
        for tr in candidate.find_all('tr'):
            headers = [c.get_text(' ', strip=True).lower() for c in tr.find_all(['th', 'td'], recursive=False)]
            if headers[:3] == ['posts', 'name', 'type']:
                table = candidate
                break
        if table is not None:
            break
    if table is None:
        raise ValueError('Table Posts / Name / Type introuvable : blocage ou format différent. Aucun contournement tenté.')
    rows = []
    for tr in table.find_all('tr'):
        cells = tr.find_all(['td', 'th'], recursive=False)
        if not cells or [c.get_text(' ', strip=True).lower() for c in cells[:3]] == ['posts','name','type']:
            continue
        if len(cells) < 3:
            if tr.find('td'):
                raise ValueError('Ligne de tableau inattendue : arrêt sans ignorer silencieusement des tags.')
            continue
        number = re.sub(r'[\s,\u00a0]', '', cells[0].get_text(strip=True))
        if not number.isdigit():
            raise ValueError('Compteur illisible : arrêt pour éviter un classement incomplet.')
        link = None
        for anchor in cells[1].find_all('a', href=True):
            query = parse_qs(urlparse(anchor['href']).query)
            if query.get('page') == ['post'] and query.get('s') == ['list'] and 'tags' in query:
                link = anchor
                break
        if link is None:
            raise ValueError('Nom de tag introuvable dans une ligne : arrêt.')
        # Le texte visible peut masquer des caractères Unicode distinctifs.
        # parse_qs décode le paramètre une fois ; ne pas strip/normaliser ce nom.
        name = parse_qs(urlparse(link['href']).query, keep_blank_values=True)['tags'][0]
        if name == '':
            raise ValueError('Identifiant de tag vide : arrêt.')
        typ = cells[2].get_text(' ', strip=True)
        rows.append({'name': name, 'count': int(number), 'type': typ,
                     'character': bool(re.match(r'^Character\b', typ, flags=re.I))})
    return rows


def show_download_button(archive):
    try:
        from google.colab import files
        import ipywidgets as widgets
        from IPython.display import display
    except ImportError:
        print('Hors Colab : récupérez le ZIP au chemin indiqué ci-dessus.')
        return
    button = widgets.Button(
        description='Télécharger le ZIP', icon='download',
        button_style='success', layout=widgets.Layout(width='240px'))
    feedback = widgets.Output()

    def download_existing_zip(_):
        with feedback:
            feedback.clear_output(wait=True)
            if not Path(archive).is_file():
                print('ZIP indisponible : la session a peut-être été supprimée.')
                return
            print('Téléchargement du ZIP sauvegardé — aucune reprise de collecte.')
            try:
                files.download(archive)
            except Exception:
                print('Si rien ne se télécharge, utilisez le panneau Fichiers de Colab :', archive)

    button.on_click(download_existing_zip)
    display(button, feedback)
    print('Vous pouvez cliquer de nouveau sur le bouton sans relancer la collecte.')


def run_export(page_start, page_end, new_limit=20):
    if any(type(v) is not int for v in (page_start, page_end, new_limit)):
        raise ValueError('Les pages et la limite de nouveaux résultats doivent être des entiers.')
    if page_start < 1 or page_end < page_start or new_limit < 1:
        raise ValueError('Il faut : page de début ≥ 1, page de fin ≥ début, limite de nouveaux résultats ≥ 1.')
    started = time.monotonic()
    delay = 3
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    folder = (Path('/content') if Path('/content').is_dir() else Path.cwd()) / ('classement_tags_html_' + stamp)
    folder.mkdir(parents=True, exist_ok=True)
    resume = page_start == SAVED_PAGES + 1
    prefix_from_start = resume or page_start == 1
    characters = [dict(r) for r in SAVED_CHARACTERS] if resume else []
    historical_names = {r['name'] for r in characters}
    initial_character_count = len(characters)
    target = initial_character_count + new_limit
    initial_tags = SAVED_TAGS if resume else 0
    seen = set()
    validated_pages = 0
    last_count = SAVED_LOWEST_COUNT if resume else None
    requests_sent = 0
    retry_after = None
    target_obtained = False
    status = 'Collecte prête.'
    budget = page_end - page_start + 1
    if resume:
        scope = 'Préfixe trié repris après la page 107 ; anciens et nouveaux relevés réunis.'
    elif page_start == 1:
        scope = 'Nouveau parcours trié depuis la première page.'
    else:
        scope = f'Intervalle {page_start}–{page_end} seulement : rangs locaux, pas un classement global.'

    def ranked_rows():
        return sorted(characters, key=lambda r: (-r['count'], r['name']))

    def save():
        ranked = ranked_rows()
        new_rows = [r for r in ranked if r['name'] not in historical_names]
        selected_new = new_rows[:new_limit]
        selected = sorted([r for r in ranked if r['name'] in historical_names] + selected_new,
                          key=lambda r: (-r['count'], r['name']))
        outputs = [('personnages_collectes.csv', ranked, 1),
                   ('classement_anciens_et_nouveaux.csv', selected, 1),
                   ('nouveaux_resultats.csv', selected_new, initial_character_count + 1)]
        for filename, data, first_rank in outputs:
            dest = folder / filename
            temp = dest.with_suffix('.tmp')
            with temp.open('w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['rang_observe','name','count','type'])
                writer.writeheader()
                for rank, r in enumerate(data, first_rank):
                    writer.writerow({'rang_observe':rank, 'name':r['name'], 'count':r['count'], 'type':r['type']})
            temp.replace(dest)
        rouge = next(((i,r) for i,r in enumerate(ranked,1) if r['name']=='rouge_the_bat'), None)
        last_page = page_start + validated_pages - 1
        data = {
            'source': BASE + '?page=tags&s=list&tags=&order_by=index_count&sort=desc',
            'script_version': 'HTML-configurable-new-counter-resume107',
            'status': status,
            'page_start_requested': page_start,
            'maximum_pages': page_end,
            'maximum_additional_pages': budget,
            'target_results': target,
            'new_results_limit': new_limit,
            'initial_character_count': initial_character_count,
            'new_character_tags_read': len(new_rows),
            'new_results_selected': len(selected_new),
            'new_rows_beyond_limit_saved': max(0, len(new_rows)-new_limit),
            'target_obtained_in_collected_scope': target_obtained,
            'prefix_from_first_page': prefix_from_start,
            'target_obtained_from_sorted_prefix': target_obtained and prefix_from_start,
            'saved_results_included': resume,
            'initial_character_tags': len(SAVED_CHARACTERS) if resume else 0,
            'initial_pages': SAVED_PAGES if resume else 0,
            'additional_pages_read': validated_pages,
            'last_page_processed': last_page if validated_pages or resume else None,
            'pages_read': (SAVED_PAGES if resume else 0) + validated_pages,
            'next_page': page_start + validated_pages,
            'next_pid': (page_start + validated_pages - 1) * 20,
            'requests_sent_this_run': requests_sent,
            'tags_read': initial_tags + len(seen),
            'character_tags_found': len(characters),
            'lowest_count_read': last_count,
            'artificial_delay_seconds': delay,
            'retry_after_header': retry_after,
            'elapsed_seconds': round(time.monotonic()-started,1),
            'saved_utc': datetime.now(timezone.utc).isoformat(),
            'rouge_rank_observed': rouge[0] if rouge else None,
            'rouge_count': rouge[1]['count'] if rouge else None,
            'scope': scope,
            'limits': ['Toutes les catégories Character sont incluses ; alias non fusionnés.',
                       'Les anciens compteurs et les nouveaux ne proviennent pas d’un instantané figé.',
                       'Les anciens exports ne contiennent pas tous les noms des tags non-Character ; le contrôle historique de doublons est incomplet en reprise.',
                       'En changeant le départ pour une page différente de 108, les 42 anciens résultats ne sont pas incorporés : nouveau classement de la plage choisie.',
                       'Un départ autre que 1 ou 108 ne permet pas de conclure à un top global.',
                       'Les ex aequo sont départagés par nom dans les données collectées.',
                       'Le compteur de nouveaux résultats exclut les tags déjà intégrés.',
                       'Les pages sont lues entièrement ; des tags supplémentaires peuvent être sauvegardés dans personnages_collectes.csv, mais nouveaux_resultats.csv est limité au nombre demandé.']
        }
        dest = folder / 'rapport.json'
        temp = dest.with_suffix('.tmp')
        temp.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        temp.replace(dest)
        (folder / 'seen_tags.json').write_text(json.dumps(sorted(historical_names | seen),ensure_ascii=False),encoding='utf-8')

    print(f'Pages {page_start} à {page_end} incluses — {budget} pages maximum — limite : {new_limit} NOUVEAUX résultats.')
    print(scope)
    if resume:
        print('ATTENTION : les 42 anciens compteurs datent du 27 septembre 2026 et ne sont pas actualisés. Pour une nouvelle collecte actuelle, choisissez PAGE_DEBUT=1.')
    print(f'{initial_character_count} anciens résultats conservés, exclus du compteur. Pause : {delay} s.')
    print(f'Nouveaux résultats retenus : 0/{new_limit}. Aucune exclusion de catégorie.')
    if not prefix_from_start:
        print('ATTENTION : classement de cet intervalle uniquement ; rangs locaux.')
    print('Aucune image ni publication téléchargée. Aucune clé API nécessaire.')
    print('Dossier :', folder)
    save()
    session = requests.Session()
    session.headers['User-Agent'] = 'LocalTagStatistics/Configurable-1.0'
    try:
        for page in range(page_start, page_end+1):
            if target_obtained:
                break
            pid = (page-1)*20
            requests_sent += 1
            print(f'\nPage {page}/{page_end} — nouvelle page {page-page_start+1}/{budget} — pid={pid}',flush=True)
            response = session.get(BASE,params={'page':'tags','s':'list','tags':'','order_by':'index_count','sort':'desc','pid':pid},timeout=(15,45))
            if response.status_code != 200:
                retry_after = response.headers.get('Retry-After')
                if retry_after:
                    print('Indication Retry-After du serveur :',retry_after)
                status = f'Arrêt HTTP {response.status_code} : aucun réessai automatique ni contournement.'
                break
            rows = parse_rows(response.text)
            if not rows:
                status = 'Table vide : fin apparente. Le nombre de résultats demandé n’est pas garanti.'
                target_obtained = len(characters) >= target
                break
            if len(rows) != 20:
                status = 'Pagination différente de 20 lignes : arrêt pour éviter de sauter des tags.'
                break
            counts = [r['count'] for r in rows]
            if any(a<b for a,b in zip(counts,counts[1:])) or (last_count is not None and counts[0]>last_count):
                status = 'Tri décroissant non respecté ou base modifiée : arrêt, objectif non validé.'
                break
            names = [r['name'] for r in rows]
            if len(set(names)) != len(names) or any(n in seen or n in historical_names for n in names):
                status = 'Tags exacts répétés : arrêt, objectif non validé.'
                break
            seen.update(names)
            characters.extend(r for r in rows if r['character'])
            validated_pages += 1
            last_count = counts[-1]
            ranked = ranked_rows()
            if len(ranked) >= target and last_count < ranked[target-1]['count']:
                target_obtained = True
                status = f'Limite de {new_limit} NOUVEAUX résultats atteinte ; seuil des ex aequo vérifié.'
            elif page == page_end:
                status = f'Plafond de la page {page_end} atteint : objectif ou seuil des ex aequo non entièrement validé.'
            else:
                status = 'Collecte en cours.'
            save()
            new_count = len(characters) - initial_character_count
            print(f'{initial_tags+len(seen)} tags lus | Nouveaux retenus : {min(new_count,new_limit)}/{new_limit} | Anciens : {initial_character_count} | {time.monotonic()-started:.0f} s',flush=True)
            if new_count > new_limit:
                print(f'{new_count-new_limit} tags supplémentaires de fin de page sauvegardés séparément dans la liste complète.',flush=True)
            print('Sauvegarde intermédiaire effectuée.',flush=True)
            if target_obtained or page == page_end:
                break
            print(f'Pause de {delay} s…',flush=True)
            time.sleep(delay)
    except KeyboardInterrupt:
        status = 'Arrêt demandé : sauvegarde partielle.'
    except requests.RequestException:
        status = 'Erreur réseau ou délai dépassé : arrêt sans réessai automatique.'
    except ValueError as exc:
        status = str(exc)
    finally:
        session.close()
    save()
    print('\n'+status)
    print(f'Anciens conservés : {initial_character_count}. Nouveaux retenus : {min(len(characters)-initial_character_count,new_limit)}/{new_limit}. Pages traitées : {validated_pages}.')
    print('Portée :',scope)
    archive = shutil.make_archive(str(folder),'zip',root_dir=str(folder))
    print('ZIP :',archive)
    show_download_button(archive)
    return folder

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Lecture statistique des tableaux de tags ; aucune image.')
    parser.add_argument('--debut',type=int,default=108)
    parser.add_argument('--fin',type=int,default=139)
    parser.add_argument('--nouveaux',type=int,default=20)
    args=parser.parse_args()
    run_export(args.debut,args.fin,args.nouveaux)
