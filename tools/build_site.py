# -*- coding: utf-8 -*-
"""Gera o site estático pré-renderizado da A M Consultoria (amconsultoriacontabil.com.br).
Uso: python build.py <pasta_saida>
Para trocar autor, telefones etc., edite o bloco CONFIG.
"""
import json, os, sys, html, secrets

OUT = sys.argv[1] if len(sys.argv) > 1 else "site"

# ---------------------------------------------------------------- CONFIG
SITE = "https://amconsultoriacontabil.com.br"
NOME = "A M Consultoria e Auditoria Contábil"
RAZAO = "A M CONSULTORIA E AUDITORIA CONTABIL LTDA"
CNPJ = "62.806.802/0001-40"
FUNDACAO = "2025-09-19"
ENDERECO = {"rua": "Rua Mocajuba, nº 93, Sala 05", "bairro": "Dom Pedro I", "cidade": "Manaus",
            "uf": "AM", "cep": "69040-530"}
GEO = (-3.0845, -60.0365)
TEL1_TXT, TEL1_INTL = "(92) 9431-2735", "+559294312735"
TEL2_TXT, TEL2_INTL = "(11) 98202-7102", "+5511982027102"
EMAIL = "contato@amconsultoriacontabil.com.br"
INSTAGRAM = "https://www.instagram.com/am.consultoria.contabil/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61587344352334"
PORTAL = "https://onvio.com.br/clientcenter/pt/auth"
HORARIO = "Segunda a sexta, das 8h às 18h"
# Autor: preencha nome e CRC do contador responsável para virar autor pessoa (Person) nos artigos.
AUTOR_NOME = ""          # ex.: "Fulano de Tal"
AUTOR_CRC = ""           # ex.: "CRC-AM 000000/O"
AUTOR_CARGO = "Contador responsável técnico"
EQUIPE = "Equipe técnica da A M Consultoria"
PUBLICADO = "2026-11-08"
ATUALIZADO = "2026-11-08"
# ------------------------------------------------------------------------

ORG_ID = SITE + "/#organizacao"
e = html.escape

FONTES = {
    "lc123": ("Lei Complementar nº 123/2006 (Simples Nacional) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm"),
    "l9249": ("Lei nº 9.249/1995 (percentuais de presunção) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/l9249.htm"),
    "l9718": ("Lei nº 9.718/1998 (PIS/Cofins cumulativos) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/l9718compilada.htm"),
    "ctn": ("Código Tributário Nacional, art. 168 (prazo de 5 anos para restituição) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm"),
    "lc116": ("Lei Complementar nº 116/2003 (ISS) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp116.htm"),
    "lc214": ("Lei Complementar nº 214/2025 (IBS e CBS) — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm"),
    "lc224": ("Lei Complementar nº 224/2025 — Planalto", "https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp224.htm"),
    "l15270": ("Lei nº 15.270/2025 (tributação de lucros e dividendos) — Planalto", "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm"),
    "simples": ("Portal do Simples Nacional — Receita Federal", "https://www8.receita.fazenda.gov.br/simplesnacional/"),
    "jucea": ("Junta Comercial do Estado do Amazonas (JUCEA)", "https://www.jucea.am.gov.br/"),
    "cfc": ("Conselho Federal de Contabilidade (CFC) — Código de Ética Profissional do Contador (NBC PG 01)", "https://cfc.org.br/"),
    "esocial": ("Portal eSocial — Governo Federal", "https://www.gov.br/esocial/pt-br"),
    "migalhas224": ("Migalhas — Pedágio do lucro presumido: análise da LC 224/25", "https://www.migalhas.com.br/depeso/447666/pedagio-do-lucro-presumido-analise-da-lc-224-25-e-desafio-da-vigencia"),
    "contabeis224": ("Contábeis — Lucro presumido terá aumento de 10% na base do IRPJ e CSLL em 2026", "https://www.contabeis.com.br/noticias/75261/lucro-presumido-tera-aumento-de-10-na-base-do-irpj-e-csll-em-2026/"),
    "jc15270": ("Jornal Contábil — Lei 15.270 define regras para taxação de lucros e dividendos", "https://jornalcontabil.com.br/noticia/lei-15-270-define-regras-para-taxacao-de-lucros-e-dividendos-a-partir-de-2026/"),
}

NAV = [("/servicos/", "Serviços"), ("/trocar-contador/", "Trocar de contador"),
       ("/abrir-empresa/", "Abrir empresa"), ("/conteudos/", "Conteúdos"), ("/faq/", "Dúvidas"),
       ("/sobre/", "Sobre"), ("/contato/", "Contato")]

PAGES = []  # (path, priority, changefreq)


def org_schema():
    return {
        "@type": ["AccountingService", "ProfessionalService"],
        "@id": ORG_ID,
        "name": NOME,
        "legalName": RAZAO,
        "alternateName": ["A M Consultoria", "AM Consultoria Contábil", "A M Consultoria Contábil"],
        "url": SITE + "/",
        "logo": SITE + "/assets/icon-512.png",
        "image": SITE + "/assets/og-image.jpg",
        "taxID": CNPJ,
        "foundingDate": FUNDACAO,
        "description": "Escritório de contabilidade em Manaus/AM: contabilidade empresarial, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria contábil e tributária, com atendimento 100% digital para empresas de Manaus e de todo o Brasil.",
        "telephone": TEL1_INTL,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": f"{ENDERECO['rua']}, {ENDERECO['bairro']}",
                    "addressLocality": ENDERECO["cidade"], "addressRegion": ENDERECO["uf"],
                    "postalCode": ENDERECO["cep"], "addressCountry": "BR"},
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "08:00", "closes": "18:00"}],
        "areaServed": [{"@type": "City", "name": "Manaus"}, {"@type": "State", "name": "Amazonas"},
                       {"@type": "Country", "name": "Brasil"}],
        "knowsAbout": ["Contabilidade empresarial", "Simples Nacional", "Lucro Presumido", "Lucro Real",
                       "Planejamento tributário", "Zona Franca de Manaus", "ICMS-AM", "ISS Manaus",
                       "Departamento pessoal", "eSocial", "BPO financeiro", "Contas a pagar e a receber", "Fluxo de caixa", "Recuperação de créditos de PIS e COFINS", "Produtos monofásicos", "PER/DCOMP", "Auditoria contábil", "Auditoria tributária",
                       "Abertura de empresas", "Troca de contador", "Reforma tributária IBS e CBS"],
        "contactPoint": [{"@type": "ContactPoint", "telephone": TEL1_INTL, "contactType": "customer service",
                          "areaServed": "BR", "availableLanguage": "Portuguese"},
                         {"@type": "ContactPoint", "telephone": TEL2_INTL, "contactType": "sales",
                          "areaServed": "BR", "availableLanguage": "Portuguese"}],
        "sameAs": [INSTAGRAM, FACEBOOK],
        "priceRange": "$$",
    }


def autor_schema():
    if AUTOR_NOME:
        p = {"@type": "Person", "name": AUTOR_NOME, "jobTitle": AUTOR_CARGO, "worksFor": {"@id": ORG_ID},
             "url": SITE + "/sobre/#equipe"}
        if AUTOR_CRC:
            p["identifier"] = AUTOR_CRC
        return p
    return {"@type": "Organization", "name": EQUIPE, "parentOrganization": {"@id": ORG_ID}, "url": SITE + "/sobre/#equipe"}


def autor_html():
    if AUTOR_NOME:
        crc = f" · {e(AUTOR_CRC)}" if AUTOR_CRC else ""
        return f'<a href="/sobre/#equipe" rel="author">{e(AUTOR_NOME)}</a>, {e(AUTOR_CARGO)}{crc}'
    return f'<a href="/sobre/#equipe" rel="author">{e(EQUIPE)}</a>'


def data_br(iso):
    m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    y, mo, d = iso.split("-")
    return f"{int(d)} de {m[int(mo)-1]} de {y}"


def fontes_html(keys):
    items = "".join(f'<li><a href="{FONTES[k][1]}" rel="noopener" target="_blank">{e(FONTES[k][0])}</a></li>' for k in keys)
    return f'<section class="fontes" aria-labelledby="fontes-titulo"><h2 id="fontes-titulo">Fontes consultadas</h2><ul>{items}</ul></section>'


def faq_block(qas, titulo="Perguntas frequentes", hid="faq"):
    items = "".join(f'<details><summary><h3>{e(q)}</h3></summary><div class="resp"><p>{a}</p></div></details>' for q, a in qas)
    return f'<section class="faq" aria-labelledby="{hid}"><h2 id="{hid}">{e(titulo)}</h2>{items}</section>'


def faq_schema(qas):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qas]}


def breadcrumb(path, titulo, parent=None):
    items = [("Início", "/")]
    if parent:
        items.append(parent)
    if path != "/":
        items.append((titulo, path))
    li = "".join(
        (f'<li><a href="{u}">{e(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{e(n)}</li>')
        for i, (n, u) in enumerate(items))
    schema = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}
    return (f'<nav class="breadcrumb" aria-label="Trilha de navegação"><ol>{li}</ol></nav>' if path != "/" else ""), schema


