import React, { useState } from 'react';
import {
  MessageSquare,
  Lock,
  ExternalLink,
  ShieldCheck,
  ArrowLeft,
  X,
  Instagram,
  Facebook
} from 'lucide-react';
import { PageId, SiteConfig } from '../data/siteData';
import { BrandLogo } from './BrandLogo';

interface FooterProps {
  config: SiteConfig;
  onNavigate: (page: PageId) => void;
  onOpenWhatsApp: (customMsg?: string) => void;
  onTrackPortalAccess: () => void;
}

export const Footer: React.FC<FooterProps> = ({
  config,
  onNavigate,
  onOpenWhatsApp,
  onTrackPortalAccess
}) => {
  return (
    <footer className="bg-[#081B33] text-slate-300 border-t border-white/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-10 pb-12 border-b border-white/10">
          {/* Col 1: Official Brand Mark & Concept */}
          <div className="lg:col-span-4 space-y-4">
            <button
              type="button"
              onClick={() => onNavigate('home')}
              aria-label="Início — A.M Consultoria Contábil"
              className="text-left cursor-pointer"
            >
              <BrandLogo variant="dark" size="lg" />
            </button>
            <div className="text-xs font-semibold text-[#F59E0B]">
              Contabilidade Digital · Consultoria · Auditoria
            </div>
            <p className="text-xs text-slate-400 leading-relaxed">
              Contabilidade inteligente para empresas que querem evoluir. Tecnologia para simplificar. Conhecimento para orientar. Contabilidade para impulsionar decisões.
            </p>
            <div className="pt-1 text-xs font-mono text-slate-300 space-y-1">
              <div>CNPJ: {config.cnpj}</div>
              <div>CNAE: 69.20-6-01 · 69.20-6-02</div>
            </div>
            {/* Official Social Media Links */}
            <div className="pt-2 flex flex-wrap items-center gap-2.5">
              <a
                href={config.instagramUrl}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Instagram oficial da A.M Consultoria Contábil"
                className="px-3.5 py-2 bg-white/10 hover:bg-[#F59E0B] hover:text-[#081B33] text-white text-xs font-semibold rounded-lg inline-flex items-center gap-1.5 transition-colors"
              >
                <Instagram className="w-3.5 h-3.5" />
                <span>@am.consultoria.contabil</span>
              </a>
              <a
                href={config.facebookUrl}
                target="_blank"
                rel="noopener noreferrer"
                aria-label="Facebook oficial da A.M Consultoria Contábil"
                className="px-3.5 py-2 bg-white/10 hover:bg-[#1769AA] text-white text-xs font-semibold rounded-lg inline-flex items-center gap-1.5 transition-colors"
              >
                <Facebook className="w-3.5 h-3.5" />
                <span>Facebook</span>
              </a>
            </div>
          </div>

          {/* Col 2: Links Institucionais e Serviços */}
          <div className="lg:col-span-3 space-y-2.5 text-xs">
            <div className="font-semibold text-white uppercase tracking-wider">
              Navegação & Serviços
            </div>
            <ul className="space-y-2 pt-1">
              {[
                { id: 'sobre', label: 'Sobre Nós & Sócios' },
                { id: 'servicos', label: 'Serviços Contábeis e Fiscais' },
                { id: 'especialidades', label: 'Especialidades por Desafio' },
                { id: 'tecnologia', label: 'Tecnologia Contábil' },
                { id: 'casos', label: 'Casos e Soluções' },
                { id: 'conteudos', label: 'A M Inteligência Contábil (Blog)' }
              ].map((item) => (
                <li key={item.id}>
                  <button
                    type="button"
                    onClick={() => onNavigate(item.id as PageId)}
                    className="text-slate-400 hover:text-white transition-colors cursor-pointer"
                  >
                    {item.label}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Col 3: Soluções Comerciais & Cliente */}
          <div className="lg:col-span-2 space-y-2.5 text-xs">
            <div className="font-semibold text-white uppercase tracking-wider">
              Acesso Rápido
            </div>
            <ul className="space-y-2 pt-1">
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('trocar-contador')}
                  className="text-slate-400 hover:text-[#F59E0B] transition-colors cursor-pointer"
                >
                  Troque de Contador
                </button>
              </li>
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('abrir-empresa')}
                  className="text-slate-400 hover:text-[#F59E0B] transition-colors cursor-pointer"
                >
                  Abra sua Empresa
                </button>
              </li>
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('orcamento')}
                  className="text-slate-400 hover:text-white transition-colors cursor-pointer"
                >
                  Solicitar Orçamento
                </button>
              </li>
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('agendamento')}
                  className="text-slate-400 hover:text-white transition-colors cursor-pointer"
                >
                  Agendar Reunião
                </button>
              </li>
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('portal-do-cliente')}
                  className="text-[#F59E0B] hover:underline font-semibold inline-flex items-center gap-1 cursor-pointer"
                >
                  <Lock className="w-3 h-3" />
                  <span>Portal do Cliente</span>
                </button>
              </li>
              <li>
                <button
                  type="button"
                  onClick={() => onNavigate('contato')}
                  className="text-slate-400 hover:text-white transition-colors cursor-pointer"
                >
                  Contato & Mapa
                </button>
              </li>
            </ul>
          </div>

          {/* Col 4: Endereço & Canais Oficiais */}
          <div className="lg:col-span-3 space-y-2.5 text-xs">
            <div className="font-semibold text-white uppercase tracking-wider">
              Sede & Atendimento
            </div>
            <p className="text-slate-400 leading-relaxed pt-1">
              {config.endereco} — {config.bairro} — {config.cidadeUf} — CEP {config.cep}
            </p>
            <div className="font-mono text-slate-300 space-y-1">
              <div>Tel/WhatsApp (AM): {config.telefonePrincipal}</div>
              <div>Tel/WhatsApp (SP): {config.telefoneSecundario}</div>
              <div className="truncate">{config.email}</div>
            </div>
            <div className="pt-2 flex flex-wrap gap-2">
              <button
                type="button"
                onClick={() => onOpenWhatsApp()}
                className="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold rounded-lg inline-flex items-center gap-1.5 transition-colors cursor-pointer"
              >
                <MessageSquare className="w-3.5 h-3.5" />
                <span>WhatsApp</span>
              </button>
              <a
                href={config.portalClienteUrl}
                target="_blank"
                rel="noopener noreferrer"
                onClick={onTrackPortalAccess}
                className="px-3.5 py-2 bg-white/10 hover:bg-white/15 text-white rounded-lg inline-flex items-center gap-1.5 transition-colors"
              >
                <span>Onvio</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Legal Row */}
        <div className="pt-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs text-slate-400">
          <div>
            © {new Date().getFullYear()} {config.razaoSocial} · CNPJ {config.cnpj}. Todos os direitos reservados.
          </div>
          <div className="flex flex-wrap items-center gap-4">
            <button
              type="button"
              onClick={() => onNavigate('privacidade')}
              className="hover:text-white transition-colors cursor-pointer"
            >
              Política de Privacidade & LGPD
            </button>
            <span aria-hidden="true">·</span>
            <button
              type="button"
              onClick={() => onNavigate('privacidade')}
              className="hover:text-white transition-colors cursor-pointer"
            >
              Termos de Uso
            </button>
            <span aria-hidden="true">·</span>
            <button
              type="button"
              onClick={() => onNavigate('admin')}
              className="hover:text-[#F59E0B] transition-colors cursor-pointer"
            >
              Painel CMS / CRM
            </button>
          </div>
        </div>
      </div>
    </footer>
  );
};

