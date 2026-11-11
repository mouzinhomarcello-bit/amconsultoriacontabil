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
GEO = (-3.0928928, -60.0455342)  # coordenadas do Google Maps
TEL1_TXT, TEL1_INTL = "(92) 99431-2735", "+5592994312735"
TEL2_TXT, TEL2_INTL = "(11) 98202-7102", "+5511982027102"
EMAIL = "contato@amconsultoriacontabil.com.br"
INSTAGRAM = "https://www.instagram.com/am.consultoria.contabil/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61587344352334"
PORTAL = "https://onvio.com.br/clientcenter/pt/auth"
GOOGLE_MAPS = "https://www.google.com/maps?cid=9222782699476468875"
GOOGLE_AVALIAR = "https://search.google.com/local/writereview?placeid=ChIJbdNKDQMRbJIRi8TpMgDo_X8"
HORARIO = "Segunda a sexta, das 8h às 18h"
# Autor: preencha nome e CRC do contador responsável para virar autor pessoa (Person) nos artigos.
AUTOR_NOME = "Marcelo da Silva Mouzinho"
AUTOR_CRC = "CRC-AM 018065/O-2"
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
    "ec132": ("Emenda Constitucional nº 132/2023 (reforma tributária) — Planalto", "https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm"),
    "ba_reforma": ("Governo da Bahia/Sefaz-BA — Reforma tributária: calendário e o que muda (set. 2026)", "https://www.ba.gov.br/comunicacao/noticias/2026-09/384149/reforma-tributaria-confira-o-calendario-e-o-que-muda-para-consumidores-e"),
    "nfeio_cgsn": ("NFE.io — Prazo do Simples Nacional para optar por IBS e CBS fora do DAS (Resolução CGSN nº 194/2026)", "https://nfe.io/blog/reforma-tributaria/novo-prazo-simples-nacional-ibs-cbs/"),
    "omie_zfm": ("Omie — Zona Franca de Manaus na reforma tributária (LC 214/2025, arts. 445 a 455)", "https://www.omie.com.br/blog/zona-franca-manaus-reforma-tributaria-impacto-industrias/"),
    "app_empregado": ("App Onvio Portal do Empregado — Thomson Reuters (App Store)", "https://apps.apple.com/br/app/id1534034198"),
    "lgpd": ("Lei nº 13.709/2018 (LGPD) — Planalto", "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm"),
    "anpd": ("Autoridade Nacional de Proteção de Dados (ANPD)", "https://www.gov.br/anpd/pt-br"),
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
        "sameAs": [INSTAGRAM, FACEBOOK, GOOGLE_MAPS],
        "hasMap": GOOGLE_MAPS,
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
        crc = f", {e(AUTOR_CRC)}" if AUTOR_CRC else ""
        return f'<a href="/sobre/#equipe" rel="author">{e(AUTOR_NOME)}</a>, contador{crc}'
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
    eyebrow = ""
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
<link rel="preload" href="/assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/source-serif-4-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v=5">
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
   Telefone: <a href="tel:{TEL1_INTL}">{TEL1_TXT}</a> ou <a href="tel:{TEL2_INTL}">{TEL2_TXT}</a><br>
   WhatsApp: <a href="https://wa.me/{TEL1_INTL[1:]}">{TEL1_TXT}</a><br>
   E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>{HORARIO}</address>
  </section>
  <nav aria-labelledby="rod-mapa"><h2 id="rod-mapa">Mapa do site</h2><ul>
   <li><a href="/servicos/">Serviços contábeis</a></li><li><a href="/contabilidade-digital-manaus/">Contabilidade digital em Manaus</a></li>
   <li><a href="/consultoria-contabil-e-fiscal-manaus/">Consultoria contábil e fiscal</a></li><li><a href="/reforma-tributaria-manaus/">Consultoria em reforma tributária</a></li>
   <li><a href="/especialidades/">Especialidades</a></li>
   <li><a href="/trocar-contador/">Como trocar de contador</a></li><li><a href="/abrir-empresa/">Abrir empresa em Manaus</a></li>
   <li><a href="/conteudos/">Artigos e estudos</a></li><li><a href="/faq/">Perguntas frequentes</a></li>
   <li><a href="/portal-do-cliente/">Portal do Cliente</a></li><li><a href="/sobre/">Sobre a A M</a></li>
   <li><a href="/contato/">Contato</a></li><li><a href="/orcamento/">Orçamento</a></li></ul></nav>
  <section aria-labelledby="rod-redes"><h2 id="rod-redes">Redes e acesso</h2><ul>
   <li><a href="{INSTAGRAM}" rel="noopener me">Instagram @am.consultoria.contabil</a></li>
   <li><a href="{FACEBOOK}" rel="noopener me">Facebook</a></li>
   <li><a href="{PORTAL}" rel="noopener">Acessar Portal do Cliente (Onvio)</a></li>
   <li><a href="{GOOGLE_MAPS}" rel="noopener">Ver no Google Maps e ler avaliações</a></li>
   <li><a href="{GOOGLE_AVALIAR}" rel="noopener">Avaliar a A M no Google</a></li></ul></section>
 </div>
 <p class="wrap legal"><a href="/politica-de-privacidade/">Política de Privacidade</a> &nbsp;|&nbsp; <a href="/politica-da-qualidade/">Política da Qualidade</a> &nbsp;|&nbsp; <a href="/lgpd/">LGPD</a><br>© {PUBLICADO[:4]} {e(NOME)} Ltda. Conteúdo informativo; não substitui análise individual do caso da sua empresa.</p>
