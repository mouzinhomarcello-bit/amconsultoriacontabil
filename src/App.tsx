import React, { useState, useEffect } from 'react';
import {
  PageId,
  SiteConfig,
  INITIAL_SITE_CONFIG,
  LeadRecord,
  INITIAL_LEADS,
  PipelineStage,
  AppointmentRecord,
  INITIAL_APPOINTMENTS,
  BlogPost,
  INITIAL_BLOG_POSTS,
  INITIAL_TESTIMONIALS,
  AnalyticsEvent
} from './data/siteData';
import { Navbar } from './components/Navbar';
import { HomePage } from './components/HomePage';
import {
  SobreNosPage,
  ServicosPage,
  EspecialidadesPage,
  ContatoPage
} from './components/InstitutionalPages';
import {
  TrocarContadorPage,
  AbrirEmpresaPage,
  TecnologiaPage,
  PortalClientePage
} from './components/CommercialPages';
import {
  BlogInteligenciaPage,
  CasosESolucoesPage,
  PrivacidadeLgpdPage
} from './components/BlogAndCasesPages';
import { QuoteFormSection, ScheduleMeetingSection } from './components/QuoteAndScheduleModals';
import { AdminCrmPanel } from './components/AdminCrmPanel';
import {
  Footer,
  FloatingWhatsAppAndLgpd,
  NotFound404Page
} from './components/FooterAndFloating';

const PAGE_TITLES: Record<PageId, string> = {
  home: 'A M Consultoria e Auditoria Contábil — Contabilidade Inteligente em Manaus/AM',
  sobre: 'Sobre Nós & Sócios — A M Consultoria e Auditoria Contábil Ltda',
  servicos: 'Serviços Contábeis, Fiscais, DP e Auditoria — A M Consultoria Manaus',
  especialidades: 'Especialidades e Soluções Empresariais — A M Consultoria Contábil',
  'trocar-contador': 'Troque de Contador com Segurança e Tecnologia — A M Consultoria',
  'abrir-empresa': 'Abra sua Empresa do Jeito Certo em Manaus/AM — A M Consultoria',
  tecnologia: 'Tecnologia Contábil e Processos Digitais — A M Consultoria',
  'portal-do-cliente': 'Portal do Cliente Domínio / Onvio — A M Consultoria Contábil',
  conteudos: 'A M Inteligência Contábil — Blog e Artigos Tributários',
  casos: 'Casos e Soluções — Portfólio Técnico A M Consultoria',
  orcamento: 'Solicitar Orçamento Contábil — A M Consultoria e Auditoria',
  agendamento: 'Agendar Reunião com Especialista — A M Consultoria Contábil',
  contato: 'Contato e Localização em Manaus/AM — A M Consultoria Contábil',
  privacidade: 'Política de Privacidade, Cookies e LGPD — A M Consultoria',
  admin: 'Painel Administrativo CMS & CRM — A M Consultoria',
  '404': 'Página Não Encontrada — A M Consultoria Contábil'
};

