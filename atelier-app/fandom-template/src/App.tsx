import imgTest from "./assets/samourai-usagi-1.jpg"; // tour 94 : image de test

type Influence = { name: string; detail?: string };
type InfluenceGroup = { label: string; items: Influence[] };

const influenceGroups: InfluenceGroup[] = [
  {
    label: "Litt\u00e9rature, mythes et imaginaires",
    items: [
      { name: "The Stormlight Archive" },
      { name: "Game of Thrones" },
      { name: "La l\u00e9gende arthurienne" },
      { name: "Harry Potter" },
      {
        name: "H. P. Lovecraft",
        detail: "L'Appel de Cthulhu, L'Affaire Charles Dexter Ward, Le Cauchemar d'Innsmouth, La Couleur tomb\u00e9e du ciel, Les Montagnes hallucin\u00e9es, etc.",
      },
      { name: "Le Seigneur des anneaux" },
      { name: "The Kingkiller Chronicle" },
      { name: "Mother of Learning" },
      { name: "La Horde du Contrevent" },
      { name: "Shakespeare", detail: "Jeanne d'Arc, Le Songe d'une nuit d'\u00e9t\u00e9, etc. (r\u00e9f\u00e9rences cit\u00e9es \u00e0 pr\u00e9ciser)" },
      { name: "La Fondation SCP", detail: "Univers" },
      { name: "The Magnus Archives" },
      { name: "L'occultisme" },
      { name: "L'\u00e9sot\u00e9risme" },
    ],
  },
  {
    label: "Comics et super-h\u00e9ros",
    items: [
      { name: "Worm / Parahumans", detail: "Wildbow" },
      { name: "Watchmen", detail: "Comic" },
      { name: "Watchmen", detail: "S\u00e9rie TV" },
      { name: "X-Men", detail: "L'univers, pas seulement le groupe" },
      { name: "Batman", detail: "L'univers, pas seulement le personnage" },
      { name: "Spider-Man", detail: "L'univers" },
      { name: "Invincible", detail: "Comics" },
      { name: "Hellboy", detail: "Comics" },
      { name: "Deadly Class", detail: "Comics" },
      { name: "Teen Titans" },
      { name: "Joe Madureira" },
      { name: "Marvel Rivals", detail: "Surtout pour l'univers Marvel" },
    ],
  },
  {
    label: "Manga et animation",
    items: [
      { name: "Yu Yu Hakusho" },
      { name: "Hunter x Hunter" },
      { name: "Jujutsu Kaisen" },
      { name: "JoJo's Bizarre Adventure", detail: "Partie 4" },
      { name: "JoJo's Bizarre Adventure", detail: "Partie 5" },
      { name: "Naruto", detail: "S\u00e9rie" },
      { name: "L'Attaque des Titans" },
      { name: "One Piece" },
      { name: "Dorohedoro" },
      { name: "Solo Leveling" },
      { name: "Fullmetal Alchemist" },
      { name: "The Hunters Guild: Red Hood" },
      { name: "World Trigger" },
      { name: "Magi" },
      { name: "The Seven Deadly Sins" },
      { name: "Steins;Gate" },
      { name: "Bakemonogatari" },
      { name: "Kekkai Sensen" },
      { name: "Haikyu!!" },
      { name: "Hayao Miyazaki", detail: "Surtout Le Ch\u00e2teau ambulant et Le Voyage de Chihiro" },
    ],
  },
  {
    label: "Jeux vid\u00e9o et univers associ\u00e9s",
    items: [
      { name: "World of Warcraft" },
      { name: "Hearthstone" },
      { name: "League of Legends" },
      { name: "Legends of Runeterra" },
      { name: "Arcane", detail: "S\u00e9rie li\u00e9e \u00e0 League of Legends" },
      { name: "The Witcher", detail: "Surtout le jeu The Witcher 3" },
      { name: "BioShock", detail: "S\u00e9rie" },
      { name: "Urban Rivals" },
      { name: "Grand Theft Auto V" },
      { name: "Street Fighter" },
      { name: "Marvel vs. Capcom" },
      { name: "Capcom vs. SNK" },
      { name: "SNK", detail: "Jeux vid\u00e9o" },
      { name: "Capcom", detail: "En g\u00e9n\u00e9ral" },
      { name: "Overwatch" },
      { name: "Final Fantasy" },
      { name: "Tekken" },
      { name: "Apex Legends" },
    ],
  },
  {
    label: "Cin\u00e9ma, s\u00e9ries et spectacle",
    items: [
      { name: "Breaking Bad" },
      {
        name: "Quentin Tarantino",
        detail: "Ses films en g\u00e9n\u00e9ral : Django Unchained, Kill Bill, Inglourious Basterds, Pulp Fiction, The Hateful Eight, Reservoir Dogs",
      },
      { name: "Doctor Who" },
      { name: "The X-Files" },
      { name: "Terminator", detail: "Films 1 et 2" },
      { name: "Alien" },
      { name: "Mad Max" },
      { name: "Disney et Pixar" },
      { name: "Les Affranchis" },
      { name: "Fargo", detail: "Saisons 1 et 2" },
      {
        name: "Films d'arts martiaux",
        detail: "La 36e Chambre de Shaolin (1978), La Fureur de vaincre (1972), Le Ma\u00eetre chinois (1978), etc.",
      },
      { name: "Le catch", detail: "WWE, NJPW et AEW" },
    ],
  },
];