def page(path, title, desc, body, h1, *, extra_schema=None, parent=None, ptype="WebPage",
         priority="0.8", freq="monthly", lead="", published=PUBLICADO, modified=ATUALIZADO, og_type="website",
         hero_extra=None, hero_ctas=None):
    url = SITE + path
    bc_html, bc_schema = breadcrumb(path, h1 if len(h1) < 60 else title.split(" | ")[0], parent)
    webpage = {"@type": ptype, "@id": url + "#pagina", "url": url, "name": title, "description": desc,
               "inLanguage": "pt-BR", "isPartOf": {"@id": SITE + "/#site"}, "about": {"@id": ORG_ID},
               "datePublished": published, "dateModified": modified, "breadcrumb": bc_schema}
    graph = [org_schema(), {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": NOME,
                            "inLanguage": "pt-BR", "publisher": {"@id": ORG_ID}}, webpage]
    for s in (extra_schema or []):
        graph.append(s)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    nav = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == path else ""}>{n}</a></li>' for u, n in NAV)
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    hero_cls = "hero hero-home" if path == "/" else "hero"
    eyebrow = '<p class="eyebrow">Contabilidade digital · Manaus/AM e todo o Brasil</p>' if path == "/" else ""
    hero_side = hero_extra or ""
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="theme-color" content="#002049">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{e(NOME)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Logo A M Consultoria Contábil">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="google-site-verification" content="qJIGMOABqli3Hxg60j7vU32LTNrX4E3hWsRZ2ecHOqI">
<meta name="msvalidate.01" content="993206048267B258A0408725297B07B2">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" type="text/plain" href="/llms.txt" title="Resumo do site para IA">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=2">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo">
 <div class="wrap topo-in">
  <a class="marca" href="/" aria-label="{e(NOME)} — página inicial"><picture><source srcset="/assets/logo-am.webp" type="image/webp"><img src="/assets/logo-am.png" alt="A M Consultoria Contábil" width="148" height="56"></picture></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-principal">Menu</button>
  <nav aria-label="Menu principal" id="menu-principal"><ul class="menu">{nav}</ul></nav>
  <a class="btn btn-ouro btn-sm topo-cta" href="/orcamento/">Solicitar orçamento</a>
 </div>
</header>
<main id="conteudo">
<article class="pagina">
<header class="{hero_cls}">
 <div class="hero-grade" aria-hidden="true"></div>
 <div class="wrap hero-in">
  <div class="hero-txt">
   {bc_html}
   {eyebrow}
   <h1>{e(h1)}</h1>
   {lead_html}
   {hero_ctas or ""}
  </div>
  {hero_side}
 </div>
</header>
<div class="wrap corpo">
{body}
</div>
</article>
</main>
<footer class="rodape">
 <div class="wrap rod-grid">
  <section aria-labelledby="rod-empresa">
   <h2 id="rod-empresa" class="rod-logo"><img src="/assets/logo-am.png" alt="{e(NOME)}" width="170" height="64" loading="lazy"></h2>
   <p>{e(RAZAO)}<br>CNPJ {CNPJ}</p>
   <address>{e(ENDERECO['rua'])} — {e(ENDERECO['bairro'])}<br>{ENDERECO['cidade']}/{ENDERECO['uf']} · CEP {ENDERECO['cep']}<br>
   WhatsApp: <a href="https://wa.me/{TEL1_INTL[1:]}">{TEL1_TXT}</a> · <a href="https://wa.me/{TEL2_INTL[1:]}">{TEL2_TXT}</a><br>
   E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>{HORARIO}</address>
  </section>
  <nav aria-labelledby="rod-mapa"><h2 id="rod-mapa">Mapa do site</h2><ul>
   <li><a href="/servicos/">Serviços contábeis</a></li><li><a href="/especialidades/">Especialidades</a></li>
   <li><a href="/trocar-contador/">Como trocar de contador</a></li><li><a href="/abrir-empresa/">Abrir empresa em Manaus</a></li>
   <li><a href="/conteudos/">Artigos e estudos</a></li><li><a href="/faq/">Perguntas frequentes</a></li>
   <li><a href="/portal-do-cliente/">Portal do Cliente</a></li><li><a href="/sobre/">Sobre a A M</a></li>
   <li><a href="/contato/">Contato</a></li><li><a href="/orcamento/">Orçamento</a></li></ul></nav>
  <section aria-labelledby="rod-redes"><h2 id="rod-redes">Redes e acesso</h2><ul>
   <li><a href="{INSTAGRAM}" rel="noopener me">Instagram @am.consultoria.contabil</a></li>
   <li><a href="{FACEBOOK}" rel="noopener me">Facebook</a></li>
   <li><a href="{PORTAL}" rel="noopener">Acessar Portal do Cliente (Onvio)</a></li></ul></section>
 </div>
 <p class="wrap legal">© {PUBLICADO[:4]} {e(NOME)} Ltda. Conteúdo informativo; não substitui análise individual do caso da sua empresa.</p>
</footer>
<a class="zap" href="https://wa.me/{TEL1_INTL[1:]}" aria-label="Falar pelo WhatsApp"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.1-1.2-.2-.2-.4-.3Z"/></svg></a>
<script>
(function(){{var d=document.documentElement;d.classList.add('js');
var b=document.querySelector('.menu-btn'),n=document.getElementById('menu-principal');
if(b&&n){{b.addEventListener('click',function(){{var o=n.classList.toggle('aberto');b.setAttribute('aria-expanded',o)}})}}
if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('visivel');io.unobserve(x.target)}}}})}},{{rootMargin:'0px 0px -8% 0px'}});
document.querySelectorAll('.corpo > section, .corpo > aside, .card').forEach(function(el){{el.classList.add('revela');io.observe(el)}});
}})();
</script>
</body>
</html>
"""
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((path, priority, freq, modified))


def cta(texto="Fale com um contador da A M"):
    return (f'<aside class="cta" aria-label="Contato"><p><strong>{e(texto)}.</strong> Atendimento 100% digital para Manaus e todo o Brasil.</p>'
            f'<p><a class="btn btn-ouro" href="/orcamento/">Solicitar orçamento</a> <a class="btn btn-linha" href="https://wa.me/{TEL1_INTL[1:]}">Falar pelo WhatsApp</a></p></aside>')


# ================================================================ ESTUDO ORIGINAL (cálculos)
ANEXO_III = [(180000, .06, 0), (360000, .112, 9360), (720000, .135, 17640), (1800000, .16, 35640),
             (3600000, .21, 125640), (4800000, .33, 648000)]
ANEXO_V = [(180000, .155, 0), (360000, .18, 4500), (720000, .195, 9900), (1800000, .205, 17100),
           (3600000, .23, 62100), (4800000, .305, 540000)]


def simples(rbt, tabela):
    for teto, a, pd in tabela:
        if rbt <= teto:
            return (rbt * a - pd) / rbt
    raise ValueError


def presumido(rbt, folha_pct, iss):
    base = .32 * rbt
    irpj = .15 * base + .10 * max(0, base - 240000)
    csll = .09 * base
    pis_cof = .0365 * rbt
    cpp = .20 * folha_pct * rbt
    return (irpj + csll + pis_cof + iss * rbt + cpp) / rbt


FAIXAS = [180000, 360000, 720000, 1200000, 1800000, 2400000, 3600000, 4800000]


def brl(v):
    return "R$ " + f"{v:,.0f}".replace(",", ".")


def pct(v):
    return f"{v*100:.1f}%".replace(".", ",")


def tabela_estudo(folha, tabela, nome_anexo):
    rows = []
    dados = []
    for r in FAIXAS:
        s = simples(r, tabela)
        p5 = presumido(r, folha, .05)
        p2 = presumido(r, folha, .02)
        menor = min((s, f"Simples ({nome_anexo})"), (p5, "Presumido (ISS 5%)"), (p2, "Presumido (ISS 2%)"))[1]
        dados.append({"receita_anual": r, "simples": round(s, 4), "presumido_iss5": round(p5, 4), "presumido_iss2": round(p2, 4)})
        rows.append(f"<tr><th scope=\"row\">{brl(r)}</th><td>{pct(s)}</td><td>{pct(p5)}</td><td>{pct(p2)}</td><td>{menor}</td></tr>")
    t = (f'<div class="tabela"><table><caption>Carga efetiva sobre a receita — folha de {int(folha*100)}% da receita</caption>'
         f'<thead><tr><th scope="col">Receita bruta anual</th><th scope="col">Simples Nacional ({nome_anexo})</th>'
         f'<th scope="col">Lucro Presumido, ISS 5%</th><th scope="col">Lucro Presumido, ISS 2%</th><th scope="col">Menor carga</th></tr></thead>'
         f'<tbody>{"".join(rows)}</tbody></table></div>')
    return t, dados


# ================================================================ PÁGINAS
def build():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

    # ---------- HOME
    servicos_resumo = [
        ("Contabilidade empresarial e gerencial", "ECD/ECF, conciliação bancária, balancetes mensais, Balanço Patrimonial e DRE com análise para decisão.", "/servicos/#contabilidade"),
        ("Fiscal e inteligência tributária", "Apuração no Simples Nacional, Lucro Presumido e Lucro Real, obrigações acessórias e planejamento tributário, incluindo ICMS-AM, ZFM e ISS Manaus.", "/servicos/#fiscal"),
        ("Departamento pessoal", "Folha, pró-labore, admissões e rescisões com eSocial, DCTFWeb e FGTS Digital.", "/servicos/#departamento-pessoal"),
        ("Consultoria contábil, tributária e financeira", "Plano de contas, centros de custo, fluxo de caixa, separação entre pessoa física e jurídica e reenquadramento tributário.", "/servicos/#consultoria"),
        ("BPO financeiro", "Terceirização da rotina financeira: contas a pagar e a receber, conciliação bancária, emissão de cobranças e notas, e fluxo de caixa integrado à contabilidade.", "/servicos/#bpo-financeiro"),
        ("Recuperação de créditos de PIS e COFINS", "Revisão dos últimos 5 anos para identificar PIS e COFINS pagos a mais, como produtos monofásicos no Simples, ICMS na base de cálculo e créditos de insumos, e recuperação por compensação ou restituição.", "/servicos/#recuperacao-pis-cofins"),
        ("Auditoria contábil e tributária", "Exame de demonstrações, revisão preventiva de apurações dos últimos 5 anos e cruzamento SPED × NF-e × bancos.", "/servicos/#auditoria"),
    ]
    ICONES = [
        '<path d="M4 19V5m0 14h16M8 15v-4m4 4V8m4 7v-6"/>',
        '<path d="M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6"/>',
        '<path d="M16 19v-1a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v1M9.5 10a3 3 0 1 0 0-6 3 3 0 0 0 0 6M21 19v-1a4 4 0 0 0-3-3.9M16 4.1a3 3 0 0 1 0 5.8"/>',
        '<path d="M12 3v3m0 12v3M3 12h3m12 0h3M6 6l2 2m8 8 2 2M6 18l2-2m8-8 2-2"/><circle cx="12" cy="12" r="3"/>',
        '<path d="M3 7h15a3 3 0 0 1 3 3v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7l12-3 1 3M17 13.5h.01"/>',
        '<path d="M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5M12 7.5v9M14.5 9.5c0-1.1-1.1-2-2.5-2s-2.5.9-2.5 2 1.1 1.7 2.5 2 2.5.9 2.5 2-1.1 2-2.5 2-2.5-.9-2.5-2"/>',
        '<path d="M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zm9 16-4-4M8.5 11l2 2 3.5-4"/>',
    ]
    cards = "".join(f'<li class="card card-serv"><span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONES[i]}</svg></span><h3><a href="{u}">{e(t)}</a></h3><p>{e(d)}</p></li>' for i, (t, d, u) in enumerate(servicos_resumo))
    home_faq = [
        ("O que a A M Consultoria faz?", f"A {NOME} é um escritório de contabilidade em Manaus/AM (CNPJ {CNPJ}) que oferece contabilidade empresarial, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria contábil e tributária, com atendimento 100% digital pelo Portal do Cliente."),
        ("A A M atende empresas fora de Manaus?", "Sim. O atendimento e o fluxo de documentos são digitais, então a A M atende empresas de Manaus, do interior do Amazonas e de outros estados."),
        ("A A M atende MEI?", "Não. O escritório atende micro, pequenas e médias empresas enquadradas no Simples Nacional, Lucro Presumido ou Lucro Real. Quem é MEI e está perto de ultrapassar o limite pode procurar a A M para planejar a migração para ME."),
        ("Onde fica o escritório?", f"{ENDERECO['rua']}, bairro {ENDERECO['bairro']}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}. Atendimento {HORARIO.lower()}."),
    ]
    body = f"""
<section class="intro" aria-label="Apresentação"><p>A <strong>{e(NOME)}</strong> é um escritório de contabilidade em Manaus/AM que cuida da contabilidade, dos impostos e da folha de pagamento de micro, pequenas e médias empresas, com processos digitais e atendimento consultivo direto com contadores. Atendemos empresas no Simples Nacional, Lucro Presumido e Lucro Real, em Manaus e em todo o país.</p>
<ul class="stack" aria-label="Tecnologias e sistemas que usamos"><li>Onvio</li><li>Domínio · Thomson Reuters</li><li>eSocial</li><li>SPED</li><li>NF-e / NFS-e</li><li>FGTS Digital</li><li>DCTFWeb</li></ul></section>

<section aria-labelledby="h-servicos"><h2 id="h-servicos">Serviços de contabilidade em Manaus</h2>
<ul class="cards">{cards}</ul>
<p><a href="/servicos/">Ver o escopo completo de cada serviço</a></p></section>

<section aria-labelledby="h-dif" class="faixa"><h2 id="h-dif">Como trabalhamos</h2>
<dl class="pilares pilares-4">
<dt>Tecnologia</dt><dd>Documentos, guias, balancetes e certidões ficam no <a href="/portal-do-cliente/">Portal do Cliente (Onvio, Domínio/Thomson Reuters)</a>, disponível 24 horas.</dd>
<dt>Atendimento</dt><dd>Você conversa diretamente com contadores que conhecem o seu CNPJ e explicam as normas em linguagem clara.</dd>
<dt>Segurança</dt><dd>Monitoramento de certidões negativas (CNDs) e conferência preventiva de obrigações acessórias para reduzir o risco de autuação.</dd>
<dt>Estratégia</dt><dd>Balancetes, DRE e comparativos de regime tributário com leitura executiva para apoiar decisões dos sócios.</dd>
</dl></section>

<section aria-labelledby="h-desafios"><h2 id="h-desafios">Qual é o desafio da sua empresa?</h2>
<ul class="lista-links">
<li><a href="/abrir-empresa/">Estou abrindo uma empresa em Manaus</a> — CNAE, regime tributário, contrato social e licenças.</li>
<li><a href="/trocar-contador/">Quero trocar de contador</a> — como funciona a transição, passo a passo.</li>
<li><a href="/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/">Quero saber se pago imposto demais</a> — estudo comparativo Simples × Presumido 2026.</li>
<li><a href="/especialidades/">Preciso de auditoria, organização contábil ou controles</a> — veja nossas especialidades.</li>
</ul></section>

