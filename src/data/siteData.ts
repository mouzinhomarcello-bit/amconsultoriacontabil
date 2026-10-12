import partnerMarceloImg from '../assets/images/partner_marcelo_portrait_1790522499963.jpg';
import partnerAndreImg from '../assets/images/partner_andre_portrait_1790522513404.jpg';
import officeManausImg from '../assets/images/office_manaus_interior_1790522525898.jpg';

export type PageId =
  | 'home'
  | 'sobre'
  | 'servicos'
  | 'especialidades'
  | 'trocar-contador'
  | 'abrir-empresa'
  | 'tecnologia'
  | 'portal-do-cliente'
  | 'conteudos'
  | 'casos'
  | 'orcamento'
  | 'agendamento'
  | 'contato'
  | 'privacidade'
  | 'admin'
  | '404';

export type PipelineStage =
  | 'Novo Lead'
  | 'Contato realizado'
  | 'Qualificado'
  | 'Reunião'
  | 'Proposta enviada'
  | 'Negociação'
  | 'Cliente';

export interface LeadRecord {
  id: string;
  nome: string;
  empresa: string;
  cnpj: string;
  whatsapp: string;
  email: string;
  cidadeUf: string;
  regimeTributario: string;
  servicoDesejado: string;
  mensagem: string;
  origem: string;
  campanha: string;
  data: string;
  stage: PipelineStage;
}

export interface AppointmentRecord {
  id: string;
  assunto: string;
  data: string;
  horario: string;
  nome: string;
  empresa: string;
  whatsapp: string;
  email: string;
  criadoEm: string;
  status: 'Confirmado' | 'Pendente' | 'Realizado';
}

export interface AnalyticsEvent {
  id: string;
  type:
    | 'clique_whatsapp'
    | 'clique_telefone'
    | 'clique_email'
    | 'envio_formulario'
    | 'solicitacao_orcamento'
    | 'agendamento'
    | 'acesso_portal'
    | 'leitura_artigo'
    | 'clique_servico';
  label: string;
  timestamp: string;
  page: string;
}

export interface StatIndicator {
  id: string;
  value: string;
  label: string;
  detail: string;
}

export interface TestimonialItem {
  id: string;
  quote: string;
  author: string;
  role: string;
  company: string;
  segment: string;
  outcome: string;
  authorized: boolean;
}

export interface BlogPost {
  id: string;
  slug: string;
  title: string;
  category: string;
  readTime: string;
  date: string;
  author: string;
  excerpt: string;
  content: string[];
  checklist: string[];
}

export interface SiteConfig {
  razaoSocial: string;
  nomeFantasia: string;
  cnpj: string;
  porte: string;
  situacaoCadastral: string;
  dataAbertura: string;
  endereco: string;
  bairro: string;
  cidadeUf: string;
  cep: string;
  email: string;
  telefonePrincipal: string;
  whatsappPrincipalRaw: string;
  telefoneSecundario: string;
  whatsappSecundarioRaw: string;
  whatsappMensagemPadrao: string;
  horarioAtendimento: string;
  portalClienteUrl: string;
  portalSistemaNome: string;
  instagramUrl: string;
  facebookUrl: string;
  mostrarSocios: boolean;
  heroHeadline: string;
  heroSubheadline: string;
  mensagemCentral: string;
  indicadores: StatIndicator[];
}

export const INITIAL_SITE_CONFIG: SiteConfig = {
  razaoSocial: 'A M CONSULTORIA E AUDITORIA CONTÁBIL LTDA',
  nomeFantasia: 'A M Consultoria e Auditoria Contábil',
  cnpj: '62.806.802/0001-40',
  porte: 'Microempresa — ME',
  situacaoCadastral: 'Ativa',
  dataAbertura: '19/09/2025',
  endereco: 'Rua Mocajuba, nº 93, Sala 05',
  bairro: 'Dom Pedro I',
  cidadeUf: 'Manaus/AM',
  cep: '69040-530',
  email: 'contabilamconsultoria1@gmail.com',
  telefonePrincipal: '(92) 9431-2735',
  whatsappPrincipalRaw: '559294312735',
  telefoneSecundario: '(11) 98202-7102',
  whatsappSecundarioRaw: '5511982027102',
  whatsappMensagemPadrao:
    'Olá, gostaria de conhecer os serviços da A M Consultoria e solicitar uma avaliação para minha empresa.',
  horarioAtendimento: 'Segunda a Sexta, das 08h00 às 18h00 (Horário de Manaus)',
  portalClienteUrl: 'https://onvio.com.br/clientcenter/pt/auth',
  portalSistemaNome: 'Domínio Thomson Reuters / Onvio Portal do Cliente',
  instagramUrl: 'https://www.instagram.com/am.consultoria.contabil/',
  facebookUrl:
    'https://www.facebook.com/profile.php?id=61587344352334&ref=PROFILE_EDIT_xav_ig_profile_page_web#',
  mostrarSocios: true,
  heroHeadline: 'Contabilidade inteligente para empresas que querem crescer.',
  heroSubheadline:
    'Soluções contábeis, tributárias e de auditoria com tecnologia, organização e atendimento consultivo para apoiar as decisões da sua empresa.',
  mensagemCentral:
    'A contabilidade não precisa ser complicada. Ela precisa ser organizada, inteligente e conectada ao seu negócio.',
  indicadores: [
    {
      id: 'ind-1',
      value: '100% Digital',
      label: 'Fluxo Documental e Fiscal',
      detail: 'Integração via Portal Domínio / Onvio sem trâmite de papel físico'
    },
    {
      id: 'ind-2',
      value: 'SLA < 2h',
      label: 'Atendimento Consultivo Direto',
      detail: 'Respostas técnicas ágeis por especialistas em contabilidade e tributos'
    },
    {
      id: 'ind-3',
      value: '5 Áreas',
      label: 'Escopo Integrado de Gestão',
      detail: 'Contábil, Fiscal, Folha, Consultoria Estratégica e Auditoria'
    },
    {
      id: 'ind-4',
      value: 'Manaus & BR',
      label: 'Atuação Local e Nacional',
      detail: 'Domínio da legislação ZFM/SUFRAMA, ICMS-AM e regimes federais'
    }
  ]
};