const sections = [
  { id: "presentation", title: "Pr\u00e9sentation", tone: "coral" },
  { id: "genealogie", title: "G\u00e9n\u00e9alogie", tone: "violet" },
  { id: "creations", title: "Dans mes cr\u00e9ations", tone: "gold" },
  { id: "commentaires", title: "Commentaires et sources", tone: "cyan" },
  { id: "repertoire", title: "R\u00e9pertoire", tone: "green" },
];


function Ref({ n }: { n: number }) {
  return <sup className="ref"><a href={`#note-${n}`}>[{n}]</a></sup>;
}

export default function App() {

  return (
    <div className="wiki" id="haut">
      <header className="site-header">
        <div className="site-header-inner">
          <a className="site-name" href="#haut">
            <span className="site-mark" aria-hidden="true"><i /><i /><i /><i /></span>
            <span className="site-name-text"><strong>Influences</strong><small>Wiki personnel</small></span>
          </a>
          <span className="site-context">Archive d'auteur</span>
        </div>
      </header>

      <div className="page-container">
        <nav className="breadcrumbs" aria-label="Fil d'Ariane">
          <span>Wiki personnel</span><span className="divider">/</span>
          <span>Pages d'auteur</span><span className="divider">/</span>
          <span aria-current="page">Influences</span>
        </nav>

        <div className="page-columns">
          <aside className="toc" aria-label="Sommaire">
            <div className="toc-inner">
              <p>Sommaire</p>
              <nav>
                {sections.map((section) => <a href={`#${section.id}`} key={section.id}>{section.title}</a>)}
              </nav>
            </div>
          </aside>

          <main className="article">
            <div className="article-heading">
              <span className="article-label">PAGE D'AUTEUR</span>
              <h1>Influences</h1>
              <span className="article-status">En cours de r&eacute;daction</span>
            </div>

            <details className="mobile-toc">
              <summary>Sommaire</summary>
              <nav aria-label="Sommaire mobile">
                {sections.map((section) => <a href={`#${section.id}`} key={section.id}>{section.title}</a>)}
              </nav>
            </details>

            <section className="article-section tone-coral" id="presentation">
              <h2>Présentation</h2>
              <p>J'ai en tête deux univers pour mes projets de manga, que j'appelle provisoirement :</p>
              <ul className="article-list">
                <li><strong>Edenia</strong> : l'univers fantasy ;</li>
                <li><strong>Arcana</strong> : l'univers urbain moderne.</li>
              </ul>
              <p>Les deux univers sont séparés, et tous les deux en sont à un stade embryonnaire.</p>
              {/* tour 94 : image ajoutée pour test de la visionneuse */}
              <figure className="article-figure">
                <img src={imgTest} alt="Couverture de Samouraï Usagi, tome 1" />
                <figcaption>Samouraï Usagi, tome 1 (image de test)</figcaption>
              </figure>
              <h3>Inspirations majeures</h3>
              <ul className="article-list">
                <li><strong>Worm</strong> (j'en suis à l'arc 9).</li>
                <li><strong>The Stormlight Archive</strong> (je n'ai lu que les 11 premiers chapitres).</li>
              </ul>
            </section>

            <section className="article-section tone-violet" id="genealogie">
              <h2>Généalogie</h2>

              <h3>La Fondation SCP, le point de départ</h3>
              <p>Ma source d'inspiration première, celle qui relie énormément de choses, c'est la Fondation SCP. Je l'ai découverte vers 12-14 ans, je ne sais plus exactement. Ma première porte d'entrée a été SCP-173<Ref n={1} />.</p>
              <p>J'ai ensuite approfondi mes recherches. Je ne sais plus exactement quand, mais c'est la vidéo de LinksTheSun sur Halloween et les SCP<Ref n={2} /> qui a été le vrai point d'entrée : c'est là que j'ai commencé à vouloir en savoir plus. À cette époque, j'aimais beaucoup SCP-106, SCP-105, SCP-096, SCP-076 et aussi SCP-682 : les plus populaires.</p>
              <p>Je ne sais pas vraiment ce qui me plaisait chez eux. Ils étaient surtout populaires, et c'étaient les seuls qui étaient surreprésentés. Il y avait aussi le fait qu'ils représentaient des monstres avec une limite originale. SCP-682, c'était surtout pour son aspect badass, pareil pour SCP-076.</p>
              <p>Ce n'est que plus tard, vers 18-22 ans, que j'ai essayé d'en savoir encore plus, grâce à la vidéo de Mythologics sur les SCP<Ref n={3} />. C'est là que je me suis intéressé aux tales et aux canons.</p>
              <p className="aside-note">Je raconte cette partie de mémoire : les âges et l'ordre ne sont peut-être pas exacts.</p>

              <h3>Des SCP à leurs inspirations</h3>
              <p>L'attrait pour cet univers m'a donné envie d'en savoir plus sur ses inspirations.</p>
              <ul className="article-list">
                <li><strong>H. P. Lovecraft</strong> : je l'ai découvert surtout grâce à ça, et encore aujourd'hui, c'est mon auteur de romans préféré. Je ne sais pas si j'avais lu <em>There Is No Antimemetics Division</em> avant de lire Lovecraft.</li>
                <li><strong>Doctor Who</strong> : SCP-173 m'a fait découvrir la série, car je voulais savoir ce qu'était sa référence : l'épisode <em>Blink</em><Ref n={4} />. Une sacrée surprise. Dans la foulée, j'ai aussi pu comprendre l'inspiration probable de SCP-049 : les épisodes de la saison 1 autour de <em>The Doctor Dances</em>.</li>
                <li><strong>La Bibliothèque de Babel</strong> : l'inspiration de la Bibliothèque des Vagabonds vient peut-être des épisodes <em>Silence in the Library</em> de Doctor Who, mais peut-être plus encore de <em>La Bibliothèque de Babel</em><Ref n={5} />. C'est grâce à ça que j'ai découvert ce livre.</li>
                <li><strong>Weird fiction et New Weird</strong> : en m'intéressant à la Fondation SCP, j'ai découvert ces genres, dans lesquels la Fondation est ancrée.</li>
              </ul>
              <p>Tout cela, c'était vraiment avant de lire Worm. À ce moment-là, j'avais déjà l'idée d'une organisation secrète (une idée potentielle que je garde toujours pour Arcana), sans avoir Worm comme inspiration.</p>

              <h4>Lovecraft</h4>
              <p>Mes œuvres préférées de Lovecraft sont <em>L'Appel de Cthulhu</em>, <em>La Couleur tombée du ciel</em> et <em>Le Cauchemar d'Innsmouth</em>, avec <em>L'Étranger</em>. C'est l'auteur que j'ai le plus lu. Je ne suis pas un très grand lecteur, d'ailleurs je l'ai surtout écouté en livre audio.</p>
              <p>Plus je le lisais, plus j'arrivais à comprendre rétroactivement les œuvres que j'aimais, car je comprenais leurs inspirations. Mais c'est aussi parce qu'il a une vraie patte : il est ingénieux et original.</p>

              <h3>Urban Rivals</h3>
              <p>Urban Rivals<Ref n={6} /> est aussi une énorme source d'inspiration : c'est un jeu dont l'univers m'a frappé très jeune, vers 11 ans. Il a sans doute développé mon attrait pour les jeux de cartes en ligne et pour les univers hétéroclites, avec des gangs et des designs reconnaissables.</p>
              <p>Il a une grande part d'influence. Le clan Skeelz m'a toujours marqué : pour moi, le mélange de Harry Potter et des X-Men était incroyable. J'avais environ 13 ans, je crois.</p>
              <p>Parmi les autres clans, il y a les Frozn et les Raptors : le mélange des genres me plaît énormément. Les Frozn trouvaient aussi un écho avec le Yéti, un cryptide qui était déjà présent dans SCP, et avec les Mi-Go de Lovecraft. Je trouvais original de mélanger la culture nordique avec les Yétis et la technologie. Pareil pour les Raptors, avec Mad Max et Jurassic Park. Il y avait aussi les Huracan<Ref n={7} />, mais surtout parce que je suis fan de catch.</p>

              <h3>Le projet de jeu vidéo</h3>
              <p>Vers 16 ans, avec Urban Rivals et l'esthétique Capcom de Street Fighter de l'époque, j'avais en tête la création d'un jeu vidéo. Ce projet s'est légèrement transféré dans mes deux mangas.</p>
              <p>C'était un jeu à la troisième personne, fortement inspiré de Gigantic<Ref n={8} /> : une espèce de MOBA, avec des personnages de mêlée à combos et des tireurs. Pour le design, je dirais que mes inspirations venaient d'Overwatch, de Capcom, d'Urban Rivals et de League of Legends : il y avait énormément de designs de jeux vidéo que j'appréciais.</p>

              <h3>Mangas préférés</h3>
              <ul className="article-list">
                <li><strong>One Piece</strong> : vers 11 ans, c'était mon manga préféré.</li>
                <li><strong>Hunter x Hunter</strong> : en grandissant, vers 14 ans je crois, il l'a détrôné.</li>
                <li><strong>L'Attaque des Titans</strong> : surtout la première saison, qui m'a tellement marqué qu'il est passé devant.</li>
              </ul>
              <p>En grandissant, One Piece m'a paru répétitif et long, l'adaptation animée étant incroyablement lente. J'ai davantage accroché à Hunter x Hunter quand je l'ai fini. À peu près tout ce que je dis sur Worm (plus bas) se retrouve dans Hunter x Hunter.</p>
              <p>L'Attaque des Titans, c'était tellement différent de ce que j'avais vu avant. C'est un peu la même chose avec Game of Thrones : c'était plus sérieux, j'avais l'impression. J'avais 14 et 16 ans quand j'ai vu ces deux œuvres. Et c'était aussi extrêmement bien fichu.</p>

              <h3>Hearthstone et Warcraft</h3>
              <p>C'est aussi vers 14 ans, je crois, que j'ai découvert Hearthstone. À ce moment-là, la Ligue des explorateurs était sortie, donc c'était peut-être plus tard<Ref n={9} />. C'était la première fois que je faisais connaissance avec l'univers de Warcraft, qui a eu une grande influence sur l'esthétique d'Edenia.</p>

              <h3>Worm</h3>
              <p>Je ne me rappelle plus exactement comment j'ai découvert Worm. Je crois que ça s'est fait de fil en aiguille : une œuvre m'a amené à une autre, qui m'a amené à Worm. Je crois que ça a commencé sur jeuxvideo.com, où une personne avait HPMOR<Ref n={10} /> en signature. Après ça, je me suis intéressé à la web fiction, puis à Worm<Ref n={11} />.</p>
              <p>J'ai découvert Worm en avril 2023 et j'ai commencé à le lire en décembre 2023. Je me suis arrêté au premier arc, puis j'ai repris en mai 2024, puis je me suis de nouveau arrêté, mais je ne sais plus quand.</p>
              <p>Pour moi, Worm est un mélange parfait de deux œuvres que j'aime énormément : Hunter x Hunter et Watchmen (une de mes œuvres préférées). En fait, j'avais l'impression de lire du Hunter x Hunter mélangé à du Watchmen. J'ai adoré, surtout à partir de l'arc 3, où ils font un braquage. Le fait que ce soient des vilains aide beaucoup aussi : c'est du Togashi.</p>
              <p>J'adore les combats tactiques. En plus, c'est un livre vraiment rationnel et réaliste dans sa façon de faire, et c'est une déconstruction du genre, faite de manière ingénieuse.</p>

              <h3>The Stormlight Archive</h3>
              <p>The Stormlight Archive, c'est un peu comme Worm. Les chapitres sur Szeth et sur Cenn m'ont complètement mis dans le bain : encore une fois des combats stratégiques, puis un monde ancré dans le réel (<em>grounded</em>) et réaliste, avec des enjeux élevés où l'on ressent la tension. La partie où Kaladin doit déplacer un pont est incroyable.</p>
              <p>L'univers est composé de personnages légendaires. Il y a aussi ça dans Worm : certains personnages ont ce mystère derrière eux, comme Scion. Et il y a cette impression de maîtrise que je retrouve dans L'Attaque des Titans.</p>
            </section>

            <section className="article-section tone-gold" id="creations">
              <h2>Dans mes créations</h2>
              <ul className="article-list">
                <li><strong>Arcana</strong> : l'idée d'une organisation qui s'occupe des affaires encombrantes, une organisation plutôt grise, inspirée de la philosophie de la Fondation SCP. Elle date d'avant ma lecture de Worm. Elle reste au stade d'idée, car ce trope est assez cliché.</li>
                <li><strong>Edenia</strong> : l'univers de Warcraft, découvert avec Hearthstone, a eu une grande influence sur son esthétique, pour la fantasy et surtout les paysages forestiers. Mais en vrai, l'esthétique d'Edenia est beaucoup plus proche de Runeterra. Le monde hétéroclite des différents univers que j'aime y est présent, mais je trouve que c'est plutôt une convention de base, sinon le monde paraîtrait répétitif.</li>
                <li><strong>Mes deux mangas</strong> : le projet de jeu vidéo que j'avais vers 16 ans (Urban Rivals, esthétique Capcom de Street Fighter) s'y est légèrement transféré.</li>
              </ul>
            </section>

            <section className="article-section tone-cyan" id="commentaires">
              <h2>Commentaires et sources</h2>
              <p className="aside-note">Ces notes viennent de sources externes. Elles complètent le récit sans le modifier.</p>
              <ol className="notes-list">
                <li id="note-1"><strong>SCP-173</strong> : premier article SCP, publié le 22 juin 2007 sur le forum /x/ de 4chan par Moto42. L'image d'origine est l'œuvre <em>Untitled 2004</em> de l'artiste Izumi Kato. <a href="https://scp-meta.fandom.com/wiki/SCP-173" target="_blank" rel="noreferrer">SCP Meta Wiki</a></li>
                <li id="note-2"><strong>Point Culture : Creepypasta (Spécial Halloween)</strong> : vidéo de LinksTheSun publiée sur YouTube le 31 octobre 2016. Sous couvert de parler de creepypastas, elle présente la Fondation SCP (SCP-173, SCP-087, SCP-682…). <a href="https://www.youtube.com/watch?v=xnywr1eFZqk" target="_blank" rel="noreferrer">YouTube</a></li>
                <li id="note-3"><strong>Mythologics</strong> : série de vidéos de la chaîne YouTube ALT 236. L'épisode 8 est consacré à la Fondation SCP (<em>La Fondation SCP – Par-delà le mur du réel</em>). <a href="http://fondationscp.wikidot.com/forum/t-13808757/a-voir-alt-236-parle-de-scp" target="_blank" rel="noreferrer">Forum de la Fondation SCP</a></li>
                <li id="note-4"><strong>Blink</strong> : épisode de Doctor Who diffusé le 9 juin 2007, environ deux semaines avant la publication de SCP-173. La ressemblance entre les deux est souvent relevée, mais aucun lien n'est confirmé. <a href="https://scp-meta.fandom.com/wiki/SCP-173" target="_blank" rel="noreferrer">SCP Meta Wiki</a></li>
                <li id="note-5"><strong>La Bibliothèque des Vagabonds</strong> (<em>Wanderers' Library</em>) : bibliothèque extradimensionnelle de l'univers SCP, décrite comme contenant tous les livres possibles, à la manière de <em>La Bibliothèque de Babel</em>, la nouvelle de Jorge Luis Borges. <a href="https://www.reddit.com/r/SCP/comments/9t05d5/what_exactly_is_the_wanderers_library/" target="_blank" rel="noreferrer">r/SCP</a></li>
                <li id="note-6"><strong>Urban Rivals</strong> : jeu de cartes en ligne du studio français Boostr (aujourd'hui Acute Games), sorti le 17 janvier 2006. <a href="https://store.steampowered.com/app/715310/Urban_Rivals/" target="_blank" rel="noreferrer">Steam</a></li>
                <li id="note-7"><strong>Huracan</strong> : clan d'Urban Rivals inspiré de la lucha libre (le catch mexicain). Son nom veut dire « ouragan » en espagnol et pourrait faire référence au catcheur Huracán Ramírez. <a href="https://urban-rivals.fandom.com/wiki/Huracan" target="_blank" rel="noreferrer">Urban Rivals Wiki</a></li>
                <li id="note-8"><strong>Gigantic</strong> : jeu d'action en équipe à la troisième personne, entre MOBA et <em>hero shooter</em>, du studio Motiga. Il est sorti en juillet 2017, ses serveurs ont fermé le 31 juillet 2018, et il a été relancé en 2024 sous le nom <em>Gigantic: Rampage Edition</em>. <a href="https://www.gamespot.com/articles/gigantic-rampage-edition-revives-the-indie-moba-after-five-years-away/1100-6521200/" target="_blank" rel="noreferrer">GameSpot</a></li>
                <li id="note-9"><strong>La Ligue des explorateurs</strong> : aventure de Hearthstone sortie le 12 novembre 2015. <a href="https://playhearthstone.com/en-us/blog/19932699/" target="_blank" rel="noreferrer">Blog officiel de Hearthstone</a></li>
                <li id="note-10"><strong>HPMOR</strong> (<em>Harry Potter and the Methods of Rationality</em>) : fanfiction d'Eliezer Yudkowsky, publiée en ligne de 2010 à 2015. <a href="https://hpmor.com/" target="_blank" rel="noreferrer">hpmor.com</a></li>
                <li id="note-11"><strong>Worm</strong> : web serial de Wildbow (John C. McCrae), publié en ligne de 2011 à 2013. <a href="https://parahumans.wordpress.com/" target="_blank" rel="noreferrer">Parahumans</a></li>
              </ol>
            </section>

            <section className="article-section repertoire-section tone-green" id="repertoire">
              <h2>R&eacute;pertoire des influences</h2>
              <p>Ces r&eacute;f&eacute;rences sont regroup&eacute;es pour &ecirc;tre retrouv&eacute;es plus facilement. Leur place dans la liste ne donne ni un ordre chronologique ni un degr&eacute; d'importance.</p>
              <details className="catalogue">
                <summary>Afficher la liste des influences <span aria-hidden="true">+</span></summary>
                <div className="catalogue-content">
                  {influenceGroups.map((group) => (
                    <section className="catalogue-group" key={group.label}>
                      <h3>{group.label}</h3>
                      <ul>
                        {group.items.map((item, index) => (
                          <li key={`${item.name}-${index}`}>
                            <span>{item.name}</span>
                            {item.detail && <small>{item.detail}</small>}
                          </li>
                        ))}
                      </ul>
                    </section>
                  ))}
                </div>
              </details>
            </section>

            <footer className="article-footer">Page personnelle en construction.</footer>
          </main>
        </div>
      </div>
    </div>
  );
}