<section aria-labelledby="h-conteudo"><h2 id="h-conteudo">Conteúdos recentes</h2>
<ul class="lista-links">
<li><a href="/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/">Estudo A M 2026: Simples Nacional ou Lucro Presumido para empresas de serviços</a></li>
<li><a href="/conteudos/quando-trocar-de-contador/">Quando trocar de contador? 7 sinais claros</a></li>
<li><a href="/conteudos/obrigacoes-simples-nacional-alem-do-das/">Simples Nacional: obrigações além do DAS</a></li>
<li><a href="/conteudos/dividendos-e-lucro-presumido-o-que-mudou-em-2026/">Dividendos e Lucro Presumido: o que mudou em 2026</a></li>
</ul></section>
{faq_block(home_faq, "Perguntas rápidas sobre a A M", "faq-home")}
<p><a href="/faq/">Ver todas as perguntas frequentes</a></p>
{cta()}
"""
    hero_ctas = ('<p class="hero-ctas"><a class="btn btn-ouro" href="/orcamento/">Solicitar orçamento</a> '
                 '<a class="btn btn-linha" href="/trocar-contador/">Quero trocar de contador</a> '
                 '<a class="btn btn-linha" href="/abrir-empresa/">Quero abrir minha empresa</a></p>'
                 f'<p class="hero-meta">CNPJ {CNPJ} · {ENDERECO["cidade"]}/{ENDERECO["uf"]} · Atendimento 100% digital</p>')
    painel = """<figure class="painel" aria-label="Ilustração do Portal do Cliente">
  <div class="painel-top"><span></span><span></span><span></span><b>Portal do Cliente · A M</b></div>
  <div class="painel-graf" aria-hidden="true"><i style="--h:38%"></i><i style="--h:52%"></i><i style="--h:66%"></i><i style="--h:84%"></i>
   <svg viewBox="0 0 200 100" preserveAspectRatio="none"><path d="M4 92 C 60 80, 120 52, 186 12" fill="none" stroke="#ECB02C" stroke-width="5" stroke-linecap="round"/><path d="M170 8 L192 8 L186 30" fill="#ECB02C"/></svg></div>
  <ul class="painel-lista">
   <li><span class="dot ok"></span>Guias do mês <em>disponíveis</em></li>
   <li><span class="dot ok"></span>Certidões negativas <em>monitoradas</em></li>
   <li><span class="dot ok"></span>Balancete e DRE <em>no portal</em></li>
   <li><span class="dot ouro"></span>Obrigações acessórias <em>conferidas</em></li>
  </ul>
  <figcaption>Ilustração. Guias, relatórios e certidões ficam no Portal do Cliente, 24 horas.</figcaption>
 </figure>"""
    page("/", f"Contabilidade em Manaus/AM | A M Consultoria Contábil",
         "Contabilidade digital em Manaus/AM: impostos, folha, BPO financeiro, recuperação de PIS e COFINS, consultoria e auditoria. Atendimento 100% digital.",
         body, "Escritório de Contabilidade Digital: um investimento para sua empresa",
         extra_schema=[faq_schema(home_faq)], priority="1.0", freq="weekly", hero_ctas=hero_ctas, hero_extra=painel,
         lead="Contabilidade, impostos e folha de pagamento com tecnologia e atendimento consultivo, em Manaus/AM e em todo o Brasil.")

    # ---------- SERVIÇOS
    serv = [
        ("contabilidade", "Contabilidade empresarial e gerencial",
         "Transformamos a movimentação financeira mensal em relatórios para análise de margens, distribuição de lucros e tomada de decisão com dados reais.",
         ["Escrituração contábil digital (ECD) e ECF conforme as Normas Brasileiras de Contabilidade (NBC TG)",
          "Conciliação bancária e financeira com integração de extratos",
          "Balancetes de verificação analíticos mensais",
          "Balanço Patrimonial para bancos, licitações e investidores",
          "DRE com análise vertical e horizontal"]),
        ("fiscal", "Fiscal e inteligência tributária",
         "Apuração de tributos federais, estaduais (ICMS-AM e incentivos da Zona Franca de Manaus) e municipais (ISS Manaus), com prevenção de multas e busca de redução lícita da carga tributária.",
         ["Apuração no Simples Nacional, Lucro Presumido e Lucro Real",
          "Entrega de obrigações acessórias: PGDAS-D, EFD-ICMS/IPI, EFD-Contribuições, DCTFWeb",
          "Parametrização de emissão de NF-e e NFS-e",
          "Planejamento tributário anual e comparativo entre regimes",
          "Revisão de NCM, CFOP, substituição tributária e retenções na fonte",
          "Preparação para a reforma tributária (IBS e CBS)"]),
        ("departamento-pessoal", "Departamento pessoal e gestão trabalhista",
         "Gestão do ciclo de vida dos colaboradores e do pró-labore dos sócios, em conformidade com eSocial, DCTFWeb e FGTS Digital, com recibos disponíveis no portal.",
         ["Folha de pagamento mensal, adiantamentos e pró-labore",
          "Admissões digitais com validação no eSocial",
          "Programação e cálculo de férias individuais e coletivas",
          "Rescisões com conferência de verbas",
          "Apuração de encargos: INSS, FGTS Digital e IRRF"]),
        ("consultoria", "Consultoria contábil, tributária e financeira",
         "Trabalhamos com sócios e gestores para reorganizar finanças, corrigir enquadramentos e preparar a empresa para crescer.",
         ["Reorganização de plano de contas e centros de custo",
          "Consultoria tributária para operações específicas, contratos B2B e precificação",
          "Análise de fluxo de caixa, capital de giro e ponto de equilíbrio",
          "Separação patrimonial entre pessoa física e jurídica",
          "Estudo de enquadramento e reenquadramento tributário"]),
        ("bpo-financeiro", "BPO financeiro",
         "Terceirizamos a rotina do seu financeiro para que os sócios cuidem do negócio. Como a mesma equipe faz a contabilidade, os lançamentos já chegam conciliados e os relatórios saem mais rápido e com menos erro.",
         ["Contas a pagar: agendamento e controle de vencimentos, com aprovação dos pagamentos pelo cliente",
          "Contas a receber: emissão de boletos e cobranças, baixa de recebimentos e controle de inadimplência",
          "Conciliação bancária e de cartões",
          "Emissão de notas fiscais de serviço e de venda",
          "Fluxo de caixa realizado e projetado",
          "Relatórios gerenciais mensais: DRE gerencial, contas por centro de custo e indicadores",
          "Organização e guarda digital de comprovantes no Portal do Cliente"]),
        ("recuperacao-pis-cofins", "Recuperação de créditos de PIS e COFINS",
         "Revisamos as apurações dos últimos 5 anos, prazo previsto no Código Tributário Nacional, para identificar PIS e COFINS recolhidos a mais e recuperar os valores por compensação com outros tributos federais ou por restituição.",
         ["Empresas do Simples Nacional: segregação de receitas de produtos monofásicos (como medicamentos, cosméticos, autopeças e bebidas), que não deveriam ter PIS e COFINS no DAS",
          "Exclusão do ICMS da base de cálculo do PIS e da COFINS (Tema 69 do STF)",
          "Lucro Real: revisão de créditos sobre insumos pelos critérios de essencialidade e relevância (Tema 779 do STJ)",
          "Revisão de retenções, alíquotas, NCM e CST nas notas fiscais",
          "Retificação de EFD-Contribuições, DCTF e PGDAS-D e pedidos por PER/DCOMP",
          "Relatório com memória de cálculo e análise de risco antes de qualquer compensação"]),
        ("auditoria", "Auditoria contábil e tributária",
         "Exame técnico de demonstrações contábeis, apurações fiscais e controles internos para encontrar inconsistências, passivos ocultos ou créditos não aproveitados.",
         ["Auditoria de balanços e demonstrações financeiras",
          "Revisão tributária preventiva das apurações dos últimos 5 anos (60 meses)",
          "Revisão de processos financeiros, fiscais e de faturamento",
          "Cruzamento SPED × NF-e × extratos bancários",
          "Verificação de lastro documental"]),
    ]
    secs = "".join(
        f'<section id="{i}" aria-labelledby="h-{i}"><h2 id="h-{i}">{e(t)}</h2><p>{e(d)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in it)}</ul>'
        f'<p><a href="/orcamento/?servico={i}">Solicitar orçamento de {e(t.lower())}</a></p></section>' for i, t, d, it in serv)
    toc = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t, *_ in serv)
    serv_schema = {"@type": "ItemList", "name": "Serviços da A M Consultoria", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "item": {"@type": "Service", "name": t, "description": d,
         "provider": {"@id": ORG_ID}, "areaServed": "Manaus, Amazonas e Brasil", "url": f"{SITE}/servicos/#{i}",
         "serviceType": t}} for n, (i, t, d, _) in enumerate(serv)]}
    serv_faq = [
        ("Quais serviços estão incluídos na contabilidade mensal?", "Depende do escopo contratado. Normalmente inclui escrituração contábil, apuração de tributos, entrega de obrigações acessórias e, quando há funcionários, folha de pagamento. Consultoria e auditoria são contratadas à parte."),
        ("O que é BPO financeiro?", "BPO financeiro (Business Process Outsourcing) é a terceirização da rotina financeira da empresa: contas a pagar e a receber, conciliação bancária, emissão de cobranças e notas e fluxo de caixa. Os pagamentos continuam sendo aprovados pelos sócios; a A M executa e controla a rotina e entrega relatórios."),
        ("Preciso contratar a contabilidade para ter o BPO financeiro?", "Não é obrigatório, mas a combinação traz mais ganho: com contabilidade e financeiro na mesma equipe, os lançamentos já chegam conciliados e o fechamento mensal fica mais rápido."),
        ("Como funciona a recuperação de créditos de PIS e COFINS?", "Analisamos as notas fiscais e as apurações dos últimos 5 anos, calculamos os valores pagos a mais e, se houver crédito, retificamos as declarações e pedimos a compensação ou restituição à Receita Federal por PER/DCOMP. Antes de compensar, você recebe um relatório com os valores e os riscos de cada tese."),
        ("Empresa do Simples Nacional pode recuperar PIS e COFINS?", "Sim, quando vende produtos sujeitos à tributação monofásica (por exemplo, medicamentos, cosméticos, autopeças e bebidas) e essas receitas não foram segregadas no PGDAS-D. Nesse caso, PIS e COFINS foram cobrados dentro do DAS sem necessidade."),
        ("A A M trabalha com empresas da Zona Franca de Manaus?", "Sim. Acompanhamos apuração de ICMS-AM e as particularidades fiscais de empresas instaladas na Zona Franca de Manaus, além do ISS do município."),
    ]
    page("/servicos/", f"Serviços de contabilidade em Manaus | A M Consultoria",
         "Contabilidade, fiscal, departamento pessoal, BPO financeiro, recuperação de PIS e COFINS, consultoria e auditoria em Manaus/AM. Veja cada serviço.",
         f'<nav class="sumario" aria-label="Nesta página"><h2>Nesta página</h2><ol>{toc}</ol></nav>{secs}{faq_block(serv_faq)}{fontes_html(["ctn", "lc123", "l9718", "esocial"])}{cta()}',
         "Serviços de contabilidade para empresas em Manaus e no Brasil",
         extra_schema=[serv_schema, faq_schema(serv_faq)], priority="0.9", freq="monthly",
         lead="Contabilidade, impostos, folha, financeiro e recuperação de tributos em um único parceiro.")

    # ---------- ESPECIALIDADES
    esp = [
        ("Abertura de empresa", "Dúvidas sobre CNAE, Simples Nacional ou Lucro Presumido, contrato social e licenças em Manaus.", "/abrir-empresa/"),
        ("Troca de contador", "Falta de retorno, guias enviadas em cima da hora, ausência de relatórios e insegurança sobre os impostos pagos.", "/trocar-contador/"),
        ("Organização contábil", "Contas misturadas, balancetes atrasados, falta de conciliação bancária e dificuldade para comprovar renda ou obter crédito.", "/servicos/#contabilidade"),
        ("Redução de riscos tributários", "Divergências entre notas emitidas e declarações, risco de malha fiscal ou bloqueio de certidões negativas (CNDs).", "/servicos/#fiscal"),
        ("Revisão de impostos", "Suspeita de pagar tributo demais ou dúvida se o Simples Nacional ainda compensa frente ao Lucro Presumido.", "/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/"),
        ("Auditoria", "Validar números entre sócios, auditar demonstrações ou revisar apurações fiscais e trabalhistas passadas.", "/servicos/#auditoria"),
        ("Controles financeiros", "Falta de visibilidade do lucro de cada serviço ou produto e ausência de indicadores para decisão.", "/servicos/#consultoria"),
        ("Contabilidade digital", "Perda de tempo com papéis e e-mails, dificuldade para achar guias, contratos, CNDs ou holerites.", "/portal-do-cliente/"),
    ]
    lis = "".join(f'<li class="card"><h2><a href="{u}">{e(t)}</a></h2><p>{e(d)}</p></li>' for t, d, u in esp)
    page("/especialidades/", f"Especialidades contábeis por desafio | A M Consultoria",
         "Abrir empresa, trocar de contador, organizar a contabilidade, revisar impostos, auditoria e controles: encontre a solução da A M para o desafio da sua empresa.",
         f'<ul class="cards">{lis}</ul>{cta()}', "Qual é o desafio da sua empresa neste momento?",
         priority="0.8", lead="Escolha o cenário mais parecido com o seu.")

    # ---------- TROCAR CONTADOR
    troca_faq = [
        ("Preciso esperar o fim do ano para trocar de contador?", "Não. A troca pode ser feita em qualquer mês. O ideal é definir uma data de corte (normalmente o fechamento de um mês) e respeitar o aviso prévio previsto no contrato com o escritório atual."),
        ("O contador atual é obrigado a entregar os documentos?", "Sim. O Código de Ética Profissional do Contador (NBC PG 01, do Conselho Federal de Contabilidade) prevê que, ao deixar o cliente, o contador entregue ao sucessor os documentos e informações necessários à continuidade dos serviços."),
        ("A troca de contador gera custo ou interrompe a empresa?", "A empresa não para. O novo escritório assume a partir da data de corte e o anterior conclui as obrigações do período que lhe cabia, conforme o contrato."),
        ("Quanto tempo leva a transição?", "Depende do volume de documentos e da colaboração do escritório anterior. A A M conduz o contato com o contador anterior e informa o cronograma no início do processo."),
    ]
    body = f"""