export const FloatingWhatsAppAndLgpd: React.FC<{
  config: SiteConfig;
  onOpenWhatsApp: (customMsg?: string, rawNumber?: string) => void;
  onNavigate: (page: PageId) => void;
}> = ({ config, onOpenWhatsApp, onNavigate }) => {
  const [lgpdDismissed, setLgpdDismissed] = useState<boolean>(() => {
    try {
      return localStorage.getItem('am_lgpd_accepted') === 'true';
    } catch {
      return false;
    }
  });
  const [wppMenuOpen, setWppMenuOpen] = useState(false);

  const acceptLgpd = () => {
    try {
      localStorage.setItem('am_lgpd_accepted', 'true');
    } catch {
      // ignore
    }
    setLgpdDismissed(true);
  };

  return (
    <>
      {/* LGPD Cookie Notice (Compact & Compliant) */}
      {!lgpdDismissed && (
        <div className="fixed bottom-4 left-4 right-20 sm:right-auto sm:max-w-md z-40 bg-[#081B33] text-white border border-white/15 rounded-xl p-4 shadow-2xl text-xs">
          <div className="flex items-start justify-between gap-3">
            <div className="space-y-1">
              <div className="font-semibold text-[#F59E0B] flex items-center gap-1.5">
                <ShieldCheck className="w-4 h-4" />
                <span>Privacidade e Proteção de Dados (LGPD)</span>
              </div>
              <p className="text-slate-300 leading-relaxed">
                Utilizamos cookies essenciais e analíticos para garantir a melhor experiência. Consulte nossa{' '}
                <button
                  type="button"
                  onClick={() => onNavigate('privacidade')}
                  className="underline text-white hover:text-[#F59E0B] cursor-pointer"
                >
                  Política de Privacidade
                </button>
                .
              </p>
            </div>
          </div>
          <div className="mt-3 flex justify-end gap-2">
            <button
              type="button"
              onClick={acceptLgpd}
              className="px-3.5 py-1.5 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] font-semibold rounded-lg cursor-pointer"
            >
              Concordar e fechar
            </button>
          </div>
        </div>
      )}

      {/* Permanent Floating WhatsApp Button (Seção 23) */}
      <div className="fixed bottom-4 right-4 z-50 flex flex-col items-end">
        {wppMenuOpen && (
          <div className="mb-2.5 w-72 bg-white border border-slate-200 rounded-2xl shadow-2xl p-4 text-xs space-y-3">
            <div className="flex items-center justify-between border-b border-slate-100 pb-2">
              <div>
                <div className="font-bold text-[#081B33]">Atendimento A M Consultoria</div>
                <div className="text-slate-500">Escolha o canal para iniciar no WhatsApp:</div>
              </div>
              <button
                type="button"
                onClick={() => setWppMenuOpen(false)}
                className="p-1 text-slate-400 hover:text-slate-700 cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <button
              type="button"
              onClick={() => {
                onOpenWhatsApp(config.whatsappMensagemPadrao, config.whatsappPrincipalRaw);
                setWppMenuOpen(false);
              }}
              className="w-full text-left p-2.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 flex items-center justify-between cursor-pointer"
            >
              <div>
                <div className="font-semibold text-emerald-950">Unidade Manaus/AM (Principal)</div>
                <div className="font-mono text-emerald-800">{config.telefonePrincipal}</div>
              </div>
              <MessageSquare className="w-4 h-4 text-emerald-700" />
            </button>

            <button
              type="button"
              onClick={() => {
                onOpenWhatsApp(config.whatsappMensagemPadrao, config.whatsappSecundarioRaw);
                setWppMenuOpen(false);
              }}
              className="w-full text-left p-2.5 rounded-xl bg-slate-50 hover:bg-slate-100 border border-slate-200 flex items-center justify-between cursor-pointer"
            >
              <div>
                <div className="font-semibold text-[#081B33]">Atendimento Nacional / SP</div>
                <div className="font-mono text-slate-600">{config.telefoneSecundario}</div>
              </div>
              <MessageSquare className="w-4 h-4 text-[#1769AA]" />
            </button>

            <div className="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500">
              <span>Siga a A.M:</span>
              <div className="flex items-center gap-2">
                <a
                  href={config.instagramUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 font-semibold text-[#081B33] hover:text-[#1769AA]"
                >
                  <Instagram className="w-3.5 h-3.5 text-[#F59E0B]" />
                  <span>Instagram</span>
                </a>
                <span>·</span>
                <a
                  href={config.facebookUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 font-semibold text-[#081B33] hover:text-[#1769AA]"
                >
                  <Facebook className="w-3.5 h-3.5 text-[#1769AA]" />
                  <span>Facebook</span>
                </a>
              </div>
            </div>
          </div>
        )}

        <button
          type="button"
          onClick={() => setWppMenuOpen((prev) => !prev)}
          aria-label="Falar pelo WhatsApp com a A M Consultoria"
          className="h-12 px-4 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full shadow-xl flex items-center gap-2 text-xs font-semibold transition-transform hover:scale-[1.02] cursor-pointer"
        >
          <MessageSquare className="w-4 h-4" />
          <span className="hidden sm:inline">WhatsApp A M</span>
        </button>
      </div>
    </>
  );
};

export const NotFound404Page: React.FC<{ onNavigate: (page: PageId) => void }> = ({
  onNavigate
}) => {
  return (
    <div className="max-w-3xl mx-auto px-4 py-20 text-center space-y-5">
      <div className="font-mono text-sm font-semibold text-[#1769AA]">Erro 404 · Página não encontrada</div>
      <h1 className="font-display text-3xl sm:text-4xl font-bold text-[#081B33]">
        O endereço acessado não existe ou foi movido.
      </h1>
      <p className="text-sm text-slate-600 max-w-lg mx-auto">
        Utilize os botões abaixo para retornar ao início ou acessar diretamente o Portal do Cliente e nossos serviços contábeis.
      </p>
      <div className="flex justify-center gap-3 pt-2">
        <button
          type="button"
          onClick={() => onNavigate('home')}
          className="px-5 py-3 bg-[#081B33] text-white text-xs font-semibold rounded-xl inline-flex items-center gap-1.5 cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Voltar para a Página Inicial</span>
        </button>
        <button
          type="button"
          onClick={() => onNavigate('orcamento')}
          className="px-5 py-3 bg-[#F59E0B] text-[#081B33] text-xs font-semibold rounded-xl cursor-pointer"
        >
          Solicitar Orçamento
        </button>
      </div>
    </div>
  );
};
