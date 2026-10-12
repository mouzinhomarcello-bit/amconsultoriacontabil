import React, { useState } from 'react';
import { CheckCircle2, ArrowUpRight, FileCheck, Calendar, TrendingUp, ShieldCheck } from 'lucide-react';
import { PageId } from '../data/siteData';

interface HeroDashboardProps {
  onNavigate: (page: PageId) => void;
}

export const HeroDashboard: React.FC<HeroDashboardProps> = ({ onNavigate }) => {
  const [activeTab, setActiveTab] = useState<'dre' | 'calendario' | 'documentos'>('dre');
  const [selectedRegime, setSelectedRegime] = useState<'otimizado' | 'anterior'>('otimizado');

  const monthlyGrowth = [
    { month: 'Abr', receita: 142, margem: 24 },
    { month: 'Mai', receita: 158, margem: 26 },
    { month: 'Jun', receita: 171, margem: 27 },
    { month: 'Jul', receita: 189, margem: 29 },
    { month: 'Ago', receita: 214, margem: 31 },
    { month: 'Set', receita: 248, margem: 34 }
  ];

  const fiscalObligations = [
    {
      obligation: 'PGDAS-D / Apuração Simples & Presumido',
      competencia: '09/2026',
      vencimento: '20/10/2026',
      status: 'Auditado e Conciliado'
    },
    {
      obligation: 'eSocial + DCTFWeb + FGTS Digital',
      competencia: '09/2026',
      vencimento: '15/10/2026',
      status: 'Guias no Portal Onvio'
    },
    {
      obligation: 'EFD-ICMS/IPI · SEFAZ-AM / DIA Manaus',
      competencia: '09/2026',
      vencimento: '10/10/2026',
      status: 'Cruzamento 100% OK'
    },
    {
      obligation: 'ISSQN Retido e Próprio · Pref. Manaus',
      competencia: '09/2026',
      vencimento: '10/10/2026',
      status: 'Conferido sem Ressalvas'
    }
  ];

  const cndRecords = [
    {
      orgao: 'Certidão Conjunta RFB / PGFN (Federal)',
      validade: 'Válida · Renovação Automática',
      situacao: 'Regular'
    },
    {
      orgao: 'Certidão Negativa SEFAZ-AM (Estadual)',
      validade: 'Válida · Sem Pendências',
      situacao: 'Regular'
    },
    {
      orgao: 'Certidão Negativa SEMEF Manaus (Municipal)',
      validade: 'Válida · Domicílio Fiscal Ativo',
      situacao: 'Regular'
    },
    {
      orgao: 'Certificado de Regularidade do FGTS (CRF)',
      validade: 'Válida · Caixa Econômica',
      situacao: 'Regular'
    }
  ];

  return (
    <div className="bg-[#0D2544] border border-white/15 rounded-2xl p-5 sm:p-6 shadow-2xl text-white">
      {/* Top Bar of the Interactive Intelligence Panel */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-white/10">
        <div>
          <div className="text-xs text-slate-400">
            <span>Painel de Inteligência Contábil A M</span>
            <span aria-hidden="true"> · </span>
            <span className="font-mono text-[#F59E0B]">Onvio / Domínio Sync</span>
          </div>
          <h2 className="text-base font-semibold text-white mt-0.5">
            Visão Executiva de Conformidade e Resultado
          </h2>
        </div>

        {/* Interactive Segmented Control */}
        <div className="flex items-center gap-1 p-1 bg-[#081B33] rounded-lg border border-white/10 self-start">
          <button
            type="button"
            onClick={() => setActiveTab('dre')}
            className={`px-2.5 py-1.5 text-xs font-medium rounded-md transition-colors whitespace-nowrap cursor-pointer ${
              activeTab === 'dre'
                ? 'bg-[#1769AA] text-white'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            DRE & Tributos
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('calendario')}
            className={`px-2.5 py-1.5 text-xs font-medium rounded-md transition-colors whitespace-nowrap cursor-pointer ${
              activeTab === 'calendario'
                ? 'bg-[#1769AA] text-white'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            Calendário Fiscal
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('documentos')}
            className={`px-2.5 py-1.5 text-xs font-medium rounded-md transition-colors whitespace-nowrap cursor-pointer ${
              activeTab === 'documentos'
                ? 'bg-[#1769AA] text-white'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            CNDs & Portal
          </button>
        </div>
      </div>

      {/* TAB 1: DRE, Crescimento e Indicadores Tributários */}
      {activeTab === 'dre' && (
        <div className="pt-5 space-y-5">
          {/* Scenario Switcher */}
          <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
            <span className="text-slate-300">Simulação de Eficiência Tributária:</span>
            <div className="flex items-center gap-1.5 bg-[#081B33] p-1 rounded-lg border border-white/10">
              <button
                type="button"
                onClick={() => setSelectedRegime('otimizado')}
                className={`px-2.5 py-1 rounded text-xs font-medium transition-colors cursor-pointer ${
                  selectedRegime === 'otimizado'
                    ? 'bg-[#F59E0B] text-[#081B33] font-semibold'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Com Planejamento A M
              </button>
              <button
                type="button"
                onClick={() => setSelectedRegime('anterior')}
                className={`px-2.5 py-1 rounded text-xs font-medium transition-colors cursor-pointer ${
                  selectedRegime === 'anterior'
                    ? 'bg-white/15 text-white font-semibold'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Sem Revisão Fiscal
              </button>
            </div>
          </div>

          {/* 3 Primary Quantitative Metrics */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="bg-[#081B33]/90 border border-white/10 rounded-xl p-3.5">
              <div className="text-xs text-slate-400">Receita Bruta Conciliada</div>
              <div className="text-xl font-mono font-semibold text-white mt-1 tabular-nums">
                R$ 248.400
              </div>
              <div className="text-xs text-emerald-400 mt-1 font-mono tabular-nums">
                +15,8% vs. mês anterior
              </div>
            </div>

            <div className="bg-[#081B33]/90 border border-white/10 rounded-xl p-3.5">
              <div className="text-xs text-slate-400">Alíquota Efetiva Auditada</div>
              <div className="text-xl font-mono font-semibold text-[#F59E0B] mt-1 tabular-nums">
                {selectedRegime === 'otimizado' ? '8,42%' : '14,15%'}
              </div>
              <div className="text-xs text-slate-300 mt-1">
                {selectedRegime === 'otimizado'
                  ? 'Economia lícita: R$ 14.233/mês'
                  : 'Tributação sem revisão de Fator R/NCM'}
              </div>
            </div>

            <div className="bg-[#081B33]/90 border border-white/10 rounded-xl p-3.5">
              <div className="text-xs text-slate-400">Lucro Distribuível (Isento IR)</div>
              <div className="text-xl font-mono font-semibold text-white mt-1 tabular-nums">
                {selectedRegime === 'otimizado' ? 'R$ 68.920' : 'R$ 54.687'}
              </div>
              <div className="text-xs text-emerald-400 mt-1">
                100% amparado por DRE contábil
              </div>
            </div>
          </div>

          {/* Visual Bar Chart of Growth & Margin */}
          <div className="bg-[#081B33]/70 border border-white/10 rounded-xl p-4">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2 text-xs font-medium text-slate-200">
                <TrendingUp className="w-4 h-4 text-[#F59E0B]" />
                <span>Evolução do Resultado Contábil e Margem Líquida (6 meses)</span>
              </div>
              <span className="text-xs font-mono text-slate-400 tabular-nums">Base: DRE Mensal</span>
            </div>

            <div className="grid grid-cols-6 gap-2.5 items-end h-28 pt-4 px-1">
              {monthlyGrowth.map((bar) => {
                const heightPercent = Math.round((bar.receita / 255) * 100);
                return (
                  <div key={bar.month} className="flex flex-col items-center gap-1.5 h-full justify-end">
                    <span className="text-[11px] font-mono text-[#F59E0B] tabular-nums">
                      {bar.margem}%
                    </span>
                    <div className="w-full bg-white/10 rounded-t-md h-20 flex items-end overflow-hidden">
                      <div
                        className="w-full bg-gradient-to-t from-[#1769AA] to-[#38bdf8] rounded-t-md transition-all duration-200"
                        style={{ height: `${heightPercent}%` }}
                      />
                    </div>
                    <span className="text-[11px] font-mono text-slate-400">{bar.month}</span>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: Calendário Fiscal e Status de Obrigações */}
      {activeTab === 'calendario' && (
        <div className="pt-5 space-y-3">
          <div className="flex items-center justify-between text-xs text-slate-300 pb-1">
            <span className="flex items-center gap-1.5">
              <Calendar className="w-4 h-4 text-[#F59E0B]" />
              <span>Cronograma de Obrigações Fiscais, Contábeis e Trabalhistas</span>
            </span>
            <span className="font-mono text-emerald-400">Zero Atrasos</span>
          </div>

          <div className="divide-y divide-white/10 border border-white/10 rounded-xl bg-[#081B33]/80">
            {fiscalObligations.map((item) => (
              <div
                key={item.obligation}
                className="p-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs"
              >
                <div>
                  <div className="font-medium text-white">{item.obligation}</div>
                  <div className="text-slate-400 font-mono mt-0.5 tabular-nums">
                    Competência: {item.competencia} · Vencimento: {item.vencimento}
                  </div>
                </div>
                <div className="flex items-center gap-1.5 text-emerald-400 font-medium whitespace-nowrap">
                  <CheckCircle2 className="w-4 h-4 shrink-0" />
                  <span>{item.status}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: Documentos & Monitoramento de Certidões (CNDs) */}
      {activeTab === 'documentos' && (
        <div className="pt-5 space-y-3">
          <div className="flex items-center justify-between text-xs text-slate-300 pb-1">
            <span className="flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-[#F59E0B]" />
              <span>Monitoramento Automático de Regularidade Fiscal (CNDs)</span>
            </span>
            <span className="font-mono text-slate-400">Atualizado hoje</span>
          </div>

          <div className="divide-y divide-white/10 border border-white/10 rounded-xl bg-[#081B33]/80">
            {cndRecords.map((cnd) => (
              <div
                key={cnd.orgao}
                className="p-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs"
              >
                <div>
                  <div className="font-medium text-white">{cnd.orgao}</div>
                  <div className="text-slate-400 mt-0.5">{cnd.validade}</div>
                </div>
                <div className="flex items-center gap-1.5 text-emerald-400 font-mono font-medium">
                  <FileCheck className="w-4 h-4" />
                  <span>{cnd.situacao}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Bottom Action Footer inside Dashboard */}
      <div className="mt-5 pt-4 border-t border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
        <span className="text-slate-300">
          Clientes A M acompanham tudo em tempo real pelo computador ou celular.
        </span>
        <button
          type="button"
          onClick={() => onNavigate('portal-do-cliente')}
          className="text-[#F59E0B] hover:text-[#fbbf24] font-semibold inline-flex items-center gap-1 whitespace-nowrap cursor-pointer"
        >
          <span>Conhecer o Portal do Cliente</span>
          <ArrowUpRight className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
};