<p>Trocar de contador é um processo comum e seguro quando segue uma ordem clara. A A M conduz a transição com o escritório anterior para que a sua empresa não perca prazos nem documentos.</p>
<section aria-labelledby="h-sinais"><h2 id="h-sinais">Sinais de que é hora de trocar</h2>
<ul><li>Guias de impostos chegam em cima do vencimento ou com erro.</li><li>Você não recebe balancete nem DRE.</li>
<li>Ninguém explica por que o imposto subiu ou se o regime tributário ainda é o melhor.</li><li>Certidões negativas são bloqueadas sem aviso.</li></ul>
<p>Veja o artigo completo: <a href="/conteudos/quando-trocar-de-contador/">7 sinais de que sua empresa precisa trocar de contador</a>.</p></section>
<section aria-labelledby="h-passos"><h2 id="h-passos">Como funciona a troca de contador, passo a passo</h2>
<ol class="passos">
<li><strong>Diagnóstico inicial:</strong> analisamos regime tributário, obrigações em aberto e situação das certidões.</li>
<li><strong>Proposta e contrato:</strong> definimos escopo, honorários e a data de corte.</li>
<li><strong>Comunicação ao escritório anterior:</strong> a empresa formaliza a saída respeitando o aviso prévio do contrato vigente.</li>
<li><strong>Transferência de documentos:</strong> recebemos livros, balancetes, arquivos SPED, folha e senhas de acesso aos órgãos, com termo de entrega.</li>
<li><strong>Procurações e acessos:</strong> atualizamos procurações eletrônicas (e-CAC, SEFAZ-AM, Prefeitura de Manaus) e o acesso ao Portal do Cliente.</li>
<li><strong>Primeiro fechamento:</strong> conferimos saldos de abertura e entregamos o primeiro mês com relatório explicativo.</li>
</ol></section>
{faq_block(troca_faq, "Dúvidas sobre trocar de contador", "faq-troca")}
{fontes_html(["cfc"])}
{cta("Quer trocar de contador com segurança?")}
"""
    howto = {"@type": "HowTo", "name": "Como trocar de contador", "step": [
        {"@type": "HowToStep", "position": i + 1, "name": n} for i, n in enumerate(
            ["Diagnóstico inicial", "Proposta e contrato", "Comunicação ao escritório anterior",
             "Transferência de documentos", "Procurações e acessos", "Primeiro fechamento"])]}
    page("/trocar-contador/", "Como trocar de contador: passo a passo | A M Consultoria",
         "Passo a passo para trocar de contador sem perder prazos: data de corte, entrega de documentos, procurações e primeiro fechamento. A A M conduz a transição.",
         body, "Como trocar de contador sem burocracia", extra_schema=[howto, faq_schema(troca_faq)],
         priority="0.95", freq="monthly", lead="Transição conduzida pela A M, do diagnóstico ao primeiro fechamento.")

    # ---------- ABRIR EMPRESA
    abrir_faq = [
        ("Qual regime tributário escolher ao abrir a empresa?", "Depende da atividade (CNAE), do faturamento previsto e do peso da folha de pagamento. Para empresas de serviços, o Fator R (folha ÷ receita ≥ 28%) define se o Simples usa o Anexo III ou o V. Veja o nosso <a href=\"/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/\">estudo comparativo 2026</a>."),
        ("Onde a empresa é registrada em Manaus?", "O registro de sociedades empresárias é feito na Junta Comercial do Estado do Amazonas (JUCEA), integrada à Redesim. Depois vêm CNPJ, inscrição municipal na Prefeitura de Manaus e, quando a atividade exige, inscrição estadual na SEFAZ-AM e licenças."),
        ("Quanto tempo leva para abrir uma empresa?", "O prazo varia conforme a atividade, a consulta de viabilidade do endereço e as licenças exigidas. Informamos o cronograma estimado após analisar o seu caso."),
        ("A A M abre MEI?", "Não. A A M trabalha com microempresas e empresas de pequeno e médio porte (ME, EPP e demais), não com MEI."),
    ]
    body = f"""
<p>Abrir a empresa com orientação contábil desde o início evita erros de CNAE, de regime tributário e de contrato social que custam caro depois. A A M acompanha todas as etapas em Manaus.</p>
<section aria-labelledby="h-etapas"><h2 id="h-etapas">Etapas para abrir uma empresa em Manaus</h2>
<ol class="passos">
<li><strong>Planejamento:</strong> definição de atividades (CNAE), sócios, capital social e regime tributário.</li>
<li><strong>Consulta de viabilidade:</strong> verificação se o endereço permite a atividade.</li>
<li><strong>Contrato social e registro:</strong> elaboração do ato constitutivo e registro na JUCEA via Redesim.</li>
<li><strong>CNPJ e inscrições:</strong> CNPJ na Receita Federal, inscrição municipal e, se aplicável, inscrição estadual na SEFAZ-AM.</li>
<li><strong>Licenças:</strong> alvará e licenças sanitárias ou ambientais, conforme a atividade.</li>
<li><strong>Opção tributária e início da operação:</strong> opção pelo Simples Nacional no prazo legal ou pelo Lucro Presumido, emissão de notas e rotina contábil.</li>
</ol></section>
{faq_block(abrir_faq, "Dúvidas sobre abrir empresa", "faq-abrir")}
{fontes_html(["jucea", "simples", "lc123"])}
{cta("Vai abrir sua empresa?")}
"""
    page("/abrir-empresa/", "Como abrir empresa em Manaus/AM: etapas e regime | A M",
         "Etapas para abrir empresa em Manaus: CNAE, viabilidade, contrato social na JUCEA, CNPJ, inscrições, licenças e escolha entre Simples Nacional e Lucro Presumido.",
         body, "Como abrir uma empresa em Manaus", extra_schema=[faq_schema(abrir_faq)], priority="0.95",
         lead="Do CNAE ao primeiro mês de operação, com planejamento tributário desde o início.")

    # ---------- PORTAL / TECNOLOGIA
    portal_body = f"""
<p>Clientes da A M acessam documentos fiscais, trabalhistas e contábeis 24 horas por dia no Portal do Cliente, plataforma Onvio da Domínio/Thomson Reuters, sem depender de trocas de e-mail.</p>
<section aria-labelledby="h-func"><h2 id="h-func">O que você encontra no Portal do Cliente</h2>
<dl class="pilares"><dt>Documentos e XMLs</dt><dd>Arquivos contábeis, fiscais e contratos sempre disponíveis.</dd>
<dt>Guias de impostos</dt><dd>DAS, DARF, ICMS e FGTS com alerta de vencimento.</dd>
<dt>DRE e balancetes</dt><dd>Relatórios gerenciais mensais.</dd>
<dt>Certidões (CNDs)</dt><dd>Acompanhamento da regularidade federal, estadual (SEFAZ-AM) e municipal.</dd>
<dt>Folha de pagamento</dt><dd>Holerites, recibos de férias e documentos dos colaboradores.</dd></dl></section>
<section aria-labelledby="h-tec"><h2 id="h-tec">Tecnologia por trás do atendimento</h2>
<p>Captura automatizada de XMLs de notas fiscais e integração de extratos bancários (OFX) reduzem digitação e retrabalho, o que permite fechar a contabilidade no prazo e com mais conferência.</p></section>
<p><a class="btn btn-ouro" href="{PORTAL}" rel="noopener">Acessar o Portal do Cliente</a></p>{cta()}
"""
    page("/portal-do-cliente/", "Portal do Cliente: guias, balancetes e CNDs | A M Consultoria",
         "Portal do Cliente A M (Onvio/Domínio): guias de impostos, balancetes, DRE, certidões negativas, folha e documentos fiscais disponíveis 24 horas.",
         portal_body, "Portal do Cliente: sua contabilidade em um só lugar", priority="0.8",
         lead="Guias, relatórios, balancetes, CNDs e folha disponíveis 24 horas.")
    page("/tecnologia/", f"Contabilidade digital em Manaus | A M Consultoria",
         "Contabilidade 100% digital: integração Onvio/Domínio, captura de XMLs, extratos OFX e atendimento consultivo sem papel para empresas de Manaus e do Brasil.",
         portal_body, "Contabilidade digital, sem papel e sem retrabalho", priority="0.6",
         lead="Como a tecnologia acelera o fechamento e reduz erros.")

    # ---------- SOBRE
    autor_bloco = (f"<p>Os conteúdos do site são escritos e revisados por {autor_html()}.</p>" if AUTOR_NOME else
                   f"<p>Os conteúdos do site são produzidos e revisados pela equipe técnica de contadores da A M, que atende diariamente empresas do Simples Nacional, Lucro Presumido e Lucro Real.</p>")
    body = f"""
<section aria-labelledby="h-quem"><h2 id="h-quem">Quem somos</h2>
<p>A <strong>{e(RAZAO)}</strong> (CNPJ {CNPJ}), fundada em {data_br(FUNDACAO)}, é um escritório de contabilidade com sede em Manaus/AM. Atuamos em contabilidade, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria, com processos digitais e atendimento próximo dos sócios.</p></section>
<section aria-labelledby="h-atuacao"><h2 id="h-atuacao">Onde atuamos</h2>
<p>Atendemos empresas em Manaus, no interior do Amazonas e em outros estados. Conhecemos as particularidades da Zona Franca de Manaus, do ICMS-AM e do ISS de Manaus, além dos regimes federais.</p></section>
<section id="equipe" aria-labelledby="h-equipe"><h2 id="h-equipe">Equipe e responsabilidade técnica</h2>{autor_bloco}</section>
<section aria-labelledby="h-dados"><h2 id="h-dados">Dados da empresa</h2>
<dl class="pilares"><dt>Razão social</dt><dd>{e(RAZAO)}</dd><dt>CNPJ</dt><dd>{CNPJ}</dd>
<dt>Endereço</dt><dd>{e(ENDERECO['rua'])}, {e(ENDERECO['bairro'])}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}</dd>
<dt>Horário</dt><dd>{HORARIO}</dd><dt>Contato</dt><dd>WhatsApp {TEL1_TXT} · {TEL2_TXT} · {EMAIL}</dd></dl></section>
{cta()}
"""
    page("/sobre/", f"Sobre a A M Consultoria Contábil | Escritório em Manaus/AM",
         f"Conheça a A M Consultoria Contábil: escritório em Manaus/AM, CNPJ {CNPJ}, atuação local e nacional, equipe técnica e contatos.",
         body, f"Sobre a {NOME}", ptype="AboutPage", priority="0.8",
         lead="Contabilidade organizada, inteligente e conectada ao seu negócio.")

    # ---------- CONTATO
    body = f"""
<address class="contato">
<p><strong>{e(RAZAO)}</strong></p>
<p>{e(ENDERECO['rua'])} — {e(ENDERECO['bairro'])}<br>{ENDERECO['cidade']}/{ENDERECO['uf']} · CEP {ENDERECO['cep']}</p>
<p>WhatsApp: <a href="https://wa.me/{TEL1_INTL[1:]}">{TEL1_TXT}</a> · <a href="https://wa.me/{TEL2_INTL[1:]}">{TEL2_TXT}</a></p>
<p>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Horário: {HORARIO}</p>
</address>
<p>Prefere enviar os dados da sua empresa? <a href="/orcamento/">Preencha o formulário de orçamento</a>.</p>
"""
    page("/contato/", f"Contato e endereço em Manaus | A M Consultoria",
         f"Fale com a {NOME}: WhatsApp {TEL1_TXT}, e-mail, endereço na Rua Mocajuba, Dom Pedro I, Manaus/AM, e horário de atendimento.",
         body, "Contato", ptype="ContactPage", priority="0.7", lead="Atendimento por WhatsApp, e-mail ou no escritório.")

    # ---------- ORÇAMENTO (Netlify Forms)
    opts_reg = "".join(f"<option>{x}</option>" for x in ["Simples Nacional", "Lucro Presumido", "Lucro Real", "Não sei informar", "Empresa nova (em abertura)"])
    opts_srv = "".join(f"<option>{x}</option>" for x in ["Contabilidade mensal", "Fiscal e tributário", "Departamento pessoal", "BPO financeiro", "Recuperação de créditos de PIS e COFINS", "Consultoria contábil/financeira", "Auditoria contábil e tributária", "Troca de contador", "Abertura de empresa", "Outro"])
    body = f"""