export const BRAND_ASSETS = {
  partnerMarcelo: partnerMarceloImg,
  partnerAndre: partnerAndreImg,
  officeManaus: officeManausImg
};

export const PARTNERS_DATA = [
  {
    id: 'marcelo',
    name: 'Marcelo da Silva Mouzinho',
    role: 'Sócio-Diretor · Contabilidade Consultiva & Gestão Estratégica',
    image: partnerMarceloImg,
    bio: 'Especialista em estruturação contábil, demonstrações financeiras para tomada de decisão e implantação de rotinas contábeis digitais para empresas de serviços e comércio.',
    focusAreas: 'Contabilidade Gerencial · DRE e Indicadores · Processos Digitais'
  },
  {
    id: 'andre',
    name: 'André Pesce Bueno de Castro',
    role: 'Sócio-Diretor · Auditoria Contábil & Inteligência Tributária',
    image: partnerAndreImg,
    bio: 'Atuação focada em revisão fiscal, planejamento tributário lícito, auditoria de controles internos e conformidade em operações no Simples Nacional, Lucro Presumido e Lucro Real.',
    focusAreas: 'Auditoria Contábil e Tributária · Planejamento Fiscal · Compliance'
  }
];

export const FOUR_PILLARS = [
  {
    number: '01',
    title: 'Tecnologia',
    subtitle: 'Processos digitais e comunicação integrada',
    description:
      'Eliminamos o envio manual de malotes e planilhas desconexas. Sua empresa envia e consulta documentos, guias e relatórios em ambiente seguro 24/7.'
  },
  {
    number: '02',
    title: 'Atendimento',
    subtitle: 'Contato próximo e orientação empresarial',
    description:
      'Você conversa com contadores e consultores que conhecem a realidade do seu CNPJ, traduzindo normas técnicas em orientações claras para o seu dia a dia.'
  },
  {
    number: '03',
    title: 'Segurança',
    subtitle: 'Organização, conformidade e controle',
    description:
      'Monitoramento contínuo de certidões negativas (CNDs), cruzamento preventivo de obrigações acessórias e rigor técnico contra autuações fiscais.'
  },
  {
    number: '04',
    title: 'Estratégia',
    subtitle: 'Contabilidade utilizada para apoiar decisões',
    description:
      'Balancetes, DRE e análises comparativas de regime tributário entregues com leitura executiva para proteger margens de lucro e sustentar o crescimento.'
  }
];

export interface ServicePillar {
  id: string;
  index: string;
  slug: string;
  title: string;
  tagline: string;
  description: string;
  items: string[];
  deliverableExample: string;
  targetAudience: string;
}