export function App() {
  const [currentPage, setCurrentPage] = useState<PageId>('home');
  const [preselectedService, setPreselectedService] = useState<string>('Contabilidade');
  const [preselectedRegime, setPreselectedRegime] = useState<string>('Simples Nacional');

  const [config, setConfig] = useState<SiteConfig>(() => {
    try {
      const saved = localStorage.getItem('am_site_config_v1');
      return saved ? { ...INITIAL_SITE_CONFIG, ...JSON.parse(saved) } : INITIAL_SITE_CONFIG;
    } catch {
      return INITIAL_SITE_CONFIG;
    }
  });

  const [leads, setLeads] = useState<LeadRecord[]>(() => {
    try {
      const saved = localStorage.getItem('am_crm_leads_v1');
      return saved ? JSON.parse(saved) : INITIAL_LEADS;
    } catch {
      return INITIAL_LEADS;
    }
  });

  const [appointments, setAppointments] = useState<AppointmentRecord[]>(() => {
    try {
      const saved = localStorage.getItem('am_appointments_v1');
      return saved ? JSON.parse(saved) : INITIAL_APPOINTMENTS;
    } catch {
      return INITIAL_APPOINTMENTS;
    }
  });

  const [blogPosts, setBlogPosts] = useState<BlogPost[]>(() => {
    try {
      const saved = localStorage.getItem('am_blog_posts_v1');
      return saved ? JSON.parse(saved) : INITIAL_BLOG_POSTS;
    } catch {
      return INITIAL_BLOG_POSTS;
    }
  });

  const [analytics, setAnalytics] = useState<AnalyticsEvent[]>(() => {
    try {
      const saved = localStorage.getItem('am_analytics_v1');
      return saved
        ? JSON.parse(saved)
        : [
            {
              id: 'ev-init-1',
              type: 'solicitacao_orcamento',
              label: 'Lead inicial registrado: Prado Automação Industrial',
              timestamp: '27/09/2026 08:05',
              page: 'servicos'
            },
            {
              id: 'ev-init-2',
              type: 'agendamento',
              label: 'Reunião agendada: Dra. Camila Rocha',
              timestamp: '26/09/2026 17:00',
              page: 'agendamento'
            }
          ];
    } catch {
      return [];
    }
  });

  useEffect(() => {
    document.title = PAGE_TITLES[currentPage] || PAGE_TITLES.home;
  }, [currentPage]);

  useEffect(() => {
    try {
      localStorage.setItem('am_site_config_v1', JSON.stringify(config));
    } catch {
      // ignore storage quota errors
    }
  }, [config]);

  useEffect(() => {
    try {
      localStorage.setItem('am_crm_leads_v1', JSON.stringify(leads));
    } catch {
      // ignore
    }
  }, [leads]);

  useEffect(() => {
    try {
      localStorage.setItem('am_appointments_v1', JSON.stringify(appointments));
    } catch {
      // ignore
    }
  }, [appointments]);

  useEffect(() => {
    try {
      localStorage.setItem('am_blog_posts_v1', JSON.stringify(blogPosts));
    } catch {
      // ignore
    }
  }, [blogPosts]);

  useEffect(() => {
    try {
      localStorage.setItem('am_analytics_v1', JSON.stringify(analytics));
    } catch {
      // ignore
    }
  }, [analytics]);

  const trackEvent = (
    type: AnalyticsEvent['type'],
    label: string,
    pageOverride?: string
  ) => {
    const now = new Date();
    const formattedTime = `${now.toLocaleDateString('pt-BR')} ${now
      .toLocaleTimeString('pt-BR')
      .slice(0, 5)}`;
    const newEv: AnalyticsEvent = {
      id: `ev-${Date.now()}-${Math.floor(Math.random() * 1000)}`,
      type,
      label,
      timestamp: formattedTime,
      page: pageOverride || currentPage
    };
    setAnalytics((prev) => [newEv, ...prev]);
  };

  const handleNavigate = (page: PageId) => {
    setCurrentPage(page);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleNavigateWithService = (service: string, regime?: string) => {
    trackEvent('clique_servico', `Interesse em serviço: ${service}`);
    setPreselectedService(service);
    if (regime) setPreselectedRegime(regime);
    setCurrentPage('orcamento');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const launchExternalUrlSafely = (url: string) => {
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.target = '_blank';
    anchor.rel = 'noopener noreferrer';
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
  };

  const handleOpenWhatsApp = (customMessage?: string, rawPhone?: string) => {
    const phone = (rawPhone || config.whatsappPrincipalRaw).replace(/\D/g, '');
    const msg = customMessage || config.whatsappMensagemPadrao;
    trackEvent('clique_whatsapp', `WhatsApp iniciado (${phone})`);
    const whatsappUrl = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
    launchExternalUrlSafely(whatsappUrl);
  };

  const handleAddLead = (newLeadData: Omit<LeadRecord, 'id' | 'data' | 'stage'>) => {
    const now = new Date();
    const formattedDate = `${now.toLocaleDateString('pt-BR')} ${now
      .toLocaleTimeString('pt-BR')
      .slice(0, 5)}`;
    const created: LeadRecord = {
      ...newLeadData,
      id: `lead-${Date.now()}`,
      data: formattedDate,
      stage: 'Novo Lead'
    };
    setLeads((prev) => [created, ...prev]);
    trackEvent(
      'solicitacao_orcamento',
      `Novo Lead: ${created.empresa} (${created.servicoDesejado})`
    );
  };

  const handleAddAppointment = (
    newApp: Omit<AppointmentRecord, 'id' | 'criadoEm' | 'status'>
  ) => {
    const now = new Date();
    const formattedDate = `${now.toLocaleDateString('pt-BR')} ${now
      .toLocaleTimeString('pt-BR')
      .slice(0, 5)}`;
    const created: AppointmentRecord = {
      ...newApp,
      id: `ag-${Date.now()}`,
      criadoEm: formattedDate,
      status: 'Confirmado'
    };
    setAppointments((prev) => [created, ...prev]);
    trackEvent(
      'agendamento',
      `Reunião agendada: ${created.nome} (${created.data} ${created.horario})`
    );
  };

  const handleUpdateLeadStage = (id: string, stage: PipelineStage) => {
    setLeads((prev) => prev.map((l) => (l.id === id ? { ...l, stage } : l)));
  };

  const handleDeleteLead = (id: string) => {
    setLeads((prev) => prev.filter((l) => l.id !== id));
  };

  const handleUpdateAppointmentStatus = (
    id: string,
    status: AppointmentRecord['status']
  ) => {
    setAppointments((prev) =>
      prev.map((a) => (a.id === id ? { ...a, status } : a))
    );
  };

  const handleAddBlogPost = (postData: Omit<BlogPost, 'id'>) => {
    const newPost: BlogPost = {
      ...postData,
      id: `post-${Date.now()}`
    };
    setBlogPosts((prev) => [newPost, ...prev]);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#F8FAFC] text-[#081B33]">
      <Navbar
        currentPage={currentPage}
        onNavigate={handleNavigate}
        leadsCount={leads.length}
        config={config}
      />

      <main className="flex-1">
        {currentPage === 'home' && (
          <HomePage
            config={config}
            testimonials={INITIAL_TESTIMONIALS}
            blogPosts={blogPosts}
            onNavigate={handleNavigate}
            onNavigateWithService={handleNavigateWithService}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackPortalAccess={() =>
              trackEvent('acesso_portal', 'Acesso ao Portal do Cliente via Home')
            }
          />
        )}

        {currentPage === 'sobre' && (
          <SobreNosPage config={config} onNavigate={handleNavigate} />
        )}

        {currentPage === 'servicos' && (
          <ServicosPage onNavigateWithService={handleNavigateWithService} />
        )}

        {currentPage === 'especialidades' && (
          <EspecialidadesPage onNavigate={handleNavigate} />
        )}

        {currentPage === 'trocar-contador' && (
          <TrocarContadorPage
            config={config}
            onNavigate={handleNavigate}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackEvent={trackEvent}
          />
        )}

        {currentPage === 'abrir-empresa' && (
          <AbrirEmpresaPage
            config={config}
            onNavigate={handleNavigate}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackEvent={trackEvent}
          />
        )}

        {currentPage === 'tecnologia' && (
          <TecnologiaPage
            config={config}
            onNavigate={handleNavigate}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackEvent={trackEvent}
          />
        )}

        {currentPage === 'portal-do-cliente' && (
          <PortalClientePage
            config={config}
            onNavigate={handleNavigate}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackEvent={trackEvent}
          />
        )}

        {currentPage === 'conteudos' && (
          <BlogInteligenciaPage
            posts={blogPosts}
            onNavigate={handleNavigate}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackArticleRead={(title) =>
              trackEvent('leitura_artigo', `Leitura: ${title}`)
            }
          />
        )}

        {currentPage === 'casos' && (
          <CasosESolucoesPage onNavigate={handleNavigate} />
        )}

        {currentPage === 'orcamento' && (
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-6">
            <QuoteFormSection
              config={config}
              defaultService={preselectedService}
              defaultRegime={preselectedRegime}
              origemLabel="Página Dedicada de Orçamento (/orcamento)"
              onAddLead={handleAddLead}
              onOpenWhatsApp={handleOpenWhatsApp}
            />
          </div>
        )}

        {currentPage === 'agendamento' && (
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-6">
            <ScheduleMeetingSection
              config={config}
              onAddAppointment={handleAddAppointment}
              onOpenWhatsApp={handleOpenWhatsApp}
            />
          </div>
        )}

        {currentPage === 'contato' && (
          <ContatoPage
            config={config}
            onAddLead={handleAddLead}
            onOpenWhatsApp={handleOpenWhatsApp}
            onTrackPhoneOrEmail={(type, label) => trackEvent(type, label)}
          />
        )}

        {currentPage === 'privacidade' && <PrivacidadeLgpdPage config={config} />}

        {currentPage === 'admin' && (
          <AdminCrmPanel
            config={config}
            onUpdateConfig={setConfig}
            leads={leads}
            onUpdateLeadStage={handleUpdateLeadStage}
            onDeleteLead={handleDeleteLead}
            appointments={appointments}
            onUpdateAppointmentStatus={handleUpdateAppointmentStatus}
            analytics={analytics}
            blogPosts={blogPosts}
            onAddBlogPost={handleAddBlogPost}
            onOpenWhatsAppDirect={(phone, text) => handleOpenWhatsApp(text, phone)}
          />
        )}

        {currentPage === '404' && <NotFound404Page onNavigate={handleNavigate} />}
      </main>

      <Footer
        config={config}
        onNavigate={handleNavigate}
        onOpenWhatsApp={handleOpenWhatsApp}
        onTrackPortalAccess={() =>
          trackEvent('acesso_portal', 'Acesso ao Portal via Rodapé')
        }
      />

      <FloatingWhatsAppAndLgpd
        config={config}
        onOpenWhatsApp={handleOpenWhatsApp}
        onNavigate={handleNavigate}
      />
    </div>
  );
}

export default App;