<form class="form" name="orcamento" method="POST" action="/obrigado/" data-netlify="true" netlify-honeypot="campo-extra">
<input type="hidden" name="form-name" value="orcamento">
<p class="oculto"><label>Não preencha: <input name="campo-extra"></label></p>
<p><label for="nome">Nome completo *</label><input id="nome" name="nome" required autocomplete="name"></p>
<p><label for="empresa">Nome da empresa</label><input id="empresa" name="empresa" autocomplete="organization"></p>
<p><label for="cnpj">CNPJ (opcional se a empresa for nova)</label><input id="cnpj" name="cnpj" inputmode="numeric"></p>
<p><label for="whatsapp">WhatsApp com DDD *</label><input id="whatsapp" name="whatsapp" required type="tel" autocomplete="tel"></p>
<p><label for="email">E-mail *</label><input id="email" name="email" required type="email" autocomplete="email"></p>
<p><label for="cidade">Cidade/UF</label><input id="cidade" name="cidade"></p>
<p><label for="regime">Regime tributário atual</label><select id="regime" name="regime">{opts_reg}</select></p>
<p><label for="servico">Serviço desejado</label><select id="servico" name="servico">{opts_srv}</select></p>
<p><label for="mensagem">Conte brevemente a necessidade da sua empresa</label><textarea id="mensagem" name="mensagem" rows="5"></textarea></p>
<p><label class="check"><input type="checkbox" name="lgpd" required> Concordo com o tratamento dos meus dados exclusivamente para retorno comercial da {e(NOME)} Ltda, nos termos da LGPD (Lei nº 13.709/2018).</label></p>
<p><button class="btn btn-ouro" type="submit">Solicitar proposta</button></p>
</form>
"""
    page("/orcamento/", f"Solicitar orçamento de contabilidade | A M Consultoria",
         "Peça uma proposta de contabilidade em Manaus ou em qualquer cidade: diagnóstico tributário inicial, plano de migração e demonstração do Portal do Cliente.",
         body, "Solicite uma avaliação e orçamento para sua empresa", priority="0.7",
         lead="Diagnóstico contábil e tributário inicial, sem compromisso.")
    page("/obrigado/", f"Solicitação recebida | A M Consultoria", "Recebemos sua solicitação de orçamento.",
         "<p>Recebemos seus dados. Um contador da A M vai entrar em contato pelo WhatsApp ou e-mail informado.</p><p><a href=\"/conteudos/\">Enquanto isso, veja nossos conteúdos</a>.</p>",
         "Obrigado! Recebemos sua solicitação", priority="0.1")
    PAGES.pop()  # /obrigado/ fora do sitemap

    # ================================================= ARTIGOS
    artigos = []

    def artigo(slug, titulo, desc, h1, corpo, fontes, faq=None, leitura=5, secao="Gestão empresarial",
               published=PUBLICADO, modified=ATUALIZADO, extra=None, resumo=""):
        path = f"/conteudos/{slug}/"
        meta = (f'<p class="meta">Por {autor_html()} · Publicado em <time datetime="{published}">{data_br(published)}</time>'
                f' · Atualizado em <time datetime="{modified}">{data_br(modified)}</time> · {leitura} min de leitura</p>')
        resumo_html = f'<aside class="resumo" aria-label="Resumo"><h2>Resposta rápida</h2><p>{resumo}</p></aside>' if resumo else ""
        body = meta + resumo_html + corpo + (faq_block(faq, "Perguntas frequentes", "faq-art") if faq else "") + fontes_html(fontes) + \
            '<nav class="relacionados" aria-label="Leia também"><h2>Leia também</h2><ul>' + \
            "".join(f'<li><a href="/conteudos/{s}/">{e(t)}</a></li>' for s, t in ARTIGOS_IDX if s != slug) + \
            '<li><a href="/faq/">Perguntas frequentes sobre contabilidade</a></li></ul></nav>' + cta()
        art = {"@type": "Article", "@id": SITE + path + "#artigo", "headline": h1[:110], "description": desc,
               "datePublished": published, "dateModified": modified, "inLanguage": "pt-BR",
               "author": autor_schema(), "publisher": {"@id": ORG_ID}, "mainEntityOfPage": SITE + path,
               "articleSection": secao, "citation": [FONTES[k][1] for k in fontes]}
        sch = [art] + ([faq_schema(faq)] if faq else []) + (extra or [])
        page(path, titulo, desc, body, h1, extra_schema=sch, parent=("Conteúdos", "/conteudos/"),
             priority="0.8", freq="monthly", published=published, modified=modified, og_type="article")
        artigos.append((path, h1, desc, secao, leitura))

    # --- ESTUDO ORIGINAL
    t30, d30 = tabela_estudo(.30, ANEXO_III, "Anexo III")
    t10, d10 = tabela_estudo(.10, ANEXO_V, "Anexo V")
    ex = 720000
    s3 = simples(ex, ANEXO_III); s5 = simples(ex, ANEXO_V); p5_30 = presumido(ex, .30, .05); p5_10 = presumido(ex, .10, .05)
    dataset = {"@type": "Dataset", "name": "Simulação A M 2026: carga efetiva Simples Nacional × Lucro Presumido para empresas de serviços",
               "description": "Carga tributária efetiva sobre a receita bruta, por faixa de faturamento anual, para empresa de serviços com folha de 30% (Anexo III) e de 10% (Anexo V), comparando Simples Nacional e Lucro Presumido com ISS de 5% e 2%.",
               "creator": {"@id": ORG_ID}, "datePublished": PUBLICADO, "license": "https://creativecommons.org/licenses/by/4.0/",
               "isAccessibleForFree": True, "spatialCoverage": "Manaus, Amazonas, Brasil", "temporalCoverage": "2026",
               "variableMeasured": ["receita_anual", "carga_efetiva_simples", "carga_efetiva_presumido_iss5", "carga_efetiva_presumido_iss2"],
               "distribution": {"@type": "DataDownload", "encodingFormat": "application/json",
                                "contentUrl": SITE + "/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/dados.json"}}
    corpo = f"""
<section aria-labelledby="h-res"><h2 id="h-res">Principais resultados</h2>
<ul>
<li>Com folha de pagamento de <strong>30% da receita</strong> (Fator R atendido, Anexo III), o Simples Nacional teve a menor carga em todas as faixas simuladas, de R$ 180 mil a R$ 4,8 milhões por ano.</li>
<li>Com folha de <strong>10% da receita</strong> (Anexo V), o resultado depende do ISS: com ISS de 2%, o Lucro Presumido teve carga menor em todas as faixas; com ISS de 5%, o Simples (Anexo V) foi mais barato em quase todas, exceto na faixa de R$ 3,6 milhões.</li>
<li>Exemplo com receita de {brl(ex)} por ano: Simples Anexo III = <strong>{pct(s3)}</strong>; Presumido com folha de 30% e ISS 5% = <strong>{pct(p5_30)}</strong>. No Anexo V: Simples = <strong>{pct(s5)}</strong>; Presumido com folha de 10% e ISS 5% = <strong>{pct(p5_10)}</strong>.</li>
<li>Para receita até R$ 4,8 milhões (limite do Simples), o acréscimo de presunção da LC 224/2025 não se aplica, porque ele incide só sobre a parcela da receita anual acima de R$ 5 milhões.</li>
</ul></section>
<section aria-labelledby="h-t30"><h2 id="h-t30">Cenário 1: empresa de serviços com folha de 30% (Anexo III)</h2>{t30}</section>
<section aria-labelledby="h-t10"><h2 id="h-t10">Cenário 2: empresa de serviços com folha de 10% (Anexo V)</h2>{t10}
<p><a href="dados.json">Baixar os dados da simulação (JSON)</a> · Licença CC BY 4.0: cite "A M Consultoria Contábil, 2026".</p></section>
<section aria-labelledby="h-met"><h2 id="h-met">Metodologia</h2>
<ul>
<li><strong>Simples Nacional:</strong> alíquota efetiva = (receita dos últimos 12 meses × alíquota nominal − parcela a deduzir) ÷ receita, usando as tabelas dos Anexos III e V da LC 123/2006. Receita mensal constante. A Contribuição Previdenciária Patronal (CPP) já está no DAS nesses anexos.</li>
<li><strong>Fator R:</strong> folha de salários dos últimos 12 meses (incluindo pró-labore) ÷ receita bruta. Igual ou maior que 28% leva ao Anexo III; abaixo, ao Anexo V.</li>
<li><strong>Lucro Presumido (serviços):</strong> presunção de 32% para IRPJ e CSLL (Lei 9.249/1995); IRPJ de 15% mais adicional de 10% sobre a base que exceder R$ 240 mil por ano; CSLL de 9%; PIS de 0,65% e Cofins de 3% no regime cumulativo (Lei 9.718/1998); ISS de 5% (alíquota máxima da LC 116/2003) ou 2% (mínima); CPP de 20% sobre a folha.</li>
<li><strong>Não incluídos:</strong> RAT/FAP e contribuições de terceiros sobre a folha no Presumido (o que favorece levemente o Presumido nas tabelas), FGTS (igual nos dois regimes), ICMS, retenções na fonte e os valores de teste de CBS e IBS de 2026, que não geram recolhimento efetivo para quem cumpre as obrigações acessórias.</li>
<li><strong>ISS em Manaus:</strong> a alíquota depende do item da lista de serviços; confira a sua no Código Tributário do Município antes de decidir.</li>
</ul></section>
<section aria-labelledby="h-lim"><h2 id="h-lim">Como usar este estudo</h2>
<p>A simulação mostra tendências, não a resposta para a sua empresa. Atividades com receitas mistas (serviço e comércio), retenções, incentivos da Zona Franca de Manaus ou distribuição de lucros relevante exigem cálculo individual. A partir de 2026, dividendos acima de R$ 50 mil por mês para a mesma pessoa física passaram a ter retenção de 10% (Lei 15.270/2025), o que também entra na conta. <a href="/orcamento/">Peça uma simulação com os números da sua empresa</a>.</p></section>
"""
    estudo_faq = [
        ("Simples Nacional ou Lucro Presumido: qual é mais barato para serviços?", "Depende principalmente do Fator R e do ISS. Na simulação da A M, com folha de 30% da receita o Simples (Anexo III) foi mais barato em todas as faixas até R$ 4,8 milhões por ano; com folha de 10% (Anexo V), o Lucro Presumido venceu quando o ISS é de 2%, e o Simples venceu na maioria das faixas quando o ISS é de 5%."),
        ("O que é Fator R?", "É a razão entre a folha de salários dos últimos 12 meses (incluindo pró-labore e encargos previstos em lei) e a receita bruta do mesmo período. Para várias atividades de serviço, Fator R igual ou superior a 28% faz a empresa ser tributada pelo Anexo III, com alíquotas menores que as do Anexo V."),
        ("A LC 224/2025 afeta empresas pequenas no Lucro Presumido?", "Não diretamente. O acréscimo de 10% nos percentuais de presunção vale apenas para a parcela da receita bruta anual acima de R$ 5 milhões; para serviços, a presunção dessa parcela passa de 32% para 35,2%."),
    ]
    global ARTIGOS_IDX
    ARTIGOS_IDX = [
        ("simples-nacional-ou-lucro-presumido-estudo-manaus-2026", "Estudo A M 2026: Simples Nacional ou Lucro Presumido para empresas de serviços"),
        ("quando-trocar-de-contador", "Quando trocar de contador? 7 sinais claros"),
        ("obrigacoes-simples-nacional-alem-do-das", "Simples Nacional: obrigações além do DAS mensal"),
        ("dividendos-e-lucro-presumido-o-que-mudou-em-2026", "Dividendos e Lucro Presumido: o que mudou em 2026"),
    ]
    artigo("simples-nacional-ou-lucro-presumido-estudo-manaus-2026",
           "Simples ou Lucro Presumido em 2026: estudo A M para serviços",
           "Estudo original A M 2026: carga efetiva do Simples Nacional (Anexos III e V) × Lucro Presumido para empresas de serviços, de R$ 180 mil a R$ 4,8 milhões de receita.",
           "Simples Nacional ou Lucro Presumido em 2026? Estudo A M com empresas de serviços",
           corpo, ["lc123", "l9249", "l9718", "lc116", "lc224", "migalhas224", "l15270", "lc214"],
           faq=estudo_faq, leitura=8, secao="Pesquisa original", extra=[dataset],
           resumo="Para empresas de serviços, quem tem folha de pagamento de pelo menos 28% da receita (Fator R) costuma pagar menos no Simples Nacional, Anexo III. Quem tem folha baixa cai no Anexo V; nesse caso o Lucro Presumido foi mais barato quando o ISS é de 2%, mas com ISS de 5% o Simples continuou mais barato na maioria das faixas.")
    with open(os.path.join(OUT, "conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/dados.json"), "w", encoding="utf-8") as f:
        json.dump({"titulo": "Simulação A M 2026 — carga efetiva Simples × Presumido (serviços)", "fonte": SITE,
                   "licenca": "CC BY 4.0", "data": PUBLICADO,
                   "premissas": "Ver metodologia em " + SITE + "/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/",
                   "cenario_folha_30_anexo_III": d30, "cenario_folha_10_anexo_V": d10}, f, ensure_ascii=False, indent=1)

    # --- TROCAR CONTADOR (atualizado)
    corpo = """