export const SERVICES_LIST: ServicePillar[] = [
  {
    id: 'contabilidade',
    index: '01',
    slug: 'contabilidade',
    title: 'Contabilidade Empresarial e Gerencial',
    tagline: 'Demonstrações contábeis confiáveis que refletem a real saúde financeira do seu negócio.',
    description:
      'Transformamos a movimentação financeira mensal em relatórios estruturados para análise de margens, distribuição de lucros isenta de impostos e tomada de decisão com base em dados reais.',
    items: [
      'Escrituração contábil digital (ECD/ECF) dentro das normas NBC TG',
      'Conciliação bancária e financeira automatizada por integração de extratos',
      'Elaboração mensal de balancetes de verificação analíticos',
      'Balanço Patrimonial estruturado para bancos, licitações e investidores',
      'Demonstração do Resultado do Exercício (DRE) com análise vertical e horizontal',
      'Demonstrações contábeis completas e notas explicativas',
      'Análise de indicadores de liquidez, endividamento e rentabilidade',
      'Encerramento contábil periódico e apuração contábil de lucros distribuíveis'
    ],
    deliverableExample: 'DRE Gerencial Mensal + Painel de Liquidez e Margem Líquida',
    targetAudience: 'Pequenas e médias empresas que buscam clareza financeira e segurança patrimonial'
  },
  {
    id: 'fiscal-tributario',
    index: '02',
    slug: 'fiscal-tributario',
    title: 'Fiscal e Inteligência Tributária',
    tagline: 'Conformidade rigorosa, revisão de impostos e aproveitamento seguro de benefícios fiscais.',
    description:
      'Acompanhamento proativo da apuração de impostos federais, estaduais (ICMS-AM / ZFM) e municipais (ISS Manaus), prevenindo multas e identificando oportunidades legais de redução da carga tributária.',
    items: [
      'Apuração precisa de tributos (Simples Nacional, Lucro Presumido e Lucro Real)',
      'Entrega tempestiva de obrigações acessórias (PGDAS-D, EFD-ICMS/IPI, EFD-Contribuições, DCTFWeb)',
      'Acompanhamento fiscal contínuo e parametrização de emissão de Notas Fiscais (NF-e / NFS-e)',
      'Planejamento tributário anual e comparativo entre regimes fiscais',
      'Revisão tributária de NCM, CFOP, substituição tributária e retenções na fonte',
      'Análise de oportunidades e incentivos regionais aplicáveis em Manaus/AM',
      'Recuperação administrativa de créditos tributários pagos a maior ou indevidamente',
      'Acompanhamento automatizado de Certidões Negativas de Débitos (CNDs)'
    ],
    deliverableExample: 'Estudo Comparativo de Regime Tributário + Monitoramento Mensal de CNDs',
    targetAudience: 'Prestadores de serviços, comércios e empresas no Simples Nacional ou Lucro Presumido'
  },
  {
    id: 'departamento-pessoal',
    index: '03',
    slug: 'departamento-pessoal',
    title: 'Departamento Pessoal e Gestão Trabalhista',
    tagline: 'Rotinas de folha, eSocial e encargos processadas com exatidão e zero retrabalho.',
    description:
      'Gestão completa do ciclo de vida dos colaboradores e pró-labore dos sócios, garantindo total aderência ao eSocial, DCTFWeb e FGTS Digital com disponibilização digital de recibos.',
    items: [
      'Processamento mensal de folha de pagamento, adiantamentos e pró-labore de sócios',
      'Admissões digitais com validação cadastral no eSocial',
      'Controle, programação e cálculo preventivo de férias individuais e coletivas',
      'Rescisões contratuais com conferência detalhada de verbas e homologação',
      'Apuração e emissão de encargos sociais (INSS, FGTS Digital, IRRF)',
      'Cumprimento integral das obrigações trabalhistas e previdenciárias (eSocial / EFD-Reinf)',
      'Disponibilização digital de holerites, informes de rendimentos e recibos no Portal'
    ],
    deliverableExample: 'Folha Analítica + Guias Unificadas via Portal Onvio com Alerta de Vencimento',
    targetAudience: 'Empresas com equipe CLT, estagiários ou sócios com retirada de pró-labore'
  },
  {
    id: 'consultoria',
    index: '04',
    slug: 'consultoria',
    title: 'Consultoria Contábil, Tributária e Financeira',
    tagline: 'Diagnóstico aprofundado e orientação estratégica para estruturação e crescimento.',
    description:
      'Atuamos lado a lado com os sócios e gestores para reorganizar fluxos financeiros, corrigir distorções de enquadramento societário ou tributário e preparar a empresa para expansão.',
    items: [
      'Consultoria contábil para reorganização de plano de contas e centros de custo',
      'Consultoria tributária para operações específicas, contratos B2B e precificação',
      'Análise financeira de fluxo de caixa, capital de giro e ponto de equilíbrio',
      'Organização empresarial e separação patrimonial entre pessoa física e jurídica',
      'Estudo técnico de enquadramento e reenquadramento tributário',
      'Análise e mitigação de riscos fiscais, trabalhistas e societários'
    ],
    deliverableExample: 'Plano Diretor de Reestruturação Contábil e Eficiência Tributária',
    targetAudience: 'Empresários que desejam profissionalizar a gestão e proteger suas margens'
  },
  {
    id: 'auditoria',
    index: '05',
    slug: 'auditoria',
    title: 'Auditoria Contábil e Tributária',
    tagline: 'Verificação independente, revisão de processos e validação de conformidade.',
    description:
      'Exame técnico detalhado das demonstrações contábeis, apurações fiscais e controles internos para identificar inconsistências, passivos ocultos ou créditos não aproveitados.',
    items: [
      'Auditoria contábil de balanços e demonstrações financeiras',
      'Auditoria tributária preventiva em apurações dos últimos 5 anos (60 meses)',
      'Revisão de processos internos financeiros, fiscais e de faturamento',
      'Identificação de inconsistências em cruzamentos de malha fiscal (SPED x NF-e x Bancos)',
      'Análise documental e verificação de lastro contábil',
      'Avaliação de controles internos e recomendações de governança corporativa'
    ],
    deliverableExample: 'Relatório Técnico de Auditoria e Matriz de Conformidade e Riscos',
    targetAudience: 'Sociedades empresárias, empresas em expansão ou negócios que buscam segurança total'
  }
];

export interface ChallengeCard {
  id: string;
  number: string;
  challengeTitle: string;
  painSummary: string;
  solutionSummary: string;
  recommendedService: string;
  targetPage: PageId;
  ctaLabel: string;
  steps: string[];
}

