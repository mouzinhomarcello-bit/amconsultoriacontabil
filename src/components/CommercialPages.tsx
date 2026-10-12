import React, { useState } from 'react';
import {
  ArrowRight,
  CheckCircle2,
  AlertTriangle,
  Lock,
  ExternalLink,
  ShieldCheck,
  FileText,
  FolderOpen,
  BarChart3,
  Award,
  Users,
  Bell,
  MessageSquare,
  Building2,
  Laptop
} from 'lucide-react';
import { PageId, SiteConfig, LeadRecord } from '../data/siteData';
import { QuoteFormSection } from './QuoteAndScheduleModals';

interface SharedPageProps {
  config: SiteConfig;
  onNavigate: (page: PageId) => void;
  onAddLead: (lead: Omit<LeadRecord, 'id' | 'data' | 'stage'>) => void;
  onOpenWhatsApp: (customMsg?: string) => void;
  onTrackEvent: (
    type:
      | 'clique_whatsapp'
      | 'clique_telefone'
      | 'clique_email'
      | 'envio_formulario'
      | 'solicitacao_orcamento'
      | 'agendamento'
      | 'acesso_portal'
      | 'leitura_artigo'
      | 'clique_servico',
    label: string
  ) => void;
}

export const TrocarContadorPage: React.FC<SharedPageProps> = ({
  config,
  onAddLead,
  onOpenWhatsApp
}) => {
  const [checkedDocs, setCheckedDocs] = useState<string[]>([
    'Contrato Social e alterações consolidadas',
    'Certificado Digital e-CNPJ (A1 ou A3)'
  ]);

  const toggleDoc = (doc: string) => {
    setCheckedDocs((prev) =>
      prev.includes(doc) ? prev.filter((d) => d !== doc) : [...prev, doc]
    );
  };

  const problemasAntigos = [
    'Guias de impostos enviadas na véspera do vencimento sem aviso prévio',
    'Falta de retorno claro no WhatsApp quando o empresário precisa tomar uma decisão',
    'Ausência de Balancetes e DRE mensal para comprovar lucro e distribuir dividendos isentos',
    'Dúvida permanente se a empresa está pagando mais impostos do que deveria',
    'Solicitação manual de papéis e falta de um Portal Digital organizado'
  ];

  const beneficiosMudanca = [
    'Diagnóstico tributário e cadastral completo nos primeiros 10 dias de parceria',
    'Transição 100% conduzida pela A M diretamente com o escritório anterior',
    'Acesso imediato ao Portal do Cliente (Domínio / Onvio) no computador e celular',
    'Monitoramento automático de Certidões Negativas (CNDs Federal, SEFAZ-AM, Pref. Manaus e FGTS)',
    'Reuniões periódicas de leitura de DRE, margem de lucro e planejamento fiscal'
  ];

  const passosTransferencia = [
    {
      step: '01',
      title: 'Alinhamento e Proposta Consultiva',
      desc: 'Avaliamos o porte, regime tributário e volume operacional da sua empresa para definir o escopo ideal.'
    },
    {
      step: '02',
      title: 'Comunicação Técnica com o Contador Anterior',
      desc: 'Você não precisa ter conversas desconfortáveis. Nossa equipe formaliza o Termo de Transferência de Responsabilidade Técnica.'
    },
    {
      step: '03',
      title: 'Auditoria de Onboarding e Procurações Eletrônicas',
      desc: 'Configuramos as procurações no e-CAC, SEFAZ-AM, Prefeitura de Manaus e eSocial, revisando eventuais pendências.'
    },
    {
      step: '04',
      title: 'Operação 100% Ativa no Portal Digital',
      desc: 'Sua empresa passa a operar com calendário fiscal organizado, conciliação integrada e suporte consultivo próximo.'
    }
  ];

  const documentosNecessarios = [
    'Contrato Social e alterações consolidadas',
    'Certificado Digital e-CNPJ (A1 ou A3)',
    'Procuração eletrônica e-CAC e SEFAZ-AM (orientamos a emissão em 3 minutos)',
    'Balancete de verificação e Livro Diário encerrado pelo escritório anterior',
    'Relação de funcionários ativos e acesso ao eSocial / FGTS Digital',
    'Senhas de emissão de Nota Fiscal (Prefeitura de Manaus / SEFAZ)'
  ];

  return (
    <div className="space-y-16 pb-16">
      {/* Hero Troque de Contador */}
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Migração Contábil Assistida · Zero Interrupção no Seu Faturamento
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3 leading-tight">
              Sua empresa cresceu. Sua contabilidade também precisa evoluir.
            </h1>
            <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
              Sua empresa merece uma contabilidade mais próxima, tecnológica e estratégica. Conduzimos todo o processo de transferência junto ao seu contador atual com segurança técnica e agilidade.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <a
                href="#form-troca"
                className="px-6 py-3.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors"
              >
                <span>Quero conversar sobre a troca de contador</span>
                <ArrowRight className="w-4 h-4" />
              </a>
              <button
                type="button"
                onClick={() =>
                  onOpenWhatsApp(
                    'Olá! Estou avaliando trocar de contador e gostaria de entender como funciona a migração para a A M Consultoria.'
                  )
                }
                className="px-6 py-3.5 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors cursor-pointer"
              >
                <MessageSquare className="w-4 h-4 text-[#F59E0B]" />
                <span>Tirar dúvidas pelo WhatsApp</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* 1. Problemas vs 2. Benefícios */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8">
            <div className="text-xs font-semibold text-amber-700">
              01. Diagnóstico do Cenário Atual
            </div>
            <h2 className="font-display text-2xl font-bold text-[#081B33] mt-1">
              Problemas de uma contabilidade desatualizada
            </h2>
            <p className="text-sm text-slate-600 mt-2">
              Quando a contabilidade atua apenas como geradora de guias, o empresário assume riscos fiscais sem perceber:
            </p>
            <ul className="mt-6 space-y-3.5">
              {problemasAntigos.map((prob) => (
                <li key={prob} className="flex items-start gap-3 text-sm text-slate-700">
                  <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0 mt-1" />
                  <span>{prob}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-[#081B33] text-white border border-white/10 rounded-2xl p-6 sm:p-8">
            <div className="text-xs font-semibold text-[#F59E0B]">
              02. O Padrão A M Consultoria
            </div>
            <h2 className="font-display text-2xl font-bold text-white mt-1">
              Benefícios imediatos da mudança para sua empresa
            </h2>
            <p className="text-sm text-slate-300 mt-2">
              Ao migrar para a A M, sua empresa ganha organização documental, revisão preventiva de impostos e visão gerencial:
            </p>
            <ul className="mt-6 space-y-3.5">
              {beneficiosMudanca.map((ben) => (
                <li key={ben} className="flex items-start gap-3 text-sm text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-[#F59E0B] shrink-0 mt-1" />
                  <span>{ben}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      {/* 3. Como funciona a transferência + 5. Prazo estimado + 6. Como a A M conduz */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-10">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-8 border-b border-slate-200">
            <div>
              <div className="text-xs font-semibold text-[#1769AA]">
                03. Processo Estruturado e Seguro
              </div>
              <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33] mt-1">
                Como a A M conduz a transferência passo a passo
              </h2>
            </div>
            <div className="text-left md:text-right">
              <div className="text-xs text-slate-500">Prazo estimado de conclusão</div>
              <div className="text-lg font-mono font-semibold text-[#081B33] tabular-nums">
                10 a 15 dias úteis · Sem parar sua empresa
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-8">
            {passosTransferencia.map((p) => (
              <div key={p.step} className="border-l-2 border-[#1769AA] pl-4 space-y-2">
                <div className="font-mono text-sm font-semibold text-[#1769AA]">
                  Etapa {p.step}
                </div>
                <h3 className="font-display text-lg font-bold text-[#081B33]">
                  {p.title}
                </h3>
                <p className="text-sm text-slate-600 leading-relaxed">{p.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 4. Checklist de Documentos Necessários + 7. Formulário de Conversão */}
      <section id="form-troca" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-5 bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-5">
            <div>
              <div className="text-xs font-semibold text-[#1769AA]">
                04. Checklist Simplificado
              </div>
              <h3 className="font-display text-xl font-bold text-[#081B33] mt-1">
                Documentos básicos para iniciar
              </h3>
              <p className="text-xs text-slate-600 mt-1">
                Você só precisa nos enviar o básico. Os arquivos contábeis técnicos (SPED, XMLs, balancetes) nós solicitamos diretamente ao contador anterior:
              </p>
            </div>

            <div className="space-y-2.5">
              {documentosNecessarios.map((doc) => {
                const isChecked = checkedDocs.includes(doc);
                return (
                  <button
                    key={doc}
                    type="button"
                    onClick={() => toggleDoc(doc)}
                    className={`w-full text-left p-3 rounded-xl border text-xs font-medium flex items-start gap-2.5 transition-colors cursor-pointer ${
                      isChecked
                        ? 'bg-sky-50/70 border-[#1769AA] text-[#081B33]'
                        : 'bg-slate-50 border-slate-200 text-slate-700 hover:bg-slate-100'
                    }`}
                  >
                    <CheckCircle2
                      className={`w-4 h-4 shrink-0 mt-0.5 ${
                        isChecked ? 'text-[#1769AA]' : 'text-slate-400'
                      }`}
                    />
                    <span>{doc}</span>
                  </button>
                );
              })}
            </div>

            <div className="p-4 bg-[#081B33] text-white rounded-xl text-xs space-y-1.5">
              <div className="font-semibold text-[#F59E0B]">
                Qual o melhor mês para trocar de contador?
              </div>
              <p className="text-slate-300 leading-relaxed">
                A troca pode ser realizada em <strong>qualquer mês do ano</strong>. Nossa equipe recepciona o balancete acumulado e assume as apurações do mês corrente sem duplicidade.
              </p>
            </div>
          </div>

          <div className="lg:col-span-7">
            <QuoteFormSection
              config={config}
              defaultService="Troca de contador"
              defaultRegime="Simples Nacional"
              origemLabel="Landing Page — Troque de Contador"
              onAddLead={onAddLead}
              onOpenWhatsApp={onOpenWhatsApp}
            />
          </div>
        </div>
      </section>
    </div>
  );
};

export const AbrirEmpresaPage: React.FC<SharedPageProps> = ({
  config,
  onAddLead,
  onOpenWhatsApp
}) => {
  const [tipoAtividade, setTipoAtividade] = useState<'servicos' | 'comercio' | 'ambos'>('servicos');
  const [possuiSocios, setPossuiSocios] = useState<'individual' | 'sociedade'>('individual');
  const [faturamentoInicial, setFaturamentoInicial] = useState<'ate30k' | '30ka100k' | 'acima100k'>('ate30k');

  const fluxoSetePassos = [
    {
      num: '01',
      title: 'Entendimento da atividade',
      desc: 'Mapeamos como sua empresa vai operar, quem serão seus clientes (B2B ou consumidor final) e a estrutura de custos.'
    },
    {
      num: '02',
      title: 'Análise tributária preventiva',
      desc: 'Simulamos a carga fiscal no Simples Nacional (Anexos I a V e Fator R) e no Lucro Presumido antes do registro.'
    },
    {
      num: '03',
      title: 'Definição da natureza jurídica',
      desc: 'Recomendamos o formato societário seguro (SLU — Sociedade Limitada Unipessoal ou LTDA com proteção patrimonial).'
    },
    {
      num: '04',
      title: 'Orientação técnica sobre CNAE',
      desc: 'Selecionamos os códigos CNAE principais e secundários corretos para evitar alíquotas desnecessárias ou vedações.'
    },
    {
      num: '05',
      title: 'Processo de abertura e protocolo',
      desc: 'Elaboração do Contrato Social, viabilidade na Prefeitura de Manaus, registro na JUCEA e emissão do CNPJ.'
    },
    {
      num: '06',
      title: 'Regularização e Inscrições',
      desc: 'Inscrição Municipal (SEMEF Manaus), Inscrição Estadual (SEFAZ-AM / SUFRAMA quando aplicável) e licenças.'
    },
    {
      num: '07',
      title: 'Início da contabilidade e emissão de NF',
      desc: 'Parametrização do emissor de Notas Fiscais, certificado digital e ativação da sua empresa no Portal do Cliente.'
    }
  ];

  const recomendacaoJuridica =
    possuiSocios === 'individual'
      ? 'SLU — Sociedade Limitada Unipessoal (protege seu CPF sem exigir sócio)'
      : 'Sociedade Empresária Limitada (LTDA) com cláusulas claras de governança';

  const recomendacaoRegime =
    faturamentoInicial === 'acima100k'
      ? 'Estudo comparativo entre Simples Nacional (Fator R) e Lucro Presumido'
      : 'Simples Nacional com parametrização de alíquota inicial reduzida';

  return (
    <div className="space-y-16 pb-16">
      {/* Hero Abra sua empresa */}
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Abertura e Legalização de Empresas · Manaus/AM e Todo o Brasil
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3 leading-tight">
              Abra sua empresa do jeito certo desde o início.
            </h1>
            <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
              Escolher o CNAE errado ou o regime tributário inadequado pode fazer sua nova empresa pagar impostos indevidos desde a primeira nota fiscal. Na A M, a abertura do seu CNPJ começa com planejamento consultivo.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <a
                href="#form-abertura"
                className="px-6 py-3.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors"
              >
                <span>Quero abrir minha empresa</span>
                <ArrowRight className="w-4 h-4" />
              </a>
              <button
                type="button"
                onClick={() =>
                  onOpenWhatsApp(
                    'Olá! Quero abrir minha empresa com a A M Consultoria e gostaria de orientação sobre CNAE, impostos e prazos.'
                  )
                }
                className="px-6 py-3.5 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors cursor-pointer"
              >
                <MessageSquare className="w-4 h-4 text-[#F59E0B]" />
                <span>Falar com especialista em abertura</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Fluxo de 7 etapas */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-2xl mb-10">
          <div className="text-xs font-semibold text-[#1769AA]">
            Roteiro Completo em 7 Etapas
          </div>
          <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33] mt-1">
            Do planejamento tributário à primeira Nota Fiscal emitida
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
          {fluxoSetePassos.map((item) => (
            <div
              key={item.num}
              className="bg-white border border-slate-200 rounded-2xl p-6 flex flex-col justify-between"
            >
              <div>
                <div className="font-mono text-sm font-semibold text-[#1769AA]">
                  Etapa {item.num}
                </div>
                <h3 className="font-display text-lg font-bold text-[#081B33] mt-2">
                  {item.title}
                </h3>
                <p className="text-sm text-slate-600 mt-2 leading-relaxed">{item.desc}</p>
              </div>
            </div>
          ))}

          {/* 8th Card: Summary Callout */}
          <div className="bg-[#081B33] text-white rounded-2xl p-6 flex flex-col justify-between border border-white/10">
            <div>
              <div className="font-mono text-xs text-[#F59E0B]">JUCEA · RFB · SEFAZ-AM · SEMEF</div>
              <h3 className="font-display text-lg font-bold text-white mt-2">
                Acompanhamento integral em Manaus/AM
              </h3>
              <p className="text-xs text-slate-300 mt-2 leading-relaxed">
                Cuidamos de todas as etapas digitais com assinatura via Certificado ou Gov.br, entregando seu CNPJ pronto para faturar.
              </p>
            </div>
            <a
              href="#form-abertura"
              className="mt-4 text-xs font-semibold text-[#F59E0B] hover:underline inline-flex items-center gap-1"
            >
              <span>Iniciar abertura agora</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </a>
          </div>
        </div>
      </section>

      {/* Interactive Configurator + Form */}
      <section id="form-abertura" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-5 bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-5">
            <div>
              <div className="text-xs font-semibold text-[#1769AA]">
                Simulador Rápido de Estrutura Societária
              </div>
              <h3 className="font-display text-xl font-bold text-[#081B33] mt-1">
                Configure o perfil da sua futura empresa
              </h3>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                1. O que sua empresa irá vender?
              </label>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: 'servicos', label: 'Serviços' },
                  { id: 'comercio', label: 'Comércio' },
                  { id: 'ambos', label: 'Ambos' }
                ].map((opt) => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => setTipoAtividade(opt.id as 'servicos' | 'comercio' | 'ambos')}
                    className={`py-2 px-3 text-xs font-medium rounded-lg border cursor-pointer ${
                      tipoAtividade === opt.id
                        ? 'bg-[#081B33] text-white border-[#081B33]'
                        : 'bg-slate-50 text-slate-700 border-slate-200'
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                2. Você abrirá sozinho ou com sócios?
              </label>
              <div className="grid grid-cols-2 gap-2">
                {[
                  { id: 'individual', label: 'Sozinho (Unipessoal)' },
                  { id: 'sociedade', label: 'Com 2 ou mais sócios' }
                ].map((opt) => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => setPossuiSocios(opt.id as 'individual' | 'sociedade')}
                    className={`py-2 px-3 text-xs font-medium rounded-lg border cursor-pointer ${
                      possuiSocios === opt.id
                        ? 'bg-[#081B33] text-white border-[#081B33]'
                        : 'bg-slate-50 text-slate-700 border-slate-200'
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                3. Previsão de faturamento mensal inicial
              </label>
              <div className="grid grid-cols-3 gap-2">
                {[
                  { id: 'ate30k', label: 'Até R$ 30 mil' },
                  { id: '30ka100k', label: 'R$ 30k a 100k' },
                  { id: 'acima100k', label: '+ R$ 100 mil' }
                ].map((opt) => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() =>
                      setFaturamentoInicial(opt.id as 'ate30k' | '30ka100k' | 'acima100k')
                    }
                    className={`py-2 px-2 text-xs font-medium rounded-lg border cursor-pointer ${
                      faturamentoInicial === opt.id
                        ? 'bg-[#081B33] text-white border-[#081B33]'
                        : 'bg-slate-50 text-slate-700 border-slate-200'
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>

            <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2.5 text-xs">
              <div className="font-semibold text-[#081B33] flex items-center gap-1.5">
                <Building2 className="w-4 h-4 text-[#1769AA]" />
                <span>Pré-Recomendação da A M Consultoria:</span>
              </div>
              <div>
                <span className="text-slate-500">Natureza Jurídica: </span>
                <strong className="text-[#081B33]">{recomendacaoJuridica}</strong>
              </div>
              <div>
                <span className="text-slate-500">Enquadramento Fiscal: </span>
                <strong className="text-[#081B33]">{recomendacaoRegime}</strong>
              </div>
              <div>
                <span className="text-slate-500">Inscrições em Manaus/AM: </span>
                <strong className="text-[#081B33]">
                  {tipoAtividade === 'servicos'
                    ? 'CNPJ + Inscrição Municipal SEMEF (NFS-e)'
                    : 'CNPJ + SEFAZ-AM (ICMS/NF-e) + SEMEF Manaus'}
                </strong>
              </div>
            </div>
          </div>

          <div className="lg:col-span-7">
            <QuoteFormSection
              config={config}
              defaultService="Abertura de empresa"
              defaultRegime="Empresa nova"
              origemLabel="Landing Page — Abra sua Empresa"
              onAddLead={onAddLead}
              onOpenWhatsApp={onOpenWhatsApp}
            />
          </div>
        </div>
      </section>
    </div>
  );
};

export const TecnologiaPage: React.FC<SharedPageProps> = ({
  onNavigate,
  onOpenWhatsApp
}) => {
  const diferenciaisTecnologicos = [
    {
      num: '01',
      title: 'Atendimento Digital Consultivo',
      desc: 'Comunicação fluida por WhatsApp corporativo, videoconferências e Portal, sem filas e com contadores que conhecem sua empresa.'
    },
    {
      num: '02',
      title: 'Documentos 100% Digitais',
      desc: 'Diga adeus aos malotes físicos. Contratos, notas, extratos e comprovantes são recebidos e arquivados digitalmente com validade jurídica.'
    },
    {
      num: '03',
      title: 'Integração Escritório / Cliente',
      desc: 'Importação automatizada de arquivos XML de notas fiscais e conciliação de extratos bancários OFX sem redigitação manual.'
    },
    {
      num: '04',
      title: 'Acompanhamento de Obrigações',
      desc: 'Rastreabilidade completa de cada obrigação fiscal, contábil e trabalhista entregue ao Fisco Federal, Estadual e Municipal.'
    },
    {
      num: '05',
      title: 'Organização Documental em Nuvem',
      desc: 'Pastas estruturadas por departamento e competência mensal para que você encontre qualquer documento em segundos.'
    },
    {
      num: '06',
      title: 'Acesso Online Multiplataforma',
      desc: 'Consulte guias, balancetes, DRE, férias e folhas de pagamento pelo navegador ou aplicativo móvel a qualquer hora.'
    },
    {
      num: '07',
      title: 'Comunicação Digital Rastreável',
      desc: 'Alertas automáticos de disponibilidade de guias e vencimentos para evitar multas por esquecimento no financeiro.'
    },
    {
      num: '08',
      title: 'Informações Centralizadas para Decisão',
      desc: 'Seus números contábeis transformados em indicadores claros de margem, liquidez e evolução patrimonial.'
    }
  ];

  const ecossistemaSteps = [
    'Atendimento & Diagnóstico',
    'Onboarding Digital',
    'Integração Fiscal & Bancária',
    'Processamento A M',
    'Portal do Cliente Onvio',
    'Relatórios & Decisão'
  ];

  return (
    <div className="space-y-16 pb-16">
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="text-xs text-[#F59E0B] font-semibold">
              Diferencial Tecnológico · Processos Conectados
            </div>
            <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3">
              Tecnologia que simplifica a contabilidade.
            </h1>
            <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
              Na A M Consultoria, a tecnologia não é apenas um discurso visual: ela conecta o financeiro da sua empresa diretamente ao nosso escritório para reduzir burocracia e aumentar a segurança das informações.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <button
                type="button"
                onClick={() => onNavigate('portal-do-cliente')}
                className="px-6 py-3.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors cursor-pointer"
              >
                <Laptop className="w-4 h-4" />
                <span>Explorar o Portal do Cliente</span>
              </button>
              <button
                type="button"
                onClick={() => onOpenWhatsApp()}
                className="px-6 py-3.5 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-sm font-semibold rounded-xl transition-colors cursor-pointer"
              >
                Falar com um especialista
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* 8 Pilares Tecnológicos */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {diferenciaisTecnologicos.map((item) => (
            <div
              key={item.num}
              className="bg-white border border-slate-200 rounded-2xl p-6 space-y-2.5"
            >
              <div className="font-mono text-xs font-semibold text-[#1769AA]">
                {item.num} · Operação Digital
              </div>
              <h2 className="font-display text-lg font-bold text-[#081B33]">
                {item.title}
              </h2>
              <p className="text-sm text-slate-600 leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Ecossistema Digital A M */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-[#081B33] text-white rounded-2xl p-6 sm:p-10 border border-white/10">
          <div className="max-w-2xl">
            <div className="text-xs font-semibold text-[#F59E0B]">
              Fluxo Integrado Ponta a Ponta
            </div>
            <h2 className="font-display text-2xl sm:text-3xl font-bold text-white mt-1">
              O Ecossistema Digital A M Consultoria
            </h2>
            <p className="text-sm text-slate-300 mt-2">
              A contabilidade não precisa ser complicada. Ela precisa ser organizada, inteligente e conectada ao seu negócio.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-4 mt-8">
            {ecossistemaSteps.map((step, idx) => (
              <div
                key={step}
                className="bg-[#0D2544] border border-white/10 rounded-xl p-4 flex flex-col justify-between"
              >
                <span className="font-mono text-xs text-[#F59E0B]">0{idx + 1}</span>
                <span className="font-semibold text-sm text-white mt-2">{step}</span>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export const PortalClientePage: React.FC<SharedPageProps> = ({
  config,
  onNavigate,
  onTrackEvent
}) => {
  const [selectedModule, setSelectedModule] = useState<
    'documentos' | 'guias' | 'relatorios' | 'certidoes' | 'dp' | 'comunicacao'
  >('documentos');

  const portalModules = [
    {
      id: 'documentos',
      title: 'Documentos',
      icon: FolderOpen,
      subtitle: 'Repositório digital criptografado da empresa',
      items: [
        'Documentos contábeis (Livros Diários, Razão e comprovantes)',
        'Documentos fiscais (XMLs de NF-e, NFS-e e arquivos SPED)',
        'Documentos trabalhistas e societários (Contrato Social, cartões CNPJ/IE/IM)',
        'Arquivos enviados pelo cliente ao escritório com protocolo digital',
        'Dashboard executivo de arquivos recentes'
      ],
      sampleRows: [
        { name: 'Contrato_Social_Consolidado_AM.pdf', date: 'Ativo · Permanente', status: 'Disponível' },
        { name: 'Lote_XML_Notas_Fiscais_Setembro_2026.zip', date: '25/09/2026', status: 'Processado' },
        { name: 'Extrato_Bancario_Conciliado_09_2026.ofx', date: '26/09/2026', status: 'Conciliado' }
      ]
    },
    {
      id: 'guias',
      title: 'Guias de Impostos',
      icon: FileText,
      subtitle: 'Tributos disponíveis com antecedência e controle de leitura',
      items: [
        'Guias de impostos federais, estaduais e municipais (DAS, DARF, DARE-AM, DAM Manaus)',
        'Documentos de pagamento com código de barras e PIX Copia e Cola',
        'Histórico completo de disponibilização, visualização e vencimentos'
      ],
      sampleRows: [
        { name: 'DAS — Simples Nacional · Comp. 09/2026', date: 'Venc.: 20/10/2026', status: 'Liberada para Pagamento' },
        { name: 'DARF Unificado DCTFWeb (INSS / IRRF)', date: 'Venc.: 20/10/2026', status: 'Liberada para Pagamento' },
        { name: 'Guia FGTS Digital · Comp. 09/2026', date: 'Venc.: 20/10/2026', status: 'Liberada para Pagamento' }
      ]
    },
    {
      id: 'relatorios',
      title: 'Relatórios Contábeis',
      icon: BarChart3,
      subtitle: 'Demonstrações para bancos, licitações e tomada de decisão',
      items: [
        'Balancetes de verificação mensais e trimestrais',
        'Balanço Patrimonial assinado digitalmente (Ativo, Passivo e Patrimônio Líquido)',
        'Demonstração do Resultado do Exercício (DRE) gerencial e contábil',
        'Relatórios contábeis de evolução de receitas, custos e lucros distribuíveis'
      ],
      sampleRows: [
        { name: 'DRE_Gerencial_e_Analise_Margem_Set2026.pdf', date: 'Fechamento Mensal', status: 'Assinado CRC' },
        { name: 'Balancete_Analitico_3T_2026.pdf', date: 'Trimestral', status: 'Assinado CRC' },
        { name: 'Balanco_Patrimonial_Consolidado.pdf', date: 'Anual / Bancos', status: 'Disponível' }
      ]
    },
    {
      id: 'certidoes',
      title: 'Certidões (CNDs)',
      icon: Award,
      subtitle: 'Monitoramento contínuo da regularidade fiscal do CNPJ',
      items: [
        'Acompanhamento automático de Certidões Negativas de Débitos (CNDs)',
        'Documentos de regularidade Federal (RFB/PGFN), Estadual (SEFAZ-AM) e Municipal (Manaus)',
        'Certidão de Regularidade do FGTS (CRF) e Certidão Negativa de Débitos Trabalhistas (CNDT)'
      ],
      sampleRows: [
        { name: 'CND Conjunta Receita Federal e PGFN', date: 'Válida por 180 dias', status: 'Negativa / Regular' },
        { name: 'CND Estadual SEFAZ Amazonas', date: 'Válida por 30 dias', status: 'Negativa / Regular' },
        { name: 'CND Municipal Prefeitura de Manaus', date: 'Válida por 90 dias', status: 'Negativa / Regular' }
      ]
    },
    {
      id: 'dp',
      title: 'Departamento Pessoal',
      icon: Users,
      subtitle: 'Gestão completa de folha, férias e rotinas trabalhistas',
      items: [
        'Holerites mensais e resumos analíticos da folha de pagamento',
        'Avisos e recibos de férias programadas',
        'Termos de rescisão contratual e guias indenizatórias',
        'Recibos de pró-labore dos sócios e informes anuais de rendimentos (DIRPF)'
      ],
      sampleRows: [
        { name: 'Folha_Analitica_e_Recibos_Setembro_2026.pdf', date: 'Comp. 09/2026', status: 'Liberado' },
        { name: 'Recibo_Pro_Labore_Socios_09_2026.pdf', date: 'Comp. 09/2026', status: 'Liberado' },
        { name: 'Programacao_Ferias_Equipe_4T_2026.pdf', date: 'Preventivo', status: 'Atualizado' }
      ]
    },
    {
      id: 'comunicacao',
      title: 'Comunicação & Agenda',
      icon: Bell,
      subtitle: 'Interação organizada entre sua empresa e nossa equipe',
      items: [
        'Avisos técnicos e comunicados sobre atualizações fiscais',
        'Calendário de vencimentos personalizados do seu CNPJ',
        'Abertura e acompanhamento de solicitações de serviços',
        'Checklist de documentos pendentes para fechamento mensal'
      ],
      sampleRows: [
        { name: 'Comunicado: Envio de Extrato OFX até dia 05/10', date: 'Alerta Automático', status: 'Em dia' },
        { name: 'Solicitação #408: Simulação de Admissão CLT', date: 'Respondido em 42 min', status: 'Concluído' },
        { name: 'Calendário Fiscal Outubro/2026', date: 'Sincronizado', status: 'Ativo' }
      ]
    }
  ] as const;

  const activeData =
    portalModules.find((m) => m.id === selectedModule) || portalModules[0];

  const handleOpenOfficialPortal = () => {
    onTrackEvent('acesso_portal', 'Clique em Acessar Portal do Cliente Oficial (Onvio/Domínio)');
  };

  return (
    <div className="space-y-16 pb-16">
      {/* Header Exclusivo do Portal do Cliente (Seção 17) */}
      <section className="bg-[#081B33] text-white py-14 sm:py-20 border-b border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
            <div className="lg:col-span-7">
              <div className="text-xs text-[#F59E0B] font-semibold">
                Área Exclusiva para Clientes · {config.portalSistemaNome}
              </div>
              <h1 className="font-display text-3xl sm:text-5xl font-bold tracking-tight text-white mt-3">
                Portal do Cliente A M Consultoria
              </h1>
              <p className="text-base sm:text-lg text-slate-300 mt-4 leading-relaxed">
                Acesse seus documentos, informações contábeis e serviços de forma rápida e segura. Seus documentos empresariais protegidos e organizados em um ambiente digital.
              </p>

              <div className="mt-8 flex flex-wrap items-center gap-4">
                <a
                  href={config.portalClienteUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={handleOpenOfficialPortal}
                  className="px-6 py-4 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-sm font-semibold rounded-xl inline-flex items-center gap-2 transition-colors shadow-lg"
                >
                  <Lock className="w-4 h-4" />
                  <span>Acessar Portal do Cliente</span>
                  <ExternalLink className="w-4 h-4" />
                </a>

                <button
                  type="button"
                  onClick={() => onNavigate('orcamento')}
                  className="px-5 py-4 bg-white/10 hover:bg-white/15 text-white border border-white/20 text-sm font-medium rounded-xl transition-colors cursor-pointer"
                >
                  Ainda não sou cliente · Solicitar proposta
                </button>
              </div>
            </div>

            {/* Security Card (Seção 19) */}
            <div className="lg:col-span-5 bg-[#0D2544] border border-white/15 rounded-2xl p-6 space-y-4">
              <div className="flex items-center gap-2.5 text-[#F59E0B] font-semibold text-sm">
                <ShieldCheck className="w-5 h-5" />
                <span>Ambiente Oficial Autenticado & Seguro</span>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed">
                Para garantir máxima proteção cibernética e conformidade com a LGPD, a autenticação ocorre diretamente no ambiente oficial <strong>Domínio / Onvio</strong> com criptografia de ponta a ponta.
              </p>
              <ul className="space-y-2 text-xs text-slate-200 border-t border-white/10 pt-4">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>Conexão criptografada SSL / HTTPS de nível bancário</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>Autenticação direta pelo sistema oficial (sem senhas salvas no site)</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>Controle de permissões por sócio ou departamento financeiro</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>Conformidade integral com a LGPD e sigilo contábil</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Seção 18: Funcionalidades do Portal do Cliente (Visual & Interativo) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mb-8">
          <div className="text-xs font-semibold text-[#1769AA]">
            Tour Visual das Funcionalidades
          </div>
          <h2 className="font-display text-2xl sm:text-3xl font-bold text-[#081B33] mt-1">
            O que sua empresa encontra dentro do Portal do Cliente
          </h2>
          <p className="text-sm text-slate-600 mt-2">
            Selecione abaixo cada módulo para visualizar como organizamos a rotina contábil, fiscal e trabalhista da sua empresa:
          </p>
        </div>

        {/* Module Selector Tabs */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 mb-8">
          {portalModules.map((mod) => {
            const Icon = mod.icon;
            const active = selectedModule === mod.id;
            return (
              <button
                key={mod.id}
                type="button"
                onClick={() => setSelectedModule(mod.id)}
                className={`p-3.5 rounded-xl border text-left transition-colors cursor-pointer flex flex-col justify-between ${
                  active
                    ? 'bg-[#081B33] text-white border-[#081B33]'
                    : 'bg-white text-slate-700 border-slate-200 hover:border-[#1769AA]'
                }`}
              >
                <Icon className={`w-5 h-5 ${active ? 'text-[#F59E0B]' : 'text-[#1769AA]'}`} />
                <span className="text-xs font-semibold mt-2.5 block">{mod.title}</span>
              </button>
            );
          })}
        </div>

        {/* Active Module Interactive Preview */}
        <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div className="lg:col-span-6 space-y-4">
            <div className="text-xs font-semibold text-[#1769AA]">
              Módulo Ativo · Portal Domínio / Onvio
            </div>
            <h3 className="font-display text-2xl font-bold text-[#081B33]">
              {activeData.title}
            </h3>
            <p className="text-sm text-slate-600">{activeData.subtitle}</p>

            <ul className="space-y-2.5 pt-2">
              {activeData.items.map((it) => (
                <li key={it} className="flex items-start gap-2.5 text-sm text-slate-700">
                  <CheckCircle2 className="w-4 h-4 text-[#1769AA] shrink-0 mt-1" />
                  <span>{it}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="lg:col-span-6 bg-[#081B33] text-white rounded-xl p-5 sm:p-6 border border-white/10 space-y-4">
            <div className="flex items-center justify-between border-b border-white/10 pb-3">
              <div>
                <div className="text-xs text-slate-400">Visualização Demonstrativa do Ambiente</div>
                <div className="text-sm font-semibold text-white mt-0.5">
                  Pasta Digital: {activeData.title}
                </div>
              </div>
              <span className="text-xs font-mono text-[#F59E0B]">Criptografia TLS 1.3</span>
            </div>

            <div className="divide-y divide-white/10">
              {activeData.sampleRows.map((row) => (
                <div
                  key={row.name}
                  className="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs"
                >
                  <div>
                    <div className="font-mono text-white font-medium">{row.name}</div>
                    <div className="text-slate-400 mt-0.5">{row.date}</div>
                  </div>
                  <span className="text-emerald-400 font-mono font-medium whitespace-nowrap">
                    {row.status}
                  </span>
                </div>
              ))}
            </div>

            <div className="pt-2 flex items-center justify-between text-xs border-t border-white/10">
              <span className="text-slate-400">Já possui credenciais de cliente A M?</span>
              <a
                href={config.portalClienteUrl}
                target="_blank"
                rel="noopener noreferrer"
                onClick={handleOpenOfficialPortal}
                className="text-[#F59E0B] hover:underline font-semibold inline-flex items-center gap-1"
              >
                <span>Entrar no Portal Oficial</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