<p>Trocar de contador costuma ser adiado por receio de burocracia, mas manter um serviço que não acompanha a empresa custa caro em multas, impostos pagos a mais e decisões tomadas sem números.</p>
<section aria-labelledby="h-7"><h2 id="h-7">7 sinais de que sua empresa precisa trocar de contador</h2><ol>
<li><strong>Guias chegam no dia do vencimento</strong>, sem tempo para conferir ou programar o caixa.</li>
<li><strong>Você nunca recebeu balancete nem DRE</strong>, apenas guias para pagar.</li>
<li><strong>Ninguém revisou o regime tributário</strong> desde a abertura da empresa, mesmo com mudança de faturamento ou de folha.</li>
<li><strong>Multas por atraso de obrigações acessórias</strong> aparecem com frequência.</li>
<li><strong>Certidões negativas (CNDs) são bloqueadas</strong> e você descobre só quando precisa delas.</li>
<li><strong>As respostas demoram dias</strong> ou vêm sem explicação técnica.</li>
<li><strong>O contador não comentou as mudanças de 2026</strong>, como a retenção de IR sobre dividendos (Lei 15.270/2025), o aumento de presunção no Lucro Presumido acima de R$ 5 milhões (LC 224/2025) e a fase de teste do IBS e da CBS.</li>
</ol></section>
<section aria-labelledby="h-como"><h2 id="h-como">Como migrar com segurança</h2>
<p>Defina uma data de corte, formalize a saída respeitando o aviso prévio do contrato e exija o termo de entrega de documentos. O Código de Ética do contador (NBC PG 01) prevê a entrega ao sucessor das informações necessárias à continuidade. Veja o <a href="/trocar-contador/">passo a passo completo da troca de contador</a>.</p></section>
"""
    artigo("quando-trocar-de-contador", "Quando trocar de contador? 7 sinais claros (2026) | A M Consultoria",
           "Guias em cima da hora, falta de balancete, CNDs bloqueadas e nenhuma orientação sobre as mudanças de 2026: 7 sinais de que é hora de trocar de contador.",
           "Quando sua empresa deve trocar de contador? 7 sinais claros", corpo, ["cfc", "l15270", "lc224", "lc214"],
           leitura=5, resumo="É hora de trocar quando o contador só envia guias, não entrega balancete nem DRE, não revisa o regime tributário e não orienta sobre mudanças legais. A troca pode ser feita em qualquer mês, com data de corte e termo de entrega de documentos.")

    # --- SIMPLES obrigações
    corpo = """
<p>O Simples Nacional reúne vários tributos em uma guia única, o DAS, mas não elimina as demais obrigações da empresa. Esquecê-las gera multa e pode levar à exclusão do regime.</p>
<section aria-labelledby="h-obr"><h2 id="h-obr">Obrigações que continuam existindo no Simples Nacional</h2><ul>
<li><strong>PGDAS-D mensal:</strong> declaração da receita que gera o DAS.</li>
<li><strong>DEFIS anual:</strong> declaração de informações socioeconômicas e fiscais.</li>
<li><strong>Folha e eSocial:</strong> admissões, folha, pró-labore e eventos trabalhistas, com DCTFWeb e FGTS Digital.</li>
<li><strong>Escrituração contábil:</strong> necessária para comprovar o lucro distribuído aos sócios e exigida por bancos e licitações.</li>
<li><strong>ICMS fora do DAS:</strong> diferencial de alíquota (DIFAL) e substituição tributária, conforme as operações e a legislação do Amazonas.</li>
<li><strong>Retenções e notas fiscais:</strong> emissão correta de NF-e e NFS-e e controle de retenções.</li>
</ul></section>
<section aria-labelledby="h-2026"><h2 id="h-2026">O que muda com a reforma tributária</h2>
<p>Em 2026, a fase de teste da CBS e do IBS não alcança as empresas do Simples Nacional. A LC 214/2025 prevê que, a partir de 2027, o optante possa escolher recolher IBS e CBS fora do DAS, pelo regime regular, o que pode interessar a quem vende para outras empresas que aproveitam créditos. Essa escolha precisa de simulação.</p></section>
"""
    artigo("obrigacoes-simples-nacional-alem-do-das", "Simples Nacional: obrigações além do DAS (2026) | A M Consultoria",
           "PGDAS-D, DEFIS, eSocial, DCTFWeb, escrituração contábil, DIFAL e notas fiscais: o que a empresa do Simples Nacional precisa cumprir além do DAS mensal.",
           "Simples Nacional: quais obrigações sua empresa precisa acompanhar além do DAS?", corpo,
           ["lc123", "simples", "esocial", "lc214"], leitura=6, secao="Simples Nacional",
           resumo="Além do DAS, a empresa do Simples entrega PGDAS-D e DEFIS, cumpre eSocial, DCTFWeb e FGTS Digital quando tem empregados ou pró-labore, mantém escrituração contábil e acompanha ICMS fora do DAS, como DIFAL e substituição tributária.")

    # --- DIVIDENDOS / PRESUMIDO 2026
    corpo = """
<section aria-labelledby="h-div"><h2 id="h-div">Dividendos: retenção de 10% acima de R$ 50 mil por mês</h2>
<p>A Lei 15.270/2025 criou, a partir de janeiro de 2026, a retenção de imposto de renda de 10% sobre lucros e dividendos pagos por uma mesma empresa a uma mesma pessoa física quando o total no mês passar de R$ 50 mil. Ultrapassado o limite, a retenção incide sobre o valor total pago no mês. A lei também instituiu uma tributação mínima para pessoas físicas de alta renda.</p>
<p>Na prática, a distribuição de lucros continua isenta para valores mensais até esse limite, mas sócios que recebem valores maiores precisam planejar o calendário de distribuição e manter escrituração contábil que comprove o lucro.</p></section>
<section aria-labelledby="h-pres"><h2 id="h-pres">Lucro Presumido: presunção maior acima de R$ 5 milhões</h2>
<p>A LC 224/2025 aumentou em 10% os percentuais de presunção do IRPJ e da CSLL, mas só sobre a parcela da receita bruta anual que exceder R$ 5 milhões. Para serviços, a presunção dessa parcela passa de 32% para 35,2%. O IRPJ seguiu a anterioridade anual (janeiro de 2026) e a CSLL, a nonagesimal (a partir de abril de 2026).</p>
<p>A regra está sendo questionada no Judiciário: há liminares e sentenças em sentidos diferentes, válidas apenas para quem as obteve, e ações diretas de inconstitucionalidade aguardam julgamento no STF. Empresas abaixo de R$ 5 milhões de receita anual não são afetadas.</p></section>
<section aria-labelledby="h-faz"><h2 id="h-faz">O que fazer agora</h2><ul>
<li>Revisar a política de distribuição de lucros dos sócios para 2026 e 2027.</li>
<li>Recalcular o regime tributário com os números atuais (veja o <a href="/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/">estudo A M Simples × Presumido</a>).</li>
<li>Para empresas acima de R$ 5 milhões, avaliar com advogado tributarista a conveniência de discutir a LC 224/2025.</li></ul></section>
"""
    artigo("dividendos-e-lucro-presumido-o-que-mudou-em-2026", "Dividendos e Lucro Presumido: o que mudou em 2026 | A M Consultoria",
           "Retenção de 10% sobre dividendos acima de R$ 50 mil/mês (Lei 15.270/2025) e presunção maior no Lucro Presumido acima de R$ 5 milhões (LC 224/2025): o que muda.",
           "Dividendos e Lucro Presumido: o que mudou em 2026", corpo,
           ["l15270", "jc15270", "lc224", "contabeis224", "migalhas224"], leitura=6, secao="Tributação",
           resumo="Desde 2026, dividendos acima de R$ 50 mil por mês pagos a uma mesma pessoa física sofrem retenção de 10% sobre o total (Lei 15.270/2025). No Lucro Presumido, a parcela da receita anual acima de R$ 5 milhões tem presunção 10% maior (LC 224/2025), regra hoje questionada na Justiça.")

    # ---------- ÍNDICE CONTEÚDOS
    lis = "".join(f'<li class="card"><p class="tag">{e(s)} · {l} min</p><h2><a href="{p}">{e(t)}</a></h2><p>{e(d)}</p></li>' for p, t, d, s, l in artigos)
    page("/conteudos/", "Artigos e estudos de contabilidade | A M Consultoria",
         "Artigos e pesquisas da A M sobre Simples Nacional, Lucro Presumido, dividendos, troca de contador e reforma tributária, com fontes oficiais e datas de atualização.",
         f'<ul class="cards">{lis}</ul>', "Conteúdo para apoiar o empresário", ptype="CollectionPage",
         priority="0.9", freq="weekly", lead="Artigos com fontes oficiais, autor e data de atualização.")

    # ---------- FAQ GERAL
    faq_geral = [
        ("O que faz a A M Consultoria e Auditoria Contábil?", f"É um escritório de contabilidade em Manaus/AM (CNPJ {CNPJ}) que presta serviços de contabilidade empresarial, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria contábil e tributária, com atendimento digital para empresas de todo o Brasil."),
        ("Quanto custa um contador em Manaus?", "Os honorários variam conforme o regime tributário, o número de notas fiscais, o número de funcionários e os serviços contratados. A A M envia uma proposta após um diagnóstico inicial gratuito. <a href=\"/orcamento/\">Solicite aqui</a>."),
        ("A A M atende MEI?", "Não. A A M atende microempresas e empresas de pequeno e médio porte no Simples Nacional, Lucro Presumido e Lucro Real."),
        ("A A M atende empresas de outros estados?", "Sim. Documentos, guias e relatórios circulam pelo Portal do Cliente e o atendimento é feito por WhatsApp, e-mail e videochamada."),
        ("Como funciona a troca de contador?", "Diagnóstico, contrato, comunicação ao escritório anterior respeitando o aviso prévio, transferência de documentos, atualização de procurações e primeiro fechamento. Veja o <a href=\"/trocar-contador/\">passo a passo</a>."),
        ("Posso trocar de contador no meio do ano?", "Sim. A troca pode acontecer em qualquer mês, com uma data de corte definida."),
        ("Como abrir uma empresa em Manaus?", "Planejamento de CNAE e regime, consulta de viabilidade, contrato social e registro na JUCEA via Redesim, CNPJ, inscrições municipal e estadual, licenças e opção tributária. Veja as <a href=\"/abrir-empresa/\">etapas</a>."),
        ("Simples Nacional ou Lucro Presumido: qual escolher?", "Depende da atividade, da folha (Fator R), do ISS e do faturamento. Nosso <a href=\"/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/\">estudo 2026</a> compara 16 cenários de empresas de serviços."),
        ("O que é Fator R?", "Folha de salários dos últimos 12 meses, incluindo pró-labore, dividida pela receita bruta do período. Para diversas atividades de serviço, resultado igual ou maior que 28% leva ao Anexo III do Simples, com alíquotas menores que as do Anexo V."),
        ("Dividendos continuam isentos em 2026?", "Parcialmente. Desde janeiro de 2026, há retenção de 10% de imposto de renda quando uma empresa paga mais de R$ 50 mil no mês à mesma pessoa física, calculada sobre o total pago (Lei 15.270/2025)."),
        ("O Lucro Presumido ficou mais caro em 2026?", "Só para quem fatura mais de R$ 5 milhões por ano: a LC 224/2025 aumentou em 10% os percentuais de presunção sobre a parcela da receita acima desse valor. A regra é questionada judicialmente."),
        ("O que muda com o IBS e a CBS?", "Em 2026 há uma fase de teste (CBS de 0,9% e IBS de 0,1%) para empresas do regime regular, sem recolhimento efetivo para quem cumpre as obrigações acessórias. Empresas do Simples não participam do teste em 2026."),
        ("A A M faz BPO financeiro?", "Sim. A A M assume a rotina financeira da empresa: contas a pagar e a receber, conciliação bancária, emissão de cobranças e notas e fluxo de caixa, com relatórios mensais. Os pagamentos continuam aprovados pelos sócios. Veja o <a href=\"/servicos/#bpo-financeiro\">escopo do BPO financeiro</a>."),
        ("É possível recuperar PIS e COFINS pagos a mais?", "Sim, dentro do prazo de 5 anos. Os casos mais comuns são produtos monofásicos não segregados no Simples Nacional, a exclusão do ICMS da base de cálculo (Tema 69 do STF) e créditos de insumos no Lucro Real. Veja como funciona a <a href=\"/servicos/#recuperacao-pis-cofins\">recuperação de créditos de PIS e COFINS</a>."),
        ("A A M atende empresas da Zona Franca de Manaus?", "Sim. Acompanhamos ICMS-AM, incentivos e obrigações próprias de empresas instaladas na Zona Franca de Manaus."),
        ("O que é o Portal do Cliente?", "É a plataforma Onvio (Domínio/Thomson Reuters) onde o cliente acessa guias, balancetes, DRE, certidões, folha e documentos 24 horas por dia."),
        ("Preciso ir ao escritório?", f"Não. Todo o atendimento pode ser digital. Se preferir, o escritório fica na {ENDERECO['rua']}, {ENDERECO['bairro']}, Manaus/AM, {HORARIO.lower()}."),
        ("Que documentos preciso para pedir orçamento?", "CNPJ (se a empresa já existir), regime tributário atual, faturamento médio mensal, número de funcionários e quantidade aproximada de notas fiscais emitidas e recebidas por mês."),
    ]
    page("/faq/", "Perguntas frequentes sobre contabilidade | A M Consultoria",
         "Respostas sobre honorários, troca de contador, abertura de empresa, Simples × Presumido, Fator R, dividendos em 2026, IBS/CBS e atendimento da A M em Manaus.",
         faq_block(faq_geral, "Perguntas e respostas", "faq-geral") + fontes_html(["lc123", "ctn", "l15270", "lc224", "lc214", "cfc", "jucea"]) + cta("Não encontrou sua dúvida?"),
         "Perguntas frequentes sobre contabilidade", ptype="FAQPage", extra_schema=[], priority="0.9",
         lead="Respostas diretas às dúvidas mais comuns de empresários sobre contabilidade e impostos.")
    # FAQPage: a própria WebPage já é FAQPage; adiciona mainEntity
    fp = os.path.join(OUT, "faq/index.html")
    s = open(fp, encoding="utf-8").read()
    graph_obj = json.loads(s.split('<script type="application/ld+json">')[1].split("</script>")[0])
    for n in graph_obj["@graph"]:
        if n.get("@type") == "FAQPage":
            n["mainEntity"] = faq_schema(faq_geral)["mainEntity"]
    new_ld = json.dumps(graph_obj, ensure_ascii=False, indent=1)
    s = s.split('<script type="application/ld+json">')[0] + '<script type="application/ld+json">\n' + new_ld + "\n</script>" + s.split("</script>", 1)[1]
    open(fp, "w", encoding="utf-8").write(s)

    # ---------- 404
    page("/404-tmp/", f"Página não encontrada | A M Consultoria", "Página não encontrada.",
         '<p>O endereço acessado não existe. Veja: <a href="/">Início</a> · <a href="/servicos/">Serviços</a> · <a href="/faq/">Perguntas frequentes</a> · <a href="/contato/">Contato</a></p>',
         "Página não encontrada", priority="0")
    PAGES.pop()
    s = open(os.path.join(OUT, "404-tmp/index.html"), encoding="utf-8").read().replace(
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">', '<meta name="robots" content="noindex">')
    import re
    s = re.sub(r'<link rel="canonical"[^>]+>\n', "", s)
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(s)
    import shutil; shutil.rmtree(os.path.join(OUT, "404-tmp"))

    # ---------- robots.txt
    bots = ["OAI-SearchBot", "ChatGPT-User", "GPTBot", "ClaudeBot", "Claude-SearchBot", "Claude-User",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot",
            "Applebot-Extended", "Amazonbot", "DuckAssistBot", "meta-externalagent", "MistralAI-User", "CCBot"]
    robots = "# robots.txt — A M Consultoria Contábil\n# Todos os robôs de busca e de IA estão liberados.\n\n"
    robots += "".join(f"User-agent: {b}\nAllow: /\nDisallow: /admin\n\n" for b in bots)
    robots += "User-agent: *\nAllow: /\nDisallow: /admin\n\n"
    robots += f"Sitemap: {SITE}/sitemap.xml\n"
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(robots)

    # ---------- sitemap.xml
    xs = "".join(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{m}</lastmod>\n    <changefreq>{f}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n"
                 for p, pr, f, m in PAGES)
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + xs + "</urlset>\n")

    # ---------- llms.txt
    llms = f"""# {NOME}

