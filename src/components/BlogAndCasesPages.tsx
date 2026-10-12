import React, { useState } from 'react';
import {
  Search,
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  MessageSquare,
  ShieldCheck
} from 'lucide-react';
import {
  BlogPost,
  BLOG_CATEGORIES,
  CASE_STUDIES,
  PageId,
  SiteConfig
} from '../data/siteData';

interface BlogPageProps {
  posts: BlogPost[];
  onNavigate: (page: PageId) => void;
  onOpenWhatsApp: (customMsg?: string) => void;
  onTrackArticleRead: (title: string) => void;
}

export const BlogInteligenciaPage: React.FC<BlogPageProps> = ({
  posts,
  onNavigate,
  onOpenWhatsApp,
  onTrackArticleRead
}) => {
  const [selectedCategory, setSelectedCategory] = useState('Todos');
  const [searchQuery, setSearchQuery] = useState('');
  const [activePost, setActivePost] = useState<BlogPost | null>(null);

  const filteredPosts = posts.filter((post) => {
    const matchesCat =
      selectedCategory === 'Todos' ||
      post.category.toLowerCase().includes(selectedCategory.toLowerCase());
    const matchesSearch =
      !searchQuery.trim() ||
      post.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      post.excerpt.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCat && matchesSearch;
  });

  const handleSelectPost = (post: BlogPost) => {
    onTrackArticleRead(post.title);
    setActivePost(post);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (activePost) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
        <button
          type="button"
          onClick={() => setActivePost(null)}
          className="text-xs font-semibold text-[#1769AA] hover:text-[#081B33] inline-flex items-center gap-1.5 cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Voltar para A M Inteligência Contábil</span>
        </button>

        <article className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-10 space-y-6">
          <div className="text-xs text-slate-500">
            <span className="font-semibold text-[#1769AA]">{activePost.category}</span>
            <span aria-hidden="true"> · </span>
            <span>{activePost.date}</span>
            <span aria-hidden="true"> · </span>
            <span>{activePost.readTime}</span>
            <span aria-hidden="true"> · </span>
            <span>Por {activePost.author}</span>
          </div>

          <h1 className="font-display text-2xl sm:text-4xl font-bold text-[#081B33] leading-tight">
            {activePost.title}
          </h1>

          <p className="text-base sm:text-lg text-slate-600 font-medium border-l-4 border-[#F59E0B] pl-4">
            {activePost.excerpt}
          </p>

          <div className="space-y-4 text-slate-700 text-base leading-relaxed pt-2">
            {activePost.content.map((paragraph, i) => (
              <p key={i}>{paragraph}</p>
            ))}
          </div>

          {activePost.checklist.length > 0 && (
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-6 space-y-3">
              <h2 className="font-display text-lg font-bold text-[#081B33]">
                Pontos de atenção recomendados pela A M Consultoria:
              </h2>
              <ul className="space-y-2">
                {activePost.checklist.map((item) => (
                  <li key={item} className="flex items-start gap-2.5 text-sm text-slate-700">
                    <CheckCircle2 className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Mandatory Article CTA (Seção 21) */}
          <div className="bg-[#081B33] text-white rounded-2xl p-6 sm:p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
            <div>
              <div className="text-xs text-[#F59E0B] font-semibold">
                Orientação Especializada para o seu CNPJ
              </div>
              <h3 className="font-display text-xl font-bold text-white mt-1">
                Precisa de ajuda com sua empresa? Fale com a A M Consultoria.
              </h3>
              <p className="text-xs text-slate-300 mt-1">
                Analisamos a situação fiscal, contábil e societária da sua empresa com clareza e segurança.
              </p>
            </div>
            <div className="flex flex-wrap gap-2.5 shrink-0">
              <button
                type="button"
                onClick={() => onNavigate('orcamento')}
                className="px-4 py-2.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-xs font-semibold rounded-xl cursor-pointer whitespace-nowrap"
              >
                Solicitar avaliação
              </button>
              <button
                type="button"
                onClick={() =>
                  onOpenWhatsApp(
                    `Olá! Li o artigo "${activePost.title}" no site da A M Consultoria e gostaria de conversar sobre minha empresa.`
                  )
                }
                className="px-4 py-2.5 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-xs font-semibold rounded-xl inline-flex items-center gap-1.5 cursor-pointer whitespace-nowrap"
              >
                <MessageSquare className="w-3.5 h-3.5 text-[#F59E0B]" />
                <span>WhatsApp</span>
              </button>
            </div>
          </div>
        </article>
      </div>
    );
  }

  return (
    <div className="space-y-12 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-16 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Central de Conteúdos · Educação Empresarial e Tributária
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-2">
              A M Inteligência Contábil
            </h1>
            <p className="text-base text-slate-300 mt-3 leading-relaxed">
              Artigos práticos sobre contabilidade, planejamento tributário, Simples Nacional, Lucro Presumido, Reforma Tributária e legislação aplicável em Manaus/AM.
            </p>
          </div>

          {/* Search & Category Filter */}
          <div className="mt-8 flex flex-col md:flex-row gap-4 items-stretch md:items-center justify-between">
            <div className="relative flex-1 max-w-md">
              <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input
                type="search"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Pesquisar por tema (ex.: Fator R, DRE, Reforma, Troca)..."
                className="w-full pl-10 pr-4 py-2.5 bg-[#0D2544] border border-white/15 rounded-xl text-xs text-white placeholder:text-slate-400 focus:outline-none focus:border-[#F59E0B]"
              />
            </div>
          </div>

          <div className="mt-4 flex flex-wrap gap-1.5">
            {BLOG_CATEGORIES.map((cat) => (
              <button
                key={cat}
                type="button"
                onClick={() => setSelectedCategory(cat)}
                className={`px-3 py-1.5 text-xs font-medium rounded-lg transition-colors cursor-pointer ${
                  selectedCategory === cat
                    ? 'bg-[#F59E0B] text-[#081B33] font-semibold'
                    : 'bg-white/5 text-slate-300 hover:bg-white/10'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {filteredPosts.length === 0 ? (
          <div className="bg-white border border-slate-200 rounded-2xl p-8 text-center space-y-3">
            <p className="text-sm text-slate-600">
              Nenhum artigo encontrado para o filtro selecionado.
            </p>
            <button
              type="button"
              onClick={() => {
                setSelectedCategory('Todos');
                setSearchQuery('');
              }}
              className="px-4 py-2 bg-[#081B33] text-white text-xs font-semibold rounded-lg cursor-pointer"
            >
              Limpar filtros
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {filteredPosts.map((post) => (
              <article
                key={post.id}
                className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-7 flex flex-col justify-between hover:border-[#1769AA] transition-colors"
              >
                <div>
                  {/* Clean unboxed metadata (Zero-Pill Discipline) */}
                  <div className="text-xs text-slate-500 flex flex-wrap items-center gap-1.5">
                    <span className="font-semibold text-[#1769AA]">{post.category}</span>
                    <span aria-hidden="true">·</span>
                    <span>{post.date}</span>
                    <span aria-hidden="true">·</span>
                    <span>{post.readTime}</span>
                  </div>

                  <h2 className="font-display text-xl font-bold text-[#081B33] mt-2.5 leading-snug">
                    <button
                      type="button"
                      onClick={() => handleSelectPost(post)}
                      className="text-left hover:text-[#1769AA] transition-colors cursor-pointer"
                    >
                      {post.title}
                    </button>
                  </h2>

                  <p className="text-sm text-slate-600 mt-2.5 leading-relaxed">
                    {post.excerpt}
                  </p>
                </div>

                <div className="pt-5 mt-5 border-t border-slate-100 flex items-center justify-between text-xs">
                  <span className="text-slate-500">Por {post.author}</span>
                  <button
                    type="button"
                    onClick={() => handleSelectPost(post)}
                    className="font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
                  >
                    <span>Ler artigo completo</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </article>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};

export const CasosESolucoesPage: React.FC<{
  onNavigate: (page: PageId) => void;
}> = ({ onNavigate }) => {
  return (
    <div className="space-y-14 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-18 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Portfólio Técnico · Metodologia Problema → Solução → Processo → Resultado
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold text-white mt-2">
              Casos e Soluções Reais
            </h1>
            <p className="text-base text-slate-300 mt-3 leading-relaxed">
              Conheça como nossa abordagem consultiva resolve gargalos contábeis, tributários e operacionais preservando total sigilo e confidencialidade dos clientes.
            </p>
          </div>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {CASE_STUDIES.map((cs, index) => (
            <div
              key={cs.id}
              className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 flex flex-col justify-between space-y-6"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between text-xs text-slate-500">
                  <span>
                    0{index + 1}. {cs.category} · {cs.segment}
                  </span>
                  <span className="font-mono font-semibold text-[#1769AA] tabular-nums">
                    {cs.metricHighlight}
                  </span>
                </div>
                <h2 className="font-display text-xl sm:text-2xl font-bold text-[#081B33]">
                  {cs.title}
                </h2>
              </div>

              <div className="space-y-3 text-sm border-t border-slate-100 pt-4">
                <div>
                  <span className="font-semibold text-[#081B33]">Problema: </span>
                  <span className="text-slate-600">{cs.problem}</span>
                </div>
                <div>
                  <span className="font-semibold text-[#1769AA]">Solução: </span>
                  <span className="text-slate-600">{cs.solution}</span>
                </div>
                <div>
                  <span className="font-semibold text-[#081B33]">Processo: </span>
                  <span className="text-slate-600">{cs.process}</span>
                </div>
                <div className="p-3.5 bg-slate-50 border border-slate-200 rounded-xl">
                  <span className="font-semibold text-emerald-800">Resultado Documentado: </span>
                  <span className="text-slate-800 font-medium">{cs.result}</span>
                </div>
              </div>

              <div className="pt-2 flex justify-end">
                <button
                  type="button"
                  onClick={() => onNavigate('orcamento')}
                  className="text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
                >
                  <span>Solicitar avaliação semelhante para minha empresa</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export const PrivacidadeLgpdPage: React.FC<{ config: SiteConfig }> = ({ config }) => {
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-14 space-y-8">
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-10 space-y-6">
        <div className="flex items-center gap-2 text-xs font-semibold text-[#1769AA]">
          <ShieldCheck className="w-4 h-4" />
          <span>Conformidade Legal · Lei nº 13.709/2018 (LGPD)</span>
        </div>
        <h1 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33]">
          Política de Privacidade, Cookies e Termos de Uso
        </h1>
        <p className="text-sm text-slate-600 leading-relaxed">
          A <strong>{config.razaoSocial}</strong>, inscrita no CNPJ sob o nº <span className="font-mono">{config.cnpj}</span>, com sede na {config.endereco}, {config.bairro}, {config.cidadeUf}, CEP {config.cep}, reafirma seu compromisso com a segurança da informação, o sigilo profissional contábil e a proteção dos dados pessoais de clientes, parceiros e visitantes.
        </p>

        <div className="space-y-4 text-sm text-slate-700 leading-relaxed">
          <h2 className="font-display text-lg font-bold text-[#081B33]">
            1. Finalidade da Coleta de Dados nos Formulários
          </h2>
          <p>
            Os dados informados nos formulários de Orçamento, Agendamento de Reunião e Contato (Nome, Empresa, CNPJ, Telefone/WhatsApp, E-mail, Cidade/UF e Regime Tributário) são coletados exclusivamente para: (a) elaborar propostas técnicas de serviços contábeis, fiscais, trabalhistas, de consultoria ou auditoria; (b) agendar reuniões solicitadas pelo titular; e (c) prestar atendimento consultivo pelos nossos canais oficiais.
          </p>

          <h2 className="font-display text-lg font-bold text-[#081B33]">
            2. Segurança do Portal do Cliente (Domínio / Onvio)
          </h2>
          <p>
            Este site institucional não armazena senhas de acesso ao Portal do Cliente nem solicita dados bancários sensíveis. O login do cliente ocorre exclusivamente em ambiente criptografado HTTPS oficial da plataforma Thomson Reuters Domínio / Onvio.
          </p>

          <h2 className="font-display text-lg font-bold text-[#081B33]">
            3. Uso de Cookies e Métricas de Desempenho
          </h2>
          <p>
            Utilizamos cookies estritamente necessários e analíticos (Google Analytics / Search Console) para compreender o desempenho das páginas e aprimorar a experiência do usuário, sem comercialização ou compartilhamento indevido de dados com terceiros.
          </p>

          <h2 className="font-display text-lg font-bold text-[#081B33]">
            4. Canal de Atendimento ao Titular de Dados (DPO)
          </h2>
          <p>
            A qualquer momento, o titular poderá solicitar confirmação de tratamento, atualização ou exclusão de seus dados de contato comercial enviando solicitação para o e-mail oficial <strong>{config.email}</strong> ou pelo telefone <strong>{config.telefonePrincipal}</strong>.
          </p>
        </div>
      </div>
    </div>
  );
};
