import React, { useState, useRef, useEffect } from 'react';
import { ChevronDown, Menu, X, Lock, ArrowUpRight, Instagram, Facebook } from 'lucide-react';
import { PageId, SiteConfig } from '../data/siteData';
import { BrandLogo } from './BrandLogo';

interface NavbarProps {
  currentPage: PageId;
  config: SiteConfig;
  onNavigate: (page: PageId, param?: string) => void;
  leadsCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentPage,
  config,
  onNavigate,
  leadsCount
}) => {
  const [moreOpen, setMoreOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setMoreOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleNav = (page: PageId) => {
    onNavigate(page);
    setMoreOpen(false);
    setMobileMenuOpen(false);
  };

  const primaryLinks: { id: PageId; label: string }[] = [
    { id: 'home', label: 'Início' },
    { id: 'servicos', label: 'Serviços' },
    { id: 'especialidades', label: 'Especialidades' },
    { id: 'trocar-contador', label: 'Trocar Contador' },
    { id: 'conteudos', label: 'Conteúdos' }
  ];

  const secondaryLinks: { id: PageId; label: string; desc: string }[] = [
    { id: 'sobre', label: 'Sobre Nós & Sócios', desc: 'História, missão, valores e diretoria' },
    { id: 'abrir-empresa', label: 'Abra sua Empresa', desc: 'Roteiro seguro para novo CNPJ em Manaus e BR' },
    { id: 'tecnologia', label: 'Tecnologia Contábil', desc: 'Processos 100% digitais e integrados' },
    { id: 'casos', label: 'Casos e Soluções', desc: 'Resultados práticos e estudos de caso' },
    { id: 'agendamento', label: 'Agendar Reunião', desc: 'Escolha data e horário com um consultor' },
    { id: 'contato', label: 'Contato & Localização', desc: 'Dom Pedro I, Manaus/AM e canais oficiais' },
    { id: 'admin', label: `Painel CMS & CRM (${leadsCount})`, desc: 'Gestão de leads, indicadores e conteúdos' }
  ];

  return (
    <header className="sticky top-0 z-40 bg-[#081B33] text-white border-b border-white/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-18 flex items-center justify-between">
        {/* Zone 1: Official Brand Mark A.M CONSULTORIA CONTÁBIL */}
        <button
          type="button"
          onClick={() => handleNav('home')}
          aria-label="Ir para o início — A.M Consultoria Contábil"
          className="hover:opacity-95 transition-opacity text-left cursor-pointer py-1"
        >
          <BrandLogo variant="dark" size="md" />
        </button>

        {/* Zone 2: 5 clean text navigation links + More dropdown */}
        <nav className="hidden lg:flex items-center gap-7 text-sm font-medium text-slate-300">
          {primaryLinks.map((link) => {
            const isActive = currentPage === link.id;
            return (
              <button
                key={link.id}
                type="button"
                onClick={() => handleNav(link.id)}
                className={`py-1 whitespace-nowrap transition-colors border-b-2 cursor-pointer ${
                  isActive
                    ? 'text-white border-[#F59E0B]'
                    : 'border-transparent hover:text-white hover:border-white/40'
                }`}
              >
                {link.label}
              </button>
            );
          })}

          <div className="relative" ref={dropdownRef}>
            <button
              type="button"
              onClick={() => setMoreOpen((prev) => !prev)}
              className={`flex items-center gap-1 py-1 whitespace-nowrap transition-colors border-b-2 cursor-pointer ${
                secondaryLinks.some((s) => s.id === currentPage)
                  ? 'text-white border-[#F59E0B]'
                  : 'border-transparent hover:text-white'
              }`}
            >
              <span> Soluções</span>
              <ChevronDown className={`w-4 h-4 transition-transform ${moreOpen ? 'rotate-180' : ''}`} />
            </button>

            {moreOpen && (
              <div className="absolute right-0 mt-3 w-80 bg-[#0D2544] border border-white/15 rounded-xl shadow-2xl py-2 z-50">
                {secondaryLinks.map((item) => (
                  <button
                    key={item.id}
                    type="button"
                    onClick={() => handleNav(item.id)}
                    className={`w-full text-left px-4 py-2.5 hover:bg-white/5 transition-colors flex flex-col cursor-pointer ${
                      currentPage === item.id ? 'bg-white/10' : ''
                    }`}
                  >
                    <span className="text-sm font-semibold text-white">{item.label}</span>
                    <span className="text-xs text-slate-400">{item.desc}</span>
                  </button>
                ))}
              </div>
            )}
          </div>
        </nav>

        {/* Zone 3: 1-2 Primary Actions */}
        <div className="hidden sm:flex items-center gap-3">
          <button
            type="button"
            onClick={() => handleNav('portal-do-cliente')}
            className={`px-3.5 py-2 text-xs font-semibold rounded-lg border transition-colors whitespace-nowrap flex items-center gap-1.5 cursor-pointer ${
              currentPage === 'portal-do-cliente'
                ? 'border-[#F59E0B] text-[#F59E0B] bg-[#F59E0B]/10'
                : 'border-white/20 text-slate-200 hover:border-white/40 hover:text-white'
            }`}
          >
            <Lock className="w-3.5 h-3.5" />
            <span>Portal do Cliente</span>
          </button>

          <button
            type="button"
            onClick={() => handleNav('orcamento')}
            className="px-4 py-2 text-xs font-semibold text-[#081B33] bg-[#F59E0B] hover:bg-[#fbbf24] rounded-lg transition-colors whitespace-nowrap flex items-center gap-1 cursor-pointer"
          >
            <span>Solicitar orçamento</span>
            <ArrowUpRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Mobile Menu Trigger */}
        <div className="flex items-center gap-2 lg:hidden">
          <button
            type="button"
            onClick={() => handleNav('orcamento')}
            className="sm:hidden px-3 py-1.5 text-xs font-semibold text-[#081B33] bg-[#F59E0B] rounded-md whitespace-nowrap"
          >
            Orçamento
          </button>
          <button
            type="button"
            onClick={() => setMobileMenuOpen((prev) => !prev)}
            aria-label="Abrir menu de navegação"
            className="p-2 text-slate-200 hover:text-white rounded-lg"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </div>

      {/* Mobile Navigation Drawer */}
      {mobileMenuOpen && (
        <div className="lg:hidden bg-[#081B33] border-b border-white/15 px-4 pt-3 pb-6 space-y-3">
          <div className="grid grid-cols-2 gap-2">
            {primaryLinks.map((link) => (
              <button
                key={link.id}
                type="button"
                onClick={() => handleNav(link.id)}
                className={`text-left px-3 py-2 rounded-lg text-sm font-medium ${
                  currentPage === link.id
                    ? 'bg-[#1769AA] text-white'
                    : 'text-slate-200 hover:bg-white/5'
                }`}
              >
                {link.label}
              </button>
            ))}
          </div>

          <div className="border-t border-white/10 pt-3 grid grid-cols-1 gap-1.5">
            {secondaryLinks.map((item) => (
              <button
                key={item.id}
                type="button"
                onClick={() => handleNav(item.id)}
                className={`text-left px-3 py-2 rounded-lg text-sm ${
                  currentPage === item.id
                    ? 'bg-white/10 text-[#F59E0B] font-semibold'
                    : 'text-slate-300 hover:bg-white/5'
                }`}
              >
                {item.label}
              </button>
            ))}
          </div>

          <div className="border-t border-white/10 pt-3 flex flex-col sm:flex-row gap-2">
            <button
              type="button"
              onClick={() => handleNav('portal-do-cliente')}
              className="w-full py-2.5 px-4 text-xs font-semibold text-white border border-white/25 rounded-lg flex items-center justify-center gap-2"
            >
              <Lock className="w-3.5 h-3.5" />
              <span>Acessar Portal do Cliente</span>
            </button>
            <button
              type="button"
              onClick={() => handleNav('orcamento')}
              className="w-full py-2.5 px-4 text-xs font-semibold text-[#081B33] bg-[#F59E0B] rounded-lg text-center"
            >
              Solicitar orçamento
            </button>
          </div>

          <div className="border-t border-white/10 pt-3 flex items-center justify-between text-xs text-slate-300">
            <span>Redes Sociais Oficiais:</span>
            <div className="flex items-center gap-3">
              <a
                href={config.instagramUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 text-slate-200 hover:text-[#F59E0B]"
              >
                <Instagram className="w-4 h-4 text-[#F59E0B]" />
                <span>Instagram</span>
              </a>
              <a
                href={config.facebookUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 text-slate-200 hover:text-[#F59E0B]"
              >
                <Facebook className="w-4 h-4 text-[#F59E0B]" />
                <span>Facebook</span>
              </a>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};
