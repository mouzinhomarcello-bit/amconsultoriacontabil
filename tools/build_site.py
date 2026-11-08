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
EMAIL = "contabilamconsultoria1@gmail.com"
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

NAV = [("/", "Início"), ("/servicos/", "Serviços"), ("/especialidades/", "Especialidades"),
       ("/trocar-contador/", "Trocar de contador"), ("/abrir-empresa/", "Abrir empresa"),
       ("/conteudos/", "Conteúdos"), ("/faq/", "Perguntas frequentes"), ("/sobre/", "Sobre"),
       ("/contato/", "Contato")]

PAGES = []  # (path, priority, changefreq)


def org_schema():
    return {
        "@type": ["AccountingService", "ProfessionalService"],
        "@id": ORG_ID,
        "name": NOME,
        "legalName": RAZAO,
        "alternateName": ["A M Consultoria", "AM Consultoria Contábil", "A M Consultoria Contábil"],
        "url": SITE + "/",
        "logo": SITE + "/favicon.svg",
        "image": SITE + "/favicon.svg",
        "taxID": CNPJ,
        "foundingDate": FUNDACAO,
        "description": "Escritório de contabilidade em Manaus/AM: contabilidade empresarial, fiscal e tributário, departamento pessoal, consultoria e auditoria contábil e tributária, com atendimento 100% digital para empresas de Manaus e de todo o Brasil.",
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
                       "Departamento pessoal", "eSocial", "Auditoria contábil", "Auditoria tributária",
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
         priority="0.8", freq="monthly", lead="", published=PUBLICADO, modified=ATUALIZADO, og_type="website"):
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
    doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{e(NOME)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="google-site-verification" content="qJIGMOABqli3Hxg60j7vU32LTNrX4E3hWsRZ2ecHOqI">
<meta name="msvalidate.01" content="993206048267B258A0408725297B07B2">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate" type="text/plain" href="/llms.txt" title="Resumo do site para IA">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo">
 <div class="wrap topo-in">
  <a class="marca" href="/" aria-label="{e(NOME)} — página inicial"><span class="sigla">A M</span><span>Consultoria Contábil</span></a>
  <nav aria-label="Menu principal"><ul class="menu">{nav}</ul></nav>
  <a class="btn btn-sm" href="/orcamento/">Solicitar orçamento</a>
 </div>
</header>
<main id="conteudo">
<div class="wrap">
{bc_html}
<article class="pagina">
<header class="cab"><h1>{e(h1)}</h1>{lead_html}</header>
{body}
</article>
</div>
</main>
<footer class="rodape">
 <div class="wrap rod-grid">
  <section aria-labelledby="rod-empresa">
   <h2 id="rod-empresa">{e(NOME)}</h2>
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
  <section aria-labelledby="rod-redes"><h2 id="rod-redes">Redes</h2><ul>
   <li><a href="{INSTAGRAM}" rel="noopener me">Instagram @am.consultoria.contabil</a></li>
   <li><a href="{FACEBOOK}" rel="noopener me">Facebook</a></li>
   <li><a href="{PORTAL}" rel="noopener">Acessar Portal do Cliente (Onvio)</a></li></ul></section>
 </div>
 <p class="wrap legal">© {PUBLICADO[:4]} {e(NOME)} Ltda. Conteúdo informativo; não substitui análise individual do caso da sua empresa.</p>
</footer>
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
            f'<p><a class="btn" href="/orcamento/">Solicitar orçamento</a> <a class="btn btn-sec" href="https://wa.me/{TEL1_INTL[1:]}">Falar pelo WhatsApp</a></p></aside>')


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
        ("Auditoria contábil e tributária", "Exame de demonstrações, revisão preventiva de apurações dos últimos 5 anos e cruzamento SPED × NF-e × bancos.", "/servicos/#auditoria"),
    ]
    cards = "".join(f'<li class="card"><h3><a href="{u}">{e(t)}</a></h3><p>{e(d)}</p></li>' for t, d, u in servicos_resumo)
    home_faq = [
        ("O que a A M Consultoria faz?", f"A {NOME} é um escritório de contabilidade em Manaus/AM (CNPJ {CNPJ}) que oferece contabilidade empresarial, fiscal e tributário, departamento pessoal, consultoria e auditoria contábil e tributária, com atendimento 100% digital pelo Portal do Cliente."),
        ("A A M atende empresas fora de Manaus?", "Sim. O atendimento e o fluxo de documentos são digitais, então a A M atende empresas de Manaus, do interior do Amazonas e de outros estados."),
        ("A A M atende MEI?", "Não. O escritório atende micro, pequenas e médias empresas enquadradas no Simples Nacional, Lucro Presumido ou Lucro Real. Quem é MEI e está perto de ultrapassar o limite pode procurar a A M para planejar a migração para ME."),
        ("Onde fica o escritório?", f"{ENDERECO['rua']}, bairro {ENDERECO['bairro']}, {ENDERECO['cidade']}/{ENDERECO['uf']}, CEP {ENDERECO['cep']}. Atendimento {HORARIO.lower()}."),
    ]
    body = f"""
<p class="selos"><span>Contabilidade digital</span><span>Manaus/AM e todo o Brasil</span><span>CNPJ {CNPJ}</span></p>
<p>A <strong>{e(NOME)}</strong> é um escritório de contabilidade em Manaus/AM que cuida da contabilidade, dos impostos e da folha de pagamento de micro, pequenas e médias empresas, com processos digitais e atendimento consultivo direto com contadores. Atendemos empresas no Simples Nacional, Lucro Presumido e Lucro Real, em Manaus e em todo o país.</p>
<p><a class="btn" href="/orcamento/">Solicitar orçamento</a> <a class="btn btn-sec" href="/trocar-contador/">Quero trocar de contador</a> <a class="btn btn-sec" href="/abrir-empresa/">Quero abrir minha empresa</a></p>

<section aria-labelledby="h-servicos"><h2 id="h-servicos">Serviços de contabilidade em Manaus</h2>
<ul class="cards">{cards}</ul>
<p><a href="/servicos/">Ver o escopo completo de cada serviço</a></p></section>

<section aria-labelledby="h-dif"><h2 id="h-dif">Como trabalhamos</h2>
<dl class="pilares">
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
    page("/", f"Contabilidade em Manaus/AM | A M Consultoria Contábil",
         "Escritório de contabilidade em Manaus/AM: contabilidade, impostos, folha, consultoria e auditoria para o Simples, Presumido e Real. Atendimento 100% digital.",
         body, "Escritório de contabilidade em Manaus para empresas que querem crescer",
         extra_schema=[faq_schema(home_faq)], priority="1.0", freq="weekly",
         lead="Contabilidade, impostos e folha de pagamento com tecnologia, organização e atendimento consultivo.")

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
        ("A A M trabalha com empresas da Zona Franca de Manaus?", "Sim. Acompanhamos apuração de ICMS-AM e as particularidades fiscais de empresas instaladas na Zona Franca de Manaus, além do ISS do município."),
    ]
    page("/servicos/", f"Serviços de contabilidade em Manaus | A M Consultoria",
         "Contabilidade empresarial, fiscal e tributário, departamento pessoal, consultoria e auditoria em Manaus/AM. Veja o escopo de cada serviço e peça orçamento.",
         f'<nav class="sumario" aria-label="Nesta página"><h2>Nesta página</h2><ol>{toc}</ol></nav>{secs}{faq_block(serv_faq)}{cta()}',
         "Serviços de contabilidade para empresas em Manaus e no Brasil",
         extra_schema=[serv_schema, faq_schema(serv_faq)], priority="0.9", freq="monthly",
         lead="Cinco áreas integradas em um único parceiro contábil.")

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
<p><a class="btn" href="{PORTAL}" rel="noopener">Acessar o Portal do Cliente</a></p>{cta()}
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
<p>A <strong>{e(RAZAO)}</strong> (CNPJ {CNPJ}), fundada em {data_br(FUNDACAO)}, é um escritório de contabilidade com sede em Manaus/AM. Atuamos em contabilidade, fiscal e tributário, departamento pessoal, consultoria e auditoria, com processos digitais e atendimento próximo dos sócios.</p></section>
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
    opts_srv = "".join(f"<option>{x}</option>" for x in ["Contabilidade mensal", "Fiscal e tributário", "Departamento pessoal", "Consultoria contábil/financeira", "Auditoria contábil e tributária", "Troca de contador", "Abertura de empresa", "Outro"])
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
<p><button class="btn" type="submit">Solicitar proposta</button></p>
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
        ("O que faz a A M Consultoria e Auditoria Contábil?", f"É um escritório de contabilidade em Manaus/AM (CNPJ {CNPJ}) que presta serviços de contabilidade empresarial, fiscal e tributário, departamento pessoal, consultoria e auditoria contábil e tributária, com atendimento digital para empresas de todo o Brasil."),
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
        ("A A M atende empresas da Zona Franca de Manaus?", "Sim. Acompanhamos ICMS-AM, incentivos e obrigações próprias de empresas instaladas na Zona Franca de Manaus."),
        ("O que é o Portal do Cliente?", "É a plataforma Onvio (Domínio/Thomson Reuters) onde o cliente acessa guias, balancetes, DRE, certidões, folha e documentos 24 horas por dia."),
        ("Preciso ir ao escritório?", f"Não. Todo o atendimento pode ser digital. Se preferir, o escritório fica na {ENDERECO['rua']}, {ENDERECO['bairro']}, Manaus/AM, {HORARIO.lower()}."),
        ("Que documentos preciso para pedir orçamento?", "CNPJ (se a empresa já existir), regime tributário atual, faturamento médio mensal, número de funcionários e quantidade aproximada de notas fiscais emitidas e recebidas por mês."),
    ]
    page("/faq/", "Perguntas frequentes sobre contabilidade | A M Consultoria",
         "Respostas sobre honorários, troca de contador, abertura de empresa, Simples × Presumido, Fator R, dividendos em 2026, IBS/CBS e atendimento da A M em Manaus.",
         faq_block(faq_geral, "Perguntas e respostas", "faq-geral") + fontes_html(["lc123", "l15270", "lc224", "lc214", "cfc", "jucea"]) + cta("Não encontrou sua dúvida?"),
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

> Escritório de contabilidade em Manaus/AM (Brasil), {RAZAO}, CNPJ {CNPJ}, fundado em {FUNDACAO}. Presta contabilidade empresarial, fiscal e tributário, departamento pessoal, consultoria e auditoria contábil e tributária para micro, pequenas e médias empresas no Simples Nacional, Lucro Presumido e Lucro Real, com atendimento 100% digital em Manaus e em todo o Brasil. Não atende MEI.

- Endereço: {ENDERECO['rua']}, {ENDERECO['bairro']}, Manaus/AM, CEP {ENDERECO['cep']}
- WhatsApp: {TEL1_TXT} e {TEL2_TXT} · E-mail: {EMAIL}
- Horário: {HORARIO}
- Instagram: {INSTAGRAM}

## Páginas principais
- [Serviços]({SITE}/servicos/): escopo de contabilidade, fiscal, departamento pessoal, consultoria e auditoria
- [Trocar de contador]({SITE}/trocar-contador/): passo a passo da transição
- [Abrir empresa em Manaus]({SITE}/abrir-empresa/): etapas, JUCEA, inscrições e regime tributário
- [Perguntas frequentes]({SITE}/faq/): 16 respostas diretas
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
    key = secrets.token_hex(16)
    open(os.path.join(OUT, f"{key}.txt"), "w").write(key)
    open(os.path.join(OUT, "..", "indexnow-key.txt"), "w").write(key)

    # ---------- favicon + css
    open(os.path.join(OUT, "favicon.svg"), "w").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#081B33"/>'
        '<text x="32" y="41" font-family="Arial,Helvetica,sans-serif" font-size="24" font-weight="700" fill="#fff" text-anchor="middle">AM</text></svg>')
    open(os.path.join(OUT, "assets/site.css"), "w").write(CSS)


CSS = """
:root{--tinta:#081B33;--azul:#1769AA;--azul2:#0F4F82;--fundo:#F8FAFC;--card:#fff;--linha:#E2E8F0;--suave:#475569;--destaque:#E8F1F9}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--fundo);color:var(--tinta);font:16px/1.65 "Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--azul)}a:hover{color:var(--azul2)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.pular{position:absolute;left:-9999px}.pular:focus{left:16px;top:16px;background:#fff;padding:8px;z-index:9}
.topo{background:#fff;border-bottom:1px solid var(--linha);position:sticky;top:0;z-index:5}
.topo-in{display:flex;align-items:center;gap:20px;min-height:68px;flex-wrap:wrap}
.marca{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--tinta);font-weight:700}
.sigla{background:var(--tinta);color:#fff;font-family:Syne,sans-serif;padding:6px 9px;border-radius:8px;letter-spacing:.04em}
.menu{display:flex;flex-wrap:wrap;gap:4px 16px;list-style:none;margin:0;padding:0;flex:1}
.menu a{text-decoration:none;color:var(--suave);font-size:.92rem;font-weight:500}
.menu a[aria-current]{color:var(--tinta);font-weight:700}
.btn{display:inline-block;background:var(--azul);color:#fff;text-decoration:none;font-weight:600;padding:12px 20px;border-radius:10px;border:0;cursor:pointer;font:inherit;font-weight:600;margin:4px 6px 4px 0}
.btn:hover{background:var(--azul2);color:#fff}.btn-sm{padding:9px 14px;font-size:.9rem}
.btn-sec{background:transparent;color:var(--azul);box-shadow:inset 0 0 0 2px var(--azul)}.btn-sec:hover{background:var(--destaque);color:var(--azul2)}
main{padding:24px 0 56px}
.breadcrumb ol{list-style:none;display:flex;flex-wrap:wrap;gap:6px;padding:0;margin:0 0 18px;font-size:.88rem;color:var(--suave)}
.breadcrumb li+li::before{content:"›";margin-right:6px}
.cab h1{font-family:Syne,sans-serif;font-size:clamp(1.9rem,4.4vw,3rem);line-height:1.12;margin:.2em 0 .3em;letter-spacing:-.01em}
.lead{font-size:1.15rem;color:var(--suave);max-width:46em}
h2{font-family:Syne,sans-serif;font-size:1.55rem;line-height:1.25;margin:2.2em 0 .6em}
h3{font-size:1.08rem;margin:.2em 0}
.pagina>p,.pagina section>p,.pagina li{max-width:48em}
.selos{display:flex;flex-wrap:wrap;gap:8px}.selos span{background:var(--destaque);color:var(--azul2);border-radius:99px;padding:4px 12px;font-size:.85rem;font-weight:600}
.cards{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--linha);border-radius:14px;padding:20px}
.card h2,.card h3{margin:.1em 0 .4em;font-size:1.12rem;font-family:"Plus Jakarta Sans",sans-serif}
.card a{text-decoration:none}.card p{margin:0;color:var(--suave)}.tag{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px!important}
.pilares{display:grid;grid-template-columns:minmax(140px,220px) 1fr;gap:10px 24px}.pilares dt{font-weight:700}.pilares dd{margin:0;color:var(--suave)}
@media(max-width:640px){.pilares{grid-template-columns:1fr}.pilares dd{margin-bottom:10px}}
.lista-links li{margin:.4em 0}
.passos li{margin:.6em 0}
.faq details{background:#fff;border:1px solid var(--linha);border-radius:12px;padding:4px 18px;margin:10px 0}
.faq summary{cursor:pointer;list-style:none;padding:10px 0}.faq summary::-webkit-details-marker{display:none}
.faq summary h3{display:inline;font-size:1.02rem}.faq summary::after{content:"+";float:right;font-weight:700;color:var(--azul)}
.faq details[open] summary::after{content:"–"}.resp p{margin-top:0;color:var(--suave)}
.resumo{background:var(--destaque);border-left:4px solid var(--azul);border-radius:10px;padding:4px 20px;margin:20px 0}
.resumo h2{font-size:1.05rem;margin:.8em 0 .2em;font-family:"Plus Jakarta Sans",sans-serif}
.meta{color:var(--suave);font-size:.9rem}
.tabela{overflow-x:auto;margin:12px 0}table{border-collapse:collapse;width:100%;min-width:620px;background:#fff;font-size:.93rem}
caption{text-align:left;font-weight:600;padding:8px 0;color:var(--suave)}th,td{border:1px solid var(--linha);padding:9px 12px;text-align:right}
thead th{background:var(--tinta);color:#fff;text-align:center}tbody th{text-align:left;background:#F1F5F9}
.fontes{font-size:.92rem}.fontes ul{padding-left:20px}
.cta{background:var(--tinta);color:#fff;border-radius:16px;padding:22px 26px;margin:40px 0 0}.cta .btn-sec{color:#fff;box-shadow:inset 0 0 0 2px #fff}.cta .btn-sec:hover{background:rgba(255,255,255,.1)}
.sumario{background:#fff;border:1px solid var(--linha);border-radius:12px;padding:6px 20px}.sumario h2{font-size:1rem;margin:.8em 0 .2em;font-family:"Plus Jakarta Sans",sans-serif}
.form{max-width:640px}.form label{display:block;font-weight:600;margin-bottom:4px}
.form input,.form select,.form textarea{width:100%;padding:11px 12px;border:1px solid #CBD5E1;border-radius:10px;font:inherit;background:#fff}
.form .check{font-weight:400}.form .check input{width:auto;margin-right:8px}.oculto{position:absolute;left:-9999px}
address{font-style:normal}
.rodape{background:var(--tinta);color:#CBD5E1;padding:40px 0 24px;font-size:.93rem}
.rodape a{color:#fff}.rodape h2{color:#fff;font-size:1.05rem;margin:0 0 .6em;font-family:"Plus Jakarta Sans",sans-serif}
.rod-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:28px}.rodape ul{list-style:none;padding:0;margin:0}.rodape li{margin:.3em 0}
.legal{margin-top:28px;font-size:.82rem;color:#94A3B8}
"""

ARTIGOS_IDX = []

if __name__ == "__main__":
    build()
    print("páginas:", len(PAGES))
    for p in PAGES:
        print(p[0])