</footer>
<a class="zap" href="https://wa.me/{TEL1_INTL[1:]}" aria-label="Falar pelo WhatsApp"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.1-1.2-.2-.2-.4-.3Z"/></svg></a>
<script>
(function(){{var d=document.documentElement;d.classList.add('js');
var b=document.querySelector('.menu-btn'),n=document.getElementById('menu-principal');
if(b&&n){{b.addEventListener('click',function(){{var o=n.classList.toggle('aberto');b.setAttribute('aria-expanded',o)}})}}
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
    return (f'<aside class="cta" aria-label="Contato"><p><strong>{e(texto)}{"" if texto[-1] in "?!." else "."}</strong> Atendimento 100% digital para Manaus e todo o Brasil.</p>'
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
        ("Departamento pessoal", "Folha, pró-labore, admissões e rescisões com eSocial, DCTFWeb e FGTS Digital. Seus empregados consultam holerite, férias, 13º e informe de rendimentos pelo aplicativo.", "/servicos/#departamento-pessoal"),
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
    cards = "".join(f'<li><h3><a href="{u}">{e(t)}</a></h3><p>{e(d)}</p></li>' for t, d, u in servicos_resumo)
    home_faq = [
        ("O que a A M Consultoria faz?", f"A {NOME} é um escritório de contabilidade em Manaus/AM (CNPJ {CNPJ}) que oferece contabilidade empresarial, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria contábil e tributária, com atendimento 100% digital pelo Portal do Cliente."),
        ("A A M atende empresas fora de Manaus?", "Sim. O atendimento e o fluxo de documentos são digitais, então a A M atende empresas de Manaus, do interior do Amazonas e de outros estados."),
        ("A A M atende MEI?", "Não. O escritório atende micro, pequenas e médias empresas enquadradas no Simples Nacional, Lucro Presumido ou Lucro Real. Quem é MEI e está perto de ultrapassar o limite pode procurar a A M para planejar a migração para ME."),
        ("Onde fica o escritório?", f"{ENDERECO['rua']}, bairro {ENDERECO['bairro']}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}. Atendimento {HORARIO.lower()}."),
    ]
    body = f"""
<section class="intro" aria-label="Apresentação"><figure class="painel-foto"><picture><source srcset="/assets/painel-am.webp" type="image/webp"><img src="/assets/painel-am.jpg" alt="Painel com o logo da A M Consultoria Contábil: barras douradas com seta para cima e as letras A M sobre fundo azul-marinho" width="680" height="380" loading="lazy"></picture></figure><div class="intro-txt"><p>A <strong>{e(NOME)}</strong> é um escritório de contabilidade em Manaus/AM que cuida da contabilidade, dos impostos e da folha de pagamento de micro, pequenas e médias empresas, com processos digitais e atendimento consultivo direto com contadores. Atendemos empresas no Simples Nacional, Lucro Presumido e Lucro Real, em Manaus e em todo o país.</p>
<p class="sistemas">Trabalhamos com os sistemas Domínio e Onvio, da Thomson Reuters, integrados ao eSocial, ao SPED, à NF-e e NFS-e, ao FGTS Digital e à DCTFWeb. Seus empregados usam o app Onvio Portal do Empregado.</p></div></section>

<section aria-labelledby="h-servicos"><h2 id="h-servicos">Serviços de contabilidade em Manaus</h2>
<ul class="razao">{cards}</ul>
<p><a href="/servicos/">Ver o escopo completo de cada serviço</a></p></section>

<section aria-labelledby="h-dif" class="faixa"><h2 id="h-dif">Como trabalhamos</h2>
<dl class="principios">
<div><dt>Tecnologia</dt><dd>Documentos, guias, balancetes e certidões ficam no <a href="/portal-do-cliente/">Portal do Cliente (Onvio, Domínio/Thomson Reuters)</a>, 24 horas. Seus empregados têm um aplicativo próprio para holerites, férias, 13º e informe de rendimentos.</dd></div>
<div><dt>Atendimento</dt><dd>Você conversa diretamente com contadores que conhecem o seu CNPJ e explicam as normas em linguagem clara.</dd></div>
<div><dt>Segurança</dt><dd>Monitoramento de certidões negativas (CNDs) e conferência preventiva de obrigações acessórias para reduzir o risco de autuação.</dd></div>
<div><dt>Estratégia</dt><dd>Balancetes, DRE e comparativos de regime tributário com leitura executiva para apoiar decisões dos sócios.</dd></div>
</dl></section>

<section aria-labelledby="h-reforma" class="destaque-reforma"><h2 id="h-reforma">Reforma tributária: sua empresa está preparada?</h2>
<p>Em janeiro de 2027 a CBS substitui o PIS e a COFINS, e o IBS passa a substituir o ICMS e o ISS até 2033. Empresas do Simples Nacional precisam decidir se recolhem IBS e CBS dentro ou fora do DAS, e a Zona Franca de Manaus tem regras próprias. A A M revisa cadastros e notas, simula a carga e orienta cada decisão.</p>
<p><a class="btn btn-ouro" href="/reforma-tributaria-manaus/">Consultoria em reforma tributária</a> <a href="/conteudos/reforma-tributaria-2027-o-que-muda-para-sua-empresa/">Entenda o que muda em 2027</a></p></section>

<section aria-labelledby="h-desafios"><h2 id="h-desafios">Qual é o desafio da sua empresa?</h2>
<ul class="lista-links">
<li><a href="/contabilidade-digital-manaus/">Quero uma contabilidade digital</a> — sistema completo, Portal do Cliente e contador dedicado.</li>
<li><a href="/consultoria-contabil-e-fiscal-manaus/">Preciso de consultoria contábil e fiscal</a> — planejamento tributário, revisão fiscal e recuperação de tributos.</li>
<li><a href="/abrir-empresa/">Estou abrindo uma empresa em Manaus</a> — CNAE, regime tributário, contrato social e licenças.</li>
<li><a href="/trocar-contador/">Quero trocar de contador</a> — como funciona a transição, passo a passo.</li>
<li><a href="/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/">Quero saber se pago imposto demais</a> — estudo comparativo Simples × Presumido 2026.</li>
<li><a href="/especialidades/">Preciso de auditoria, organização contábil ou controles</a> — veja nossas especialidades.</li>
</ul></section>

<section aria-labelledby="h-conteudo"><h2 id="h-conteudo">Conteúdos recentes</h2>
<ul class="lista-links">
<li><a href="/conteudos/reforma-tributaria-2027-o-que-muda-para-sua-empresa/">Reforma tributária: o que muda para sua empresa em 2027</a></li>
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
                 '<a class="btn btn-linha" href="/trocar-contador/">Quero trocar de contador</a></p>'
                 f'<p class="hero-meta">Escritório em Manaus, CNPJ {CNPJ}. Atendimento online para empresas de todo o Brasil.</p>')
    painel = """<figure class="balancete" aria-labelledby="bal-tit">
  <figcaption id="bal-tit"><strong>Fechamento do mês</strong><span>O que entregamos a cada cliente, todo mês</span></figcaption>
  <table>
   <thead><tr><th scope="col">Rotina</th><th scope="col">Situação</th></tr></thead>
   <tbody>
    <tr><th scope="row">Notas fiscais e extratos importados</th><td>automático</td></tr>
    <tr><th scope="row">Impostos apurados, guias no portal</th><td>conferido</td></tr>
    <tr><th scope="row">Folha, holerites e app do empregado</th><td>processado</td></tr>
    <tr><th scope="row">Certidões negativas</th><td>monitoradas</td></tr>
    <tr><th scope="row">Balancete e DRE</th><td>entregues</td></tr>
   </tbody>
   <tfoot><tr><th scope="row">Sua empresa</th><td>em dia</td></tr></tfoot>
  </table>
 </figure>"""
    page("/", f"Contabilidade e Consultoria Contábil em Manaus | A M",
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
          "Preparação para a reforma tributária: CBS, IBS, Imposto Seletivo e escolha do Simples entre DAS e regime regular"]),
        ("departamento-pessoal", "Departamento pessoal e gestão trabalhista",
         "Gestão do ciclo de vida dos colaboradores e do pró-labore dos sócios, em conformidade com eSocial, DCTFWeb e FGTS Digital, com recibos disponíveis no portal.",
         ["Folha de pagamento mensal, adiantamentos e pró-labore",
          "Admissões digitais com validação no eSocial",
          "Programação e cálculo de férias individuais e coletivas",
          "Rescisões com conferência de verbas",
          "Apuração de encargos: INSS, FGTS Digital e IRRF",
          "Aplicativo para o empregado consultar holerites, férias, 13º salário e informe de rendimentos no celular"]),
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
         f'<nav class="sumario" aria-label="Nesta página"><h2>Nesta página</h2><ol>{toc}</ol><p>Veja também: <a href="/contabilidade-digital-manaus/">contabilidade digital</a> · <a href="/consultoria-contabil-e-fiscal-manaus/">consultoria contábil e fiscal</a> · <a href="/reforma-tributaria-manaus/">consultoria em reforma tributária</a></p></nav>{secs}{faq_block(serv_faq)}{fontes_html(["ctn", "lc123", "l9718", "esocial"])}{cta()}',
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
<section aria-labelledby="h-app"><h2 id="h-app">Aplicativo para os seus empregados</h2>
<p>Além do Portal do Cliente, usado pela empresa, cada empregado tem acesso ao aplicativo <strong>Onvio Portal do Empregado</strong> (Thomson Reuters) no celular. Sem precisar pedir ao RH, ele consulta:</p>
<ul class="lista-app"><li>Holerites (recibos de pagamento) de todos os meses</li><li>Recibos e avisos de férias</li><li>Recibos do 13º salário</li><li>Informe de rendimentos para a declaração do Imposto de Renda</li></ul>
<p>Isso reduz pedidos repetidos ao departamento pessoal e dá ao empregado acesso aos próprios documentos a qualquer hora. A A M faz a liberação do acesso de cada colaborador.</p></section>
<section aria-labelledby="h-tec"><h2 id="h-tec">Tecnologia por trás do atendimento</h2>
<p>Captura automatizada de XMLs de notas fiscais e integração de extratos bancários (OFX) reduzem digitação e retrabalho, o que permite fechar a contabilidade no prazo e com mais conferência.</p></section>
<p><a class="btn btn-ouro" href="{PORTAL}" rel="noopener">Acessar o Portal do Cliente</a></p>{fontes_html(["app_empregado"])}{cta()}
"""
    page("/portal-do-cliente/", "Portal do Cliente: guias, balancetes e CNDs | A M Consultoria",
         "Portal do Cliente A M (Onvio/Domínio) com guias, balancetes e certidões, e app para o empregado ver holerite, férias, 13º e informe de rendimentos.",
         portal_body, "Portal do Cliente e app do empregado", priority="0.8",
         lead="Para a empresa, guias, relatórios e certidões 24 horas. Para os empregados, um aplicativo com holerite, férias, 13º e informe de rendimentos.")
    page("/tecnologia/", f"Contabilidade digital em Manaus | A M Consultoria",
         "Contabilidade 100% digital: integração Onvio/Domínio, captura de XMLs, extratos OFX e atendimento consultivo sem papel para empresas de Manaus e do Brasil.",
         portal_body, "Contabilidade digital, sem papel e sem retrabalho", priority="0.6",
         lead="Como a tecnologia acelera o fechamento e reduz erros.")

    # ---------- SOBRE
    autor_bloco = (f"<p>A responsabilidade técnica do escritório é do contador <strong>{e(AUTOR_NOME)}</strong>, registrado no Conselho Regional de Contabilidade do Amazonas sob o número {e(AUTOR_CRC)}. Ele escreve e revisa os artigos e orientações publicados neste site.</p>" if AUTOR_NOME else
                   f"<p>Os conteúdos do site são produzidos e revisados pela equipe técnica de contadores da A M, que atende diariamente empresas do Simples Nacional, Lucro Presumido e Lucro Real.</p>")
    body = f"""
<section aria-labelledby="h-quem"><figure class="painel-foto"><picture><source srcset="/assets/painel-am.webp" type="image/webp"><img src="/assets/painel-am.jpg" alt="Painel com o logo da A M Consultoria Contábil: barras douradas com seta para cima e as letras A M sobre fundo azul-marinho" width="680" height="380" loading="eager"></picture></figure><h2 id="h-quem">Quem somos</h2>
<p>A <strong>{e(RAZAO)}</strong> (CNPJ {CNPJ}), fundada em {data_br(FUNDACAO)}, é um escritório de contabilidade com sede em Manaus/AM. Atuamos em contabilidade, fiscal e tributário, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria, com processos digitais e atendimento próximo dos sócios.</p></section>
<section aria-labelledby="h-atuacao"><h2 id="h-atuacao">Onde atuamos</h2>
<p>Atendemos empresas em Manaus, no interior do Amazonas e em outros estados. Conhecemos as particularidades da Zona Franca de Manaus, do ICMS-AM e do ISS de Manaus, além dos regimes federais.</p></section>
<section id="equipe" aria-labelledby="h-equipe"><h2 id="h-equipe">Equipe e responsabilidade técnica</h2>{autor_bloco}</section>
<section aria-labelledby="h-dados"><h2 id="h-dados">Dados da empresa</h2>
<dl class="pilares"><dt>Razão social</dt><dd>{e(RAZAO)}</dd><dt>CNPJ</dt><dd>{CNPJ}</dd>
<dt>Endereço</dt><dd>{e(ENDERECO['rua'])}, {e(ENDERECO['bairro'])}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}</dd>
<dt>Horário</dt><dd>{HORARIO}</dd><dt>Contato</dt><dd>WhatsApp {TEL1_TXT} ou {TEL2_TXT}, e-mail {EMAIL}</dd></dl></section>
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
<p>Telefone: <a href="tel:{TEL1_INTL}">{TEL1_TXT}</a> ou <a href="tel:{TEL2_INTL}">{TEL2_TXT}</a></p>
<p>WhatsApp: <a href="https://wa.me/{TEL1_INTL[1:]}">{TEL1_TXT}</a> ou <a href="https://wa.me/{TEL2_INTL[1:]}">{TEL2_TXT}</a></p>
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
<p><label class="check"><input type="checkbox" name="lgpd" required> Concordo com o tratamento dos meus dados exclusivamente para retorno comercial da {e(NOME)} Ltda, nos termos da LGPD (Lei nº 13.709/2018) e da <a href="/politica-de-privacidade/">Política de Privacidade</a>.</label></p>
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
    _ob = os.path.join(OUT, "obrigado", "index.html")
    _t = open(_ob, encoding="utf-8").read().replace('<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">', '<meta name="robots" content="noindex, follow">')
    open(_ob, "w", encoding="utf-8").write(_t)

    # ================================================= ARTIGOS
    artigos = []

    def artigo(slug, titulo, desc, h1, corpo, fontes, faq=None, leitura=5, secao="Gestão empresarial",
               published=PUBLICADO, modified=ATUALIZADO, extra=None, resumo=""):
        path = f"/conteudos/{slug}/"
        meta = (f'<p class="meta">Por {autor_html()}. Publicado em <time datetime="{published}">{data_br(published)}</time>'
                f', atualizado em <time datetime="{modified}">{data_br(modified)}</time>. Leitura de {leitura} minutos.</p>')
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
<p><a href="dados.json">Baixar os dados da simulação (JSON)</a>. Licença CC BY 4.0: cite "A M Consultoria Contábil, 2026".</p></section>
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
        ("reforma-tributaria-2027-o-que-muda-para-sua-empresa", "Reforma tributária: o que muda para sua empresa em 2027"),
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

    # --- REFORMA TRIBUTÁRIA
    corpo = """
<section aria-labelledby="h-crono"><h2 id="h-crono">Cronograma da reforma tributária</h2>
<div class="tabela"><table><caption>Principais etapas da transição (EC 132/2023 e LC 214/2025)</caption>
<thead><tr><th scope="col">Quando</th><th scope="col">O que acontece</th></tr></thead><tbody>
<tr><th scope="row">2026</th><td style="text-align:left">Ano de teste: CBS de 0,9% e IBS de 0,1% destacados nas notas fiscais das empresas do regime regular, sem recolhimento efetivo para quem cumpre as obrigações acessórias. Novos campos de IBS e CBS na NF-e e na NFS-e.</td></tr>
<tr><th scope="row">Janeiro de 2027</th><td style="text-align:left">A CBS substitui integralmente o PIS e a COFINS. O IPI passa a ter alíquota zero para a maior parte dos produtos e continua apenas para itens que também são fabricados na Zona Franca de Manaus. Começa o Imposto Seletivo sobre produtos prejudiciais à saúde e ao meio ambiente. Empresas do Simples passam a informar IBS e CBS nas notas.</td></tr>
<tr><th scope="row">2027 e 2028</th><td style="text-align:left">O IBS segue com alíquota simbólica de teste.</td></tr>
<tr><th scope="row">2029 a 2032</th><td style="text-align:left">O ICMS e o ISS são reduzidos gradualmente e substituídos pelo IBS.</td></tr>
<tr><th scope="row">2033</th><td style="text-align:left">Fim do ICMS e do ISS. Sistema novo em vigor de forma completa.</td></tr>
</tbody></table></div></section>
<section aria-labelledby="h-simples"><h2 id="h-simples">Empresas do Simples Nacional</h2>
<p>O Simples Nacional continua existindo. A partir de 2027, a empresa optante pode escolher entre duas formas de recolher IBS e CBS:</p>
<ul><li><strong>Dentro do DAS</strong>, como hoje: mais simples, mas os clientes que são empresas do regime regular aproveitam menos crédito na compra.</li>
<li><strong>Fora do DAS, pelo regime regular</strong>: IBS e CBS apurados à parte, com crédito integral para o cliente. Pode valer a pena para quem vende principalmente para outras empresas.</li></ul>
<p>Para o primeiro semestre de 2027, o prazo de opção foi prorrogado até 30 de outubro de 2026 pela Resolução CGSN nº 194/2026, e há uma janela de desistência no fim de 2026. A escolha depende de quem são os seus clientes e da sua margem, por isso precisa de simulação antes.</p></section>
<section aria-labelledby="h-regular"><h2 id="h-regular">Empresas do Lucro Presumido e do Lucro Real</h2>
<ul><li><strong>Crédito amplo:</strong> IBS e CBS são não cumulativos, com crédito sobre praticamente tudo o que a empresa compra para a atividade, desde que o imposto tenha sido pago pelo fornecedor.</li>
<li><strong>Preço e contratos:</strong> como o imposto é cobrado "por fora", é preciso revisar formação de preço e cláusulas de reajuste dos contratos longos.</li>
<li><strong>Fornecedores:</strong> comprar de quem está no Simples gera menos crédito, o que muda a escolha de fornecedores.</li>
<li><strong>Sistemas e notas:</strong> cadastros de produtos (NCM, CST e classificação tributária) precisam estar corretos para destacar IBS e CBS.</li></ul></section>
<section aria-labelledby="h-zfm"><h2 id="h-zfm">Zona Franca de Manaus</h2>
<p>A Constituição manteve o tratamento diferenciado da Zona Franca de Manaus. A LC 214/2025 prevê, entre outros pontos:</p>
<ul><li>alíquota zero de IBS e CBS na entrada de insumos vindos de outras regiões para a indústria incentivada, com crédito presumido de IBS;</li>
<li>crédito presumido de CBS para a indústria da ZFM a partir de 2027;</li>
<li>manutenção do IPI fora da ZFM para produtos que também são fabricados no polo, preservando a vantagem competitiva de quem produz em Manaus.</li></ul>
<p>Os percentuais variam conforme o tipo de bem e a origem dos insumos, e há discussões judiciais em andamento. Cada empresa precisa de análise individual.</p></section>
<section aria-labelledby="h-checklist"><h2 id="h-checklist">Checklist para se preparar</h2>
<ol class="passos">
<li>Revisar o cadastro de produtos e serviços (NCM, NBS, CST e classificação tributária).</li>
<li>Confirmar que o sistema emissor de notas já destaca IBS e CBS.</li>
<li>Simular a carga de 2027 e a escolha entre DAS e regime regular, se a empresa for do Simples.</li>
<li>Revisar preços e contratos de longo prazo.</li>
<li>Mapear fornecedores pelo regime tributário e pelo crédito que geram.</li>
<li>Acompanhar o fluxo de caixa: o recolhimento passa a ser feito, aos poucos, no momento do pagamento (split payment).</li>
</ol>
<p>A A M faz esse trabalho com você: conheça a <a href="/reforma-tributaria-manaus/">consultoria em reforma tributária</a>.</p></section>
"""
    reforma_faq = [
        ("Quando o PIS e a COFINS deixam de existir?", "Em janeiro de 2027, quando a CBS passa a substituir integralmente os dois tributos."),
        ("O Simples Nacional acaba com a reforma tributária?", "Não. O Simples continua. A partir de 2027 a empresa optante pode escolher recolher IBS e CBS dentro do DAS ou fora dele, pelo regime regular."),
        ("A Zona Franca de Manaus perde os incentivos?", "Não. A Emenda Constitucional 132/2023 manteve o tratamento diferenciado da ZFM, e a LC 214/2025 criou mecanismos próprios, como alíquota zero e créditos presumidos de IBS e CBS e a manutenção do IPI fora da ZFM para produtos fabricados no polo."),
    ]
    artigo("reforma-tributaria-2027-o-que-muda-para-sua-empresa", "Reforma tributária: o que muda em 2027 para sua empresa | A M",
           "CBS no lugar de PIS e COFINS em 2027, IBS até 2033, opções do Simples Nacional e regras da Zona Franca de Manaus: cronograma e checklist da reforma.",
           "Reforma tributária: o que muda para sua empresa em 2027", corpo,
           ["ec132", "lc214", "ba_reforma", "nfeio_cgsn", "omie_zfm"], faq=reforma_faq, leitura=7, secao="Reforma tributária", published="2026-11-09", modified="2026-11-09",
           resumo="Em 2027 a CBS substitui o PIS e a COFINS e o IPI é zerado para a maioria dos produtos, exceto os que concorrem com a Zona Franca de Manaus. O IBS substitui o ICMS e o ISS aos poucos, de 2029 a 2032, e o sistema novo vale por completo em 2033. Empresas do Simples podem escolher recolher IBS e CBS dentro ou fora do DAS.")

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

    # ================================================= PÁGINAS DE PALAVRA-CHAVE (captação)
    def servico_schema(nome, desc, path):
        return {"@type": "Service", "name": nome, "description": desc, "provider": {"@id": ORG_ID},
                "areaServed": [{"@type": "City", "name": "Manaus"}, {"@type": "State", "name": "Amazonas"}, {"@type": "Country", "name": "Brasil"}],
                "url": SITE + path, "serviceType": nome}

    # --- CONTABILIDADE DIGITAL EM MANAUS
    cd_faq = [
        ("O que é contabilidade digital?", "É a contabilidade feita com processos online: notas fiscais e extratos chegam por integração, guias e relatórios ficam num portal na internet e o atendimento acontece por WhatsApp, e-mail e videochamada. Na A M, isso vem junto com contadores que acompanham a sua empresa de perto."),
        ("Contabilidade digital é mais barata?", "Costuma ser mais eficiente, porque elimina papel, malote e retrabalho. O valor depende do regime tributário, do volume de notas e do número de empregados. A A M envia a proposta depois de um diagnóstico inicial gratuito."),
        ("Contabilidade digital atende empresa de Manaus com particularidades da Zona Franca?", "Sim. A A M é de Manaus e acompanha ICMS-AM, incentivos da Zona Franca e ISS do município, com a praticidade da contabilidade digital."),
        ("Vou falar com um robô ou com um contador?", "Com um contador. A tecnologia cuida da parte repetitiva; as dúvidas, as reuniões e as decisões são tratadas com a equipe técnica da A M."),
    ]
    body = f"""
<p>Contabilidade digital não é só trocar o papel pelo computador. Na A M, é a soma de <strong>tecnologia de ponta</strong> com <strong>atendimento próximo</strong>: sistemas que automatizam a rotina e contadores de Manaus que conhecem a sua empresa pelo nome.</p>
<section aria-labelledby="h-cd-como"><h2 id="h-cd-como">Como funciona a contabilidade digital da A M</h2>
<ol class="passos">
<li><strong>Documentos automáticos:</strong> notas fiscais (XML) e extratos bancários (OFX) chegam por integração, sem você precisar enviar nada todo mês.</li>
<li><strong>Portal do Cliente 24 horas:</strong> guias, balancetes, DRE, certidões e contratos ficam no <a href="/portal-do-cliente/">Portal do Cliente Onvio (Domínio/Thomson Reuters)</a>, com alerta de vencimento.</li>
<li><strong>App para os empregados:</strong> holerite, férias, 13º e informe de rendimentos no celular de cada colaborador.</li>
<li><strong>Atendimento humano:</strong> WhatsApp, e-mail e videochamada com contadores, e reuniões para explicar os números.</li>
<li><strong>Relatórios para decidir:</strong> balancete e DRE mensais com leitura executiva, não só guias para pagar.</li>
</ol></section>
<section aria-labelledby="h-cd-dif" class="faixa"><h2 id="h-cd-dif">Digital, mas perto de você</h2>
<dl class="principios">
<div><dt>Sistema completo</dt><dd>Domínio e Onvio, da Thomson Reuters, integrados ao eSocial, SPED, NF-e e FGTS Digital.</dd></div>
<div><dt>Contador dedicado</dt><dd>Você sabe quem cuida do seu CNPJ e fala direto com essa pessoa.</dd></div>
<div><dt>Conhecimento local</dt><dd>Escritório em Manaus, com domínio de ICMS-AM, Zona Franca e ISS de Manaus.</dd></div>
<div><dt>Todo o Brasil</dt><dd>Como tudo é online, atendemos empresas de qualquer estado.</dd></div>
</dl></section>
<section aria-labelledby="h-cd-para"><h2 id="h-cd-para">Para quem é</h2>
<ul class="lista-links">
<li>Empresas de serviços, comércio e indústria no <strong>Simples Nacional, Lucro Presumido ou Lucro Real</strong>.</li>
<li>Quem quer <a href="/trocar-contador/">trocar de contador</a> e ter mais clareza sobre os impostos.</li>
<li>Quem vai <a href="/abrir-empresa/">abrir empresa em Manaus</a> e quer começar organizado.</li>
<li>Empresas que querem terceirizar o financeiro com <a href="/servicos/#bpo-financeiro">BPO financeiro</a>.</li>
</ul></section>
{faq_block(cd_faq, "Perguntas sobre contabilidade digital", "faq-cd")}
{cta("Quer uma contabilidade digital com contador de verdade?")}
"""
    page("/contabilidade-digital-manaus/", "Contabilidade Digital em Manaus | A M Consultoria Contábil",
         "Contabilidade digital em Manaus com sistema Onvio/Domínio, Portal do Cliente 24h, app para empregados e contador dedicado. Atendemos todo o Brasil.",
         body, "Contabilidade digital em Manaus, com contador de verdade ao seu lado",
         extra_schema=[servico_schema("Contabilidade digital", "Contabilidade online com integração de documentos, Portal do Cliente e atendimento por contador dedicado.", "/contabilidade-digital-manaus/"), faq_schema(cd_faq)],
         priority="0.95", lead="Tecnologia que automatiza a rotina e atendimento próximo de contadores que conhecem o seu negócio.")

    # --- CONSULTORIA CONTÁBIL E FISCAL
    cf_faq = [
        ("Qual a diferença entre contabilidade e consultoria contábil?", "A contabilidade cuida das obrigações: escrituração, impostos e declarações. A consultoria usa esses números para orientar decisões, como escolher o regime tributário, reduzir impostos de forma legal, organizar o caixa e preparar a empresa para crescer."),
        ("O que faz uma consultoria fiscal?", "Revisa a apuração de impostos federais, estaduais e municipais, a classificação dos produtos e serviços nas notas, as retenções e as obrigações acessórias, para evitar multas e identificar tributos pagos a mais."),
        ("Preciso ser cliente da contabilidade para contratar a consultoria?", "Não. A consultoria pode ser contratada por projeto, por exemplo, uma revisão tributária ou um estudo de regime, mesmo que a sua contabilidade seja feita por outro escritório."),
        ("A consultoria pode reduzir meus impostos?", "Muitas vezes, sim, de forma legal: escolhendo o regime certo, aproveitando créditos, segregando receitas corretamente e recuperando valores pagos a mais nos últimos 5 anos. O resultado depende de cada caso e é apresentado com cálculos antes de qualquer mudança."),
    ]
    body = f"""
<p>A consultoria contábil e fiscal da A M transforma a contabilidade em ferramenta de decisão. Analisamos os números da sua empresa, encontramos riscos e oportunidades e explicamos tudo em linguagem clara, <strong>com reunião e relatório</strong>.</p>
<section aria-labelledby="h-cf-o-que"><h2 id="h-cf-o-que">O que entregamos</h2>
<ul class="cards">
<li class="card"><h3>Planejamento tributário</h3><p>Comparação entre Simples Nacional, Lucro Presumido e Lucro Real com os números reais da empresa. Veja nosso <a href="/conteudos/simples-nacional-ou-lucro-presumido-estudo-manaus-2026/">estudo Simples × Presumido 2026</a>.</p></li>
<li class="card"><h3>Revisão fiscal</h3><p>Conferência de NCM, CFOP, CST, retenções, substituição tributária e ICMS-AM, para evitar autuação e pagamento a mais.</p></li>
<li class="card"><h3>Recuperação de tributos</h3><p>Identificação de PIS e COFINS pagos a mais nos últimos 5 anos e recuperação por compensação ou restituição. <a href="/servicos/#recuperacao-pis-cofins">Saiba mais</a>.</p></li>
<li class="card"><h3>Reforma tributária</h3><p>Simulação de impacto da CBS e do IBS e escolha do Simples entre DAS e regime regular. <a href="/reforma-tributaria-manaus/">Consultoria em reforma tributária</a>.</p></li>
<li class="card"><h3>Consultoria financeira</h3><p>Fluxo de caixa, capital de giro, ponto de equilíbrio, precificação e separação entre pessoa física e jurídica.</p></li>
<li class="card"><h3>Auditoria</h3><p>Exame de demonstrações e apurações para validar números entre sócios ou antes de uma venda ou investimento. <a href="/servicos/#auditoria">Ver escopo</a>.</p></li>
</ul></section>
<section aria-labelledby="h-cf-como"><h2 id="h-cf-como">Como funciona</h2>
<ol class="passos">
<li><strong>Diagnóstico:</strong> conversa inicial e levantamento de documentos (declarações, notas e apurações).</li>
<li><strong>Análise técnica:</strong> cálculos e cruzamentos feitos pela equipe de contadores.</li>
<li><strong>Relatório e reunião:</strong> resultados, riscos e recomendações explicados aos sócios.</li>
<li><strong>Implantação:</strong> ajustes em cadastros, regime ou rotinas, com acompanhamento.</li>
</ol></section>
{faq_block(cf_faq, "Perguntas sobre consultoria contábil e fiscal", "faq-cf")}
{fontes_html(["lc123", "ctn", "lc214"])}
{cta("Quer uma análise contábil e fiscal da sua empresa?")}
"""
    page("/consultoria-contabil-e-fiscal-manaus/", "Consultoria Contábil e Fiscal em Manaus | A M Consultoria",
         "Consultoria contábil e fiscal em Manaus: planejamento tributário, revisão fiscal, recuperação de PIS e COFINS, reforma tributária e consultoria financeira.",
         body, "Consultoria contábil e fiscal em Manaus",
         extra_schema=[servico_schema("Consultoria contábil e fiscal", "Planejamento tributário, revisão fiscal, recuperação de tributos e consultoria financeira para empresas.", "/consultoria-contabil-e-fiscal-manaus/"), faq_schema(cf_faq)],
         priority="0.95", lead="Números que viram decisões: planejamento tributário, revisão fiscal e recuperação de tributos com relatório e reunião.")

    # --- CONSULTORIA EM REFORMA TRIBUTÁRIA
    rt_faq = [
        ("Por que contratar uma consultoria em reforma tributária agora?", "Porque as primeiras mudanças com efeito no caixa começam em janeiro de 2027, quando a CBS substitui o PIS e a COFINS. Cadastros, notas fiscais, preços e contratos precisam estar ajustados antes disso."),
        ("Minha empresa é do Simples. A reforma me afeta?", "Sim. O Simples continua, mas a empresa pode escolher recolher IBS e CBS dentro ou fora do DAS, e essa escolha muda o crédito que os seus clientes aproveitam. Também passa a ser obrigatório informar IBS e CBS nas notas."),
        ("A consultoria atende empresas da Zona Franca de Manaus?", "Sim. A A M analisa os mecanismos próprios da ZFM na LC 214/2025, como alíquota zero e créditos presumidos de IBS e CBS e a manutenção do IPI fora da ZFM para produtos fabricados no polo."),
    ]
    body = f"""
<p>A reforma tributária muda a forma como todas as empresas calculam e pagam impostos. A A M prepara a sua empresa <strong>antes</strong> que as mudanças cheguem ao caixa, com diagnóstico, simulação de impacto e ajustes práticos.</p>
<section aria-labelledby="h-rt-o-que"><h2 id="h-rt-o-que">O que a consultoria inclui</h2>
<ol class="passos">
<li><strong>Diagnóstico:</strong> regime atual, perfil de clientes e fornecedores, produtos e serviços vendidos.</li>
<li><strong>Revisão de cadastros:</strong> NCM, NBS, CST e classificação tributária para destacar IBS e CBS corretamente nas notas.</li>
<li><strong>Simulação de impacto:</strong> carga tributária e fluxo de caixa de 2027 em diante, incluindo o split payment.</li>
<li><strong>Decisão do Simples:</strong> estudo para recolher IBS e CBS dentro ou fora do DAS.</li>
<li><strong>Preços e contratos:</strong> revisão de formação de preço e cláusulas de reajuste.</li>
<li><strong>Zona Franca de Manaus:</strong> análise de créditos presumidos e do tratamento do IPI para quem opera no polo.</li>
</ol></section>
<section aria-labelledby="h-rt-datas"><h2 id="h-rt-datas">Datas que importam</h2>
<ul class="lista-links">
<li><strong>2026:</strong> teste com CBS de 0,9% e IBS de 0,1% nas notas, sem recolhimento efetivo.</li>
<li><strong>Janeiro de 2027:</strong> a CBS substitui o PIS e a COFINS e começa o Imposto Seletivo.</li>
<li><strong>2029 a 2032:</strong> o IBS substitui gradualmente o ICMS e o ISS.</li>
<li><strong>2033:</strong> sistema novo em vigor de forma completa.</li>
</ul>
<p>Detalhes no artigo <a href="/conteudos/reforma-tributaria-2027-o-que-muda-para-sua-empresa/">Reforma tributária: o que muda para sua empresa em 2027</a>.</p></section>
{faq_block(rt_faq, "Perguntas sobre a consultoria em reforma tributária", "faq-rt")}
{fontes_html(["ec132", "lc214", "ba_reforma", "omie_zfm"])}
{cta("Prepare sua empresa para a reforma tributária")}
"""
    page("/reforma-tributaria-manaus/", "Consultoria em Reforma Tributária em Manaus | A M Consultoria",
         "Consultoria em reforma tributária em Manaus: diagnóstico, revisão de cadastros, simulação de CBS e IBS, decisão do Simples e regras da Zona Franca.",
         body, "Consultoria em reforma tributária para empresas de Manaus",
         extra_schema=[servico_schema("Consultoria em reforma tributária", "Diagnóstico, simulação de impacto de CBS e IBS e adequação de cadastros, preços e contratos.", "/reforma-tributaria-manaus/"), faq_schema(rt_faq)],
         priority="0.95", lead="Diagnóstico, simulação de impacto e ajustes práticos antes de a CBS e o IBS chegarem ao seu caixa.")

    # ================================================= PÁGINAS INSTITUCIONAIS (privacidade, qualidade, LGPD)
    VIGENCIA = "2026-11-11"
    vig = f'<p class="meta">Vigente desde <time datetime="{VIGENCIA}">{data_br(VIGENCIA)}</time>. Responsável: {e(RAZAO)}, CNPJ {CNPJ}.</p>'

    body = vig + f"""
<section aria-labelledby="pp-1"><h2 id="pp-1">Quem é o controlador dos dados</h2>
<p>O controlador dos dados pessoais tratados neste site é a {e(RAZAO)}, inscrita no CNPJ {CNPJ}, com sede na {e(ENDERECO['rua'])}, {e(ENDERECO['bairro'])}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}.</p>
<p><strong>Encarregado pelo tratamento de dados (DPO):</strong> {e(AUTOR_NOME)}, pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></section>
<section aria-labelledby="pp-2"><h2 id="pp-2">Quais dados coletamos</h2>
<ul>
<li><strong>Formulário de orçamento:</strong> nome, nome da empresa, CNPJ, WhatsApp, e-mail, cidade, regime tributário, serviço desejado e a mensagem que você escrever.</li>
<li><strong>Contato por WhatsApp, e-mail ou telefone:</strong> os dados que você enviar na conversa.</li>
<li><strong>Dados técnicos de acesso:</strong> endereço IP, data e hora, navegador e páginas acessadas, registrados automaticamente pelo provedor de hospedagem para segurança e funcionamento do site.</li>
</ul>
<p>Não coletamos dados sensíveis pelo site e não vendemos dados pessoais.</p></section>
<section aria-labelledby="pp-3"><h2 id="pp-3">Para que usamos e com qual base legal</h2>
<div class="tabela"><table><caption>Finalidades e bases legais (art. 7º da Lei 13.709/2018)</caption>
<thead><tr><th scope="col">Finalidade</th><th scope="col" style="text-align:left">Base legal</th></tr></thead><tbody>
<tr><th scope="row">Responder ao pedido de orçamento e enviar proposta</th><td style="text-align:left">Consentimento e procedimentos preliminares a um contrato (art. 7º, I e V)</td></tr>
<tr><th scope="row">Prestar os serviços contratados</th><td style="text-align:left">Execução de contrato e cumprimento de obrigação legal ou regulatória (art. 7º, V e II)</td></tr>
<tr><th scope="row">Segurança do site e prevenção de fraudes</th><td style="text-align:left">Legítimo interesse (art. 7º, IX)</td></tr>
<tr><th scope="row">Atender a órgãos públicos e ordens judiciais</th><td style="text-align:left">Cumprimento de obrigação legal e exercício regular de direitos (art. 7º, II e VI)</td></tr>
</tbody></table></div></section>
<section aria-labelledby="pp-4"><h2 id="pp-4">Com quem compartilhamos</h2>
<ul>
<li><strong>Hospedagem do site (Netlify, Inc.):</strong> armazena as páginas e recebe os dados do formulário. Os servidores podem ficar fora do Brasil; essa transferência internacional segue o art. 33 da LGPD.</li>
<li><strong>Sistemas contábeis (Domínio e Onvio, da Thomson Reuters):</strong> usados para prestar os serviços aos clientes.</li>
<li><strong>Órgãos públicos:</strong> Receita Federal, SEFAZ-AM, Prefeitura de Manaus, eSocial e outros, quando a lei exige para cumprir as obrigações dos clientes.</li>
</ul></section>
<section aria-labelledby="pp-5"><h2 id="pp-5">Por quanto tempo guardamos</h2>
<p>Dados de quem pediu orçamento e não contratou: até 12 meses, ou antes se você pedir a exclusão. Dados de clientes: pelo tempo do contrato e pelos prazos legais de guarda de documentos contábeis, fiscais e trabalhistas. Registros técnicos de acesso: pelo prazo do Marco Civil da Internet (6 meses).</p></section>
<section aria-labelledby="pp-6"><h2 id="pp-6">Cookies</h2>
<p>Este site não usa cookies de publicidade nem ferramentas de rastreamento. As fontes e imagens são servidas pelo próprio site. Ao clicar em links externos (WhatsApp, Instagram, Facebook, Google Maps, Portal do Cliente), você passa a seguir a política de privacidade desses serviços.</p></section>
<section aria-labelledby="pp-7"><h2 id="pp-7">Seus direitos</h2>
<p>Conforme o art. 18 da LGPD, você pode pedir a qualquer momento: confirmação de que tratamos seus dados, acesso, correção, anonimização, bloqueio ou eliminação de dados desnecessários, portabilidade, informação sobre compartilhamento e revogação do consentimento. Envie o pedido para <a href="mailto:{EMAIL}">{EMAIL}</a>; respondemos em até 15 dias. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p></section>
<section aria-labelledby="pp-8"><h2 id="pp-8">Alterações</h2>
<p>Esta política pode ser atualizada. A data de vigência no topo da página sempre mostra a versão em vigor.</p></section>
{fontes_html(["lgpd", "anpd"])}
"""
    page("/politica-de-privacidade/", f"Política de Privacidade | {NOME}",
         "Como a A M Consultoria Contábil coleta, usa, compartilha e protege dados pessoais no site e nos serviços, e como exercer seus direitos pela LGPD.",
         body, "Política de Privacidade", priority="0.3", freq="yearly", published=VIGENCIA, modified=VIGENCIA,
         lead="Como tratamos os dados pessoais de quem visita o site, pede orçamento ou é nosso cliente.")

    body = vig + f"""
<p>A {e(NOME)} tem como propósito entregar contabilidade correta, no prazo e explicada com clareza, para que cada cliente tome decisões com segurança. Para isso, assume os compromissos abaixo.</p>
<section aria-labelledby="pq-1"><h2 id="pq-1">Nossos compromissos</h2>
<dl class="pilares">
<dt>Exatidão técnica</dt><dd>Seguir as Normas Brasileiras de Contabilidade e a legislação tributária, trabalhista e societária, com conferência das apurações antes da entrega.</dd>
<dt>Cumprimento de prazos</dt><dd>Entregar guias, declarações e obrigações acessórias dentro dos prazos legais, com antecedência suficiente para o cliente se organizar.</dd>
<dt>Comunicação clara</dt><dd>Explicar números, impostos e mudanças legais em linguagem simples e responder às dúvidas com agilidade.</dd>
<dt>Sigilo e ética</dt><dd>Guardar sigilo sobre as informações dos clientes, conforme o Código de Ética Profissional do Contador (NBC PG 01), e tratar dados pessoais conforme a LGPD.</dd>
<dt>Tecnologia e segurança</dt><dd>Usar sistemas confiáveis e integrados, com acesso controlado a documentos pelo Portal do Cliente.</dd>
<dt>Atualização constante</dt><dd>Manter a equipe atualizada sobre mudanças na legislação, como a reforma tributária, por meio de educação profissional continuada.</dd>
<dt>Melhoria contínua</dt><dd>Ouvir os clientes, registrar sugestões e reclamações e revisar processos para evitar que falhas se repitam.</dd>
</dl></section>
<section aria-labelledby="pq-2"><h2 id="pq-2">Como acompanhamos</h2>
<p>Revisamos periodicamente o cumprimento de prazos, a ocorrência de retrabalho e a satisfação dos clientes. Sugestões e reclamações podem ser enviadas para <a href="mailto:{EMAIL}">{EMAIL}</a> ou pelo WhatsApp e são respondidas pelo responsável técnico.</p></section>
{fontes_html(["cfc"])}
{cta()}
"""
    page("/politica-da-qualidade/", f"Política da Qualidade | {NOME}",
         "Compromissos da A M Consultoria Contábil com exatidão técnica, prazos, comunicação clara, sigilo, segurança da informação e melhoria contínua.",
         body, "Política da Qualidade", priority="0.3", freq="yearly", published=VIGENCIA, modified=VIGENCIA,
         lead="Os compromissos que orientam o trabalho da A M com cada cliente.")

    lgpd_faq = [
        ("O escritório de contabilidade precisa seguir a LGPD?", "Sim. O escritório trata dados pessoais de sócios, empregados e clientes das empresas que atende, como CPF, endereço, salário e dados de dependentes, e por isso deve seguir a Lei 13.709/2018."),
        ("A A M é controladora ou operadora dos dados dos meus empregados?", "Em regra, a sua empresa é a controladora dos dados dos empregados, e a A M atua como operadora, tratando esses dados por conta da sua empresa para processar folha, eSocial e obrigações trabalhistas. Para os dados coletados no próprio site, a A M é a controladora."),
        ("Como peço acesso ou exclusão dos meus dados?", f"Envie um e-mail para {EMAIL} informando o pedido. Respondemos em até 15 dias. Dados que a lei obriga a guardar, como documentos fiscais e trabalhistas, são mantidos pelo prazo legal."),
    ]
    body = vig + f"""
<p>A Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018) define regras para coletar, usar, guardar e compartilhar dados de pessoas. Por lidar diariamente com dados de sócios, empregados e clientes, a contabilidade é uma das atividades em que a LGPD mais pesa. Veja como a A M cumpre a lei.</p>
<section aria-labelledby="lg-1"><h2 id="lg-1">Nosso papel</h2>
<ul>
<li><strong>Como controladora:</strong> dados de quem visita o site, pede orçamento ou fala com a A M. Detalhes na <a href="/politica-de-privacidade/">Política de Privacidade</a>.</li>
<li><strong>Como operadora:</strong> dados de sócios, empregados e terceiros que os clientes nos entregam para contabilidade, folha de pagamento e obrigações fiscais. Tratamos esses dados apenas para executar os serviços contratados e conforme as instruções do cliente.</li>
</ul></section>
<section aria-labelledby="lg-2"><h2 id="lg-2">Princípios que seguimos</h2>
<ul>
<li><strong>Finalidade e necessidade:</strong> pedimos só os dados necessários para cada serviço.</li>
<li><strong>Segurança:</strong> documentos trocados pelo Portal do Cliente, com login individual, em vez de e-mails e papéis soltos; site com conexão segura (HTTPS).</li>
<li><strong>Sigilo profissional:</strong> além da LGPD, o contador tem dever de sigilo pelo Código de Ética Profissional (NBC PG 01).</li>
<li><strong>Transparência:</strong> informamos com quem os dados são compartilhados, como órgãos públicos e sistemas contábeis.</li>
<li><strong>Guarda pelo prazo legal:</strong> documentos contábeis, fiscais e trabalhistas são mantidos pelos prazos exigidos em lei.</li>
</ul></section>
<section aria-labelledby="lg-3"><h2 id="lg-3">Encarregado e canal do titular</h2>
<p>Encarregado pelo tratamento de dados: <strong>{e(AUTOR_NOME)}</strong>. Pedidos de acesso, correção, exclusão ou informações sobre seus dados: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></section>
{faq_block(lgpd_faq, "Perguntas sobre LGPD", "faq-lgpd")}
{fontes_html(["lgpd", "anpd", "cfc"])}
"""
    page("/lgpd/", f"LGPD: como protegemos seus dados | {NOME}",
         "Como a A M Consultoria Contábil aplica a LGPD: papel de controladora e operadora, princípios, segurança, sigilo profissional e canal do titular de dados.",
         body, "LGPD: como protegemos os seus dados", extra_schema=[faq_schema(lgpd_faq)],
         priority="0.4", freq="yearly", published=VIGENCIA, modified=VIGENCIA,
         lead="Contabilidade lida com dados de pessoas todos os dias. Veja como cuidamos deles.")

    # ---------- ÍNDICE CONTEÚDOS
    lis = "".join(f'<li class="card"><p class="tag">{e(s)}, leitura de {l} min</p><h2><a href="{p}">{e(t)}</a></h2><p>{e(d)}</p></li>' for p, t, d, s, l in artigos)
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
        ("Meus empregados conseguem ver o holerite pelo celular?", "Sim. Clientes da A M com folha de pagamento dão aos empregados acesso ao aplicativo Onvio Portal do Empregado, onde eles consultam holerites, recibos de férias, 13º salário e o informe de rendimentos para o Imposto de Renda."),
        ("O que muda com a reforma tributária em 2027?", "A CBS substitui o PIS e a COFINS, o IPI é zerado para a maioria dos produtos (exceto os que concorrem com a Zona Franca de Manaus) e começa o Imposto Seletivo. O IBS substitui o ICMS e o ISS gradualmente até 2033. Veja o <a href=\"/conteudos/reforma-tributaria-2027-o-que-muda-para-sua-empresa/\">guia completo</a>."),
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
- Google Maps e avaliações: {GOOGLE_MAPS}
- Responsável técnico: {AUTOR_NOME}, contador, {AUTOR_CRC}

## Páginas principais
- [Contabilidade digital em Manaus]({SITE}/contabilidade-digital-manaus/): sistema Onvio/Domínio, Portal do Cliente, app do empregado e contador dedicado
- [Consultoria contábil e fiscal em Manaus]({SITE}/consultoria-contabil-e-fiscal-manaus/): planejamento tributário, revisão fiscal, recuperação de tributos
- [Consultoria em reforma tributária]({SITE}/reforma-tributaria-manaus/): diagnóstico, simulação de CBS/IBS, Simples e Zona Franca
- [Serviços]({SITE}/servicos/): escopo de contabilidade, fiscal, departamento pessoal, BPO financeiro, recuperação de créditos de PIS e COFINS, consultoria e auditoria
- [Trocar de contador]({SITE}/trocar-contador/): passo a passo da transição
- [Abrir empresa em Manaus]({SITE}/abrir-empresa/): etapas, JUCEA, inscrições e regime tributário
- [Perguntas frequentes]({SITE}/faq/): 20 respostas diretas
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
https://amconsultoriacontabil.netlify.app/*  https://amconsultoriacontabil.com.br/:splat  301!
"""
    open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8").write(redirects)
    open(os.path.join(OUT, "_headers"), "w", encoding="utf-8").write(
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n\n"
        "/assets/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n\n"
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
    for fn in ["logo-am.png", "logo-am.webp", "og-image.jpg", "icon-512.png", "painel-am.jpg", "painel-am.webp"]:
        _sh.copy(os.path.join(brand, fn), os.path.join(OUT, "assets", fn))
    os.makedirs(os.path.join(OUT, "assets", "fonts"), exist_ok=True)
    for fn in os.listdir(os.path.join(brand, "fonts")):
        _sh.copy(os.path.join(brand, "fonts", fn), os.path.join(OUT, "assets", "fonts", fn))
    for fn in ["apple-touch-icon.png", "favicon-48.png"]:
        _sh.copy(os.path.join(brand, fn), os.path.join(OUT, fn))


CSS = """
@font-face{font-family:Archivo;src:url(/assets/fonts/archivo-latin-wdth-normal.woff2) format("woff2-variations"),url(/assets/fonts/archivo-latin-wdth-normal.woff2) format("woff2");font-weight:100 900;font-stretch:62% 125%;font-style:normal;font-display:swap}
@font-face{font-family:"Source Serif 4";src:url(/assets/fonts/source-serif-4-latin-opsz-normal.woff2) format("woff2");font-weight:200 900;font-style:normal;font-display:swap}
@font-face{font-family:"Source Serif 4";src:url(/assets/fonts/source-serif-4-latin-opsz-italic.woff2) format("woff2");font-weight:200 900;font-style:italic;font-display:swap}
/* A M Consultoria Contábil. Conceito: livro-razão. Tokens: */
:root{
 --navy:#002049;      /* marca */
 --tinta:#00122B;     /* fundo profundo, rodapé */
 --ouro:#ECB02C;      /* marca: totais, ação */
 --papel:#FFFFFF;
 --gelo:#F3F6FA;      /* fundo da página */
 --pauta:#D5DEEA;     /* linhas do razão */
 --texto:#13243D;
 --suave:#55667F;
 --link:#1B5498;
 --serif:"Source Serif 4",Georgia,"Times New Roman",serif;
 --sans:Archivo,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--gelo);color:var(--texto);font:400 1.0625rem/1.68 var(--serif);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{max-width:100%;height:auto}
a{color:var(--link);text-decoration-thickness:1px;text-underline-offset:.18em}a:hover{color:var(--navy);text-decoration-thickness:2px}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.pular{position:absolute;left:-9999px}.pular:focus{left:16px;top:16px;background:#fff;padding:8px 12px;z-index:99;font-family:var(--sans)}
:focus-visible{outline:3px solid var(--ouro);outline-offset:3px}
h1,h2,h3,.btn,.menu,.breadcrumb,.meta,caption,th,summary,label,.tag,.legal,figcaption,.hero-meta{font-family:var(--sans)}

/* topo */
.topo{background:var(--navy);position:sticky;top:0;z-index:50;border-bottom:1px solid rgba(255,255,255,.08)}
.topo-in{display:flex;align-items:center;gap:28px;min-height:74px}
.marca{display:flex;flex-shrink:0}.marca img{height:44px;width:auto;display:block}
#menu-principal{flex:1;display:flex;justify-content:flex-end}
.menu{display:flex;flex-wrap:wrap;gap:0 2px;list-style:none;margin:0;padding:0}
.menu a{display:block;text-decoration:none;color:#C7D3E6;font-size:.92rem;font-weight:500;padding:10px 10px}
.menu a:hover{color:#fff}
.menu a[aria-current]{color:#fff;box-shadow:inset 0 -2px 0 var(--ouro)}
.menu-btn{display:none;margin-left:auto;background:none;color:#fff;border:1px solid rgba(255,255,255,.35);border-radius:6px;padding:8px 14px;font:600 .92rem var(--sans);cursor:pointer}
@media(max-width:1060px){
 .menu-btn{display:block}.topo .topo-cta{display:none}
 .topo-in{flex-wrap:wrap;padding:10px 24px;gap:12px}
 #menu-principal{flex-basis:100%;justify-content:flex-start}.js #menu-principal{display:none}.js #menu-principal.aberto{display:block}
 .menu{flex-direction:column;padding:4px 0 14px}.menu a{padding:12px 0;border-top:1px solid rgba(255,255,255,.08)}
}

/* botões: uma ação principal (ouro), uma secundária (contorno) */
.btn{display:inline-block;text-decoration:none;font-weight:600;font-size:.98rem;line-height:1;padding:16px 22px;border-radius:6px;border:0;cursor:pointer;margin:4px 10px 4px 0;font-stretch:105%}
.btn-sm{padding:12px 16px;font-size:.9rem;margin:0}
.btn-ouro{background:var(--ouro);color:var(--navy)}
.btn-ouro:hover{background:#F4C04A;color:var(--navy);text-decoration:none}
.btn-linha{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.5)}
.btn-linha:hover{color:#fff;box-shadow:inset 0 0 0 1.5px #fff;text-decoration:none}

/* hero */
.hero{background:var(--navy);color:#fff;padding:44px 0 56px}
.hero-in{display:grid;grid-template-columns:1fr;gap:48px;align-items:center}
.hero h1{font-weight:750;font-stretch:112%;font-size:clamp(2rem,4.4vw,3.1rem);line-height:1.06;letter-spacing:-.015em;margin:.15em 0 .4em;max-width:17em;text-wrap:balance}
.hero .lead{font-family:var(--serif);font-size:1.2rem;line-height:1.55;color:#D2DCEB;max-width:34em;margin:0}
.hero-home{padding:72px 0 88px}
.hero-home .hero-in{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:64px}
.hero-home h1{font-size:clamp(2.05rem,4.6vw,3.5rem);font-stretch:112%}
.hero-ctas{margin:32px 0 0}
.hero-meta{font-size:.86rem;color:#9FB1CC;margin:18px 0 0}
.breadcrumb ol{list-style:none;display:flex;flex-wrap:wrap;gap:6px;padding:0;margin:0 0 12px;font-size:.86rem;color:#9FB1CC}
.breadcrumb a{color:#D2DCEB;text-decoration:none}.breadcrumb a:hover{color:#fff;text-decoration:underline}
.breadcrumb li+li::before{content:"/";margin-right:6px;color:#6D84A6}
@media(max-width:920px){.hero-home .hero-in{grid-template-columns:1fr;gap:40px}.hero-home{padding:48px 0 60px}}
@media(max-width:560px){.hero-ctas .btn{display:block;text-align:center;margin:0 0 10px}.marca img{height:38px}.wrap{padding:0 18px}}

/* o elemento-assinatura: balancete em papel com traço duplo no total */
.balancete{margin:0;background:var(--papel);color:var(--texto);border-radius:3px;padding:26px 28px 30px;box-shadow:0 30px 60px -28px rgba(0,0,0,.55)}
.balancete figcaption{display:flex;flex-direction:column;gap:2px;margin-bottom:14px}
.balancete figcaption strong{font-size:1.15rem;font-weight:700;font-stretch:110%;color:var(--navy)}
.balancete figcaption span{font-size:.86rem;color:var(--suave)}
.balancete table{width:100%;min-width:0;border-collapse:collapse;font-family:var(--sans);font-size:.95rem}
.balancete thead th{font-size:.78rem;font-weight:600;color:var(--suave);text-align:left;padding:0 0 8px;border-bottom:1.5px solid var(--navy)}
.balancete thead th:last-child,.balancete td{text-align:right}
.balancete tbody th{text-align:left;font-weight:500;color:var(--texto);padding:11px 12px 11px 0;border-bottom:1px solid var(--pauta)}
.balancete tbody td{padding:11px 0;border-bottom:1px solid var(--pauta);color:var(--navy);font-weight:600;font-style:italic;font-family:var(--serif)}
.balancete tfoot th,.balancete tfoot td{padding:14px 0 10px;font-size:1.08rem;font-weight:750;color:var(--navy);text-align:left}
.balancete tfoot td{text-align:right;font-family:var(--sans);font-style:normal}
.balancete tfoot tr{background:linear-gradient(var(--ouro),var(--ouro)) left bottom/100% 2.5px no-repeat,linear-gradient(var(--ouro),var(--ouro)) left calc(100% - 6px)/100% 2.5px no-repeat}
.balancete tbody tr{animation:lancar .5s cubic-bezier(.2,.7,.2,1) both}
.balancete tbody tr:nth-child(2){animation-delay:.12s}.balancete tbody tr:nth-child(3){animation-delay:.24s}.balancete tbody tr:nth-child(4){animation-delay:.36s}.balancete tbody tr:nth-child(5){animation-delay:.48s}
.balancete tfoot tr{animation:fechar .7s .75s cubic-bezier(.2,.7,.2,1) both}
@keyframes lancar{from{opacity:0;transform:translateX(-8px)}}
@keyframes fechar{from{background-size:0 2.5px,0 2.5px}}
@media(prefers-reduced-motion:reduce){.balancete tbody tr,.balancete tfoot tr{animation:none}}

/* corpo */
.corpo{padding:56px 24px 80px}
.corpo>p,.corpo section>p,.corpo li,.corpo dd{max-width:42rem}
h2{font-weight:700;font-stretch:108%;font-size:clamp(1.5rem,2.6vw,2rem);line-height:1.18;letter-spacing:-.01em;color:var(--navy);margin:2.6em 0 .7em;text-wrap:balance}
.corpo>section:first-child>h2:first-child{margin-top:.2em}
h3{font-weight:650;font-size:1.12rem;line-height:1.3;color:var(--navy);margin:0 0 .3em}
.intro p{font-size:1.2rem;line-height:1.6;max-width:40rem}
.intro{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:24px 48px;align-items:center}
.intro .intro-txt{order:1}.intro .painel-foto{order:2}
.painel-foto{margin:0}.painel-foto img{display:block;width:100%;max-width:560px;height:auto;border-radius:4px;box-shadow:0 24px 50px -28px rgba(0,32,73,.55)}
section[aria-labelledby="h-quem"]>h2{margin-top:.2em}
section[aria-labelledby="h-quem"] .painel-foto{float:right;width:min(46%,460px);margin:6px 0 16px 32px}
@media(max-width:820px){.intro{grid-template-columns:1fr}.intro .painel-foto{order:0}section[aria-labelledby="h-quem"] .painel-foto{float:none;width:100%;margin:0 0 20px}}
.sistemas{color:var(--suave);font-size:1rem;border-left:3px solid var(--ouro);padding-left:16px}

/* serviços como linhas de um razão */
.razao{list-style:none;padding:0;margin:0;border-top:1.5px solid var(--navy)}
.razao li{display:grid;grid-template-columns:minmax(220px,.9fr) 1.6fr;gap:8px 40px;padding:20px 0;border-bottom:1px solid var(--pauta);max-width:none}
.razao h3{margin:0;font-size:1.15rem}.razao h3 a{color:var(--navy);text-decoration:none}.razao h3 a:hover{text-decoration:underline}
.razao p{margin:0;color:var(--suave)}
@media(max-width:720px){.razao li{grid-template-columns:1fr}}

/* grades de itens (especialidades, artigos, entregas): sem sombras, com régua no topo */
.cards{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:0 32px}
.card{padding:20px 0 26px;border-top:1.5px solid var(--navy);max-width:none}
.card h2,.card h3{margin:0 0 .4em;font-size:1.15rem;font-weight:650;font-stretch:104%}
.card h2{text-wrap:pretty}
.card a{color:var(--navy);text-decoration:none}.card a:hover{text-decoration:underline}
.card p{margin:0;color:var(--suave);font-size:1rem}
.card p a{color:var(--link);text-decoration:underline}
.tag{font-size:.84rem!important;color:var(--suave)!important;margin:0 0 6px!important}

/* faixa escura: princípios */
.faixa{background:var(--navy);color:#D2DCEB;margin:64px 0;padding:8px 40px 40px;border-radius:4px}
.faixa h2{color:#fff}
.faixa a{color:#fff}
.principios{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px 48px;margin:0}
.principios dt{font:650 1.1rem var(--sans);color:#fff;padding-top:14px;border-top:2px solid var(--ouro)}
.principios dd{margin:6px 0 0;color:#C7D3E6}
.pilares{display:grid;grid-template-columns:minmax(150px,230px) 1fr;gap:12px 32px;margin:0}
.pilares dt{font:650 1rem var(--sans);color:var(--navy)}.pilares dd{margin:0;color:var(--suave)}
.pilares-4{grid-template-columns:repeat(2,minmax(0,1fr))}
.faixa .pilares-4 dt{color:#fff;padding-top:14px;border-top:2px solid var(--ouro)}.faixa .pilares-4 dd{color:#C7D3E6}
@media(max-width:720px){.principios,.pilares,.pilares-4{grid-template-columns:1fr}.pilares dd{margin-bottom:10px}.faixa{padding:4px 22px 30px}}

/* listas */
.lista-links{list-style:none;padding:0;margin:0;border-top:1px solid var(--pauta)}
.lista-links li{padding:14px 0;border-bottom:1px solid var(--pauta);max-width:none}
.lista-links a{font-family:var(--sans);font-weight:600;color:var(--navy)}
.passos{counter-reset:p;list-style:none;padding:0;margin:0}
.passos li{counter-increment:p;position:relative;padding:14px 0 14px 56px;border-bottom:1px solid var(--pauta)}
.passos li:first-child{border-top:1px solid var(--pauta)}
.passos li::before{content:counter(p);position:absolute;left:0;top:10px;font:700 1.6rem/1 var(--sans);font-stretch:115%;color:var(--ouro)}
.lista-app{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:0 28px;border-top:1.5px solid var(--navy)}
.lista-app li{padding:14px 0;border-bottom:1px solid var(--pauta);font-family:var(--sans);font-weight:500;color:var(--navy)}

/* destaque: reforma tributária */
.destaque-reforma{background:var(--papel);border-left:4px solid var(--ouro);padding:4px 36px 30px;margin:64px 0}
.destaque-reforma h2{margin-top:1em}

/* perguntas */
.faq details{border-bottom:1px solid var(--pauta)}
.faq details:first-of-type{border-top:1.5px solid var(--navy)}
.faq summary{cursor:pointer;list-style:none;padding:16px 36px 16px 0;position:relative}.faq summary::-webkit-details-marker{display:none}
.faq summary h3{display:inline;font-size:1.05rem;font-weight:600}
.faq summary::after{content:"+";position:absolute;right:4px;top:12px;font:400 1.5rem/1 var(--sans);color:var(--navy);transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg)}
.resp p{margin:0 0 18px;color:var(--suave)}

/* artigos */
.meta{color:var(--suave);font-size:.9rem}
.resumo{background:var(--papel);border-left:4px solid var(--ouro);padding:4px 26px 8px;margin:26px 0 8px}
.resumo h2{font-size:1.05rem;margin:1em 0 .2em}
.tabela{overflow-x:auto;margin:16px 0;background:var(--papel)}
table{border-collapse:collapse;width:100%;min-width:620px;font-size:.95rem}
.tabela table{font-family:var(--sans)}
caption{text-align:left;font-weight:600;padding:12px 0;color:var(--suave);background:var(--gelo)}
th,td{padding:11px 14px;text-align:right;border-bottom:1px solid var(--pauta);font-variant-numeric:tabular-nums}
thead th{color:var(--navy);text-align:right;font-weight:650;border-bottom:1.5px solid var(--navy);background:var(--papel)}
thead th:first-child,tbody th{text-align:left}
tbody th{font-weight:600;color:var(--navy)}
.fontes{font-size:.95rem;color:var(--suave)}.fontes ul,.relacionados ul{padding-left:20px}
.sumario{border-top:1.5px solid var(--navy);border-bottom:1px solid var(--pauta);padding:4px 0 14px}
.sumario h2{font-size:1rem;margin:.9em 0 .3em}

/* chamada final */
.cta{background:var(--navy);color:#fff;padding:34px 40px;margin:72px 0 0;border-radius:4px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px 32px}
.cta p{margin:0;max-width:none}.cta strong{font-family:var(--sans);font-stretch:110%;font-size:1.35rem;display:block;margin-bottom:4px}
.cta p:last-child{flex-shrink:1}
.cta .btn{margin:4px 0 4px 10px}
@media(max-width:640px){.cta{display:block;padding:26px 22px}.cta p:last-child{margin-top:14px}.cta .btn{margin:6px 10px 0 0}}

/* formulários e contato */
.form{max-width:640px;background:var(--papel);padding:28px 30px;border-top:3px solid var(--navy)}
.form label{display:block;font-weight:600;margin-bottom:6px;color:var(--navy);font-size:.95rem}
.form input,.form select,.form textarea{width:100%;padding:12px 14px;border:1px solid #BCC9DA;border-radius:4px;font:1rem var(--sans);background:#fff;color:var(--texto)}
.form input:focus,.form select:focus,.form textarea:focus{outline:0;border-color:var(--navy);box-shadow:0 0 0 3px rgba(236,176,44,.45)}
.form .check{font-weight:400;color:var(--suave);font-family:var(--serif)}.form .check input{width:auto;margin-right:8px}
.oculto{position:absolute;left:-9999px}
address{font-style:normal}
.contato{background:var(--papel);border-top:3px solid var(--navy);padding:14px 28px;max-width:600px}

/* rodapé */
.rodape{background:var(--tinta);color:#A9B8CE;padding:60px 0 28px;font:400 .95rem/1.7 var(--sans)}
.rodape a{color:#E3EAF4;text-decoration:none}.rodape a:hover{color:#fff;text-decoration:underline}
.rodape h2{color:#fff;font-size:1rem;font-weight:650;margin:0 0 .9em}
.rod-logo{margin:0 0 14px!important}.rod-logo img{height:56px;width:auto}
.rod-grid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:40px}
@media(max-width:820px){.rod-grid{grid-template-columns:1fr}}
.rodape ul{list-style:none;padding:0;margin:0}.rodape li{margin:.35em 0}
.legal{margin-top:40px;padding-top:20px;border-top:1px solid rgba(255,255,255,.1);font-size:.82rem;color:#7488A6}
.zap{position:fixed;right:18px;bottom:18px;z-index:60;width:54px;height:54px;border-radius:50%;display:grid;place-items:center;background:#1FA855;color:#fff;box-shadow:0 8px 20px -6px rgba(0,0,0,.4)}
.zap:hover{color:#fff;background:#1B9A4D}
"""

ARTIGOS_IDX = []

if __name__ == "__main__":
    build()
    print("páginas:", len(PAGES))
    for p in PAGES:
        print(p[0])
