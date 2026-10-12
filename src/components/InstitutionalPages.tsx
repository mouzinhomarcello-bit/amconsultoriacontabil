import React, { useState } from 'react';
import {
  CheckCircle2,
  ArrowRight,
  MapPin,
  Phone,
  Mail,
  Clock,
  MessageSquare,
  Building2,
  Instagram,
  Facebook
} from 'lucide-react';
import {
  SiteConfig,
  PageId,
  PARTNERS_DATA,
  BRAND_ASSETS,
  SERVICES_LIST,
  BUSINESS_CHALLENGES,
  LeadRecord
} from '../data/siteData';
import { TaxDiagnosticSimulator, QuoteFormSection } from './QuoteAndScheduleModals';
import { BrandLogo } from './BrandLogo';

export const ResilientImage: React.FC<{
  src: string;
  alt: string;
  className?: string;
  fallbackLabel: string;
}> = ({ src, alt, className = '', fallbackLabel }) => {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return (
      <div
        className={`bg-gradient-to-br from-[#081B33] to-[#1769AA] flex flex-col items-center justify-center p-6 text-center text-white ${className}`}
      >
        <Building2 className="w-8 h-8 text-[#F59E0B] mb-2" />
        <span className="font-display text-sm font-semibold">{fallbackLabel}</span>
      </div>
    );
  }

  return (
    <img
      src={src}
      alt={alt}
      referrerPolicy="no-referrer"
      loading="lazy"
      onError={() => setFailed(true)}
      className={className}
    />
  );
};