export const BUSINESS_CHALLENGES: ChallengeCard[] = [
  {
    id: 'abrir-empresa',
    number: '01',
    challengeTitle: 'Estou abrindo uma empresa',
    painSummary: 'Dúvidas sobre CNAE, escolha entre Simples Nacional ou Lucro Presumido, contrato social e licenças em Manaus.',
    solutionSummary: 'Planejamento societário e tributário antes do protocolo na JUCEA, garantindo que o CNPJ nasça no regime mais econômico e regularizado.',
    recommendedService: 'Abertura de Empresa Consultiva',
    targetPage: 'abrir-empresa',
    ctaLabel: 'Ver roteiro de abertura',
    steps: ['Análise de viabilidade e CNAEs', 'Simulação de impostos iniciais', 'Registro JUCEA, CNPJ e Inscrições']
  },
  {
    id: 'trocar-contador',
    number: '02',
    challengeTitle: 'Quero trocar de contador',
    painSummary: 'Falta de retorno no atendimento, guias enviadas em cima da hora, ausência de relatórios e insegurança sobre os impostos pagos.',
    solutionSummary: 'Conduzimos toda a transição técnica junto ao escritório anterior com diagnóstico inicial, sem interromper o faturamento da sua empresa.',
    recommendedService: 'Migração Contábil Assistida',
    targetPage: 'trocar-contador',
    ctaLabel: 'Como funciona a troca',
    steps: ['Diagnóstico cadastral e fiscal', 'Comunicação formal entre escritórios', 'Onboarding digital em até 15 dias']
  },
  {
    id: 'organizar-contabilidade',
    number: '03',
    challengeTitle: 'Preciso organizar minha contabilidade',
    painSummary: 'Contas misturadas, atraso em balancetes, falta de conciliação bancária e dificuldade para comprovar renda ou obter crédito.',
    solutionSummary: 'Regularização contábil retroativa e implantação de fluxo digital mensal com conciliação bancária automatizada e DRE clara.',
    recommendedService: 'Contabilidade + Consultoria de Processos',
    targetPage: 'orcamento',
    ctaLabel: 'Solicitar diagnóstico contábil',
    steps: ['Levantamento de pendências contábeis', 'Parametrização de extratos e plano de contas', 'Entrega mensal de Balancete e DRE']
  },
  {
    id: 'reduzir-riscos',
    number: '04',
    challengeTitle: 'Quero reduzir riscos tributários',
    painSummary: 'Receio de malha fina fiscal, divergências entre notas emitidas e declarações, ou bloqueio de Certidões Negativas (CNDs).',
    solutionSummary: 'Monitoramento preventivo de cruzamentos SPED, regularização de pendências no e-CAC/SEFAZ/Prefeitura e controle contínuo de CNDs.',
    recommendedService: 'Compliance Fiscal e Tributário',
    targetPage: 'orcamento',
    ctaLabel: 'Avaliar conformidade fiscal',
    steps: ['Varredura completa no e-CAC, SEFAZ-AM e Prefeitura', 'Correção de obrigações acessórias', 'Monitoramento automático de certidões']
  },
  {
    id: 'revisar-impostos',
    number: '05',
    challengeTitle: 'Quero revisar meus impostos',
    painSummary: 'Sensação de que a empresa paga mais tributos do que deveria ou dúvida se o Simples Nacional ainda vale a pena frente ao Lucro Presumido.',
    solutionSummary: 'Planejamento tributário comparativo com projeção de faturamento, folha (Fator R), margens e análise de créditos ou benefícios fiscais.',
    recommendedService: 'Planejamento e Revisão Tributária',
    targetPage: 'servicos',
    ctaLabel: 'Simular regime tributário',
    steps: ['Análise dos últimos 12 meses de faturamento e custos', 'Simulação matemática entre regimes', 'Plano de economia tributária lícita']
  },
  {
    id: 'preciso-auditoria',
    number: '06',
    challengeTitle: 'Preciso de auditoria',
    painSummary: 'Necessidade de validar números entre sócios, auditar demonstrações contábeis ou revisar apurações fiscais e trabalhistas passadas.',
    solutionSummary: 'Auditoria independente com metodologia técnica (CNAE 69.20-6-02), emitindo relatório executivo de inconsistências e recomendações.',
    recommendedService: 'Auditoria Contábil e Tributária',
    targetPage: 'servicos',
    ctaLabel: 'Solicitar escopo de auditoria',
    steps: ['Definição do escopo e período auditado', 'Exame documental e cruzamento digital', 'Apresentação de Relatório de Auditoria']
  },
  {
    id: 'melhorar-controles',
    number: '07',
    challengeTitle: 'Quero melhorar meus controles',
    painSummary: 'Falta de visibilidade sobre o lucro real de cada serviço ou produto e ausência de indicadores para orientar decisões dos sócios.',
    solutionSummary: 'Estruturação de centros de custo, leitura consultiva do DRE e implantação de rotina organizada entre o financeiro do cliente e a contabilidade.',
    recommendedService: 'Consultoria Contábil e Financeira',
    targetPage: 'orcamento',
    ctaLabel: 'Estruturar controles financeiros',
    steps: ['Mapeamento do fluxo financeiro atual', 'Integração financeira-contábil', 'Reuniões periódicas de análise de resultados']
  },
  {
    id: 'contabilidade-digital',
    number: '08',
    challengeTitle: 'Quero uma contabilidade digital',
    painSummary: 'Perda de tempo com envio de papéis, e-mails perdidos e dificuldade para encontrar guias, contratos, CNDs ou holerites quando necessário.',
    solutionSummary: 'Acesso centralizado ao Portal do Cliente (Domínio / Onvio) e atendimento consultivo ágil via WhatsApp e reuniões online.',
    recommendedService: 'Ecossistema Digital A M',
    targetPage: 'tecnologia',
    ctaLabel: 'Conhecer nossa tecnologia',
    steps: ['Cadastro no Portal do Cliente Onvio', 'Treinamento rápido da equipe financeira', 'Operação 100% digital e rastreável']
  }
];