> Escritório de contabilidade em Manaus/AM (Brasil), {RAZAO}, CNPJ {CNPJ}, fundado em {FUNDACAO}. Presta contabilidade empresarial, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria contábil e tributária para micro, pequenas e médias empresas no Simples Nacional, Lucro Presumido e Lucro Real, com atendimento 100% digital em Manaus e em todo o Brasil. Não atende MEI.

- Endereço: {ENDERECO['rua']}, {ENDERECO['bairro']}, Manaus/AM, CEP {ENDERECO['cep']}
- WhatsApp: {TEL1_TXT} e {TEL2_TXT} · E-mail: {EMAIL}
- Horário: {HORARIO}
- Instagram: {INSTAGRAM}

## Páginas principais
- [Serviços]({SITE}/servicos/): escopo de contabilidade, fiscal, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria
- [Trocar de contador]({SITE}/trocar-contador/): passo a passo da transição
- [Abrir empresa em Manaus]({SITE}/abrir-empresa/): etapas, JUCEA, inscrições e regime tributário
- [Perguntas frequentes]({SITE}/faq/): 18 respostas diretas
- [Sobre]({SITE}/sobre/): dados da empresa e equipe
- [Contato]({SITE}/contato/)

## Conteúdos e pesquisas
""" + "".join(f"- [{t}]({SITE}{p}): {d}\n" for p, t, d, s, l in artigos) + f"""
## Dados abertos
- [Simulação Simples × Presumido 2026 (JSON, CC BY 4.0)]({SITE}/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/dados.json)
"""
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(llms)

    # ---------- Netlify: redirects + headers
    redirects = """# Rotas antigas sem página própria
