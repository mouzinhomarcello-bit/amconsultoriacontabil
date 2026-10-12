import React from 'react';
import {
  ArrowRight,
  ArrowUpRight,
  CheckCircle2,
  Lock,
  MessageSquare,
  Calendar,
  ExternalLink,
  Settings
} from 'lucide-react';
import {
  SiteConfig,
  PageId,
  FOUR_PILLARS,
  SERVICES_LIST,
  BUSINESS_CHALLENGES,
  CASE_STUDIES,
  TestimonialItem,
  BlogPost,
  LeadRecord
} from '../data/siteData';
import { HeroDashboard } from './HeroDashboard';
import { QuoteFormSection } from './QuoteAndScheduleModals';

interface HomePageProps {
  config: SiteConfig;
  testimonials: TestimonialItem[];
  blogPosts: BlogPost[];
  onNavigate: (page: PageId) => void;
  onNavigateWithService: (service: string, regime?: string) => void;
  onAddLead: (lead: Omit<LeadRecord, 'id' | 'data' | 'stage'>) => void;
  onOpenWhatsApp: (customMsg?: string) => void;
  onTrackPortalAccess: () => void;
}

export const HomePage: React.FC<HomePageProps> = ({
  config,
  testimonials,
  blogPosts,
  onNavigate,
  onNavigateWithService,
  onAddLead,
  onOpenWhatsApp,
  onTrackPortalAccess
}) => {
  return (
    <div className="space-y-20 pb-20">
      {/* 8.1 HERO SECTION */}
      <section className="bg-[#081B33] text-white pt-10 pb-16 sm:pt-16 sm:pb-24 border-b border-white/10 relative overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
            {/* Left Column: Proposition & CTAs */}
            <div className="lg:col-span-6 space-y-6">
              <div className="text-xs text-slate-300 flex flex-wrap items-center gap-2">
                <span className="text-[#F59E0B] font-semibold">
                  Contabilidade Digital, Consultoria & Auditoria
                </span>
                <span aria-hidden="true">·</span>
                <span>Manaus/AM & Brasil</span>
                <span aria-hidden="true">·</span>
                <span className="font-mono">CNPJ {config.cnpj}</span>
              </div>

              <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white leading-[1.12]">
                {config.heroHeadline}
              </h1>

              <p className="text-base sm:text-lg text-slate-300 leading-relaxed max-w-xl">
                {config.heroSubheadline}
              </p>

              {/* Primary & Secondary CTAs */}
              <div className="pt-2 flex flex-col sm:flex-row gap-3.5">
                <button
                  type="button"
                  onClick={() => onNavigate('orcamento')}
                  className="px-6 py-4 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer whitespace-nowrap shadow-lg"
                >
                  <span>Solicitar orçamento</span>
                  <ArrowRight className="w-4 h-4" />
                </button>

                <button
                  type="button"
                  onClick={() => onOpenWhatsApp()}
                  className="px-6 py-4 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer whitespace-nowrap"
                >
                  <MessageSquare className="w-4 h-4 text-[#F59E0B]" />
                  <span>Falar pelo WhatsApp</span>
                </button>
              </div>

              {/* Quick Conversion Shortcuts */}
              <div className="pt-4 border-t border-white/10 flex flex-wrap items-center gap-x-6 gap-y-2 text-xs text-slate-300">
                <button
                  type="button"
                  onClick={() => onNavigate('trocar-contador')}
                  className="hover:text-[#F59E0B] inline-flex items-center gap-1 transition-colors cursor-pointer"
                >
                  <span>Quero trocar de contador</span>
                  <ArrowUpRight className="w-3.5 h-3.5 text-[#F59E0B]" />
                </button>
                <button
                  type="button"
                  onClick={() => onNavigate('abrir-empresa')}
                  className="hover:text-[#F59E0B] inline-flex items-center gap-1 transition-colors cursor-pointer"
                >
                  <span>Quero abrir minha empresa</span>
                  <ArrowUpRight className="w-3.5 h-3.5 text-[#F59E0B]" />
                </button>
                <button
                  type="button"
                  onClick={() => onNavigate('agendamento')}
                  className="hover:text-[#F59E0B] inline-flex items-center gap-1 transition-colors cursor-pointer"
                >
                  <Calendar className="w-3.5 h-3.5 text-[#F59E0B]" />
                  <span>Agendar uma conversa</span>
                </button>
              </div>
            </div>

            {/* Right Column: Interactive Futuristic Accounting/Tax Dashboard */}
            <div className="lg:col-span-6">
              <HeroDashboard onNavigate={onNavigate} />
            </div>
          </div>

          {/* 9. SEÇÃO "A AM EM NÚMEROS" (Cadastráveis pelo Administrador) */}
          <div className="mt-14 pt-10 border-t border-white/10">
            <div className="flex items-center justify-between mb-4">
              <span className="text-xs font-semibold text-slate-400">
                A A M em Números · Indicadores Operacionais e Tecnológicos
              </span>
              <button
                type="button"
                onClick={() => onNavigate('admin')}
                className="text-xs text-slate-400 hover:text-[#F59E0B] inline-flex items-center gap-1 cursor-pointer"
              >
                <Settings className="w-3.5 h-3.5" />
                <span>Editar indicadores no CMS</span>
              </button>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {config.indicadores.map((stat) => (
                <div
                  key={stat.id}
                  className="bg-[#0D2544]/90 border border-white/10 rounded-xl p-5"
                >
                  <div className="font-mono text-2xl sm:text-3xl font-bold text-[#F59E0B] tabular-nums">
                    {stat.value}
                  </div>
                  <div className="font-display text-sm font-bold text-white mt-1.5">
                    {stat.label}
                  </div>
                  <p className="text-xs text-slate-300 mt-1 leading-relaxed">{stat.detail}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* 39. OS QUATRO PILARES COMPETITIVOS + 40. MENSAGEM CENTRAL */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-10">
          <div className="max-w-2xl">
            <div className="text-xs font-semibold text-[#1769AA]">
              Posicionamento Estratégico · Diferencial Competitivo
            </div>
            <h2 className="font-display text-2xl sm:text-4xl font-bold text-[#081B33] mt-1">
              Mais do que cumprir obrigações fiscais: impulsionamos decisões empresariais.
            </h2>
          </div>
          <p className="text-sm text-slate-600 max-w-md border-l-2 border-[#F59E0B] pl-4">
            {config.mensagemCentral}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {FOUR_PILLARS.map((pillar) => (
            <div
              key={pillar.number}
              className="bg-white border border-slate-200 rounded-2xl p-6 space-y-3"
            >
              <div className="font-mono text-sm font-semibold text-[#1769AA]">
                {pillar.number}. Pilar A M
              </div>
              <h3 className="font-display text-xl font-bold text-[#081B33]">
                {pillar.title}
              </h3>
              <div className="text-xs font-semibold text-slate-700">{pillar.subtitle}</div>
              <p className="text-sm text-slate-600 leading-relaxed">{pillar.description}</p>
            </div>
          ))}
        </div>
      </section>

      {/* 13. ESPECIALIDADES — "QUAL É O DESAFIO DA SUA EMPRESA?" */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-[#081B33] text-white rounded-3xl p-6 sm:p-12 border border-white/10">
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-10">
            <div>
              <div className="text-xs font-semibold text-[#F59E0B]">
                Autodiagnóstico Empresarial · Soluções Sob Medida
              </div>
              <h2 className="font-display text-2xl sm:text-4xl font-bold text-white mt-1">
                Qual é o desafio da sua empresa neste momento?
              </h2>
            </div>
            <button
              type="button"
              onClick={() => onNavigate('especialidades')}
              className="text-xs font-semibold text-[#F59E0B] hover:underline inline-flex items-center gap-1 self-start lg:self-auto cursor-pointer"
            >
              <span>Ver matriz completa de especialidades</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {BUSINESS_CHALLENGES.map((ch) => (
              <button
                key={ch.id}
                type="button"
                onClick={() => onNavigate(ch.targetPage)}
                className="text-left bg-[#0D2544] hover:bg-[#13325b] border border-white/10 hover:border-[#F59E0B]/60 rounded-2xl p-5 flex flex-col justify-between transition-colors cursor-pointer group"
              >
                <div>
                  <div className="font-mono text-xs text-[#F59E0B]">{ch.number}</div>
                  <h3 className="font-display text-base font-bold text-white mt-1.5 group-hover:text-[#F59E0B] transition-colors">
                    {ch.challengeTitle}
                  </h3>
                  <p className="text-xs text-slate-300 mt-2 leading-relaxed line-clamp-3">
                    {ch.painSummary}
                  </p>
                </div>
                <div className="pt-4 mt-4 border-t border-white/10 flex items-center justify-between text-xs font-semibold text-white">
                  <span>{ch.ctaLabel}</span>
                  <ArrowRight className="w-3.5 h-3.5 text-[#F59E0B]" />
                </div>
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* 12. SERVIÇOS — ASYMMETRIC BENTO GRID */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-10">
          <div>
            <div className="text-xs font-semibold text-[#1769AA]">
              Arquitetura de Serviços Integrados
            </div>
            <h2 className="font-display text-2xl sm:text-4xl font-bold text-[#081B33] mt-1">
              Tudo o que sua empresa precisa em um único parceiro contábil
            </h2>
          </div>
          <button
            type="button"
            onClick={() => onNavigate('servicos')}
            className="text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
          >
            <span>Explorar escopo detalhado e simulador</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {SERVICES_LIST.map((srv, idx) => {
            const isWide = idx === 0 || idx === 1;
            return (
              <div
                key={srv.id}
                className={`${
                  isWide ? 'lg:col-span-6' : 'lg:col-span-4'
                } bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 flex flex-col justify-between`}
              >
                <div className="space-y-3">
                  <div className="font-mono text-xs font-semibold text-[#1769AA]">
                    {srv.index}. {srv.slug.toUpperCase()}
                  </div>
                  <h3 className="font-display text-xl sm:text-2xl font-bold text-[#081B33]">
                    {srv.title}
                  </h3>
                  <p className="text-sm text-slate-600 leading-relaxed">{srv.description}</p>

                  <ul className="space-y-2 pt-3">
                    {srv.items.slice(0, 5).map((sub) => (
                      <li key={sub} className="flex items-start gap-2 text-xs text-slate-700">
                        <CheckCircle2 className="w-3.5 h-3.5 text-[#1769AA] shrink-0 mt-0.5" />
                        <span>{sub}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <div className="pt-6 mt-6 border-t border-slate-100 flex items-center justify-between">
                  <button
                    type="button"
                    onClick={() => onNavigateWithService(srv.title)}
                    className="text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1.5 cursor-pointer"
                  >
                    <span>Solicitar orçamento desta área</span>
                    <ArrowRight className="w-3.5 h-3.5 text-[#1769AA]" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 38. CASOS E SOLUÇÕES + 37. PROVA SOCIAL (CLAIM-TO-PROOF ADJACENCY) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
          <div>
            <div className="text-xs font-semibold text-[#1769AA]">
              Resultados Documentados · Prova Social e Técnica
            </div>
            <h2 className="font-display text-2xl sm:text-4xl font-bold text-[#081B33] mt-1">
              Como geramos eficiência real para empresas em Manaus e no Brasil
            </h2>
          </div>
          <button
            type="button"
            onClick={() => onNavigate('casos')}
            className="text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
          >
            <span>Ver todos os casos e soluções</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>

        {/* 2 Featured Case Studies */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {CASE_STUDIES.slice(0, 2).map((cs) => (
            <div
              key={cs.id}
              className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-4"
            >
              <div className="flex items-center justify-between text-xs text-slate-500">
                <span>
                  {cs.category} · {cs.segment}
                </span>
                <span className="font-mono font-semibold text-[#1769AA] tabular-nums">
                  {cs.metricHighlight}
                </span>
              </div>
              <h3 className="font-display text-xl font-bold text-[#081B33]">{cs.title}</h3>
              <div className="text-xs text-slate-600 space-y-2 border-t border-slate-100 pt-3">
                <p>
                  <strong className="text-[#081B33]">Desafio:</strong> {cs.problem}
                </p>
                <p>
                  <strong className="text-[#1769AA]">Solução A M:</strong> {cs.solution}
                </p>
                <p className="font-semibold text-emerald-800">
                  Resultado: {cs.result}
                </p>
              </div>
            </div>
          ))}
        </div>

        {/* Depoimentos Autorizados */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {testimonials
            .filter((t) => t.authorized)
            .map((item) => (
              <div
                key={item.id}
                className="bg-white border border-slate-200 rounded-2xl p-6 flex flex-col justify-between space-y-4"
              >
                <p className="text-sm text-slate-700 leading-relaxed">"{item.quote}"</p>
                <div className="pt-4 border-t border-slate-100">
                  <div className="font-display text-sm font-bold text-[#081B33]">
                    {item.author}
                  </div>
                  <div className="text-xs text-slate-500">
                    {item.role} · {item.company}
                  </div>
                  <div className="text-[11px] text-[#1769AA] font-medium mt-1">
                    {item.segment}
                  </div>
                </div>
              </div>
            ))}
        </div>
      </section>

      {/* 17. PORTAL DO CLIENTE BANNER ESTRATÉGICO */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-[#081B33] text-white rounded-3xl p-6 sm:p-12 border border-white/10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div className="lg:col-span-7 space-y-4">
            <div className="text-xs font-semibold text-[#F59E0B]">
              Ambiente Digital Exclusivo · {config.portalSistemaNome}
            </div>
            <h2 className="font-display text-2xl sm:text-4xl font-bold text-white">
              Guias, relatórios, balancetes, CNDs e folha em um único Portal.
            </h2>
            <p className="text-sm sm:text-base text-slate-300 leading-relaxed">
              Clientes da A M Consultoria contam com acesso seguro 24 horas por dia ao Portal do Cliente para consultar documentos fiscais, trabalhistas e contábeis sem depender de trocas intermináveis de e-mails.
            </p>
            <div className="pt-2 flex flex-wrap gap-3">
              <a
                href={config.portalClienteUrl}
                target="_blank"
                rel="noopener noreferrer"
                onClick={onTrackPortalAccess}
                className="px-5 py-3.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-xs font-semibold rounded-xl inline-flex items-center gap-2 transition-colors"
              >
                <Lock className="w-4 h-4" />
                <span>Acessar Portal do Cliente</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
              <button
                type="button"
                onClick={() => onNavigate('portal-do-cliente')}
                className="px-5 py-3.5 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-xs font-semibold rounded-xl transition-colors cursor-pointer"
              >
                Ver funcionalidades do Portal
              </button>
            </div>
          </div>

          <div className="lg:col-span-5 grid grid-cols-2 gap-3 text-xs">
            {[
              { title: 'Documentos & XMLs', desc: 'Arquivos contábeis, fiscais e contratos sempre à mão' },
              { title: 'Guias de Impostos', desc: 'DAS, DARF, ICMS e FGTS com alerta de vencimento' },
              { title: 'DRE & Balancetes', desc: 'Relatórios gerenciais assinados digitalmente' },
              { title: 'CNDs Monitoradas', desc: 'Regularidade Federal, SEFAZ-AM e Prefeitura' }
            ].map((box) => (
              <div
                key={box.title}
                className="bg-[#0D2544] border border-white/10 rounded-xl p-4 space-y-1.5"
              >
                <div className="font-semibold text-white">{box.title}</div>
                <p className="text-slate-300 leading-relaxed">{box.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 20. BLOG PREVIEW — A M INTELIGÊNCIA CONTÁBIL */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
          <div>
            <div className="text-xs font-semibold text-[#1769AA]">
              A M Inteligência Contábil · Artigos e Orientações
            </div>
            <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33] mt-1">
              Conteúdo estratégico para apoiar o empresário
            </h2>
          </div>
          <button
            type="button"
            onClick={() => onNavigate('conteudos')}
            className="text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
          >
            <span>Acessar todos os artigos ({blogPosts.length})</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {blogPosts.slice(0, 3).map((post) => (
            <div
              key={post.id}
              className="bg-white border border-slate-200 rounded-2xl p-6 flex flex-col justify-between"
            >
              <div>
                <div className="text-xs text-slate-500">
                  <span className="font-semibold text-[#1769AA]">{post.category}</span>
                  <span aria-hidden="true"> · </span>
                  <span>{post.readTime}</span>
                </div>
                <h3 className="font-display text-lg font-bold text-[#081B33] mt-2 leading-snug">
                  {post.title}
                </h3>
                <p className="text-xs text-slate-600 mt-2 leading-relaxed line-clamp-3">
                  {post.excerpt}
                </p>
              </div>
              <button
                type="button"
                onClick={() => onNavigate('conteudos')}
                className="mt-5 pt-4 border-t border-slate-100 text-xs font-semibold text-[#081B33] hover:text-[#1769AA] inline-flex items-center gap-1 cursor-pointer"
              >
                <span>Ler artigo completo</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>
          ))}
        </div>
      </section>

      {/* 22. FORMULÁRIO DE ORÇAMENTO DE ALTA CONVERSÃO NA HOME */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-5 bg-[#081B33] text-white rounded-2xl p-6 sm:p-8 space-y-6 border border-white/10">
            <div>
              <div className="text-xs font-semibold text-[#F59E0B]">
                Próximo Passo para Sua Empresa
              </div>
              <h2 className="font-display text-2xl sm:text-3xl font-bold text-white mt-2">
                Converse com nossos especialistas e receba uma proposta sob medida.
              </h2>
              <p className="text-sm text-slate-300 mt-3 leading-relaxed">
                Atendemos empresas em Manaus/AM e em todo o território nacional com processos 100% digitais, segurança tributária e acompanhamento próximo dos sócios.
              </p>
            </div>

            <div className="space-y-3 pt-2 border-t border-white/10 text-xs text-slate-200">
              <div className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#F59E0B] shrink-0" />
                <span>Análise inicial do enquadramento tributário (Simples x Presumido)</span>
              </div>
              <div className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#F59E0B] shrink-0" />
                <span>Plano de migração contábil sem burocracia para você</span>
              </div>
              <div className="flex items-center gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-[#F59E0B] shrink-0" />
                <span>Demonstração do Portal do Cliente Domínio / Onvio</span>
              </div>
            </div>

            <div className="p-4 bg-[#0D2544] rounded-xl border border-white/10 text-xs space-y-1">
              <div className="font-semibold text-white">{config.razaoSocial}</div>
              <div className="text-slate-300">
                {config.endereco} — {config.bairro}, {config.cidadeUf}
              </div>
              <div className="font-mono text-[#F59E0B] pt-1">
                WhatsApp: {config.telefonePrincipal} · {config.telefoneSecundario}
              </div>
            </div>
          </div>

          <div className="lg:col-span-7">
            <QuoteFormSection
              config={config}
              origemLabel="Home Page — Formulário Principal"
              onAddLead={onAddLead}
              onOpenWhatsApp={onOpenWhatsApp}
            />
          </div>
        </div>
      </section>
    </div>
  );
};