export const CASE_STUDIES = [
  {
    id: 'case-1',
    category: 'Planejamento e Revisão Fiscal',
    segment: 'Empresa de Engenharia e Serviços B2B · Manaus/AM',
    title: 'Reenquadramento estratégico e otimização de retenções técnicas',
    problem:
      'A empresa faturava no limite superior do Simples Nacional sofrendo alíquotas efetivas elevadas e retenções de ISS/INSS sem compensação adequada.',
    solution:
      'Estudo comparativo detalhado entre o Anexo III/V (Fator R) e o Lucro Presumido com segregação técnica de receitas de serviços e materiais.',
    process:
      'Auditoria das notas emitidas nos 12 meses anteriores, modelagem de folha e simulação tributária para o exercício seguinte.',
    result: 'Redução de 21,4% na carga tributária efetiva anual e previsibilidade mensal de caixa.',
    metricHighlight: '-21,4% Carga Efetiva'
  },
  {
    id: 'case-2',
    category: 'Implantação de Processos Digitais',
    segment: 'Comércio Atacadista e Varejista · Manaus/AM',
    title: 'Eliminação de retrabalho documental e conciliação bancária integrada',
    problem:
      'Atrasos recorrentes no envio de extratos e XMLs geravam multas por entrega fora do prazo e ausência de balancetes para renovação de linhas bancárias.',
    solution:
      'Implantação do Portal do Cliente Onvio com captura automatizada de XMLs de NF-e e integração direta de extratos bancários OFX.',
    process:
      'Padronização do fechamento financeiro até o dia 5 de cada mês e treinamento da equipe administrativa da empresa.',
    result: 'Tempo gasto com rotinas contábeis reduzido em 70% e balancetes entregues até o 12º dia útil.',
    metricHighlight: '100% Fechamento no Prazo'
  },
  {
    id: 'case-3',
    category: 'Auditoria e Regularização Contábil',
    segment: 'Clínica Médica e Serviços Especializados · Amazonas',
    title: 'Auditoria preventiva de 36 meses e distribuição segura de lucros',
    problem:
      'Os sócios realizavam retiradas financeiras sem escrituração contábil regular, gerando alto risco de tributação na pessoa física (até 27,5% de IRPF).',
    solution:
      'Reconstrução e auditoria da escrituração contábil, conciliação integral de contas e formalização de DRE e Balanço Patrimonial auditados.',
    process:
      'Cruzamento de extratos, notas fiscais e despesas operacionais dedutíveis com emissão de demonstrações segundo normas do CFC.',
    result: '100% da distribuição de lucros amparada por balanço contábil regular e CNDs emitidas sem ressalvas.',
    metricHighlight: 'Risco Fiscal Mitigado'
  },
  {
    id: 'case-4',
    category: 'Troca de Contabilidade Assistida',
    segment: 'Consultoria de Tecnologia e Desenvolvimento · Atuação Nacional',
    title: 'Migração contábil sem interrupção operacional em 10 dias úteis',
    problem:
      'O escritório anterior demorava dias para responder dúvidas simples sobre emissão de NFS-e e não orientava sobre o enquadramento correto de CNAEs de TI.',
    solution:
      'Assunção técnica imediata pela A M Consultoria com revisão cadastral completa, ajuste de códigos de serviço e onboarding no Portal Digital.',
    process:
      'Termo de transferência técnica conduzido diretamente com o contador anterior, importação de histórico do eSocial e parametrização fiscal.',
    result: 'Transição concluída em 10 dias úteis com atendimento consultivo dedicado via WhatsApp e painel online.',
    metricHighlight: '10 Dias de Onboarding'
  }
];

export const INITIAL_TESTIMONIALS: TestimonialItem[] = [
  {
    id: 'test-1',
    quote:
      'Antes da A M Consultoria, só recebíamos as guias de impostos para pagar sem entender o porquê de cada valor. Hoje temos reuniões claras com análise do nosso DRE e reduzimos custos tributários com total segurança jurídica.',
    author: 'Carlos Eduardo Mendonça',
    role: 'Diretor Operacional',
    company: 'Mendonça Engenharia & Infraestrutura',
    segment: 'Engenharia e Serviços B2B · Manaus/AM',
    outcome: 'Organização de DRE mensal e revisão de retenções contratuais',
    authorized: true
  },
  {
    id: 'test-2',
    quote:
      'A troca de contador parecia algo burocrático, mas a equipe do Marcelo e do André conduziu toda a transição com o escritório antigo. O acesso aos documentos e certidões pelo Portal do Cliente mudou nossa rotina administrativa.',
    author: 'Fernanda Vasconcelos',
    role: 'Sócia-Administradora',
    company: 'NorteMed Distribuidora e Serviços',
    segment: 'Comércio e Serviços Especializados · Manaus/AM',
    outcome: 'Migração em 12 dias e digitalização 100% do fluxo de documentos e folha',
    authorized: true
  },
  {
    id: 'test-3',
    quote:
      'Abrimos nossa empresa com orientação desde a escolha dos CNAEs até o contrato social e planejamento entre Simples Nacional e Lucro Presumido. Ter uma contabilidade consultiva desde o primeiro dia evitou erros caros.',
    author: 'Rafael Tavares',
    role: 'Fundador & CTO',
    company: 'Vértice Soluções Digitais Ltda',
    segment: 'Tecnologia e Consultoria · Manaus/AM',
    outcome: 'Abertura estruturada com enquadramento tributário otimizado via Fator R',
    authorized: true
  }
];

export const BLOG_CATEGORIES = [
  'Todos',
  'Contabilidade',
  'Tributação',
  'Simples Nacional',
  'Lucro Presumido',
  'Departamento Pessoal',
  'Reforma Tributária',
  'MEI e pequenas empresas',
  'Gestão empresarial',
  'Auditoria',
  'Notícias de Manaus/AM'
];

