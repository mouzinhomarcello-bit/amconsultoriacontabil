import React, { useState } from 'react';
import {
  Users,
  Calendar,
  Settings,
  BarChart2,
  FilePlus,
  Download,
  MessageSquare,
  CheckCircle2,
  Trash2
} from 'lucide-react';
import {
  LeadRecord,
  PipelineStage,
  AppointmentRecord,
  AnalyticsEvent,
  SiteConfig,
  BlogPost,
  BLOG_CATEGORIES
} from '../data/siteData';

const PIPELINE_STAGES: PipelineStage[] = [
  'Novo Lead',
  'Contato realizado',
  'Qualificado',
  'Reunião',
  'Proposta enviada',
  'Negociação',
  'Cliente'
];

interface AdminCrmPanelProps {
  config: SiteConfig;
  onUpdateConfig: (newConfig: SiteConfig) => void;
  leads: LeadRecord[];
  onUpdateLeadStage: (id: string, stage: PipelineStage) => void;
  onDeleteLead: (id: string) => void;
  appointments: AppointmentRecord[];
  onUpdateAppointmentStatus: (id: string, status: AppointmentRecord['status']) => void;
  analytics: AnalyticsEvent[];
  blogPosts: BlogPost[];
  onAddBlogPost: (post: Omit<BlogPost, 'id'>) => void;
  onOpenWhatsAppDirect: (phone: string, text: string) => void;
}