/agendamento   /contato/   301
/solucoes      /especialidades/   301
# Domínio único (sem www)
https://www.amconsultoriacontabil.com.br/*  https://amconsultoriacontabil.com.br/:splat  301!
"""
    open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8").write(redirects)
    open(os.path.join(OUT, "_headers"), "w", encoding="utf-8").write(
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n\n"
        "/llms.txt\n  Content-Type: text/plain; charset=utf-8\n\n/robots.txt\n  Content-Type: text/plain; charset=utf-8\n")

    # ---------- IndexNow key
    key = "6c8eed4838e5bc22db961959049de48e"  # chave IndexNow fixa (já registrada)
    open(os.path.join(OUT, f"{key}.txt"), "w").write(key)

    # ---------- favicon + css
    open(os.path.join(OUT, "favicon.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#002049"/>'
        '<g fill="#ECB02C"><rect x="12" y="38" width="8" height="16" rx="1"/><rect x="24" y="32" width="8" height="22" rx="1"/>'
        '<rect x="36" y="26" width="8" height="28" rx="1"/><rect x="48" y="18" width="8" height="36" rx="1"/>'
        '<path d="M10 33 C 24 30, 38 22, 50 11 l-4 -1 l12 -3 l-3 12 l-2 -4 C 41 26, 26 34, 10 35 z"/></g></svg>')
    open(os.path.join(OUT, "assets/site.css"), "w").write(CSS)
    import shutil as _sh
    brand = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand")
    for fn in ["logo-am.png", "logo-am.webp", "og-image.jpg", "icon-512.png"]:
        _sh.copy(os.path.join(brand, fn), os.path.join(OUT, "assets", fn))
    for fn in ["apple-touch-icon.png", "favicon-48.png"]:
        _sh.copy(os.path.join(brand, fn), os.path.join(OUT, fn))


CSS = """
:root{--navy:#002049;--navy2:#011634;--navy3:#0A2D5C;--ouro:#ECB02C;--ouro2:#F6C95A;--ouro-esc:#B9860F;
--fundo:#F5F7FB;--card:#fff;--linha:#E1E7F0;--texto:#0E1B2E;--suave:#4A5A70;--azul:#1D5FA8;--gelo:#EAF1FA;
--raio:16px;--sombra:0 1px 2px rgba(0,32,73,.06),0 8px 24px rgba(0,32,73,.08)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--fundo);color:var(--texto);font:16px/1.7 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto}
a{color:var(--azul);text-underline-offset:3px}a:hover{color:var(--navy)}
.wrap{max-width:1160px;margin:0 auto;padding:0 20px}
.pular{position:absolute;left:-9999px}.pular:focus{left:16px;top:16px;background:#fff;padding:8px 12px;z-index:99;border-radius:8px}
:focus-visible{outline:3px solid var(--ouro);outline-offset:2px}

/* topo */
.topo{background:rgba(0,32,73,.96);backdrop-filter:saturate(140%) blur(10px);position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(236,176,44,.18)}
.topo-in{display:flex;align-items:center;gap:24px;min-height:76px}
.marca{display:flex;flex-shrink:0}.marca img{height:46px;width:auto;display:block}
.menu{display:flex;flex-wrap:wrap;gap:2px 4px;list-style:none;margin:0;padding:0}
#menu-principal{flex:1;display:flex;justify-content:flex-end}
.menu a{display:block;text-decoration:none;color:#C9D6EA;font-size:.9rem;font-weight:500;padding:8px 10px;border-radius:8px;transition:color .2s,background .2s}
.menu a:hover{color:#fff;background:rgba(255,255,255,.06)}
.menu a[aria-current]{color:var(--ouro);font-weight:600}
.menu-btn{display:none;margin-left:auto;background:transparent;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:10px;padding:8px 14px;font:inherit;font-weight:600;cursor:pointer}
@media(max-width:1060px){
 .menu-btn{display:block}.topo .topo-cta{display:none}
 .js #menu-principal{display:none;flex-basis:100%}.js #menu-principal.aberto{display:block}
 .topo-in{flex-wrap:wrap;padding:10px 20px}.menu{flex-direction:column;padding:6px 0 14px}
 #menu-principal{flex-basis:100%}
}

/* botões */
.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font:600 .97rem/1 Inter,sans-serif;padding:15px 22px;border-radius:12px;border:0;cursor:pointer;margin:4px 8px 4px 0;transition:transform .15s,box-shadow .2s,background .2s,color .2s}
.btn-sm{padding:11px 16px;font-size:.88rem;margin:0}
.btn-ouro{background:linear-gradient(180deg,var(--ouro2),var(--ouro));color:var(--navy);box-shadow:0 6px 20px -6px rgba(236,176,44,.6)}
.btn-ouro:hover{color:var(--navy);transform:translateY(-1px);box-shadow:0 10px 26px -6px rgba(236,176,44,.75)}
.btn-linha{background:rgba(255,255,255,.04);color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.35)}
.btn-linha:hover{color:var(--navy);background:#fff}

/* hero */
.hero{position:relative;overflow:hidden;background:radial-gradient(1100px 500px at 85% -10%,rgba(29,95,168,.55),transparent 60%),radial-gradient(700px 400px at 0% 120%,rgba(236,176,44,.14),transparent 60%),linear-gradient(180deg,var(--navy),var(--navy2));color:#fff;padding:42px 0 54px}
.hero-grade{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:radial-gradient(ellipse at 70% 30%,#000 20%,transparent 75%);mask-image:radial-gradient(ellipse at 70% 30%,#000 20%,transparent 75%);pointer-events:none}
.hero-in{position:relative;display:grid;grid-template-columns:1fr;gap:40px;align-items:center}
.hero h1{font-family:Montserrat,sans-serif;font-weight:800;font-size:clamp(1.85rem,4.2vw,3rem);line-height:1.12;letter-spacing:-.02em;margin:.2em 0 .35em;max-width:20em}
.hero .lead{font-size:1.14rem;color:#C9D6EA;max-width:40em;margin:0 0 8px}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font:500 .78rem/1 "JetBrains Mono",monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--ouro);background:rgba(236,176,44,.1);border:1px solid rgba(236,176,44,.35);padding:8px 12px;border-radius:99px;margin:6px 0 10px}
.eyebrow::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--ouro);box-shadow:0 0 0 4px rgba(236,176,44,.25);animation:pulsa 2.2s infinite}
@keyframes pulsa{50%{box-shadow:0 0 0 8px rgba(236,176,44,0)}}
.hero-home{padding:64px 0 84px}
.hero-home .hero-in{grid-template-columns:1.15fr .85fr}
.hero-home h1{font-size:clamp(2.1rem,5vw,3.6rem)}
.hero-ctas{margin:26px 0 10px}.hero-meta{font:500 .8rem/1.5 "JetBrains Mono",monospace;color:#8FA3C0;margin:6px 0 0}
@media(max-width:900px){.hero-home .hero-in{grid-template-columns:1fr}.hero-home{padding:44px 0 56px}}
@media(max-width:560px){.eyebrow{font-size:.68rem;letter-spacing:.03em}.hero-ctas .btn{width:100%;justify-content:center;margin-right:0}.marca img{height:40px}}
.breadcrumb ol{list-style:none;display:flex;flex-wrap:wrap;gap:6px;padding:0;margin:0 0 14px;font-size:.84rem;color:#8FA3C0}
.breadcrumb a{color:#C9D6EA;text-decoration:none}.breadcrumb a:hover{color:var(--ouro)}
.breadcrumb li+li::before{content:"/";margin-right:6px;color:#5C7395}

/* painel ilustrativo */
.painel{margin:0;background:linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.03));border:1px solid rgba(255,255,255,.14);border-radius:20px;padding:18px;box-shadow:0 30px 80px -30px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.08);backdrop-filter:blur(6px)}
.painel-top{display:flex;align-items:center;gap:6px;font:500 .78rem "JetBrains Mono",monospace;color:#AFC0D8;margin-bottom:14px}
.painel-top span{width:9px;height:9px;border-radius:50%;background:#2E4A73}.painel-top span:first-child{background:var(--ouro)}
.painel-top b{font-weight:500;margin-left:8px}
.painel-graf{position:relative;height:170px;display:flex;align-items:flex-end;gap:14%;padding:0 6% 0 8%;background:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px) 0 0/100% 34px;border-radius:12px;border:1px solid rgba(255,255,255,.08)}
.painel-graf i{flex:1;height:var(--h);background:linear-gradient(180deg,var(--ouro2),var(--ouro-esc));border-radius:5px 5px 0 0;transform-origin:bottom;animation:cresce 1.1s cubic-bezier(.2,.8,.2,1) both}
.painel-graf i:nth-child(2){animation-delay:.12s}.painel-graf i:nth-child(3){animation-delay:.24s}.painel-graf i:nth-child(4){animation-delay:.36s}
.painel-graf svg{position:absolute;inset:8px 10px 18px;width:calc(100% - 20px);height:calc(100% - 26px)}
.painel-graf svg path:first-child{stroke-dasharray:260;stroke-dashoffset:260;animation:traca 1.4s .5s ease-out forwards}
@keyframes cresce{from{transform:scaleY(0)}}@keyframes traca{to{stroke-dashoffset:0}}
.painel-lista{list-style:none;padding:0;margin:16px 0 6px;display:grid;gap:8px}
.painel-lista li{display:flex;align-items:center;gap:10px;font-size:.9rem;color:#E4ECF7;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:10px;padding:9px 12px}
.painel-lista em{margin-left:auto;font:500 .74rem "JetBrains Mono",monospace;font-style:normal;color:#8FD6A8}
.dot{width:8px;height:8px;border-radius:50%}.dot.ok{background:#3DDC84;box-shadow:0 0 10px #3DDC84}.dot.ouro{background:var(--ouro);box-shadow:0 0 10px var(--ouro)}
.painel figcaption{font-size:.74rem;color:#7F93B2;margin-top:8px}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.painel-graf svg path:first-child{stroke-dashoffset:0}}

/* corpo */
.corpo{padding:48px 20px 72px}
.corpo>p,.corpo section>p,.corpo li{max-width:52em}
h2{font-family:Montserrat,sans-serif;font-weight:700;font-size:clamp(1.4rem,2.6vw,1.9rem);line-height:1.25;letter-spacing:-.01em;margin:2.4em 0 .7em;color:var(--navy)}
.corpo>section:first-child h2,.corpo>h2:first-child{margin-top:.4em}
h2::after{content:"";display:block;width:44px;height:3px;border-radius:3px;background:linear-gradient(90deg,var(--ouro),var(--ouro2));margin-top:12px}
h3{font-size:1.06rem;margin:.2em 0;color:var(--navy)}
.intro{font-size:1.08rem}
.stack{list-style:none;padding:0;margin:22px 0 0;display:flex;flex-wrap:wrap;gap:8px}
.stack li{font:500 .8rem "JetBrains Mono",monospace;color:var(--navy3);background:#fff;border:1px solid var(--linha);border-radius:8px;padding:7px 11px}

.cards{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px;margin:0}
.card{position:relative;background:var(--card);border:1px solid var(--linha);border-radius:var(--raio);padding:24px;box-shadow:var(--sombra);transition:transform .2s,box-shadow .2s,border-color .2s}
.card:hover{transform:translateY(-3px);border-color:rgba(236,176,44,.6);box-shadow:0 2px 4px rgba(0,32,73,.06),0 18px 40px -10px rgba(0,32,73,.22)}
.card h2,.card h3{margin:.2em 0 .45em;font-size:1.1rem;font-family:Montserrat,sans-serif;font-weight:700}
.card h2::after{display:none}
.card a{text-decoration:none;color:var(--navy)}.card a::after{content:"";position:absolute;inset:0;border-radius:var(--raio)}
.card p{margin:0;color:var(--suave);font-size:.95rem}
.ico{display:inline-grid;place-items:center;width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,var(--navy),var(--navy3));color:var(--ouro);margin-bottom:10px;box-shadow:inset 0 0 0 1px rgba(236,176,44,.3)}
.tag{font:500 .74rem "JetBrains Mono",monospace!important;text-transform:uppercase;letter-spacing:.06em;color:var(--ouro-esc)!important;margin-bottom:8px!important}

.faixa{position:relative;background:linear-gradient(180deg,var(--navy),var(--navy2));color:#E4ECF7;border-radius:24px;padding:8px 32px 34px;margin:56px 0;overflow:hidden}
.faixa h2{color:#fff}
.faixa::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:36px 36px;pointer-events:none}
.faixa a{color:var(--ouro2)}
.pilares{display:grid;grid-template-columns:minmax(150px,230px) 1fr;gap:12px 28px;position:relative}
.pilares dt{font-weight:700;color:var(--navy)}.pilares dd{margin:0;color:var(--suave)}
.pilares-4{grid-template-columns:repeat(4,1fr);gap:16px}
.pilares-4 dt{color:var(--ouro);font:600 .8rem "JetBrains Mono",monospace;text-transform:uppercase;letter-spacing:.08em;padding-top:16px;border-top:1px solid rgba(236,176,44,.4)}
.pilares-4 dd{color:#C9D6EA;font-size:.95rem;grid-row:2}
@media(max-width:860px){.pilares-4{grid-template-columns:1fr 1fr}.pilares-4 dd{grid-row:auto}}
@media(max-width:640px){.pilares,.pilares-4{grid-template-columns:1fr}.pilares dd{margin-bottom:10px}.faixa{padding:4px 20px 26px}}

.lista-links{padding:0;list-style:none;display:grid;gap:10px}
.lista-links li{background:#fff;border:1px solid var(--linha);border-left:3px solid var(--ouro);border-radius:12px;padding:14px 18px}
.lista-links a{font-weight:600;color:var(--navy)}
.passos{counter-reset:p;list-style:none;padding:0;display:grid;gap:12px}
.passos li{counter-increment:p;position:relative;background:#fff;border:1px solid var(--linha);border-radius:14px;padding:16px 18px 16px 64px}
.passos li::before{content:counter(p,decimal-leading-zero);position:absolute;left:16px;top:15px;font:600 .9rem "JetBrains Mono",monospace;color:var(--ouro);background:var(--navy);border-radius:8px;padding:4px 7px}

.faq details{background:#fff;border:1px solid var(--linha);border-radius:14px;padding:4px 20px;margin:10px 0;transition:border-color .2s}
.faq details[open]{border-color:rgba(236,176,44,.7);box-shadow:var(--sombra)}
.faq summary{cursor:pointer;list-style:none;padding:12px 28px 12px 0;position:relative}.faq summary::-webkit-details-marker{display:none}
.faq summary h3{display:inline;font-size:1rem}
.faq summary::after{content:"+";position:absolute;right:0;top:9px;font:600 1.3rem/1 Inter;color:var(--ouro-esc)}
.faq details[open] summary::after{content:"−"}.resp p{margin-top:0;color:var(--suave)}

.resumo{background:linear-gradient(135deg,#fff,var(--gelo));border:1px solid var(--linha);border-left:4px solid var(--ouro);border-radius:14px;padding:6px 22px;margin:24px 0}
.resumo h2{font-size:.82rem;margin:1em 0 .2em;font:600 .78rem "JetBrains Mono",monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--ouro-esc)}
.resumo h2::after{display:none}
.meta{color:var(--suave);font-size:.88rem;font-family:"JetBrains Mono",monospace}
.tabela{overflow-x:auto;margin:14px 0;border-radius:14px;border:1px solid var(--linha);box-shadow:var(--sombra)}
table{border-collapse:collapse;width:100%;min-width:640px;background:#fff;font-size:.92rem}
caption{text-align:left;font-weight:600;padding:12px 14px;color:var(--suave);background:#fff}
th,td{border-top:1px solid var(--linha);padding:10px 14px;text-align:right;font-variant-numeric:tabular-nums}
thead th{background:var(--navy);color:#fff;text-align:center;font-weight:600;border:0}
tbody th{text-align:left;background:#F3F6FB;color:var(--navy)}
tbody tr:hover td{background:#FFFBF0}
.fontes{font-size:.9rem;color:var(--suave)}.fontes ul{padding-left:20px}
.relacionados ul{padding-left:20px}
.cta{position:relative;overflow:hidden;background:radial-gradient(600px 240px at 100% 0,rgba(236,176,44,.22),transparent 60%),linear-gradient(135deg,var(--navy),var(--navy3));color:#fff;border-radius:24px;padding:30px 34px;margin:56px 0 0}
.cta p{max-width:none;margin:.3em 0}.cta strong{font-family:Montserrat,sans-serif;font-size:1.25rem}
.sumario{background:#fff;border:1px solid var(--linha);border-radius:14px;padding:8px 22px}
.sumario h2{font:600 .78rem "JetBrains Mono",monospace;text-transform:uppercase;letter-spacing:.08em;margin:1em 0 .2em;color:var(--ouro-esc)}.sumario h2::after{display:none}
.form{max-width:680px;background:#fff;border:1px solid var(--linha);border-radius:20px;padding:26px 28px;box-shadow:var(--sombra)}
.form label{display:block;font-weight:600;margin-bottom:6px;color:var(--navy);font-size:.94rem}
.form input,.form select,.form textarea{width:100%;padding:12px 14px;border:1px solid #CCD6E4;border-radius:10px;font:inherit;background:#FBFCFE;transition:border-color .2s,box-shadow .2s}
.form input:focus,.form select:focus,.form textarea:focus{outline:0;border-color:var(--ouro);box-shadow:0 0 0 4px rgba(236,176,44,.2)}
.form .check{font-weight:400;color:var(--suave)}.form .check input{width:auto;margin-right:8px}.oculto{position:absolute;left:-9999px}
address{font-style:normal}
.contato{background:#fff;border:1px solid var(--linha);border-radius:18px;padding:12px 26px;box-shadow:var(--sombra);max-width:620px}

/* revelar ao rolar (só com JS) */
.js .revela{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease}
.js .revela.visivel{opacity:1;transform:none}

/* rodapé */
.rodape{background:linear-gradient(180deg,var(--navy),#00142E);color:#AFC0D8;padding:56px 0 28px;font-size:.92rem;border-top:3px solid var(--ouro)}
.rodape a{color:#E4ECF7;text-decoration:none}.rodape a:hover{color:var(--ouro)}
.rodape h2{color:#fff;font:600 .8rem "JetBrains Mono",monospace;text-transform:uppercase;letter-spacing:.08em;margin:0 0 1em}.rodape h2::after{display:none}
.rod-logo img{height:58px;width:auto}
.rod-grid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:36px}
@media(max-width:820px){.rod-grid{grid-template-columns:1fr}}
.rodape ul{list-style:none;padding:0;margin:0}.rodape li{margin:.45em 0}
.legal{margin-top:36px;padding-top:20px;border-top:1px solid rgba(255,255,255,.08);font-size:.8rem;color:#6F84A5}
.zap{position:fixed;right:18px;bottom:18px;z-index:60;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;background:#25D366;color:#fff;box-shadow:0 10px 26px -6px rgba(37,211,102,.7);transition:transform .2s}
.zap:hover{transform:scale(1.07);color:#fff}
"""

ARTIGOS_IDX = []

if __name__ == "__main__":
    build()
    print("páginas:", len(PAGES))
    for p in PAGES:
        print(p[0])