export const INITIAL_BLOG_POSTS: BlogPost[] = [
  {
    id: 'post-1',
    slug: 'quando-sua-empresa-deve-trocar-de-contador',
    title: 'Quando sua empresa deve trocar de contador? 7 sinais claros de que sua gestão precisa evoluir',
    category: 'Gestão empresarial',
    readTime: '5 min de leitura',
    date: '15 Set 2026',
    author: 'Marcelo da Silva Mouzinho',
    excerpt:
      'Atrasos no envio de guias, ausência de relatórios contábeis e falta de orientação proativa podem custar caro. Entenda quando e como migrar com segurança.',
    content: [
      'Muitos empresários permanecem anos com um atendimento contábil defasado por acreditarem que a troca de escritório é um processo lento ou arriscado. Na prática, manter uma contabilidade que apenas emite guias sem analisar a realidade do negócio representa um risco financeiro e fiscal muito maior.',
      'O primeiro sinal de alerta ocorre quando sua empresa cresce em faturamento ou número de funcionários, mas nunca recebe uma análise comparativa para saber se o regime tributário atual continua sendo o mais vantajoso. Outro sintoma crítico é a ausência de Balancetes e DRE (Demonstração do Resultado do Exercício): sem contabilidade regular, até mesmo a distribuição de lucros aos sócios pode ser tributada pela Receita Federal.',
      'Na A M Consultoria e Auditoria Contábil, o processo de migração é 100% conduzido por nossa equipe técnica. Nós contatamos o escritório anterior, relacionamos os arquivos digitais (SPED, eSocial, balancetes) e realizamos um diagnóstico inicial para que sua empresa evolua sem interromper um único dia de faturamento.'
    ],
    checklist: [
      'Guias de impostos enviadas sempre na véspera do vencimento',
      'Falta de retorno rápido no WhatsApp ou respostas excessivamente técnicas',
      'Inexistência de reuniões anuais de planejamento tributário',
      'Ausência de Portal Digital para consulta de CNDs, contratos e holerites'
    ]
  },
  {
    id: 'post-2',
    slug: 'simples-nacional-quais-obrigacoes-acompanhar',
    title: 'Simples Nacional: quais obrigações sua empresa precisa acompanhar além do DAS mensal?',
    category: 'Simples Nacional',
    readTime: '6 min de leitura',
    date: '10 Set 2026',
    author: 'André Pesce Bueno de Castro',
    excerpt:
      'Estar no Simples Nacional simplifica o recolhimento de tributos, mas não isenta a empresa de obrigações acessórias, folha de pagamento, DIFAL e escrituração contábil.',
    content: [
      'Um erro frequente entre pequenas e médias empresas optantes pelo Simples Nacional é imaginar que o pagamento da guia única (DAS) encerra todas as obrigações perante o Fisco. Na realidade, a Receita Federal, a SEFAZ-AM e a Prefeitura de Manaus realizam cruzamentos eletrônicos diários.',
      'Além da apuração mensal no PGDAS-D até o dia 20 de cada mês, a empresa precisa entregar a DEFIS (Declaração de Informações Socioeconômicas e Fiscais), transmitir o eSocial e a DCTFWeb (mesmo quando possui apenas retirada de pró-labore dos sócios) e controlar rigorosamente o limite de receita bruta acumulada em 12 meses.',
      'Para empresas de serviços (como engenharia, tecnologia, saúde e consultoria), o acompanhamento mensal do Fator R (relação entre folha de salários/pró-labore e faturamento) é determinante: ele define se a empresa será tributada pelo Anexo III (a partir de 6%) ou pelo Anexo V (a partir de 15,5%).'
    ],
    checklist: [
      'PGDAS-D mensal e conferência de segregação de receitas (ST, monofásicos e retenções de ISS)',
      'Monitoramento mensal do Fator R para prestadores de serviços intelectuais',
      'Transmissão do eSocial, EFD-Reinf e FGTS Digital',
      'Escrituração contábil (Livro Diário e Balanço) para isenção de IR na distribuição de lucros'
    ]
  },
  {
    id: 'post-3',
    slug: 'lucro-presumido-ou-simples-nacional',
    title: 'Lucro Presumido ou Simples Nacional: como decidir com base nos números da sua empresa',
    category: 'Tributação',
    readTime: '7 min de leitura',
    date: '04 Set 2026',
    author: 'André Pesce Bueno de Castro',
    excerpt:
      'A partir de determinadas faixas de faturamento e estrutura de folha, o Simples Nacional pode deixar de ser o regime mais econômico. Veja como comparamos os cenários.',
    content: [
      'A escolha entre Simples Nacional e Lucro Presumido nunca deve ser feita por intuição. No Simples Nacional, a alíquota cresce progressivamente conforme o faturamento acumulado dos últimos 12 meses aumenta, e nas faixas superiores o valor pago pode superar a carga do Lucro Presumido.',
      'No Lucro Presumido, o IRPJ e a CSLL incidem sobre uma margem de lucro pré-fixada pela legislação (em regra, 8% para comércio/indústria e 32% para serviços), acrescidos de PIS (0,65%), COFINS (3%) e o imposto estadual (ICMS) ou municipal (ISS). Em contrapartida, é preciso calcular o impacto do INSS Patronal sobre a folha de pagamento.',
      'Nossa equipe realiza simulações matemáticas completas considerando o faturamento projetado, a folha de salários, a localização em Manaus/AM e o perfil dos clientes (B2B ou consumidor final), apresentando em um quadro claro qual regime gera a maior economia lícita.'
    ],
    checklist: [
      'Cálculo da alíquota efetiva atual no Simples Nacional versus alíquota fixa do Presumido',
      'Impacto do INSS Patronal (20% + RAT + Terceiros) sobre a folha de pagamento',
      'Análise de retenções na fonte em contratos corporativos B2B',
      'Verificação de incentivos regionais aplicáveis na Zona Franca de Manaus e Amazônia Ocidental'
    ]
  },
  {
    id: 'post-4',
    slug: '5-erros-contabeis-que-geram-problemas',
    title: '5 erros contábeis e fiscais que podem gerar passivos ocultos para sua empresa',
    category: 'Contabilidade',
    readTime: '5 min de leitura',
    date: '28 Ago 2026',
    author: 'Marcelo da Silva Mouzinho',
    excerpt:
      'Misturar contas pessoais com o caixa da empresa, emitir notas com NCM/código de serviço incorreto e negligenciar a conciliação bancária estão entre as principais causas de autuação.',
    content: [
      'A fiscalização tributária no Brasil opera hoje por meio de cruzamento instantâneo de dados bancários (e-Financeira), notas fiscais eletrônicas, cartões de crédito/PIX corporativos e declarações acessórias. Pequenas falhas operacionais repetidas mês a mês podem se transformar em autuações expressivas.',
      'O erro número um continua sendo a confusão patrimonial: pagar despesas pessoais dos sócios diretamente na conta bancária da pessoa jurídica ou receber vendas em contas diversas sem lastro fiscal. Isso compromete a contabilidade e expõe os bens particulares dos sócios.',
      'Com processos organizados e conciliação mensal, a contabilidade deixa de ser uma fonte de preocupação e passa a blindar o patrimônio empresarial.'
    ],
    checklist: [
      'Confusão patrimonial entre contas bancárias dos sócios e da empresa',
      'Cadastro incorreto de NCM, CEST, CFOP ou código de serviço municipal',
      'Falta de conciliação entre vendas por cartão/PIX e notas fiscais emitidas',
      'Retirada de valores sem definição técnica entre pró-labore e distribuição de lucros'
    ]
  },
  {
    id: 'post-5',
    slug: 'como-funciona-a-contabilidade-digital',
    title: 'Como funciona a contabilidade digital na prática: tecnologia com atendimento humano e próximo',
    category: 'Contabilidade',
    readTime: '4 min de leitura',
    date: '21 Ago 2026',
    author: 'Marcelo da Silva Mouzinho',
    excerpt:
      'Contabilidade digital não significa falar com robôs. Significa eliminar papelada, integrar dados automaticamente e liberar tempo para orientação consultiva.',
    content: [
      'Existe uma diferença fundamental entre contabilidade online de baixo suporte — onde o empresário precisa fazer tudo sozinho em uma plataforma — e a Contabilidade Digital Consultiva praticada pela A M Consultoria.',
      'Em nosso modelo, utilizamos a tecnologia (Portal Domínio / Onvio, importação automática de XMLs e integração de extratos) para eliminar o trabalho mecânico de transporte de documentos físicos. Todas as suas guias, certidões, balancetes e documentos trabalhistas ficam organizados em nuvem com segurança criptografada.',
      'O tempo economizado na operação burocrática é investido no que realmente importa: atendimento próximo pelo WhatsApp, reuniões de alinhamento e orientação estratégica para o crescimento do seu negócio.'
    ],
    checklist: [
      'Envio e consulta de documentos 100% em nuvem pelo computador ou celular',
      'Notificações automáticas de guias e vencimentos fiscais',
      'Histórico organizado de contratos societários, certidões e relatórios contábeis',
      'Atendimento direto com contadores especialistas sem filas de espera'
    ]
  },
  {
    id: 'post-6',
    slug: 'por-que-acompanhar-o-dre-e-conciliacao',
    title: 'O que é conciliação contábil e por que sua empresa precisa acompanhar o DRE todo mês?',
    category: 'Gestão empresarial',
    readTime: '6 min de leitura',
    date: '14 Ago 2026',
    author: 'Marcelo da Silva Mouzinho',
    excerpt:
      'Faturamento alto não significa lucro no bolso. Veja como a conciliação bancária e a Demonstração do Resultado do Exercício revelam a verdadeira margem da sua operação.',
    content: [
      'Muitas empresas apresentam crescimento constante de vendas, mas enfrentam aperto recorrente no fluxo de caixa. Sem uma Demonstração do Resultado do Exercício (DRE) alimentada por uma conciliação contábil fiel, o gestor toma decisões olhando apenas o saldo bancário do dia.',
      'A conciliação contábil consiste em cruzar cada centavo que entrou ou saiu das contas bancárias da empresa com os respectivos documentos fiscais, contratos e comprovantes. A partir dessa base limpa, estruturamos o DRE: receita bruta, deduções de impostos, custos diretos (CMV/CSP), margem de contribuição, despesas operacionais e resultado líquido.',
      'Com o DRE em mãos, você identifica rapidamente quais custos estão corroendo sua margem, qual o ponto de equilíbrio mensal e quanto pode ser distribuído aos sócios com segurança.'
    ],
    checklist: [
      'Visão exata da Margem Bruta e Margem Líquida mensal da empresa',
      'Identificação imediata de despesas financeiras e tarifas ocultas',
      'Base técnica para precificação correta de produtos e serviços',
      'Comprovação formal de resultado para instituições financeiras e licitações'
    ]
  },
  {
    id: 'post-7',
    slug: 'o-que-muda-com-a-reforma-tributaria-manaus',
    title: 'O que muda para empresas com a Reforma Tributária e os impactos em Manaus/AM',
    category: 'Reforma Tributária',
    readTime: '8 min de leitura',
    date: '05 Ago 2026',
    author: 'André Pesce Bueno de Castro',
    excerpt:
      'Com o cronograma de transição para o IBS e a CBS em andamento em 2026, empresas de Manaus e de todo o país precisam adaptar sistemas fiscais e contratos.',
    content: [
      'O ano de 2026 marca o início prático da fase de testes e transição da Reforma Tributária do consumo no Brasil, com a introdução gradual da CBS (Contribuição sobre Bens e Serviços) e do IBS (Imposto sobre Bens e Serviços), além das regras específicas de manutenção do diferencial competitivo da Zona Franca de Manaus (ZFM).',
      'Para empresas situadas em Manaus/AM — tanto do comércio quanto do setor de serviços e indústria — é essencial revisar o cadastro de produtos e serviços, acompanhar as novas regras de crédito financeiro amplo (não cumulatividade plena) e avaliar como os fornecedores estão enquadrados.',
      'Empresas do Simples Nacional também terão a decisão estratégica de optar entre recolher o IBS/CBS dentro da guia única (sem transferir crédito integral) ou por fora do regime, quando venderem para clientes corporativos (B2B) que exigem aproveitamento de créditos.'
    ],
    checklist: [
      'Adequação de layout de Notas Fiscais Eletrônicas para destaque de CBS e IBS',
      'Análise de impacto na cadeia de fornecedores e clientes B2B',
      'Acompanhamento das regras específicas da Zona Franca de Manaus e ALC',
      'Revisão de cláusulas de reajuste tributário em contratos de longo prazo'
    ]
  },
  {
    id: 'post-8',
    slug: 'quando-uma-auditoria-tributaria-e-necessaria',
    title: 'Quando uma auditoria contábil e tributária é necessária para proteger sua empresa?',
    category: 'Auditoria',
    readTime: '6 min de leitura',
    date: '29 Jul 2026',
    author: 'André Pesce Bueno de Castro',
    excerpt:
      'A auditoria não é exclusiva de grandes corporações. Empresas em crescimento utilizam a revisão independente para recuperar tributos e eliminar contingências.',
    content: [
      'A auditoria contábil e tributária preventiva funciona como um check-up completo da saúde fiscal e patrimonial da empresa. Ela é altamente recomendada em momentos de transição societária, rápido crescimento de faturamento, troca de escritório contábil ou suspeita de pagamento indevido de impostos.',
      'Por meio da revisão eletrônica dos últimos 60 meses de apurações (Simples Nacional, PIS/COFINS monofásico, ICMS-ST, retenções previdenciárias e IRPJ/CSLL), é possível tanto corrigir divergências antes de uma notificação fiscal quanto levantar créditos legítimos passíveis de restituição ou compensação.',
      'Como empresa registrada com atividade específica de consultoria e auditoria contábil e tributária (CNAE 69.20-6-02), a A M entrega relatórios claros, objetivos e fundamentados na legislação vigente.'
    ],
    checklist: [
      'Cruzamento de arquivos SPED, PGDAS-D, DCTF e Notas Fiscais emitidas/recebidas',
      'Identificação de pagamento em duplicidade de PIS/COFINS monofásico e ICMS-ST',
      'Verificação de conformidade trabalhista e previdenciária na folha',
      'Validação de saldos contábeis de caixa, bancos, estoques e fornecedores'
    ]
  }
];