export const AdminCrmPanel: React.FC<AdminCrmPanelProps> = ({
  config,
  onUpdateConfig,
  leads,
  onUpdateLeadStage,
  onDeleteLead,
  appointments,
  onUpdateAppointmentStatus,
  analytics,
  blogPosts,
  onAddBlogPost,
  onOpenWhatsAppDirect
}) => {
  const [activeTab, setActiveTab] = useState<'crm' | 'agendamentos' | 'cms' | 'artigos' | 'analytics'>('crm');
  const [stageFilter, setStageFilter] = useState<string>('Todos');

  // New Article State
  const [newTitle, setNewTitle] = useState('');
  const [newCategory, setNewCategory] = useState('Tributação');
  const [newAuthor, setNewAuthor] = useState('Marcelo da Silva Mouzinho');
  const [newExcerpt, setNewExcerpt] = useState('');
  const [newParagraph, setNewParagraph] = useState('');
  const [articleSavedMsg, setArticleSavedMsg] = useState('');
  const [cmsSavedMsg, setCmsSavedMsg] = useState('');

  const filteredLeads =
    stageFilter === 'Todos' ? leads : leads.filter((l) => l.stage === stageFilter);

  const handleExportCsv = () => {
    const headers = [
      'ID',
      'Nome',
      'Empresa',
      'CNPJ',
      'WhatsApp',
      'Email',
      'Cidade/UF',
      'Regime',
      'Servico',
      'Etapa Pipeline',
      'Origem',
      'Data'
    ];
    const rows = leads.map((l) =>
      [
        l.id,
        `"${l.nome}"`,
        `"${l.empresa}"`,
        `"${l.cnpj}"`,
        `"${l.whatsapp}"`,
        `"${l.email}"`,
        `"${l.cidadeUf}"`,
        `"${l.regimeTributario}"`,
        `"${l.servicoDesejado}"`,
        `"${l.stage}"`,
        `"${l.origem}"`,
        `"${l.data}"`
      ].join(',')
    );
    const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows].join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'leads_am_consultoria.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleIndicatorChange = (index: number, field: 'value' | 'label' | 'detail', val: string) => {
    const updated = [...config.indicadores];
    updated[index] = { ...updated[index], [field]: val };
    onUpdateConfig({ ...config, indicadores: updated });
  };

  const handleCreatePost = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim() || !newExcerpt.trim()) return;
    onAddBlogPost({
      slug: newTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
      title: newTitle.trim(),
      category: newCategory,
      readTime: '5 min de leitura',
      date: '27 Set 2026',
      author: newAuthor,
      excerpt: newExcerpt.trim(),
      content: [
        newParagraph.trim() || newExcerpt.trim(),
        'A equipe da A M Consultoria e Auditoria Contábil acompanha diariamente as atualizações fiscais em Manaus/AM e em âmbito federal para orientar sua empresa com segurança.'
      ],
      checklist: [
        'Avaliação personalizada do impacto tributário no seu CNPJ',
        'Acompanhamento preventivo via Portal do Cliente Domínio / Onvio'
      ]
    });
    setNewTitle('');
    setNewExcerpt('');
    setNewParagraph('');
    setArticleSavedMsg('Artigo publicado com sucesso na Central A M Inteligência Contábil.');
    setTimeout(() => setArticleSavedMsg(''), 4000);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      <div className="bg-[#081B33] text-white rounded-2xl p-6 sm:p-8 border border-white/10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
        <div>
          <div className="text-xs text-[#F59E0B] font-semibold">
            Administração do Site · CMS & CRM Comercial Integrado
          </div>
          <h1 className="font-display text-2xl sm:text-3xl font-bold text-white mt-1">
            Painel de Gestão A M Consultoria
          </h1>
          <p className="text-sm text-slate-300 mt-1">
            Gerencie o pipeline de leads, agendamentos, indicadores de "A A M em Números", links do Portal Onvio e artigos do blog.
          </p>
        </div>

        <div className="flex flex-wrap gap-1.5 bg-[#0D2544] p-1.5 rounded-xl border border-white/10">
          {[
            { id: 'crm', label: `Pipeline Leads (${leads.length})`, icon: Users },
            { id: 'agendamentos', label: `Agenda (${appointments.length})`, icon: Calendar },
            { id: 'cms', label: 'CMS & Números', icon: Settings },
            { id: 'artigos', label: `Blog (${blogPosts.length})`, icon: FilePlus },
            { id: 'analytics', label: `Analytics (${analytics.length})`, icon: BarChart2 }
          ].map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.id}
                type="button"
                onClick={() =>
                  setActiveTab(tab.id as 'crm' | 'agendamentos' | 'cms' | 'artigos' | 'analytics')
                }
                className={`px-3 py-2 text-xs font-semibold rounded-lg inline-flex items-center gap-1.5 transition-colors cursor-pointer whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'bg-[#F59E0B] text-[#081B33]'
                    : 'text-slate-300 hover:text-white'
                }`}
              >
                <Icon className="w-3.5 h-3.5" />
                <span>{tab.label}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* TAB 1: CRM PIPELINE DE LEADS */}
      {activeTab === 'crm' && (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200">
            <div className="flex flex-wrap items-center gap-1.5">
              <button
                type="button"
                onClick={() => setStageFilter('Todos')}
                className={`px-3 py-1.5 text-xs font-medium rounded-lg cursor-pointer ${
                  stageFilter === 'Todos'
                    ? 'bg-[#081B33] text-white'
                    : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                }`}
              >
                Todos ({leads.length})
              </button>
              {PIPELINE_STAGES.map((st) => {
                const count = leads.filter((l) => l.stage === st).length;
                return (
                  <button
                    key={st}
                    type="button"
                    onClick={() => setStageFilter(st)}
                    className={`px-3 py-1.5 text-xs font-medium rounded-lg cursor-pointer ${
                      stageFilter === st
                        ? 'bg-[#1769AA] text-white'
                        : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                    }`}
                  >
                    {st} ({count})
                  </button>
                );
              })}
            </div>

            <button
              type="button"
              onClick={handleExportCsv}
              className="px-3.5 py-2 text-xs font-semibold text-[#081B33] border border-slate-300 rounded-lg hover:bg-slate-50 inline-flex items-center gap-1.5 self-start cursor-pointer"
            >
              <Download className="w-3.5 h-3.5" />
              <span>Exportar CSV</span>
            </button>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-slate-200 text-xs text-slate-500">
                  <th className="py-3 px-3 font-semibold">Empresa / Contato</th>
                  <th className="py-3 px-3 font-semibold">Serviço & Regime</th>
                  <th className="py-3 px-3 font-semibold">Origem / Data</th>
                  <th className="py-3 px-3 font-semibold">Etapa do Pipeline</th>
                  <th className="py-3 px-3 font-semibold text-right">Ações</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200 text-xs">
                {filteredLeads.map((lead) => (
                  <tr key={lead.id} className="hover:bg-slate-50/80">
                    <td className="py-3.5 px-3">
                      <div className="font-semibold text-[#081B33] text-sm">{lead.empresa}</div>
                      <div className="text-slate-600">
                        {lead.nome} · <span className="font-mono">{lead.cnpj}</span>
                      </div>
                      <div className="text-slate-500 font-mono mt-0.5">
                        {lead.whatsapp} · {lead.email}
                      </div>
                    </td>
                    <td className="py-3.5 px-3">
                      <div className="font-semibold text-[#1769AA]">{lead.servicoDesejado}</div>
                      <div className="text-slate-600">Regime: {lead.regimeTributario}</div>
                      <div className="text-slate-500 mt-0.5 max-w-xs truncate" title={lead.mensagem}>
                        "{lead.mensagem}"
                      </div>
                    </td>
                    <td className="py-3.5 px-3">
                      <div className="text-slate-700">{lead.origem}</div>
                      <div className="font-mono text-slate-500 mt-0.5 tabular-nums">{lead.data}</div>
                    </td>
                    <td className="py-3.5 px-3">
                      <select
                        value={lead.stage}
                        onChange={(e) =>
                          onUpdateLeadStage(lead.id, e.target.value as PipelineStage)
                        }
                        className="px-2.5 py-1.5 bg-slate-100 border border-slate-300 rounded-lg text-xs font-semibold text-[#081B33]"
                      >
                        {PIPELINE_STAGES.map((st) => (
                          <option key={st} value={st}>
                            {st}
                          </option>
                        ))}
                      </select>
                    </td>
                    <td className="py-3.5 px-3 text-right whitespace-nowrap space-x-2">
                      <button
                        type="button"
                        onClick={() =>
                          onOpenWhatsAppDirect(
                            lead.whatsapp,
                            `Olá ${lead.nome}, aqui é da A M Consultoria Contábil sobre sua solicitação para a empresa ${lead.empresa}.`
                          )
                        }
                        className="px-2.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-md inline-flex items-center gap-1 cursor-pointer"
                      >
                        <MessageSquare className="w-3.5 h-3.5" />
                        <span>WhatsApp</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => onDeleteLead(lead.id)}
                        aria-label="Remover lead"
                        className="p-1.5 text-slate-400 hover:text-red-600 rounded-md cursor-pointer"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 2: AGENDAMENTOS */}
      {activeTab === 'agendamentos' && (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-4">
          <h2 className="font-display text-xl font-bold text-[#081B33]">
            Reuniões Agendadas pelo Site
          </h2>
          <div className="divide-y divide-slate-200">
            {appointments.map((app) => (
              <div
                key={app.id}
                className="py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs"
              >
                <div>
                  <div className="font-semibold text-sm text-[#081B33]">{app.assunto}</div>
                  <div className="text-slate-600 mt-0.5">
                    {app.nome} ({app.empresa}) · <span className="font-mono">{app.whatsapp}</span> · {app.email}
                  </div>
                  <div className="font-mono text-[#1769AA] mt-1 tabular-nums">
                    Data: {app.data} às {app.horario}
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <select
                    value={app.status}
                    onChange={(e) =>
                      onUpdateAppointmentStatus(
                        app.id,
                        e.target.value as AppointmentRecord['status']
                      )
                    }
                    className="px-3 py-1.5 bg-slate-100 border border-slate-300 rounded-lg font-semibold text-[#081B33]"
                  >
                    <option value="Confirmado">Confirmado</option>
                    <option value="Pendente">Pendente</option>
                    <option value="Realizado">Realizado</option>
                  </select>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: CMS INSTITUCIONAL & "A AM EM NÚMEROS" */}
      {activeTab === 'cms' && (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-8">
          <div className="flex items-center justify-between border-b border-slate-200 pb-4">
            <div>
              <h2 className="font-display text-xl font-bold text-[#081B33]">
                Configurações Institucionais, Contatos e "A A M em Números"
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                Qualquer alteração feita abaixo atualiza imediatamente o site em tempo real.
              </p>
            </div>
            {cmsSavedMsg && (
              <span className="text-xs font-semibold text-emerald-700 flex items-center gap-1">
                <CheckCircle2 className="w-4 h-4" />
                <span>{cmsSavedMsg}</span>
              </span>
            )}
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Telefone / WhatsApp Principal (Manaus)
              </label>
              <input
                type="text"
                value={config.telefonePrincipal}
                onChange={(e) => {
                  onUpdateConfig({ ...config, telefonePrincipal: e.target.value });
                  setCmsSavedMsg('Dados salvos automaticamente');
                }}
                className="w-full px-3 py-2 text-sm font-mono border border-slate-300 rounded-lg"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Telefone / WhatsApp Secundário (SP/Nacional)
              </label>
              <input
                type="text"
                value={config.telefoneSecundario}
                onChange={(e) => {
                  onUpdateConfig({ ...config, telefoneSecundario: e.target.value });
                  setCmsSavedMsg('Dados salvos automaticamente');
                }}
                className="w-full px-3 py-2 text-sm font-mono border border-slate-300 rounded-lg"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                E-mail Oficial
              </label>
              <input
                type="email"
                value={config.email}
                onChange={(e) => {
                  onUpdateConfig({ ...config, email: e.target.value });
                  setCmsSavedMsg('Dados salvos automaticamente');
                }}
                className="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                URL Oficial do Portal do Cliente (Domínio / Onvio)
              </label>
              <input
                type="url"
                value={config.portalClienteUrl}
                onChange={(e) => {
                  onUpdateConfig({ ...config, portalClienteUrl: e.target.value });
                  setCmsSavedMsg('Link do Portal atualizado');
                }}
                className="w-full px-3 py-2 text-sm font-mono border border-slate-300 rounded-lg"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Instagram Oficial
              </label>
              <input
                type="url"
                value={config.instagramUrl}
                onChange={(e) => {
                  onUpdateConfig({ ...config, instagramUrl: e.target.value });
                  setCmsSavedMsg('Instagram atualizado');
                }}
                className="w-full px-3 py-2 text-sm font-mono border border-slate-300 rounded-lg"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Facebook Oficial
              </label>
              <input
                type="url"
                value={config.facebookUrl}
                onChange={(e) => {
                  onUpdateConfig({ ...config, facebookUrl: e.target.value });
                  setCmsSavedMsg('Facebook atualizado');
                }}
                className="w-full px-3 py-2 text-sm font-mono border border-slate-300 rounded-lg"
              />
            </div>

            <div className="flex items-center gap-3 pt-5">
              <input
                id="toggle-socios"
                type="checkbox"
                checked={config.mostrarSocios}
                onChange={(e) => {
                  onUpdateConfig({ ...config, mostrarSocios: e.target.checked });
                  setCmsSavedMsg('Visibilidade dos sócios atualizada');
                }}
                className="rounded border-slate-300 text-[#1769AA]"
              />
              <label htmlFor="toggle-socios" className="text-xs font-semibold text-[#081B33]">
                Exibir seção dos Sócios (Marcelo & André) na página Sobre Nós
              </label>
            </div>
          </div>

          <div className="border-t border-slate-200 pt-6">
            <h3 className="font-display text-lg font-bold text-[#081B33] mb-4">
              Editar Indicadores da Seção "A A M em Números" (Seção 9 do PRD)
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              {config.indicadores.map((ind, idx) => (
                <div key={ind.id} className="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-2.5">
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-500">
                      Número / Destaque
                    </label>
                    <input
                      type="text"
                      value={ind.value}
                      onChange={(e) => handleIndicatorChange(idx, 'value', e.target.value)}
                      className="w-full px-2.5 py-1.5 text-sm font-mono font-semibold bg-white border border-slate-300 rounded"
                    />
                  </div>
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-500">
                      Título do Indicador
                    </label>
                    <input
                      type="text"
                      value={ind.label}
                      onChange={(e) => handleIndicatorChange(idx, 'label', e.target.value)}
                      className="w-full px-2.5 py-1.5 text-xs bg-white border border-slate-300 rounded"
                    />
                  </div>
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-500">
                      Contexto Explicativo
                    </label>
                    <input
                      type="text"
                      value={ind.detail}
                      onChange={(e) => handleIndicatorChange(idx, 'detail', e.target.value)}
                      className="w-full px-2.5 py-1.5 text-xs bg-white border border-slate-300 rounded"
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 4: PUBLICAR ARTIGO NO BLOG */}
      {activeTab === 'artigos' && (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 space-y-6">
          <h2 className="font-display text-xl font-bold text-[#081B33]">
            Publicar Novo Conteúdo em "A M Inteligência Contábil"
          </h2>
          {articleSavedMsg && (
            <div className="p-3.5 bg-emerald-50 border border-emerald-200 rounded-xl text-xs font-semibold text-emerald-800">
              {articleSavedMsg}
            </div>
          )}
          <form onSubmit={handleCreatePost} className="space-y-4 max-w-3xl">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Título do Artigo *
              </label>
              <input
                type="text"
                required
                value={newTitle}
                onChange={(e) => setNewTitle(e.target.value)}
                placeholder="Ex.: Como organizar os documentos da sua empresa em Manaus"
                className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg"
              />
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Categoria
                </label>
                <select
                  value={newCategory}
                  onChange={(e) => setNewCategory(e.target.value)}
                  className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg"
                >
                  {BLOG_CATEGORIES.filter((c) => c !== 'Todos').map((cat) => (
                    <option key={cat} value={cat}>
                      {cat}
                    </option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Autor
                </label>
                <select
                  value={newAuthor}
                  onChange={(e) => setNewAuthor(e.target.value)}
                  className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg"
                >
                  <option value="Marcelo da Silva Mouzinho">Marcelo da Silva Mouzinho</option>
                  <option value="André Pesce Bueno de Castro">André Pesce Bueno de Castro</option>
                  <option value="Equipe Técnica A M Consultoria">Equipe Técnica A M Consultoria</option>
                </select>
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Resumo Executivo (Excerpt SEO) *
              </label>
              <textarea
                rows={2}
                required
                value={newExcerpt}
                onChange={(e) => setNewExcerpt(e.target.value)}
                placeholder="Síntese objetiva do artigo para listagem e Google..."
                className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Conteúdo Principal do Artigo
              </label>
              <textarea
                rows={4}
                value={newParagraph}
                onChange={(e) => setNewParagraph(e.target.value)}
                placeholder="Desenvolva a orientação consultiva para o empresário..."
                className="w-full px-3.5 py-2 text-sm border border-slate-300 rounded-lg"
              />
            </div>
            <button
              type="submit"
              className="px-5 py-2.5 bg-[#081B33] hover:bg-[#1769AA] text-white text-xs font-semibold rounded-xl cursor-pointer"
            >
              Publicar artigo agora
            </button>
          </form>
        </div>
      )}

      {/* TAB 5: ANALYTICS & EVENTOS RASTREADOS */}
      {activeTab === 'analytics' && (
        <div className="bg-white border border-slate-200 rounded-2xl p-6 space-y-6">
          <div>
            <h2 className="font-display text-xl font-bold text-[#081B33]">
              Métricas de Conversão e Eventos Rastreados (Seção 35 & 44)
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Registro em tempo real das interações comerciais realizadas no site (WhatsApp, Orçamentos, Portal, Artigos e Serviços).
            </p>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div className="text-xs text-slate-500">Total de Leads Captados</div>
              <div className="text-2xl font-mono font-bold text-[#081B33] mt-1 tabular-nums">
                {leads.length}
              </div>
            </div>
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div className="text-xs text-slate-500">Reuniões Agendadas</div>
              <div className="text-2xl font-mono font-bold text-[#1769AA] mt-1 tabular-nums">
                {appointments.length}
              </div>
            </div>
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div className="text-xs text-slate-500">Cliques WhatsApp / Portal</div>
              <div className="text-2xl font-mono font-bold text-emerald-700 mt-1 tabular-nums">
                {
                  analytics.filter(
                    (a) => a.type === 'clique_whatsapp' || a.type === 'acesso_portal'
                  ).length
                }
              </div>
            </div>
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div className="text-xs text-slate-500">Total de Eventos Sessão</div>
              <div className="text-2xl font-mono font-bold text-[#081B33] mt-1 tabular-nums">
                {analytics.length}
              </div>
            </div>
          </div>

          <div className="divide-y divide-slate-200 border border-slate-200 rounded-xl max-h-80 overflow-y-auto">
            {analytics.map((ev) => (
              <div
                key={ev.id}
                className="p-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs"
              >
                <div>
                  <span className="font-mono font-semibold text-[#1769AA]">{ev.type}</span>
                  <span aria-hidden="true"> · </span>
                  <span className="text-slate-800 font-medium">{ev.label}</span>
                </div>
                <div className="text-slate-500 font-mono tabular-nums">
                  Página: {ev.page} · {ev.timestamp}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