export const SobreNosPage: React.FC<{
  config: SiteConfig;
  onNavigate: (page: PageId) => void;
}> = ({ config, onNavigate }) => {
  const valores = [
    'Ética',
    'Transparência',
    'Competência técnica',
    'Inovação',
    'Segurança',
    'Responsabilidade',
    'Atendimento próximo',
    'Evolução contínua'
  ];

  return (
    <div className="space-y-16 pb-16">
      {/* Hero Institucional */}
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
            <div className="lg:col-span-7 space-y-4">
              <div className="pb-2">
                <BrandLogo variant="dark" size="lg" />
              </div>
              <div className="text-xs text-[#F59E0B] font-semibold">
                Institucional · CNPJ {config.cnpj} · Manaus/AM
              </div>
              <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white leading-tight">
                Conhecimento técnico, tecnologia e visão estratégica para o seu negócio.
              </h1>
              <p className="text-base text-slate-300 leading-relaxed">
                A <strong>{config.razaoSocial}</strong> atua como parceira consultiva de empresários que buscam mais do que o cumprimento burocrático de guias fiscais: entregamos organização contábil, processos digitais e inteligência tributária para apoiar decisões.
              </p>
              <div className="pt-2 text-xs text-slate-300 font-mono space-y-1">
                <div>CNAE Principal: 69.20-6-01 — Atividades de contabilidade</div>
                <div>CNAE Secundário: 69.20-6-02 — Atividades de consultoria e auditoria contábil e tributária</div>
              </div>
              <div className="pt-3 flex flex-wrap items-center gap-3">
                <a
                  href={config.instagramUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/10 hover:bg-white/15 border border-white/15 text-xs font-semibold text-white transition-colors"
                >
                  <Instagram className="w-4 h-4 text-[#F59E0B]" />
                  <span>@am.consultoria.contabil</span>
                </a>
                <a
                  href={config.facebookUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/10 hover:bg-white/15 border border-white/15 text-xs font-semibold text-white transition-colors"
                >
                  <Facebook className="w-4 h-4 text-[#38BDF8]" />
                  <span>Facebook Oficial</span>
                </a>
              </div>
            </div>

            <div className="lg:col-span-5">
              <div className="rounded-2xl overflow-hidden border border-white/15 shadow-2xl">
                <ResilientImage
                  src={BRAND_ASSETS.officeManaus}
                  alt="Sede A M Consultoria e Auditoria Contábil em Manaus/AM"
                  fallbackLabel="Sede A M Consultoria — Dom Pedro I, Manaus/AM"
                  className="w-full h-72 object-cover"
                />
                <div className="bg-[#0D2544] p-4 text-xs text-slate-300 flex items-center justify-between">
                  <span>Sede: {config.endereco} — {config.bairro}, {config.cidadeUf}</span>
                  <span className="font-mono text-[#F59E0B]">CEP {config.cep}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Missão, Visão e Valores (Seção 11) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-3">
            <div className="text-xs font-semibold text-[#1769AA]">01. Propósito</div>
            <h2 className="font-display text-2xl font-bold text-[#081B33]">Nossa Missão</h2>
            <p className="text-sm text-slate-600 leading-relaxed">
              Simplificar a gestão contábil, fiscal e tributária, garantindo conformidade legal, segurança nas informações e suporte estratégico para o crescimento dos nossos clientes.
            </p>
          </div>

          <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-3">
            <div className="text-xs font-semibold text-[#1769AA]">02. Direção</div>
            <h2 className="font-display text-2xl font-bold text-[#081B33]">Nossa Visão</h2>
            <p className="text-sm text-slate-600 leading-relaxed">
              Ser parceira estratégica de empresas que buscam organização, conformidade e decisões mais inteligentes, por meio de uma contabilidade atualizada e tecnológica, confiável e orientada a resultados.
            </p>
          </div>

          <div className="bg-[#081B33] text-white border border-white/10 rounded-2xl p-6 sm:p-8 space-y-4">
            <div className="text-xs font-semibold text-[#F59E0B]">03. Princípios</div>
            <h2 className="font-display text-2xl font-bold text-white">Nossos Valores</h2>
            <div className="grid grid-cols-2 gap-2.5 pt-1">
              {valores.map((val) => (
                <div key={val} className="flex items-center gap-2 text-xs text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-[#F59E0B] shrink-0" />
                  <span>{val}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Sócios (Seção 10) */}
      {config.mostrarSocios && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-2xl mb-8">
            <div className="text-xs font-semibold text-[#1769AA]">
              Liderança Técnica e Consultiva
            </div>
            <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33] mt-1">
              Sócios-Diretores da A M Consultoria
            </h2>
            <p className="text-sm text-slate-600 mt-2">
              Atendimento próximo conduzido diretamente por profissionais com sólida experiência em contabilidade empresarial, consultoria e auditoria.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {PARTNERS_DATA.map((partner) => (
              <div
                key={partner.id}
                className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 flex flex-col sm:flex-row gap-6 items-start"
              >
                <ResilientImage
                  src={partner.image}
                  alt={partner.name}
                  fallbackLabel={partner.name}
                  className="w-28 h-28 sm:w-32 sm:h-32 rounded-2xl object-cover shrink-0 border border-slate-200"
                />
                <div className="space-y-2.5">
                  <div className="text-xs text-[#1769AA] font-semibold">{partner.role}</div>
                  <h3 className="font-display text-xl font-bold text-[#081B33]">
                    {partner.name}
                  </h3>
                  <p className="text-sm text-slate-600 leading-relaxed">{partner.bio}</p>
                  <div className="pt-2 text-xs text-slate-500 font-medium">
                    {partner.focusAreas}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Mensagem Central */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white border border-slate-200 rounded-2xl p-8 sm:p-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="max-w-2xl">
            <div className="text-xs font-semibold text-[#1769AA]">Mensagem Central da Marca</div>
            <blockquote className="font-display text-xl sm:text-2xl font-bold text-[#081B33] mt-2">
              "{config.mensagemCentral}"
            </blockquote>
          </div>
          <button
            type="button"
            onClick={() => onNavigate('orcamento')}
            className="px-6 py-3.5 bg-[#081B33] hover:bg-[#1769AA] text-white text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors self-start cursor-pointer whitespace-nowrap"
          >
            <span>Solicitar uma avaliação</span>
            <ArrowRight className="w-4 h-4 text-[#F59E0B]" />
          </button>
        </div>
      </section>
    </div>
  );
};

export const ServicosPage: React.FC<{
  onNavigateWithService: (service: string, regime?: string) => void;
}> = ({ onNavigateWithService }) => {
  return (
    <div className="space-y-16 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Portfólio Completo de Serviços · CNAE 69.20-6-01 & 69.20-6-02
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3">
              Soluções contábeis, fiscais, trabalhistas e de auditoria para sua empresa.
            </h1>
            <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
              Nós ajudamos sua empresa a entender os números e tomar decisões com mais segurança. Conheça em detalhes cada área de atuação da A M Consultoria.
            </p>
          </div>
        </div>
      </section>

      {/* 5 Áreas de Serviços Detalhadas (Seção 12) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        {SERVICES_LIST.map((service) => (
          <div
            key={service.id}
            className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start"
          >
            <div className="lg:col-span-5 space-y-4">
              <div className="font-mono text-sm font-semibold text-[#1769AA]">
                {service.index}. Área de Atuação
              </div>
              <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33]">
                {service.title}
              </h2>
              <p className="text-sm font-medium text-slate-700">{service.tagline}</p>
              <p className="text-sm text-slate-600 leading-relaxed">{service.description}</p>

              <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs space-y-1.5">
                <div className="font-semibold text-[#081B33]">Entrega Consultiva em Destaque:</div>
                <div className="text-[#1769AA] font-mono">{service.deliverableExample}</div>
                <div className="text-slate-500 pt-1">Perfil: {service.targetAudience}</div>
              </div>

              <button
                type="button"
                onClick={() => onNavigateWithService(service.title)}
                className="px-5 py-3 bg-[#081B33] hover:bg-[#1769AA] text-white text-xs font-semibold rounded-xl inline-flex items-center gap-2 transition-colors cursor-pointer"
              >
                <span>Solicitar proposta de {service.title.split(' ')[0]}</span>
                <ArrowRight className="w-3.5 h-3.5 text-[#F59E0B]" />
              </button>
            </div>

            <div className="lg:col-span-7 bg-slate-50 border border-slate-200 rounded-xl p-6">
              <h3 className="text-xs font-semibold text-slate-500 mb-4">
                Escopo Técnico Incluso na {service.title}:
              </h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                {service.items.map((item) => (
                  <div
                    key={item}
                    className="flex items-start gap-2.5 text-sm text-slate-800 bg-white p-3.5 rounded-lg border border-slate-200/80"
                  >
                    <CheckCircle2 className="w-4 h-4 text-[#1769AA] shrink-0 mt-0.5" />
                    <span>{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ))}
      </section>

      {/* Simulador Tributário Integrado */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <TaxDiagnosticSimulator
          onSelectQuoteWithContext={(serv, reg) => onNavigateWithService(serv, reg)}
        />
      </section>
    </div>
  );
};

export const EspecialidadesPage: React.FC<{
  onNavigate: (page: PageId) => void;
}> = ({ onNavigate }) => {
  const segmentosPrioritarios = [
    {
      title: 'Pequenas e Médias Empresas (PMEs)',
      desc: 'Empresas que precisam profissionalizar sua gestão contábil, organizar fluxo documental e ter relatórios claros de lucro.'
    },
    {
      title: 'Empresas do Simples Nacional',
      desc: 'Acompanhamento de sublimites, cálculo mensal de Fator R, segregação de receitas (ST e monofásicos) e folha de pagamento.'
    },
    {
      title: 'Empresas no Lucro Presumido',
      desc: 'Gestão fiscal rigorosa de IRPJ, CSLL, PIS, COFINS, ICMS/ISS, obrigações SPED e distribuição isenta de lucros contábeis.'
    },
    {
      title: 'Prestadores de Serviços e B2B',
      desc: 'Engenharia, tecnologia, clínicas médicas, consultorias e profissionais especializados com foco em redução legal de carga.'
    },
    {
      title: 'Comércio Atacadista e Varejista',
      desc: 'Controle de emissão de NF-e/NFC-e, estoque, ICMS-AM, Substituição Tributária e incentivos da Zona Franca de Manaus.'
    },
    {
      title: 'Empresas em Abertura ou Migração',
      desc: 'Estruturação societária desde o zero ou transição segura para empresários insatisfeitos com a contabilidade atual.'
    }
  ];

  return (
    <div className="space-y-16 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Soluções Orientadas ao Momento do Empresário
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3">
              Qual é o desafio da sua empresa hoje?
            </h1>
            <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
              Identifique abaixo a necessidade prioritária do seu negócio e veja como a A M Consultoria atua para resolvê-la com rapidez e segurança técnica.
            </p>
          </div>
        </div>
      </section>

      {/* 8 Cards de Desafios (Seção 13) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {BUSINESS_CHALLENGES.map((item) => (
            <div
              key={item.id}
              className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 flex flex-col justify-between hover:border-[#1769AA] transition-colors"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between text-xs">
                  <span className="font-mono font-semibold text-[#1769AA]">
                    Desafio {item.number}
                  </span>
                  <span className="text-slate-500">{item.recommendedService}</span>
                </div>
                <h2 className="font-display text-2xl font-bold text-[#081B33]">
                  "{item.challengeTitle}"
                </h2>
                <p className="text-sm text-slate-600 leading-relaxed">{item.painSummary}</p>
                <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-700 space-y-2">
                  <div className="font-semibold text-[#081B33]">Como a A M resolve:</div>
                  <p>{item.solutionSummary}</p>
                  <div className="pt-1 space-y-1">
                    {item.steps.map((st) => (
                      <div key={st} className="flex items-center gap-1.5 text-slate-600">
                        <CheckCircle2 className="w-3.5 h-3.5 text-[#1769AA] shrink-0" />
                        <span>{st}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              <div className="pt-5 mt-5 border-t border-slate-100 flex justify-end">
                <button
                  type="button"
                  onClick={() => onNavigate(item.targetPage)}
                  className="px-4 py-2.5 bg-[#081B33] hover:bg-[#1769AA] text-white text-xs font-semibold rounded-xl inline-flex items-center gap-1.5 transition-colors cursor-pointer"
                >
                  <span>{item.ctaLabel}</span>
                  <ArrowRight className="w-3.5 h-3.5 text-[#F59E0B]" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Segmentos Prioritários (Seção 6) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-[#081B33] text-white rounded-2xl p-6 sm:p-10 border border-white/10">
          <div className="max-w-2xl mb-8">
            <div className="text-xs font-semibold text-[#F59E0B]">
              Especialização por Porte e Regime Fiscal
            </div>
            <h2 className="font-display text-2xl sm:text-3xl font-bold text-white mt-1">
              Segmentos Prioritários Atendidos pela A M
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {segmentosPrioritarios.map((seg, i) => (
              <div
                key={seg.title}
                className="bg-[#0D2544] border border-white/10 rounded-xl p-5 space-y-2"
              >
                <div className="font-mono text-xs text-[#F59E0B]">0{i + 1}. Segmento</div>
                <h3 className="font-display text-lg font-bold text-white">{seg.title}</h3>
                <p className="text-xs text-slate-300 leading-relaxed">{seg.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export const ContatoPage: React.FC<{
  config: SiteConfig;
  onAddLead: (lead: Omit<LeadRecord, 'id' | 'data' | 'stage'>) => void;
  onOpenWhatsApp: (customMsg?: string) => void;
  onTrackPhoneOrEmail: (type: 'clique_telefone' | 'clique_email', label: string) => void;
}> = ({ config, onAddLead, onOpenWhatsApp, onTrackPhoneOrEmail }) => {
  return (
    <div className="space-y-16 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-16 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Canais Oficiais de Atendimento · Manaus/AM e Nacional
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold text-white mt-2">
              Fale com a A M Consultoria
            </h1>
            <p className="text-base text-slate-300 mt-3 leading-relaxed">
              Estamos prontos para atender sua empresa presencialmente em nossa sede no bairro Dom Pedro I em Manaus/AM ou de forma 100% digital em todo o Brasil.
            </p>
          </div>
        </div>
      </section>

      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Dados Cadastrais Oficiais do CNPJ + Mapa (Seção 25) */}
          <div className="lg:col-span-5 space-y-6">
            <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-5">
              <div className="pb-2 border-b border-slate-100">
                <BrandLogo variant="light" size="md" />
              </div>
              <div>
                <div className="text-xs font-semibold text-[#1769AA]">
                  Dados Oficiais do CNPJ
                </div>
                <h2 className="font-display text-xl font-bold text-[#081B33] mt-1">
                  {config.razaoSocial}
                </h2>
                <div className="text-xs font-mono text-slate-500 mt-1">
                  CNPJ: {config.cnpj} · Situação: {config.situacaoCadastral}
                </div>
              </div>

              <div className="space-y-4 text-sm border-t border-slate-100 pt-4">
                <div className="flex items-start gap-3">
                  <MapPin className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                  <div>
                    <div className="font-semibold text-[#081B33]">Sede em Manaus/AM</div>
                    <div className="text-slate-600">
                      {config.endereco} — {config.bairro}
                    </div>
                    <div className="text-slate-600">
                      {config.cidadeUf} · CEP <span className="font-mono">{config.cep}</span>
                    </div>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Phone className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                  <div>
                    <div className="font-semibold text-[#081B33]">Telefones e WhatsApp</div>
                    <div className="space-x-3 mt-0.5 font-mono text-xs">
                      <a
                        href={`tel:${config.whatsappPrincipalRaw}`}
                        onClick={() =>
                          onTrackPhoneOrEmail('clique_telefone', config.telefonePrincipal)
                        }
                        className="text-[#1769AA] hover:underline font-semibold"
                      >
                        {config.telefonePrincipal} (Manaus)
                      </a>
                      <span>·</span>
                      <a
                        href={`tel:${config.whatsappSecundarioRaw}`}
                        onClick={() =>
                          onTrackPhoneOrEmail('clique_telefone', config.telefoneSecundario)
                        }
                        className="text-[#1769AA] hover:underline font-semibold"
                      >
                        {config.telefoneSecundario} (SP)
                      </a>
                    </div>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Mail className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                  <div>
                    <div className="font-semibold text-[#081B33]">E-mail Corporativo</div>
                    <a
                      href={`mailto:${config.email}`}
                      onClick={() => onTrackPhoneOrEmail('clique_email', config.email)}
                      className="text-[#1769AA] hover:underline font-mono text-xs"
                    >
                      {config.email}
                    </a>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Clock className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                  <div>
                    <div className="font-semibold text-[#081B33]">Horário de Atendimento</div>
                    <div className="text-slate-600 text-xs">{config.horarioAtendimento}</div>
                  </div>
                </div>

                <div className="pt-2 border-t border-slate-100">
                  <div className="text-xs font-semibold text-[#081B33] mb-2">
                    Redes Sociais Oficiais
                  </div>
                  <div className="grid grid-cols-2 gap-2.5">
                    <a
                      href={config.instagramUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl bg-slate-50 hover:bg-[#081B33] text-[#081B33] hover:text-white border border-slate-200 text-xs font-semibold transition-colors"
                    >
                      <Instagram className="w-4 h-4 text-[#F59E0B]" />
                      <span>Instagram</span>
                    </a>
                    <a
                      href={config.facebookUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="flex items-center justify-center gap-2 py-2.5 px-3 rounded-xl bg-slate-50 hover:bg-[#081B33] text-[#081B33] hover:text-white border border-slate-200 text-xs font-semibold transition-colors"
                    >
                      <Facebook className="w-4 h-4 text-[#1769AA]" />
                      <span>Facebook</span>
                    </a>
                  </div>
                </div>
              </div>

              <button
                type="button"
                onClick={() => onOpenWhatsApp()}
                className="w-full py-3.5 px-4 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer"
              >
                <MessageSquare className="w-4 h-4" />
                <span>Iniciar conversa no WhatsApp agora</span>
              </button>
            </div>

            {/* Google Maps Embed — Rua Mocajuba, 93, Dom Pedro I, Manaus/AM */}
            <div className="bg-white border border-slate-200 rounded-2xl overflow-hidden">
              <div className="p-4 border-b border-slate-100 flex items-center justify-between text-xs">
                <span className="font-semibold text-[#081B33]">
                  Localização · Rua Mocajuba, 93, Sala 05 — Dom Pedro I
                </span>
                <span className="font-mono text-slate-500">Manaus/AM</span>
              </div>
              <iframe
                title="Mapa Sede A M Consultoria e Auditoria Contábil Manaus"
                src="https://www.google.com/maps?q=Rua+Mocajuba,+93,+Dom+Pedro,+Manaus,+AM,+69040-530&output=embed"
                className="w-full h-64 border-0"
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
              />
            </div>
          </div>

          {/* Formulário de Orçamento / Contato ao lado */}
          <div className="lg:col-span-7">
            <QuoteFormSection
              config={config}
              origemLabel="Página de Contato Institucional"
              onAddLead={onAddLead}
              onOpenWhatsApp={onOpenWhatsApp}
            />
          </div>
        </div>
      </section>
    </div>
  );
};