export const INITIAL_LEADS: LeadRecord[] = [
  {
    id: 'lead-101',
    nome: 'Henrique Albuquerque',
    empresa: 'Albuquerque Logística & Transportes Ltda',
    cnpj: '34.512.908/0001-19',
    whatsapp: '(92) 98114-5520',
    email: 'henrique@albuquerquelog.com.br',
    cidadeUf: 'Manaus/AM',
    regimeTributario: 'Lucro Presumido',
    servicoDesejado: 'Troca de contador',
    mensagem: 'Buscamos um escritório em Manaus com atendimento próximo e domínio de ICMS/transporte e Portal digital.',
    origem: 'Google Search — Trocar de Contador Manaus',
    campanha: 'Search_Troca_Contador_AM',
    data: '26/09/2026 14:20',
    stage: 'Reunião'
  },
  {
    id: 'lead-102',
    nome: 'Dra. Camila Rocha',
    empresa: 'Instituto Integrado de Saúde Amazônia',
    cnpj: 'Nova Empresa (Em abertura)',
    whatsapp: '(92) 99203-1184',
    email: 'camila.rocha@saudeamazonia.med.br',
    cidadeUf: 'Manaus/AM',
    regimeTributario: 'Empresa nova',
    servicoDesejado: 'Abertura de empresa',
    mensagem: 'Preciso abrir CNPJ médico com sócios e entender a tributação entre Simples (Fator R) e Presumido.',
    origem: 'Página Abra Sua Empresa',
    campanha: 'Organico_Abertura_Manaus',
    data: '26/09/2026 16:45',
    stage: 'Proposta enviada'
  },
  {
    id: 'lead-103',
    nome: 'Marcos Vinícius Prado',
    empresa: 'Prado Automação Industrial e Engenharia',
    cnpj: '19.840.221/0001-80',
    whatsapp: '(92) 98440-9012',
    email: 'diretoria@pradoautomacao.com.br',
    cidadeUf: 'Manaus/AM',
    regimeTributario: 'Simples Nacional',
    servicoDesejado: 'Auditoria',
    mensagem: 'Solicito avaliação para revisão tributária dos últimos anos e análise de migração para Lucro Presumido.',
    origem: 'Simulador Tributário — Serviços',
    campanha: 'Direto_Consultoria_Tributaria',
    data: '27/09/2026 08:05',
    stage: 'Novo Lead'
  }
];

export const INITIAL_APPOINTMENTS: AppointmentRecord[] = [
  {
    id: 'ag-1',
    assunto: 'Diagnóstico para Troca de Contador',
    data: '2026-09-29',
    horario: '10:00',
    nome: 'Henrique Albuquerque',
    empresa: 'Albuquerque Logística & Transportes Ltda',
    whatsapp: '(92) 98114-5520',
    email: 'henrique@albuquerquelog.com.br',
    criadoEm: '26/09/2026 14:25',
    status: 'Confirmado'
  },
  {
    id: 'ag-2',
    assunto: 'Planejamento de Abertura de Empresa',
    data: '2026-09-30',
    horario: '15:00',
    nome: 'Dra. Camila Rocha',
    empresa: 'Instituto Integrado de Saúde Amazônia',
    whatsapp: '(92) 99203-1184',
    email: 'camila.rocha@saudeamazonia.med.br',
    criadoEm: '26/09/2026 17:00',
    status: 'Confirmado'
  }
];
