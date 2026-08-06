import { useState, useEffect, useRef } from 'react'

// Types
type InfoboxItem = { id:string, type:'title'|'image'|'data'|'header'|'group'|'navigation', label:string, source:string, value:string }
type GalleryImg = { id:string, src:string, caption:string, alt:string }
type Tier = { id:string, label:string, color:string, items:{id:string, label:string, img:string}[] }
type DiagramType = 'pie'|'bar'|'radar'|'flow'

export default function App(){
  // -- Wiki config (full customisable)
  const [wikiName, setWikiName] = useState("Chroniques d'Elyndra")
  const [slogan, setSlogan] = useState("WIKI OFFICIELLE • 12 482 PAGES • 4 201 IMAGES")
  const [accent, setAccent] = useState("#ff004d")
  const [accent2, setAccent2] = useState("#7c3aed")
  const [bgPage, setBgPage] = useState("#f6f7f8")
  const [paperBg, setPaperBg] = useState("#ffffff")
  const [textColor] = useState("#0f172a")
  const [fontTitle, setFontTitle] = useState("Rubik")
  const [radius, setRadius] = useState(16)
  const [layout, setLayout] = useState<'desktop'|'oasis'>("desktop")
  const [darkMode, setDarkMode] = useState(false)
  const [showCustomizer, setShowCustomizer] = useState(true)
  const [editorMode, setEditorMode] = useState<'visual'|'source'>('visual')
  const [activePanel, setActivePanel] = useState<'infobox'|'gallery'|'media'|'tier'|'diagram'|'template'>('infobox')
  const [infoboxLayout, setInfoboxLayout] = useState<'default'|'stacked'>('default')
  const [infoboxTheme, setInfoboxTheme] = useState("elyndra")
  const [showPanels, setShowPanels] = useState(true)
  const [sliderIdx, setSliderIdx] = useState(0)

  const [infoboxItems, setInfoboxItems] = useState<InfoboxItem[]>([
    {id:'t1', type:'title', label:'Titre', source:'title', value:'Aeris Vael — La Sentinelle Écarlate'},
    {id:'i1', type:'image', label:'Image', source:'image', value:'Aeris_Vael.png'},
    {id:'d1', type:'data', label:'Espèce', source:'espece', value:'Sylphide Écarlate'},
    {id:'d2', type:'data', label:'Affiliation', source:'affiliation', value:'Ordre de l\'Aube'},
    {id:'d3', type:'data', label:'Âge', source:'age', value:'127 ans (apparence 23)'},
    {id:'d4', type:'data', label:'Arme', source:'arme', value:'Lame-Phoenix & Sceau Solaire'},
    {id:'h1', type:'header', label:'Biographie', source:'', value:'Biographie'},
    {id:'d5', type:'data', label:'Statut', source:'statut', value:'Vivante — Gardienne du Sanctuaire'},
    {id:'d6', type:'data', label:'Doubleur', source:'voix', value:'Léana Moreau (FR) / Ayaka Ishihara (JP)'},
    {id:'n1', type:'navigation', label:'Nav', source:'', value:'Voir l\'arbre généalogique • Timeline'},
  ])

  const [gallery, setGallery] = useState<GalleryImg[]>([
    {id:'g1', src:'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&q=80', caption:'Sanctuaire d\'Elyndra au crépuscule', alt:'Sanctuaire'},
    {id:'g2', src:'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&q=80', caption:'La Lame-Phoenix, détail runique', alt:'Lame'},
    {id:'g3', src:'https://images.unsplash.com/photo-1519681393784-d120267933ba?w=600&q=80', caption:'Carte de l\'Archipel Céleste', alt:'Carte'},
    {id:'g4', src:'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=600&q=80', caption:'Concept art — Costume d\'hiver', alt:'Concept'},
    {id:'g5', src:'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=600&q=80', caption:'Forêt des Murmures (saison 2)', alt:'Forêt'},
    {id:'g6', src:'https://images.unsplash.com/photo-1486915309851-b0cc1f8a0084?w=600&q=80', caption:'Ending — "Cendres d\'Étoiles"', alt:'Ending'},
  ])

  const [galleryMode, setGalleryMode] = useState<'grid'|'slideshow'|'slider'|'single'>('grid')

  const [tiers, setTiers] = useState<Tier[]>([
    {id:'S', label:'S', color:'#ff004d', items:[
      {id:'c1', label:'Aeris Vael', img:'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&q=80'},
      {id:'c2', label:'Kael Obscur', img:'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&q=80'},
    ]},
    {id:'A', label:'A', color:'#ff8c00', items:[
      {id:'c3', label:'Lyra', img:'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=200&q=80'},
      {id:'c4', label:'Thalion', img:'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&q=80'},
      {id:'c5', label:'Mira', img:'https://images.unsplash.com/photo-1488426862026-3ee34e13d341?w=200&q=80'},
    ]},
    {id:'B', label:'B', color:'#facc15', items:[
      {id:'c6', label:'Général Varric', img:'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&q=80'},
      {id:'c7', label:'Sœur Yui', img:'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&q=80'},
    ]},
    {id:'C', label:'C', color:'#22c55e', items:[
      {id:'c8', label:'Rook', img:'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=200&q=80'},
    ]},
    {id:'D', label:'D', color:'#38bdf8', items:[]},
    {id:'F', label:'F', color:'#a78bfa', items:[
      {id:'c9', label:'Slime Mascotte', img:'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=200&q=80'},
    ]},
  ])

  const [bankItems] = useState([
    {id:'b1', label:'Nimra', img:'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=200&q=80'},
    {id:'b2', label:'Eldric', img:'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&q=80'},
    {id:'b3', label:'Seraphine', img:'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200&q=80'},
  ])

  const [dragged, setDragged] = useState<{tierId:string|null, itemId:string}|null>(null)

  const [diagramType, setDiagramType] = useState<DiagramType>('pie')
  const [diagramData, setDiagramData] = useState([
    {label:'Sylphes', value:42, color:'#ff004d'},
    {label:'Humains', value:28, color:'#7c3aed'},
    {label:'Nains célestes', value:14, color:'#06b6d4'},
    {label:'Spectres', value:10, color:'#f59e0b'},
    {label:'Autres', value:6, color:'#10b981'},
  ])

  const [tableData, setTableData] = useState([
    ["Personnage","Rôle","Puissance","Région"],
    ["Aeris Vael","Sentinelle","★★★★★","Sanctuaire"],
    ["Kael Obscur","Antagoniste","★★★★★","Abysses"],
    ["Lyra","Alchimiste","★★★★☆","Archipel"],
    ["Thalion","Éclaireur","★★★☆☆","Forêt"],
  ])

  const [categories, setCategories] = useState(["Personnages","Sylphes","Ordre de l'Aube","Protagonistes","Saison 1"])
  const [newCat, setNewCat] = useState("")
  const [tocVisible, setTocVisible] = useState(true)
  const [articleTitle, setArticleTitle] = useState("Aeris Vael")
  const [siteNotice, setSiteNotice] = useState("Bienvenue sur le Wiki ! Aidez-nous à compléter les 482 articles manquants — Rejoignez le Discord !")

  const editorRef = useRef<HTMLDivElement>(null)

  // image insert form
  const [imgForm, setImgForm] = useState({file:'Aeris_Vael.png', size:'300px', align:'right', caption:"Aeris dans l'épisode 12", thumb:true, alt:"Portrait Aeris"})

  // Template quick inserts
  const templates = [
    {name:"Infobox Personnage", code:"{{Infobox Personnage | nom = Aeris Vael | espece = Sylphide}}"},
    {name:"Navbox Elyndra", code:"{{Navbox Elyndra}}"},
    {name:"Citation", code:"{{Citation | texte = La lumière ne meurt jamais. | auteur = Aeris}}"},
    {name:"Spoiler", code:"{{Spoiler | saison = 2}}"},
    {name:"Stub", code:"{{Ébauche}}"},
    {name:"Chrono", code:"{{Timeline | année = 847}}"},
  ]

  // generate wikitext
  const wikitext = `{{Infobox Personnage
 | title = ${infoboxItems.find(i=>i.type==='title')?.value || articleTitle}
 | theme = ${infoboxTheme}
 | image = ${imgForm.file}
 | espece = Sylphide Écarlate
 | affiliation = Ordre de l'Aube
 | age = 127 ans
}}
'''${articleTitle}''' est un personnage principal de ''${wikiName}''.

== Biographie ==
Aeris est la Sentinelle Écarlate, gardienne du Sanctuaire depuis la Chute des Étoiles.

[[File:${imgForm.file}|${imgForm.thumb?'thumb|':''}${imgForm.size}|${imgForm.align}|alt=${imgForm.alt}|${imgForm.caption}]]

== Pouvoirs ==
{| class="wikitable sortable" style="text-align:center"
|-
! Personnage !! Rôle !! Puissance
|-
${tableData.slice(1).map(r=>`| ${r[0]} || ${r[1]} || ${r[2]}`).join("\n|-\n")}
|}

<gallery mode="${galleryMode}" caption="Galerie d'Elyndra">
${gallery.map(g=>`${g.src.split('/').pop()}|${g.caption}`).join("\n")}
</gallery>

{{Tier List | S = Aeris, Kael | A = Lyra, Thalion }}

{{Diagramme | type = ${diagramType} | données = ${diagramData.map(d=>`${d.label}:${d.value}`).join(", ")} }}

[[Category:${categories.join("]]\n[[Category:")}]]`

  // tier drag handlers
  const onDragStart = (tierId:string, itemId:string)=>{
    setDragged({tierId, itemId})
  }
  const onDropTier = (targetTierId:string)=>{
    if(!dragged) return
    const sourceTierId = dragged.tierId
    const itemId = dragged.itemId
    if(sourceTierId===targetTierId) return
    setTiers(prev=>{
      const copy = JSON.parse(JSON.stringify(prev)) as Tier[]
      let moving:any = null
      if(sourceTierId){
        const src = copy.find(t=>t.id===sourceTierId)
        if(src){
          const idx = src.items.findIndex(i=>i.id===itemId)
          if(idx>=0) moving = src.items.splice(idx,1)[0]
        }
      } else {
        // from bank - find in bankItems static? we move from tiers bank is not in state, so create dummy
        const bank = bankItems.find(b=>b.id===itemId)
        if(bank) moving = {...bank, id: Math.random().toString(36).slice(2,6)}
      }
      if(moving){
        const tgt = copy.find(t=>t.id===targetTierId)
        if(tgt) tgt.items.push(moving)
      }
      return copy
    })
    setDragged(null)
  }

  const allowDrop = (e:React.DragEvent)=>{e.preventDefault()}

  // auto slideshow
  useEffect(()=>{
    if(galleryMode==='slideshow'){
      const id = setInterval(()=> setSliderIdx(s=> (s+1)% gallery.length), 3000)
      return ()=>clearInterval(id)
    }
  },[galleryMode, gallery.length])

  const addGalleryImage = ()=>{
    const url = `https://picsum.photos/seed/${Math.random()}/600/400`
    setGallery(g=>[...g, {id:Math.random().toString(36).slice(2), src:url, caption:'Nouvelle image — légende à éditer', alt:''}])
  }

  const updateTierLabel = (id:string, label:string)=>{
    setTiers(t=> t.map(x=> x.id===id? {...x, label}:x))
  }

  return (
    <div style={{
      background: darkMode ? "#0a0e1a" : bgPage,
      color: darkMode ? "#e2e8f0" : textColor,
      fontFamily: `Inter, system-ui, sans-serif`,
      minHeight:'100vh'
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600;800&family=Inter:wght@400;600&display=swap');
        .scrollbar-thin::-webkit-scrollbar{width:6px;height:6px}
        .scrollbar-thin::-webkit-scrollbar-thumb{background:#cbd5e1;border-radius:999px}
        .pi-title{font-family:${fontTitle}, sans-serif}
      `}</style>

      {/* FANDOM GLOBAL BAR */}
      <div className="sticky top-0 z-[60] border-b" style={{background: darkMode? '#0f172a' : '#fff', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
        <div className="max-w-[1600px] mx-auto px-3 md:px-4 h-[48px] flex items-center gap-3">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded bg-[#ff004d] grid place-items-center text-white font-black text-[14px] tracking-tighter">F</div>
            <span className="hidden sm:block font-black text-[17px] tracking-tight" style={{fontFamily:'Rubik'}}><span className="text-[#ff004d]">FAN</span><span>DOM</span></span>
            <span className="hidden lg:inline-flex ml-2 text-xs font-semibold px-2 py-1 rounded-full bg-[#f1f5f9] text-slate-600">Studio Wiki • v2.5 UCP</span>
          </div>

          <div className="flex-1 max-w-[620px] mx-2 md:mx-6 relative">
            <input placeholder="Rechercher sur le wiki..." className="w-full h-9 pl-9 pr-3 rounded-full border text-sm outline-none" style={{background: darkMode?'#1e293b':'#f1f5f9', borderColor: darkMode?'#334155':'#e2e8f0', color: darkMode?'#fff':'#0f172a'}}/>
            <span className="absolute left-3 top-2.5 text-slate-400">⌕</span>
            <span className="hidden md:block absolute right-2 top-1.5 text-[10px] font-bold px-1.5 py-1 rounded bg-white border">CTRL K</span>
          </div>

          <div className="flex items-center gap-1 md:gap-2">
            <button className="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border text-xs font-bold" style={{borderColor:'#e2e8f0'}}>＋ Créer un Wiki</button>
            <button onClick={()=>setDarkMode(!darkMode)} className="w-8 h-8 grid place-items-center rounded-full border text-sm">{darkMode?'☀️':'🌙'}</button>
            <button onClick={()=>setShowCustomizer(!showCustomizer)} className="hidden sm:inline-flex items-center gap-2 px-3 md:px-4 h-8 rounded-full text-white text-xs font-extrabold" style={{background: accent}}>🎨 Personnaliser</button>
            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-pink-500 grid place-items-center text-white font-bold text-xs">A</div>
          </div>
        </div>
      </div>

      {/* WIKI HEADER */}
      <div className="relative overflow-hidden" style={{background: darkMode? '#101a2e' : paperBg, borderBottom:`1px solid ${darkMode?'#1e293b':'#e2e8f0'}`}}>
        {/* themed banner */}
        <div className="h-[110px] md:h-[140px] w-full relative" style={{
          background: `linear-gradient(90deg, ${accent} 0%, ${accent2} 55%, #0ea5e9 100%)`,
          opacity: darkMode?0.9:1
        }}>
          <div className="absolute inset-0 opacity-20" style={{backgroundImage:`repeating-linear-gradient(45deg, transparent 0 12px, rgba(255,255,255,.15) 12px 13px)`}}/>
          <div className="max-w-[1600px] mx-auto h-full px-4 flex items-end pb-3 relative">
            <div className="flex items-center gap-3">
              <div className="w-[68px] h-[68px] md:w-[88px] md:h-[88px] rounded-2xl bg-white grid place-items-center text-3xl shadow-xl border-4 border-white overflow-hidden">
                <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=200&q=80" className="w-full h-full object-cover"/>
              </div>
              <div className="text-white drop-shadow">
                <input value={wikiName} onChange={e=>setWikiName(e.target.value)} className="bg-transparent border-b border-white/30 outline-none font-black text-[22px] md:text-[30px] tracking-tight w-[220px] md:w-[420px]" style={{fontFamily:'Rubik'}}/>
                <div className="flex items-center gap-2 mt-1">
                  <input value={slogan} onChange={e=>setSlogan(e.target.value)} className="bg-white/15 backdrop-blur rounded-full px-3 py-1 text-[10px] md:text-xs font-bold tracking-widest outline-none w-[300px] md:w-[520px] border border-white/20"/>
                  <span className="hidden md:inline text-xs opacity-80">✎ cliquer pour éditer</span>
                </div>
              </div>
            </div>
            <div className="hidden lg:flex ml-auto gap-2">
              <div className="bg-white rounded-full px-3 py-1.5 flex items-center gap-2 text-xs font-bold text-slate-700 shadow">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"/> 1 284 en ligne
              </div>
              <button className="bg-black text-white rounded-full px-5 py-2 text-xs font-black">＋ CONTRIBUER</button>
            </div>
          </div>
        </div>

        {/* wiki nav */}
        <div className="max-w-[1600px] mx-auto px-2 md:px-4 h-[46px] flex items-center gap-1 overflow-x-auto scrollbar-thin">
          {[
            {l:'Accueil',a:true},{l:'Explorer',a:false},{l:'Personnages',a:false},{l:'Lore & Cartes',a:false},{l:'Galerie',a:false},{l:'Communauté',a:false},{l:'Discussions',badge:'99+'},{l:'Aide Wiki',a:false}
          ].map(n=>(
            <a key={n.l} className={`whitespace-nowrap px-3 py-1.5 rounded-full text-[13px] font-bold flex items-center gap-1.5 ${n.a?'text-white shadow-sm': darkMode?'text-slate-300 hover:bg-white/10':'text-slate-600 hover:bg-slate-100'}`} style={n.a?{background:accent}:{}}>
              {n.l} {n.badge && <span className="bg-[#ff004d] text-white text-[10px] px-1.5 py-0.5 rounded-full">{n.badge}</span>}
              {!n.a && <span className="opacity-40 text-[10px]">▾</span>}
            </a>
          ))}
          <div className="ml-auto hidden md:flex items-center gap-2 text-xs font-bold">
            <span className="px-3 py-1 rounded-full border" style={{borderColor:darkMode?'#334155':'#e2e8f0'}}>{layout==='desktop'?'FandomDesktop':'Oasis'} • {darkMode?'Sombre':'Clair'}</span>
            <button onClick={()=>setEditorMode(editorMode==='visual'?'source':'visual')} className="px-4 py-1.5 rounded-full text-white" style={{background:accent2}}>
              {editorMode==='visual'?'◐ Éditeur Visuel':'‹› Source'}
            </button>
          </div>
        </div>

        {/* site notice */}
        <div className="max-w-[1600px] mx-auto px-4 pb-3">
          <div className="rounded-xl px-3 py-2 flex items-center gap-3 text-xs font-medium border" style={{background: darkMode?'#1e293b':'#fffbeb', borderColor:'#fde68a'}}>
            <span className="hidden sm:inline-flex w-7 h-7 rounded-full bg-amber-400 grid place-items-center">📢</span>
            <input value={siteNotice} onChange={e=>setSiteNotice(e.target.value)} className="flex-1 bg-transparent outline-none font-semibold"/>
            <button onClick={()=>setSiteNotice("")} className="text-slate-400">✕</button>
          </div>
        </div>
      </div>

      {/* MAIN LAYOUT */}
      <div className="max-w-[1600px] mx-auto px-2 md:px-4 py-4 grid grid-cols-12 gap-4 items-start">

        {/* LEFT RAIL */}
        <aside className="hidden xl:block col-span-2 sticky top-[56px] space-y-3">
          <div className="rounded-2xl border p-3" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="text-[11px] font-black tracking-widest opacity-60 mb-2">NAVIGATION</div>
            {[
              "Accueil du Wiki","Portail Personnages","Chronologie","Magie & Runes","Bestiaire","Épisodes","Forum Aide"
            ].map(l=>(
              <a key={l} className="flex items-center gap-2 px-2 py-1.5 rounded-lg text-[13px] font-semibold hover:bg-slate-50" style={{color: darkMode?'#cbd5e1':'#334155'}}>
                <span className="w-1.5 h-1.5 rounded-full" style={{background:accent}}/> {l}
              </a>
            ))}
            <button className="mt-3 w-full py-2 rounded-full text-white text-xs font-black" style={{background:accent}}>＋ Créer une page</button>
          </div>

          <div className="rounded-2xl border p-3" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="text-[11px] font-black tracking-widest opacity-60 mb-2">OUTILS WIKI</div>
            <div className="grid grid-cols-2 gap-1.5">
              {[
                {k:'Modèle',icon:'▭'},{k:'Infobox',icon:'⊞'},{k:'Galerie',icon:'▦'},{k:'Tableau',icon:'▤'},{k:'Catégorie',icon:'🏷️'},{k:'Redirection',icon:'↗'}
              ].map(b=>(
                <button key={b.k} onClick={()=>setActivePanel(b.k.toLowerCase() as any)} className={`py-2 rounded-xl border text-xs font-bold ${activePanel===b.k.toLowerCase()?'text-white':''}`} style={activePanel===b.k.toLowerCase()?{background:accent, borderColor:accent}:{background: darkMode?'#0f172a':'#f8fafc', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>{b.icon} {b.k}</button>
              ))}
            </div>
            <div className="mt-3 text-[11px] leading-3 p-2 rounded-xl" style={{background: darkMode?'#0f172a':'#f1f5f9'}}>
              <b>Astuce Fandom :</b> Utilisez <code className="px-1 rounded bg-white border text-[10px]">{"{{Infobox"}</code> ou <code className="px-1 rounded bg-white border text-[10px]">{"<gallery>"}</code> en mode source.
            </div>
          </div>

          <div className="rounded-2xl border p-3" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="text-xs font-black mb-2">Activité récente</div>
            {[
              {u:"Mira",p:"Aeris Vael",t:"il y a 2 min"},
              {u:"Kael",p:"Carte du Sanctuaire",t:"il y a 11 min"},
              {u:"Admin Lyra",p:"Modèle:Infobox",t:"il y a 37 min"},
            ].map(r=>(
              <div key={r.p} className="flex gap-2 py-2 border-b last:border-0" style={{borderColor:darkMode?'#1e293b':'#f1f5f9'}}>
                <div className="w-7 h-7 rounded-full bg-slate-200 flex-shrink-0"/>
                <div className="text-xs leading-tight">
                  <div className="font-bold" style={{color:accent}}>{r.u}</div>
                  <div className="truncate">{r.p}</div>
                  <div className="opacity-50 text-[11px]">{r.t}</div>
                </div>
              </div>
            ))}
          </div>
        </aside>

        {/* CENTER ARTICLE */}
        <main className="col-span-12 xl:col-span-7 space-y-4">
          {/* Article header + edit bar */}
          <div className="rounded-2xl border overflow-hidden" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            {/* VisualEditor toolbar */}
            <div className="flex flex-wrap items-center gap-1 px-2 py-2 border-b text-xs" style={{background: darkMode?'#0f172a':'#f8fafc', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
              <div className="flex items-center gap-1">
                <span className="hidden sm:inline text-[11px] font-black tracking-widest opacity-60 mr-2">ÉDITEUR</span>
                <button onClick={()=>setEditorMode('visual')} className={`px-2.5 py-1 rounded-full font-bold ${editorMode==='visual'?'text-white':''}`} style={editorMode==='visual'?{background:accent}:{background: darkMode?'#1e293b':'#fff', border:'1px solid #e2e8f0'}}>Visuel</button>
                <button onClick={()=>setEditorMode('source')} className={`px-2.5 py-1 rounded-full font-bold ${editorMode==='source'?'text-white':''}`} style={editorMode==='source'?{background:accent}:{background: darkMode?'#1e293b':'#fff', border:'1px solid #e2e8f0'}}>Source</button>
              </div>
              <div className="h-6 w-px bg-slate-200 mx-1 hidden sm:block"/>
              <div className="flex items-center gap-1">
                <button className="w-7 h-7 grid place-items-center rounded border font-black" title="Gras">B</button>
                <button className="w-7 h-7 grid place-items-center rounded border italic">I</button>
                <button className="w-7 h-7 grid place-items-center rounded border">🔗</button>
                <div className="hidden sm:flex items-center gap-1 ml-1">
                  <select className="h-7 rounded border px-1 text-xs" style={{background: darkMode?'#1e293b':'#fff'}}>
                    <option>Paragraphe</option><option>Titre</option><option>Sous-titre</option>
                  </select>
                  <select className="h-7 rounded border px-1 text-xs" style={{background: darkMode?'#1e293b':'#fff'}}>
                    <option>Insérer ▾</option>
                  </select>
                </div>
              </div>
              <div className="ml-auto flex items-center gap-1">
                <button className="hidden md:inline-flex px-3 py-1 rounded-full border text-xs font-bold">Prévisualiser</button>
                <button className="px-4 py-1.5 rounded-full text-white text-xs font-black" style={{background:accent}}>Publier</button>
              </div>
            </div>

            {/* Insert bar like Fandom VisualEditor */}
            <div className="px-2 md:px-3 py-2 flex flex-wrap gap-1.5 border-b text-[12px] font-bold" style={{background: darkMode?'#111d33':'#fff', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
              <span className="opacity-50 mr-1 hidden md:inline">Insérer :</span>
              {[
                {l:'Média',a:'media',i:'🖼️'},
                {l:'Galerie',a:'gallery',i:'▦'},
                {l:'Infobox',a:'infobox',i:'⊞'},
                {l:'Tableau',a:'tier',i:'▤'},
                {l:'Modèle',a:'template',i:'▭'},
                {l:'Tier List',a:'tier',i:'🏆'},
                {l:'Diagramme',a:'diagram',i:'📊'},
              ].map(b=>(
                <button key={b.l} onClick={()=>setActivePanel(b.a as any)} className={`px-2.5 py-1 rounded-full border inline-flex items-center gap-1 ${activePanel===b.a?'text-white':''}`} style={activePanel===b.a?{background:accent, borderColor:accent, color:'#fff'}:{background: darkMode?'#1e293b':'#f8fafc'}}>
                  <span>{b.i}</span> {b.l}
                </button>
              ))}
              <span className="ml-auto hidden md:inline text-[10px] opacity-50">Raccourcis : Ctrl+K lien • Ctrl+Shift+I infobox • Ctrl+G galerie</span>
            </div>

            {/* Article content header */}
            <div className="px-4 md:px-6 pt-4">
              <div className="flex items-start gap-3">
                <div className="flex-1">
                  <div className="flex items-center gap-2 text-[11px] font-bold tracking-widest opacity-60">
                    <span>CHRONIQUES D'ELYNDRA</span><span>›</span><span>PERSONNAGES</span>
                  </div>
                  <div className="flex items-center gap-2 mt-1">
                    <input value={articleTitle} onChange={e=>setArticleTitle(e.target.value)} className="text-[28px] md:text-[34px] font-black leading-none bg-transparent outline-none border-b border-transparent focus:border-slate-200 w-full" style={{fontFamily:fontTitle}}/>
                    <span className="hidden md:inline-flex items-center gap-1 px-2 py-1 rounded-full border text-[11px] font-bold" style={{borderColor:accent, color:accent}}>● Protégé</span>
                  </div>
                  <div className="flex flex-wrap items-center gap-2 mt-2 text-xs">
                    <span className="px-2 py-1 rounded-full bg-amber-100 text-amber-700 font-bold">★ Article de qualité</span>
                    <span className="opacity-60">Modifié il y a 8 min par <b style={{color:accent}}>Admin Lyra</b> • 2 841 vues</span>
                    <span className="ml-auto flex items-center gap-1">
                      <button className="px-3 py-1 rounded-full border text-xs font-bold">♡ Suivre</button>
                      <button className="px-3 py-1 rounded-full border text-xs font-bold">◰ Historique</button>
                    </span>
                  </div>
                </div>
              </div>

              {/* TOC */}
              {tocVisible && (
                <div className="mt-4 rounded-xl border p-3 flex gap-4" style={{background: darkMode?'#0f172a':'#f8fafc', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
                  <div className="flex-1">
                    <div className="flex items-center gap-2 font-black text-xs tracking-widest">
                      SOMMAIRE <button onClick={()=>setTocVisible(false)} className="ml-auto text-[10px] px-2 py-0.5 rounded-full border">[masquer]</button>
                    </div>
                    <ol className="mt-2 grid grid-cols-2 gap-1 text-xs font-semibold leading-tight">
                      <li>1. Biographie</li><li>4. Galerie</li>
                      <li>2. Pouvoirs & Tableau</li><li>5. Tier List Communauté</li>
                      <li>3. Apparitions</li><li>6. Diagrammes & Stats</li>
                    </ol>
                  </div>
                  <div className="hidden md:block w-px bg-slate-200"/>
                  <div className="hidden md:block text-[11px] leading-tight opacity-70">
                    <div className="font-bold">Raccourcis wikitexte</div>
                    <code className="block mt-1 p-2 rounded bg-white border text-[10px] leading-3">__TOC__<br/>__NOTOC__<br/>__NOEDITSECTION__</code>
                  </div>
                </div>
              )}
              {!tocVisible && <button onClick={()=>setTocVisible(true)} className="mt-3 text-xs font-bold underline">Afficher le sommaire</button>}
            </div>

            {/* Editor area */}
            <div className="px-4 md:px-6 pb-6">
              {editorMode==='source' ? (
                <div className="mt-4">
                  <div className="flex items-center gap-2 mb-2 text-xs font-bold opacity-60"><span className="w-2 h-2 rounded-full bg-red-500"/> MODE SOURCE • Wikitexte brut • Coloration syntaxique</div>
                  <pre className="p-4 rounded-xl border overflow-auto text-[12px] leading-5 max-h-[420px] scrollbar-thin" style={{background: darkMode?'#020617':'#0f172a', color:'#e2e8f0', fontFamily:'JetBrains Mono, monospace'}}>
{wikitext}
                  </pre>
                  <div className="mt-2 flex gap-2 text-xs">
                    <button onClick={()=>navigator.clipboard.writeText(wikitext)} className="px-3 py-1.5 rounded-full bg-slate-900 text-white font-bold">⎘ Copier le wikitexte</button>
                    <span className="opacity-60">ParserFunctions : {"{{#if:}}"} • {"{{#ifeq:}}"} • {"{{#switch:}}"} pris en charge</span>
                  </div>
                </div>
              ) : (
                <div ref={editorRef} className="mt-4 prose max-w-none text-[15px] leading-6" style={{color: darkMode?'#e2e8f0':'#1e293b'}}>
                  <p className="opacity-90">
                    <b className="text-[16px]">{articleTitle}</b> est un personnage central de <i>{wikiName}</i>, introduite au chapitre 1 de la saison 1. Sylphide écarlate de l'<b>Ordre de l'Aube</b>, elle est la gardienne du <a href="#" style={{color:accent}} className="underline">Sanctuaire d'Elyndra</a> depuis la <b>Chute des Étoiles</b> (an 842).
                    <span className="ml-2 inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-bold text-white" style={{background:accent}}>Mise à jour S2</span>
                  </p>

                  <div className="not-prose my-4 rounded-xl border-2 border-dashed p-3 flex flex-wrap gap-2 items-center text-xs font-bold" style={{borderColor:accent, background: `${accent}10`}}>
                    <span>Insertion rapide d'image :</span>
                    <code className="px-2 py-1 rounded bg-white border text-[11px]">{"[[File:"}{imgForm.file}|{imgForm.thumb?'thumb|':''}{imgForm.size}|{imgForm.align}|alt={imgForm.alt}|{imgForm.caption}]]</code>
                    <span className="ml-auto opacity-60">Glisser-déposer une image ici pour l'uploader</span>
                  </div>

                  <h2 className="text-[22px] font-black mt-6 mb-2" style={{fontFamily:fontTitle, color:accent}}>1. Biographie</h2>
                  <p>
                    Née sous la constellation du Phoenix, Aeris fut recueillie par l'Oracle Caelith. Son héritage hybride lui confère une affinité unique avec le <b>Feu Céleste</b> et les <b>Vents d'Aether</b>. D'après le <a href="#" style={{color:accent}}>Journal de Caelith (Tome III)</a>, elle aurait scellé la Brèche d'Obsidienne à seulement 19 ans.
                  </p>
                  <blockquote className="border-l-4 pl-4 italic my-3" style={{borderColor:accent, background: darkMode?'#1e293b':'#fff7ed'}}>
                    “La lumière ne meurt jamais. Elle attend seulement d'être rappelée.” — <b>Aeris, épisode 12</b>
                  </blockquote>

                  <h2 className="text-[22px] font-black mt-6 mb-3" style={{fontFamily:fontTitle, color:accent}}>2. Pouvoirs & Tableau comparatif</h2>
                  <p className="text-sm opacity-70 mb-2">Tableau wikitable triable — éditable en Visuel via le menu <b>Insérer → Tableau</b> (fusion, tri, légende).</p>
                  <div className="overflow-auto rounded-xl border" style={{borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
                    <table className="w-full text-sm border-collapse">
                      <thead>
                        <tr style={{background: accent, color:'#fff'}}>
                          {tableData[0].map(h=>(
                            <th key={h} className="px-3 py-2 text-left font-black text-xs tracking-widest">{h.toUpperCase()} ▾</th>
                          ))}
                          <th className="px-2 py-2">✎</th>
                        </tr>
                      </thead>
                      <tbody>
                        {tableData.slice(1).map((row,i)=>(
                          <tr key={i} className={i%2===0? '' : ''} style={{background: i%2===0? (darkMode?'#0f172a':'#fff') : (darkMode?'#132034':'#f8fafc')}}>
                            {row.map((c,j)=>(
                              <td key={j} className="px-3 py-2 border-t" style={{borderColor: darkMode?'#1e293b':'#f1f5f9'}}>
                                {j===0 ? <span className="font-bold" style={{color:accent}}>{c}</span> : c}
                              </td>
                            ))}
                            <td className="px-2 border-t text-center opacity-40">⋮</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  <div className="mt-2 flex gap-2 text-xs">
                    <button onClick={()=>{
                      const n = [...tableData, ["Nouveau","—","★★★☆☆","—"]]
                      setTableData(n)
                    }} className="px-3 py-1 rounded-full border font-bold">＋ Ligne</button>
                    <button className="px-3 py-1 rounded-full border font-bold">⇅ Rendre triable</button>
                    <button className="px-3 py-1 rounded-full border font-bold">Merge cells</button>
                  </div>

                  <h2 className="text-[22px] font-black mt-6 mb-2" style={{fontFamily:fontTitle, color:accent}}>3. Apparitions</h2>
                  <ul className="list-disc pl-5 space-y-1">
                    <li><b>Saison 1</b> — Épisodes 1 à 13 (rôle principal)</li>
                    <li><b>Film : Écho des Cendres</b> — caméo post-générique</li>
                    <li><b>Manga chap. 47–112</b> — arc du Sanctuaire</li>
                  </ul>

                  <h2 className="text-[22px] font-black mt-6 mb-3" style={{fontFamily:fontTitle, color:accent}}>4. Galerie</h2>
                  <div className="flex items-center gap-2 mb-3 text-xs font-bold">
                    <span className="opacity-60">Mode :</span>
                    {(['grid','slider','slideshow','single'] as const).map(m=>(
                      <button key={m} onClick={()=>setGalleryMode(m)} className={`px-3 py-1 rounded-full border capitalize ${galleryMode===m?'text-white':''}`} style={galleryMode===m?{background:accent, borderColor:accent}:{}}>{m}</button>
                    ))}
                    <button onClick={addGalleryImage} className="ml-auto px-3 py-1 rounded-full text-white font-black" style={{background:accent2}}>＋ Ajouter</button>
                  </div>

                  {/* Gallery renderers */}
                  {galleryMode==='grid' && (
                    <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
                      {gallery.map(g=>(
                        <figure key={g.id} className="group relative overflow-hidden rounded-xl border bg-slate-100">
                          <img src={g.src} alt={g.alt} className="w-full h-[140px] object-cover group-hover:scale-[1.03] transition"/>
                          <figcaption className="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/70 to-transparent p-2 text-white text-xs leading-tight">
                            <input value={g.caption} onChange={e=> setGallery(gal=> gal.map(x=> x.id===g.id? {...x, caption:e.target.value}:x))} className="w-full bg-transparent outline-none border-b border-white/30 focus:border-white"/>
                          </figcaption>
                          <button onClick={()=> setGallery(gal=> gal.filter(x=> x.id!==g.id))} className="absolute top-1 right-1 w-6 h-6 grid place-items-center rounded-full bg-black/60 text-white text-xs">✕</button>
                        </figure>
                      ))}
                    </div>
                  )}
                  {galleryMode==='slideshow' && (
                    <div className="relative rounded-xl overflow-hidden border bg-black">
                      <img src={gallery[sliderIdx].src} className="w-full h-[320px] object-cover"/>
                      <div className="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black via-black/40 to-transparent p-4 text-white">
                        <div className="text-sm font-bold">{gallery[sliderIdx].caption}</div>
                        <div className="text-xs opacity-70">{sliderIdx+1} / {gallery.length} — autoplay</div>
                      </div>
                      <button onClick={()=>setSliderIdx((sliderIdx-1+gallery.length)%gallery.length)} className="absolute left-2 top-1/2 -translate-y-1/2 w-9 h-9 grid place-items-center rounded-full bg-white/90">‹</button>
                      <button onClick={()=>setSliderIdx((sliderIdx+1)%gallery.length)} className="absolute right-2 top-1/2 -translate-y-1/2 w-9 h-9 grid place-items-center rounded-full bg-white/90">›</button>
                    </div>
                  )}
                  {galleryMode==='slider' && (
                    <div className="flex gap-2 overflow-auto pb-2 snap-x">
                      {gallery.map(g=>(
                        <div key={g.id} className="min-w-[220px] snap-start rounded-xl overflow-hidden border bg-white">
                          <img src={g.src} className="w-full h-[150px] object-cover"/>
                          <div className="p-2 text-xs font-semibold leading-tight">{g.caption}</div>
                        </div>
                      ))}
                    </div>
                  )}
                  {galleryMode==='single' && (
                    <div className="rounded-xl overflow-hidden border">
                      <img src={gallery[0].src} className="w-full h-[340px] object-cover"/>
                      <div className="p-3 text-sm">{gallery[0].caption} — <a style={{color:accent}} href="#" className="underline">Voir toutes les images (42)</a></div>
                    </div>
                  )}
                  <div className="mt-2 text-[11px] font-mono p-2 rounded bg-slate-900 text-slate-200 overflow-auto">
                    {`<gallery mode="${galleryMode}" caption="Galerie d'Elyndra" widths="180" spacing="small">`}<br/>
                    {gallery.map(g=> `${g.src.split('/').pop()}|${g.caption}`).join("<br/>")}<br/>
                    {`</gallery>`}
                  </div>

                  <h2 className="text-[22px] font-black mt-6 mb-3" style={{fontFamily:fontTitle, color:accent}}>5. Tier List — Classement Communauté</h2>
                  <p className="text-xs opacity-60 mb-2">Glissez-déposez les portraits entre les rangs S → F. Inspiré du Tier Maker Fandom. Exportable en modèle <code>{"{{Tier List}}"}</code>.</p>
                  <div className="rounded-xl border overflow-hidden" style={{borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
                    {tiers.map(t=>(
                      <div key={t.id} onDragOver={allowDrop} onDrop={()=>onDropTier(t.id)} className="flex min-h-[64px] border-b last:border-0" style={{borderColor: darkMode?'#1e293b':'#f1f5f9'}}>
                        <div className="w-[64px] md:w-[84px] grid place-items-center font-black text-white text-xl" style={{background:t.color}}>{t.label}</div>
                        <div className="flex-1 p-2 flex flex-wrap gap-2" style={{background: darkMode?'#0f172a':'#f8fafc'}}>
                          {t.items.map(it=>(
                            <div key={it.id} draggable onDragStart={()=>onDragStart(t.id, it.id)} className="group relative w-[64px] h-[64px] rounded-xl overflow-hidden border-2 bg-white cursor-grab active:cursor-grabbing shadow-sm" style={{borderColor:t.color}}>
                              <img src={it.img} className="w-full h-full object-cover"/>
                              <div className="absolute inset-x-0 bottom-0 bg-black/70 text-white text-[10px] font-bold px-1 py-0.5 text-center leading-tight truncate">{it.label}</div>
                            </div>
                          ))}
                          {t.items.length===0 && <span className="text-xs opacity-40 self-center">Déposez ici…</span>}
                        </div>
                        <div className="hidden md:flex flex-col gap-1 p-2">
                          <input value={t.label} onChange={e=>updateTierLabel(t.id,e.target.value)} className="w-12 text-center font-black rounded border text-xs py-1"/>
                          <input type="color" value={t.color} onChange={e=> setTiers(ts=> ts.map(x=> x.id===t.id? {...x, color:e.target.value}:x))} className="w-12 h-6 p-0 rounded"/>
                        </div>
                      </div>
                    ))}
                    <div className="p-3 flex flex-wrap gap-2" style={{background: darkMode?'#020617':'#fff'}}>
                      <span className="text-xs font-bold opacity-60 self-center">Réserve :</span>
                      {bankItems.map(b=>(
                        <div key={b.id} draggable onDragStart={()=>onDragStart(null as any, b.id)} className="w-[56px] h-[56px] rounded-xl overflow-hidden border-2 border-dashed cursor-grab bg-white">
                          <img src={b.img} className="w-full h-full object-cover"/>
                        </div>
                      ))}
                      <button onClick={()=>{
                        const id = String.fromCharCode(65+tiers.length)
                        setTiers([...tiers, {id, label:id, color:'#94a3b8', items:[]}])
                      }} className="px-3 py-1 rounded-full border text-xs font-bold">＋ Rang</button>
                    </div>
                  </div>

                  <h2 className="text-[22px] font-black mt-6 mb-3" style={{fontFamily:fontTitle, color:accent}}>6. Diagrammes & Statistiques</h2>
                  <div className="grid md:grid-cols-5 gap-3">
                    <div className="md:col-span-2 rounded-xl border p-3" style={{background: darkMode?'#0f172a':'#fff'}}>
                      <div className="flex gap-1 mb-3">
                        {(['pie','bar','radar','flow'] as DiagramType[]).map(t=>(
                          <button key={t} onClick={()=>setDiagramType(t)} className={`flex-1 py-1.5 rounded-full text-xs font-black capitalize ${diagramType===t?'text-white':''}`} style={diagramType===t?{background:accent}:{background: darkMode?'#1e293b':'#f1f5f9'}}>{t}</button>
                        ))}
                      </div>

                      {/* Chart render */}
                      <div className="rounded-xl border p-3 flex flex-col items-center" style={{background: darkMode?'#020617':'#f8fafc'}}>
                        {diagramType==='pie' && (
                          <div className="relative w-[180px] h-[180px]">
                            <svg viewBox="0 0 100 100" className="w-full h-full -rotate-90">
                              {(()=>{
                                let acc=0
                                const total = diagramData.reduce((s,d)=>s+d.value,0)
                                return diagramData.map(d=>{
                                  const v = d.value/total*100
                                  const dash = `${v} ${100-v}`
                                  const offset = -acc
                                  acc+=v
                                  return <circle key={d.label} r="15.915" cx="50" cy="50" fill="transparent" stroke={d.color} strokeWidth="12" strokeDasharray={dash} strokeDashoffset={offset}/>
                                })
                              })()}
                            </svg>
                            <div className="absolute inset-0 grid place-items-center text-center">
                              <div className="bg-white rounded-full w-16 h-16 grid place-items-center shadow">
                                <div className="text-[10px] font-black leading-none">TOTAL<br/><span className="text-lg">{diagramData.reduce((s,d)=>s+d.value,0)}</span></div>
                              </div>
                            </div>
                          </div>
                        )}
                        {diagramType==='bar' && (
                          <div className="w-full flex items-end gap-2 h-[180px] px-2">
                            {diagramData.map(d=>(
                              <div key={d.label} className="flex-1 flex flex-col items-center gap-1">
                                <div className="w-full rounded-t-lg transition-all" style={{height: `${d.value*1.8}px`, background:d.color}}/>
                                <span className="text-[10px] font-bold truncate w-full text-center">{d.label}</span>
                                <span className="text-[10px] font-black">{d.value}%</span>
                              </div>
                            ))}
                          </div>
                        )}
                        {diagramType==='radar' && (
                          <svg viewBox="0 0 200 200" className="w-[180px] h-[180px]">
                            <polygon points="100,20 180,70 150,170 50,170 20,70" fill="none" stroke="#e2e8f0" strokeWidth="1"/>
                            <polygon points="100,40 160,80 140,150 60,150 40,80" fill="none" stroke="#e2e8f0" strokeWidth="1"/>
                            {(()=>{
                              const pts = diagramData.map((d,i)=>{
                                const ang = (i/diagramData.length)*Math.PI*2 - Math.PI/2
                                const r = 30 + d.value*0.7
                                return `${100+Math.cos(ang)*r},${100+Math.sin(ang)*r}`
                              }).join(" ")
                              return <polygon points={pts} fill={`${accent}30`} stroke={accent} strokeWidth="2"/>
                            })()}
                          </svg>
                        )}
                        {diagramType==='flow' && (
                          <div className="w-full text-[11px] leading-tight font-mono">
                            <div className="rounded-xl border p-2 bg-white text-slate-700">
                              <div className="font-black mb-1" style={{color:accent}}>Flowchart — Progression Aeris</div>
                              <div className="space-y-1">
                                <div className="flex items-center gap-2"><span className="px-2 py-1 rounded bg-slate-900 text-white">Début: Oracle</span> → <span className="px-2 py-1 rounded border">Entraînement</span> → <span className="px-2 py-1 rounded text-white" style={{background:accent}}>Brèche scellée</span></div>
                                <div className="ml-8 border-l-2 pl-3" style={{borderColor:accent}}>↳ Choix : Rejoindre l'Ordre → Gardienne → <b>Sanctuaire</b></div>
                                <div className="text-[10px] opacity-60">Mermaid: graph TD; A[Oracle]--&gt;B[Entraînement]--&gt;C[Brèche]</div>
                              </div>
                            </div>
                          </div>
                        )}
                      </div>

                      <div className="mt-3 space-y-1.5">
                        {diagramData.map((d,i)=>(
                          <div key={d.label} className="flex items-center gap-2 text-xs">
                            <input type="color" value={d.color} onChange={e=>{
                              const nd=[...diagramData]; nd[i].color=e.target.value; setDiagramData(nd)
                            }} className="w-6 h-6 p-0 rounded"/>
                            <input value={d.label} onChange={e=>{
                              const nd=[...diagramData]; nd[i].label=e.target.value; setDiagramData(nd)
                            }} className="flex-1 px-2 py-1 rounded border text-xs font-semibold" style={{background: darkMode?'#020617':'#fff'}}/>
                            <input type="range" min={1} max={60} value={d.value} onChange={e=>{
                              const nd=[...diagramData]; nd[i].value= parseInt(e.target.value); setDiagramData(nd)
                            }} className="w-20"/>
                            <span className="w-8 text-right font-bold">{d.value}</span>
                          </div>
                        ))}
                        <button onClick={()=>{
                          setDiagramData([...diagramData, {label:'Nouveau', value:10, color:'#94a3b8'}])
                        }} className="w-full py-1.5 rounded-full border text-xs font-bold">＋ Ajouter une donnée</button>
                      </div>
                    </div>

                    <div className="md:col-span-3 rounded-xl border p-3" style={{background: darkMode?'#0f172a':'#fff'}}>
                      <div className="text-xs font-black tracking-widest opacity-60">APERÇU WIKITEXTE DIAGRAMME</div>
                      <pre className="mt-2 p-3 rounded-xl bg-slate-900 text-slate-200 text-xs overflow-auto">
{`{{Diagramme
 | type = ${diagramType}
 | titre = Répartition des espèces
 | données =
${diagramData.map(d=>`  ${d.label} = ${d.value}`).join("\n")}
}}`}
                      </pre>
                      <div className="mt-3 grid grid-cols-3 gap-2 text-center text-xs">
                        <div className="rounded-xl border p-2" style={{background: darkMode?'#020617':'#f8fafc'}}>
                          <div className="font-black text-lg" style={{color:accent}}>84%</div>
                          <div className="opacity-60">Complétion lore</div>
                        </div>
                        <div className="rounded-xl border p-2" style={{background: darkMode?'#020617':'#f8fafc'}}>
                          <div className="font-black text-lg" style={{color:accent2}}>127</div>
                          <div className="opacity-60">Pages liées</div>
                        </div>
                        <div className="rounded-xl border p-2" style={{background: darkMode?'#020617':'#f8fafc'}}>
                          <div className="font-black text-lg">4.9★</div>
                          <div className="opacity-60">Note communauté</div>
                        </div>
                      </div>
                      <div className="mt-3 text-[11px] opacity-70">
                        Astuce : utilisez <code className="px-1 rounded bg-slate-100 border">{"<chart>"}</code> ou <code className="px-1 rounded bg-slate-100 border">{"{{#tag:chart}}"}</code> pour intégrer Chart.js / Mermaid dans un modèle.
                      </div>
                    </div>
                  </div>

                  {/* Categories */}
                  <div className="mt-6 rounded-xl border p-3 flex flex-wrap items-center gap-2" style={{background: darkMode?'#0f172a':'#f8fafc', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
                    <span className="text-xs font-black tracking-widest opacity-60">CATÉGORIES</span>
                    {categories.map(c=>(
                      <span key={c} className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full border text-xs font-bold bg-white">
                        <span style={{color:accent}}>#</span> {c}
                        <button onClick={()=> setCategories(cats=> cats.filter(x=> x!==c))} className="ml-1 opacity-40">✕</button>
                      </span>
                    ))}
                    <div className="flex items-center gap-1 ml-auto">
                      <input value={newCat} onChange={e=>setNewCat(e.target.value)} placeholder="Ajouter [[Category:...]]" className="px-3 py-1 rounded-full border text-xs w-[180px]" style={{background:'#fff'}}/>
                      <button onClick={()=>{
                        if(newCat.trim()){ setCategories([...categories, newCat.trim()]); setNewCat("")}
                      }} className="px-3 py-1 rounded-full text-white text-xs font-bold" style={{background:accent}}>＋</button>
                    </div>
                  </div>
                  <div className="text-[11px] opacity-50 mt-1">Syntaxe source : <code>{"[[Category:Personnages]]"}</code> • Les catégories s'affichent en bas d'article et alimentent <b>Special:Categories</b>.</div>
                </div>
              )}
            </div>
          </div>

          {/* Comments / Discussions teaser */}
          <div className="rounded-2xl border p-4" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="flex items-center gap-2 font-black text-sm"><span>💬 Discussions</span><span className="px-2 py-0.5 rounded-full text-white text-xs" style={{background:accent}}>42 commentaires</span><span className="ml-auto text-xs opacity-60">Trier : Récents</span></div>
            <div className="mt-3 space-y-3">
              {[
                {u:"ElyndraFan42",t:"Cette infobox est magnifique ! Comment reproduire le thème élyndra ?",a:"il y a 1h"},
                {u:"WikiGardien",t:"Le tier list S/A est validé par le staff. Pensez à sourcer vos classements !",a:"il y a 3h"},
              ].map(c=>(
                <div key={c.t} className="flex gap-3 p-3 rounded-xl border" style={{background: darkMode?'#0f172a':'#f8fafc'}}>
                  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-pink-500 flex-shrink-0"/>
                  <div className="flex-1">
                    <div className="flex items-center gap-2 text-xs"><span className="font-black" style={{color:accent}}>{c.u}</span><span className="opacity-50">{c.a}</span></div>
                    <div className="text-sm mt-1">{c.t}</div>
                  </div>
                </div>
              ))}
              <div className="flex gap-2">
                <input placeholder="Écrire un commentaire... (wikitexte supporté : '''gras''' ''italique'' [[Lien]])" className="flex-1 px-3 py-2 rounded-full border text-sm" style={{background: darkMode?'#0f172a':'#fff'}}/>
                <button className="px-5 py-2 rounded-full text-white font-bold text-sm" style={{background:accent}}>Envoyer</button>
              </div>
            </div>
          </div>
        </main>

        {/* RIGHT RAIL : Infobox + builder */}
        <aside className="col-span-12 xl:col-span-3 space-y-4">
          {/* Infobox portable */}
          <div className="rounded-2xl border overflow-hidden shadow-sm" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="h-1.5 w-full" style={{background: `linear-gradient(90deg, ${accent}, ${accent2})`}}/>
            <div className="p-3">
              <div className="flex items-center gap-2 text-[11px] font-black tracking-widest opacity-60">
                INFOBOX PORTABLE <span className="ml-auto px-2 py-0.5 rounded-full text-white text-[10px]" style={{background:accent}}>{infoboxTheme}</span>
              </div>

              {/* portable infobox preview */}
              <div className={`mt-2 rounded-xl overflow-hidden border ${infoboxLayout==='stacked'?'':'table'}`} style={{borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
                <div className="px-3 py-3 text-center font-black text-white" style={{background: `linear-gradient(135deg, ${accent}, ${accent2})`, fontFamily:fontTitle}}>
                  <div className="text-[15px] leading-tight">{infoboxItems.find(i=>i.type==='title')?.value}</div>
                  <div className="text-[11px] font-bold opacity-90 tracking-widest mt-1">SENTINELLE • ORDRE DE L'AUBE</div>
                </div>
                <div className="relative">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=600&q=80" className="w-full h-[220px] object-cover"/>
                  <div className="absolute bottom-0 inset-x-0 bg-gradient-to-t from-black/70 to-transparent p-2 flex gap-1">
                    <span className="px-2 py-1 rounded-full bg-white text-[11px] font-black">Image 1 / 3</span>
                    <span className="ml-auto w-7 h-7 grid place-items-center rounded-full bg-white/90">🔍</span>
                  </div>
                </div>
                <div className="divide-y" style={{borderColor: darkMode?'#1e293b':'#f1f5f9'}}>
                  {infoboxItems.filter(i=>i.type==='data').map(item=>(
                    <div key={item.id} className={`${infoboxLayout==='stacked'?'flex flex-col':'flex'} px-3 py-2 text-xs`}>
                      <div className={`${infoboxLayout==='stacked'?'opacity-60 font-black text-[11px] tracking-widest':'w-[110px] font-black opacity-60 shrink-0'}`}>{item.label.toUpperCase()}</div>
                      <div className="flex-1 font-semibold">{item.value}</div>
                    </div>
                  ))}
                  {infoboxItems.filter(i=>i.type==='header').map(h=>(
                    <div key={h.id} className="px-3 py-2 font-black text-xs tracking-widest text-white text-center" style={{background:accent}}>{h.value.toUpperCase()}</div>
                  ))}
                  {infoboxItems.filter(i=>i.type==='navigation').map(n=>(
                    <div key={n.id} className="px-3 py-2 text-xs text-center font-bold flex items-center justify-center gap-2" style={{background: darkMode?'#0f172a':'#f8fafc', color:accent}}>
                      ◀ {n.value} ▶
                    </div>
                  ))}
                </div>
                <div className="p-2 flex gap-1 flex-wrap">
                  <span className="px-2 py-1 rounded-full border text-[10px] font-bold">PortableInfobox</span>
                  <span className="px-2 py-1 rounded-full border text-[10px] font-bold">type=character</span>
                  <span className="px-2 py-1 rounded-full border text-[10px] font-bold">theme={infoboxTheme}</span>
                </div>
              </div>

              <div className="mt-3 grid grid-cols-2 gap-2 text-xs">
                <label className="flex flex-col gap-1 font-bold">Layout
                  <select value={infoboxLayout} onChange={e=>setInfoboxLayout(e.target.value as any)} className="px-2 py-1.5 rounded-lg border">
                    <option value="default">Défaut (table)</option>
                    <option value="stacked">Stacked (mobile)</option>
                  </select>
                </label>
                <label className="flex flex-col gap-1 font-bold">Thème
                  <select value={infoboxTheme} onChange={e=>setInfoboxTheme(e.target.value)} className="px-2 py-1.5 rounded-lg border">
                    <option value="elyndra">elyndra</option>
                    <option value="obsidian">obsidian</option>
                    <option value="aube">aube</option>
                    <option value="phoenix">phoenix</option>
                  </select>
                </label>
              </div>
              <div className="mt-2 flex gap-1.5">
                <button onClick={()=>setInfoboxItems(items=>[...items, {id:Math.random().toString(36).slice(2), type:'data', label:'Nouveau', source:'nouveau', value:'Valeur'}])} className="flex-1 py-1.5 rounded-full border text-xs font-bold">＋ Donnée</button>
                <button onClick={()=>setInfoboxItems(items=> items.slice(0,-1))} className="px-3 py-1.5 rounded-full border text-xs font-bold">↩︎ Retirer</button>
              </div>
            </div>
          </div>

          {/* Panel switcher - builder */}
          <div className="rounded-2xl border overflow-hidden" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="flex overflow-auto scrollbar-thin border-b text-xs font-black" style={{borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
              {[
                {id:'infobox',l:'Infobox Builder'},
                {id:'gallery',l:'Galerie'},
                {id:'media',l:'Média'},
                {id:'tier',l:'Tier & Table'},
                {id:'diagram',l:'Diagrammes'},
                {id:'template',l:'Modèles'},
              ].map(p=>(
                <button key={p.id} onClick={()=>setActivePanel(p.id as any)} className={`px-3 py-2.5 whitespace-nowrap border-b-2 ${activePanel===p.id?'':'opacity-60 border-transparent'}`} style={activePanel===p.id?{borderColor:accent, color:accent}:{}}>{p.l}</button>
              ))}
            </div>

            <div className="p-3 max-h-[520px] overflow-auto scrollbar-thin">
              {activePanel==='infobox' && (
                <div className="space-y-3">
                  <div className="text-xs font-black tracking-widest opacity-60">BUILDER VISUEL (Special:InfoboxBuilder)</div>
                  <div className="grid grid-cols-3 gap-1.5">
                    {[
                      {t:'Titre',ty:'title'},{t:'Image',ty:'image'},{t:'Donnée',ty:'data'},{t:'Header',ty:'header'},{t:'Groupe',ty:'group'},{t:'Nav',ty:'navigation'},{t:'Panel',ty:'group'}
                    ].map(b=>(
                      <button key={b.t} onClick={()=>{
                        setInfoboxItems([...infoboxItems, {id:Math.random().toString(36).slice(2), type:b.ty as any, label:b.t, source:b.t.toLowerCase(), value: b.t}])
                      }} className="py-2 rounded-xl border text-xs font-bold hover:bg-slate-50">＋ {b.t}</button>
                    ))}
                  </div>

                  <div className="space-y-1.5 max-h-[220px] overflow-auto pr-1">
                    {infoboxItems.map(it=>(
                      <div key={it.id} className="flex items-center gap-1 p-2 rounded-xl border text-xs" style={{background: darkMode?'#0f172a':'#f8fafc'}}>
                        <span className="px-1.5 py-0.5 rounded bg-white border text-[10px] font-black">{it.type}</span>
                        <input value={it.label} onChange={e=> setInfoboxItems(arr=> arr.map(x=> x.id===it.id? {...x, label:e.target.value}:x))} className="flex-1 px-2 py-1 rounded border text-xs" placeholder="label"/>
                        <input value={it.source} onChange={e=> setInfoboxItems(arr=> arr.map(x=> x.id===it.id? {...x, source:e.target.value}:x))} className="w-16 px-1 py-1 rounded border text-[10px] font-mono" placeholder="source"/>
                        <button onClick={()=> setInfoboxItems(arr=> arr.filter(x=> x.id!==it.id))} className="w-6 h-6 grid place-items-center rounded-full bg-white border">✕</button>
                      </div>
                    ))}
                  </div>

                  <div className="rounded-xl p-2 border bg-slate-900 text-slate-200 text-[11px] font-mono leading-4 overflow-auto">
                    <div className="opacity-60">{`<infobox layout="${infoboxLayout}" theme="${infoboxTheme}" type="character">`}</div>
                    {infoboxItems.map(it=>{
                      if(it.type==='title') return `  <title source="${it.source}"><default>${it.value}</default></title>`
                      if(it.type==='image') return `  <image source="${it.source}"><caption source="caption"/></image>`
                      if(it.type==='data') return `  <data source="${it.source}"><label>${it.label}</label><default>${it.value}</default></data>`
                      if(it.type==='header') return `  <header>${it.value}</header>`
                      if(it.type==='navigation') return `  <navigation>${it.value}</navigation>`
                      return `  <group><header>${it.label}</header></group>`
                    }).join("\n")}
                    <div className="opacity-60">{"</infobox>"}</div>
                  </div>
                  <div className="text-[11px] opacity-60">Aide : <a className="underline" href="#" style={{color:accent}}>Help:Infoboxes/Tags</a> • <a className="underline" href="#" style={{color:accent}}>Help:Infoboxes/CSS</a> • Classe <code>.pi-theme-{infoboxTheme}</code></div>
                </div>
              )}

              {activePanel==='gallery' && (
                <div className="space-y-3">
                  <div className="text-xs font-black">Galerie — Help:Galleries</div>
                  <div className="grid grid-cols-2 gap-2 text-xs">
                    <label className="flex flex-col gap-1 font-bold">Mode
                      <select value={galleryMode} onChange={e=>setGalleryMode(e.target.value as any)} className="px-2 py-1 rounded border">
                        <option value="grid">grid (classic)</option><option value="slider">slider</option><option value="slideshow">slideshow</option><option value="single">single</option>
                      </select>
                    </label>
                    <label className="flex flex-col gap-1 font-bold">Largeur
                      <select className="px-2 py-1 rounded border"><option>180</option><option>270</option><option>300</option></select>
                    </label>
                  </div>
                  <div className="rounded-xl border p-2 bg-amber-50 text-xs">
                    En <b>Éditeur Visuel</b> : Insérer → Galerie → rechercher <code>File:</code> → glisser pour réordonner → légende → Insérer.
                  </div>
                  <div className="space-y-1">
                    {gallery.slice(0,4).map(g=>(
                      <div key={g.id} className="flex gap-2 items-center p-1.5 rounded-xl border bg-white">
                        <img src={g.src} className="w-12 h-12 rounded-lg object-cover"/>
                        <div className="flex-1 min-w-0">
                          <div className="text-xs font-bold truncate">{g.caption}</div>
                          <div className="text-[11px] opacity-60">File:{g.src.split('/').pop()}</div>
                        </div>
                        <span className="text-[11px]">⋮</span>
                      </div>
                    ))}
                  </div>
                  <button onClick={addGalleryImage} className="w-full py-2 rounded-full text-white font-bold text-xs" style={{background:accent}}>＋ Ajouter une image à la galerie</button>
                </div>
              )}

              {activePanel==='media' && (
                <div className="space-y-3">
                  <div className="text-xs font-black">Insertion d'image — Help:Adding_images</div>
                  <div className="rounded-xl border p-3 space-y-2" style={{background: darkMode?'#0f172a':'#f8fafc'}}>
                    <div className="grid grid-cols-2 gap-2 text-xs">
                      <label className="flex flex-col gap-1 font-bold">Fichier
                        <input value={imgForm.file} onChange={e=>setImgForm({...imgForm, file:e.target.value})} className="px-2 py-1.5 rounded-lg border"/>
                      </label>
                      <label className="flex flex-col gap-1 font-bold">Taille
                        <input value={imgForm.size} onChange={e=>setImgForm({...imgForm, size:e.target.value})} className="px-2 py-1.5 rounded-lg border"/>
                      </label>
                      <label className="flex flex-col gap-1 font-bold">Alignement
                        <select value={imgForm.align} onChange={e=>setImgForm({...imgForm, align:e.target.value})} className="px-2 py-1.5 rounded-lg border">
                          <option value="left">left</option><option value="right">right</option><option value="center">center</option><option value="none">none</option>
                        </select>
                      </label>
                      <label className="flex items-center gap-2 font-bold text-xs mt-5">
                        <input type="checkbox" checked={imgForm.thumb} onChange={e=>setImgForm({...imgForm, thumb:e.target.checked})}/> thumb
                      </label>
                    </div>
                    <label className="flex flex-col gap-1 font-bold text-xs">Légende (caption)
                      <input value={imgForm.caption} onChange={e=>setImgForm({...imgForm, caption:e.target.value})} className="px-2 py-1.5 rounded-lg border"/>
                    </label>
                    <label className="flex flex-col gap-1 font-bold text-xs">Texte alt
                      <input value={imgForm.alt} onChange={e=>setImgForm({...imgForm, alt:e.target.value})} className="px-2 py-1.5 rounded-lg border"/>
                    </label>
                    <div className="flex gap-2">
                      <div className="flex-1 rounded-xl border bg-white p-2 flex gap-2 items-center">
                        <img src={`https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&q=80`} className="w-14 h-14 rounded-lg object-cover"/>
                        <div className="text-[11px] leading-tight">
                          <div className="font-bold">Aperçu thumb</div>
                          <div className="opacity-60">{imgForm.caption}</div>
                        </div>
                      </div>
                      <button className="px-4 rounded-xl text-white font-bold" style={{background:accent}}>Insérer</button>
                    </div>
                    <div className="text-[11px] p-2 rounded bg-slate-900 text-slate-200 font-mono">
                      {`[[File:${imgForm.file}|${imgForm.thumb?'thumb|':''}${imgForm.size}|${imgForm.align}|alt=${imgForm.alt}|${imgForm.caption}]]`}
                    </div>
                    <div className="text-[10px] opacity-60">Uploader via <b>Special:Upload</b> ou glisser-déposer. Images doivent exister sur le wiki (File:). “Image:” = syntaxe legacy.</div>
                  </div>
                  <div className="rounded-xl border p-2 flex gap-2 overflow-auto">
                    {gallery.slice(0,5).map(g=>(
                      <img key={g.id} src={g.src} onClick={()=> setImgForm({...imgForm, file: g.src.split('/').pop()||'File.jpg'})} className="w-14 h-14 rounded-lg object-cover border-2 cursor-pointer hover:border-pink-500"/>
                    ))}
                  </div>
                </div>
              )}

              {activePanel==='tier' && (
                <div className="space-y-3">
                  <div className="text-xs font-black">Tableau & Tier Maker</div>
                  <div className="rounded-xl border p-2 bg-white">
                    <div className="text-[11px] font-bold mb-1">Wikitable source</div>
                    <pre className="text-[11px] font-mono bg-slate-900 text-slate-200 p-2 rounded-xl overflow-auto leading-3">
{`{| class="wikitable sortable" style="text-align:center"
|-
! Personnage !! Rôle !! Puissance
${tableData.slice(1).map(r=>`|-\n| ${r.join(" || ")}`).join("\n")}
|}`}
                    </pre>
                    <button onClick={()=>{
                      const n = [...tableData]
                      n[1][2] = n[1][2]==="★★★★★"?"★★★★☆":"★★★★★"
                      setTableData([...n])
                    }} className="mt-2 w-full py-1.5 rounded-full border text-xs font-bold">Changer étoiles ★</button>
                  </div>
                  <div className="rounded-xl border p-2" style={{background: darkMode?'#0f172a':'#fffbeb'}}>
                    <div className="text-xs font-bold">Tier List → Modèle</div>
                    <pre className="text-[11px] font-mono mt-1 p-2 rounded bg-white border overflow-auto">
{`{{Tier List
 | S = ${tiers.find(t=>t.id==='S')?.items.map(i=>i.label).join(", ")}
 | A = ${tiers.find(t=>t.id==='A')?.items.map(i=>i.label).join(", ")}
 | B = ${tiers.find(t=>t.id==='B')?.items.map(i=>i.label).join(", ")}
}}`}
                    </pre>
                    <div className="text-[11px] opacity-60 mt-1">Faire glisser les cartes dans la colonne centrale pour tester. Export PNG via html2canvas (à implémenter).</div>
                  </div>
                </div>
              )}

              {activePanel==='diagram' && (
                <div className="space-y-3">
                  <div className="text-xs font-black">Diagrammes — Chart & Mermaid</div>
                  <div className="grid grid-cols-2 gap-1.5">
                    {(['pie','bar','radar','flow'] as DiagramType[]).map(t=>(
                      <button key={t} onClick={()=>setDiagramType(t)} className={`py-2 rounded-xl border text-xs font-bold capitalize ${diagramType===t?'text-white':''}`} style={diagramType===t?{background:accent, borderColor:accent}:{}}>{t}</button>
                    ))}
                  </div>
                  <div className="rounded-xl border p-2 bg-white text-xs">
                    <div className="font-bold">Données (label:valeur)</div>
                    <textarea value={diagramData.map(d=>`${d.label}:${d.value}:${d.color}`).join("\n")} onChange={e=>{
                      const lines = e.target.value.split("\n").filter(Boolean)
                      setDiagramData(lines.map(l=>{
                        const [label,val,color]=l.split(":")
                        return {label: label||'Item', value: parseInt(val)||10, color: color||'#94a3b8'}
                      }))
                    }} className="w-full h-[90px] mt-1 p-2 rounded border font-mono text-xs"/>
                  </div>
                  <div className="text-[11px] opacity-60">Astuce Fandom : installez l'extension <b>Chart</b> ou utilisez <code>{"<graph>"}</code> / Mermaid pour les flows. Ici rendu SVG natif sans dépendance.</div>
                </div>
              )}

              {activePanel==='template' && (
                <div className="space-y-2">
                  <div className="text-xs font-black">Modèles & ParserFunctions</div>
                  <div className="rounded-xl border p-2 bg-amber-50 text-xs">
                    Syntaxe : <code>{"{{NomDuModèle|param=valeur}}"}</code> • Condition : <code>{"{{#if: {{{param|}}} | oui | non }}"}</code>
                  </div>
                  <div className="space-y-1.5">
                    {templates.map(t=>(
                      <div key={t.name} className="p-2 rounded-xl border flex items-center gap-2 bg-white">
                        <div className="flex-1 min-w-0">
                          <div className="text-xs font-black">{t.name}</div>
                          <div className="text-[11px] font-mono truncate opacity-60">{t.code}</div>
                        </div>
                        <button onClick={()=>navigator.clipboard.writeText(t.code)} className="px-3 py-1 rounded-full border text-xs font-bold">Copier</button>
                      </div>
                    ))}
                  </div>
                  <div className="rounded-xl p-2 bg-slate-900 text-slate-200 text-xs font-mono">
                    {"{{#switch: {{{affiliation|}}} | Ordre de l'Aube = [[Category:Ordre]] | Abysses = [[Category:Antagonistes]] | #default = [[Category:Autre]] }}"}
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Quick poll / popular */}
          <div className="rounded-2xl border p-3" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="text-xs font-black">📊 Sondage</div>
            <div className="text-sm font-bold mt-1">Qui est le meilleur personnage S2 ?</div>
            {[
              {n:"Aeris",p:62},{n:"Kael",p:23},{n:"Lyra",p:15},
            ].map(o=>(
              <div key={o.n} className="mt-2">
                <div className="flex justify-between text-xs font-bold"><span>{o.n}</span><span>{o.p}%</span></div>
                <div className="h-2 rounded-full bg-slate-100 overflow-hidden mt-1"><div className="h-full" style={{width:`${o.p}%`, background:accent}}/></div>
              </div>
            ))}
            <button className="w-full mt-3 py-1.5 rounded-full text-white text-xs font-black" style={{background:accent}}>Voter</button>
          </div>

          <div className="rounded-2xl border p-3" style={{background:paperBg, borderColor: darkMode?'#1e293b':'#e2e8f0', borderRadius:radius}}>
            <div className="text-xs font-black tracking-widest opacity-60">PAGES POPULAIRES</div>
            <div className="mt-2 space-y-2 text-xs">
              {["Carte interactive","Timeline complète","Bestiaire","Théories fans"].map(p=>(
                <a key={p} className="flex items-center gap-2 p-2 rounded-xl border hover:bg-slate-50">
                  <span className="w-7 h-7 rounded-lg bg-slate-200 grid place-items-center">📄</span>
                  <span className="font-bold">{p}</span><span className="ml-auto opacity-40">›</span>
                </a>
              ))}
            </div>
          </div>
        </aside>
      </div>

      {/* CUSTOMIZER DRAWER */}
      <div className={`fixed inset-y-0 right-0 w-[360px] max-w-[92vw] z-50 transition-transform duration-300 ${showCustomizer?'translate-x-0':'translate-x-full'}`}>
        <div className="h-full overflow-auto border-l shadow-2xl p-4" style={{background: darkMode?'#0f172a':'#ffffff', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full grid place-items-center text-white font-black" style={{background:accent}}>🎨</div>
            <div>
              <div className="font-black text-sm leading-none">Theme Designer</div>
              <div className="text-xs opacity-60">Full customisable — FandomDesktop</div>
            </div>
            <button onClick={()=>setShowCustomizer(false)} className="ml-auto w-8 h-8 grid place-items-center rounded-full border">✕</button>
          </div>

          <div className="mt-4 space-y-4">
            <div className="rounded-2xl border p-3 space-y-3">
              <div className="text-xs font-black tracking-widest opacity-60">IDENTITÉ</div>
              <label className="flex flex-col gap-1 text-xs font-bold">Nom du Wiki
                <input value={wikiName} onChange={e=>setWikiName(e.target.value)} className="px-3 py-2 rounded-xl border"/>
              </label>
              <label className="flex flex-col gap-1 text-xs font-bold">Slogan / sous-titre
                <input value={slogan} onChange={e=>setSlogan(e.target.value)} className="px-3 py-2 rounded-xl border"/>
              </label>
              <div className="grid grid-cols-2 gap-2">
                <label className="flex flex-col gap-1 text-xs font-bold">Accent
                  <div className="flex items-center gap-2">
                    <input type="color" value={accent} onChange={e=>setAccent(e.target.value)} className="w-10 h-10 rounded-lg p-1 border"/>
                    <input value={accent} onChange={e=>setAccent(e.target.value)} className="flex-1 px-2 py-2 rounded-xl border font-mono text-xs"/>
                  </div>
                </label>
                <label className="flex flex-col gap-1 text-xs font-bold">Accent 2
                  <div className="flex items-center gap-2">
                    <input type="color" value={accent2} onChange={e=>setAccent2(e.target.value)} className="w-10 h-10 rounded-lg p-1 border"/>
                    <input value={accent2} onChange={e=>setAccent2(e.target.value)} className="flex-1 px-2 py-2 rounded-xl border font-mono text-xs"/>
                  </div>
                </label>
              </div>
              <div className="grid grid-cols-2 gap-2">
                <label className="flex flex-col gap-1 text-xs font-bold">Fond page
                  <input type="color" value={bgPage} onChange={e=>setBgPage(e.target.value)} className="w-full h-8 rounded-lg p-1 border"/>
                </label>
                <label className="flex flex-col gap-1 text-xs font-bold">Fond article
                  <input type="color" value={paperBg} onChange={e=>setPaperBg(e.target.value)} className="w-full h-8 rounded-lg p-1 border"/>
                </label>
              </div>
              <div className="grid grid-cols-2 gap-2 text-xs">
                <label className="flex flex-col gap-1 font-bold">Police titres
                  <select value={fontTitle} onChange={e=>setFontTitle(e.target.value)} className="px-2 py-2 rounded-xl border">
                    <option value="Rubik">Rubik (Fandom)</option><option value="Inter">Inter</option><option value="Georgia">Serif</option>
                  </select>
                </label>
                <label className="flex flex-col gap-1 font-bold">Arrondi
                  <input type="range" min={8} max={24} value={radius} onChange={e=>setRadius(parseInt(e.target.value))}/>
                </label>
              </div>
            </div>

            <div className="rounded-2xl border p-3 space-y-3">
              <div className="text-xs font-black tracking-widest opacity-60">MISE EN PAGE</div>
              <div className="grid grid-cols-2 gap-2">
                <button onClick={()=>setLayout('desktop')} className={`py-2 rounded-xl border text-xs font-bold ${layout==='desktop'?'text-white':''}`} style={layout==='desktop'?{background:accent, borderColor:accent}:{}}>FandomDesktop</button>
                <button onClick={()=>setLayout('oasis')} className={`py-2 rounded-xl border text-xs font-bold ${layout==='oasis'?'text-white':''}`} style={layout==='oasis'?{background:accent, borderColor:accent}:{}}>Oasis (legacy)</button>
              </div>
              <label className="flex items-center justify-between text-xs font-bold p-2 rounded-xl border">
                <span>Afficher les panels d'aide</span>
                <input type="checkbox" checked={showPanels} onChange={e=>setShowPanels(e.target.checked)} className="w-4 h-4"/>
              </label>
              <label className="flex items-center justify-between text-xs font-bold p-2 rounded-xl border">
                <span>Mode sombre global</span>
                <input type="checkbox" checked={darkMode} onChange={e=>setDarkMode(e.target.checked)} className="w-4 h-4"/>
              </label>
            </div>

            <div className="rounded-2xl border p-3">
              <div className="text-xs font-black tracking-widest opacity-60">EXPORT & AIDE</div>
              <div className="mt-2 grid grid-cols-2 gap-2 text-xs font-bold">
                <button onClick={()=>navigator.clipboard.writeText(wikitext)} className="py-2 rounded-xl text-white" style={{background:accent}}>⎘ Copier wikitexte</button>
                <button className="py-2 rounded-xl border">⬇︎ Export JSON</button>
              </div>
              <div className="mt-3 text-[11px] leading-tight opacity-70">
                <b>Help:Categories</b> pour classer • <b>Help:Templates</b> pour créer des modèles • <b>Help:Galleries</b> pour les galeries avancées • <b>Help:Tables</b> pour tri & fusion.
                Tous les modules sont reliés : une modification ici met à jour l'aperçu et le wikitexte source en temps réel.
              </div>
            </div>

            <div className="text-[11px] text-center opacity-50">
              Studio inspiré de Fandom UCP • PortableInfobox • VisualEditor • Gallery • File: • TierMaker • Charts • 100% customisable
            </div>
          </div>
        </div>
      </div>

      {/* Floating customizer toggle when closed */}
      {!showCustomizer && (
        <button onClick={()=>setShowCustomizer(true)} className="fixed bottom-4 right-4 z-40 px-4 py-3 rounded-full text-white font-black shadow-xl flex items-center gap-2" style={{background:accent}}>
          🎨 Personnaliser le Wiki
        </button>
      )}

      {/* Footer */}
      <footer className="mt-6 border-t py-6" style={{background: darkMode?'#0f172a':'#fff', borderColor: darkMode?'#1e293b':'#e2e8f0'}}>
        <div className="max-w-[1600px] mx-auto px-4 flex flex-col md:flex-row gap-4 items-center justify-between text-xs opacity-70">
          <div className="flex items-center gap-3">
            <span className="w-8 h-8 rounded bg-[#ff004d] grid place-items-center text-white font-black">F</span>
            <span><b>{wikiName}</b> — Communauté Fandom • Propulsé par MediaWiki + PortableInfobox • Contenu sous CC-BY-SA</span>
          </div>
          <div className="flex gap-3 font-bold">
            <a href="#" className="underline">Aide</a><a href="#" className="underline">Confidentialité</a><a href="#" className="underline">Conditions</a>
          </div>
        </div>
      </footer>
    </div>
  )
}
