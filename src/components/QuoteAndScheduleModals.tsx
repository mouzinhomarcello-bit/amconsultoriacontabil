import React, { useState } from 'react';
import {
  CheckCircle2,
  Calendar,
  Clock,
  Send,
  MessageSquare,
  Calculator,
  ArrowRight,
  ShieldCheck
} from 'lucide-react';
import { LeadRecord, AppointmentRecord, SiteConfig } from '../data/siteData';

interface QuoteFormSectionProps {
  config: SiteConfig;
  defaultService?: string;
  defaultRegime?: string;
  origemLabel?: string;
  onAddLead: (lead: Omit<LeadRecord, 'id' | 'data' | 'stage'>) => void;
  onOpenWhatsApp: (customMessage?: string) => void;
}

export const QuoteFormSection: React.FC<QuoteFormSectionProps> = ({
  config,
  defaultService = 'Contabilidade',
  defaultRegime = 'Simples Nacional',
  origemLabel = 'Formulário de Orçamento do Site',
  onAddLead,
  onOpenWhatsApp
}) => {
  const [nome, setNome] = useState('');
  const [empresa, setEmpresa] = useState('');
  const [cnpj, setCnpj] = useState('');
  const [whatsapp, setWhatsapp] = useState('');
  const [email, setEmail] = useState('');
  const [cidadeUf, setCidadeUf] = useState('Manaus/AM');
  const [regimeTributario, setRegimeTributario] = useState(defaultRegime);
  const [servicoDesejado, setServicoDesejado] = useState(defaultService);
  const [mensagem, setMensagem] = useState('');
  const [lgpdAccepted, setLgpdAccepted] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');
  const [submittedLead, setSubmittedLead] = useState<{
    nome: string;
    empresa: string;
    servicoDesejado: string;
    regimeTributario: string;
  } | null>(null);

  const formatCnpjOrPhone = (value: string, type: 'cnpj' | 'phone') => {
    const digits = value.replace(/\D/g, '');
    if (type === 'phone') {
      if (digits.length <= 2) return digits;
      if (digits.length <= 7) return `(${digits.slice(0, 2)}) ${digits.slice(2)}`;
      return `(${digits.slice(0, 2)}) ${digits.slice(2, 7)}-${digits.slice(7, 11)}`;
    }
    if (digits.length <= 2) return digits;
    if (digits.length <= 5) return `${digits.slice(0, 2)}.${digits.slice(2)}`;
    if (digits.length <= 8) return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5)}`;
    if (digits.length <= 12) {
      return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5, 8)}/${digits.slice(8)}`;
    }
    return `${digits.slice(0, 2)}.${digits.slice(2, 5)}.${digits.slice(5, 8)}/${digits.slice(8, 12)}-${digits.slice(12, 14)}`;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!nome.trim() || !whatsapp.trim() || !email.trim()) {
      setErrorMsg('Por favor, preencha seu nome, WhatsApp e e-mail corporativo para receber a proposta.');
      return;
    }
    if (!email.includes('@')) {
      setErrorMsg('Informe um endereço de e-mail válido.');
      return;
    }
    if (!lgpdAccepted) {
      setErrorMsg('É necessário concordar com a Política de Privacidade (LGPD) para o envio.');
      return;
    }

    setErrorMsg('');
    onAddLead({
      nome: nome.trim(),
      empresa: empresa.trim() || 'Não informada',
      cnpj: cnpj.trim() || 'Em apuração / Nova',
      whatsapp: whatsapp.trim(),
      email: email.trim(),
      cidadeUf: cidadeUf.trim() || 'Manaus/AM',
      regimeTributario,
      servicoDesejado,
      mensagem: mensagem.trim() || 'Solicitação de proposta comercial via site.',
      origem: origemLabel,
      campanha: 'Conversao_Direta_Site'
    });

    setSubmittedLead({
      nome: nome.trim(),
      empresa: empresa.trim() || 'Minha Empresa',
      servicoDesejado,
      regimeTributario
    });
  };

  if (submittedLead) {
    const customWppText = `Olá, sou ${submittedLead.nome} da empresa ${submittedLead.empresa}. Acabei de solicitar uma proposta no site da A M Consultoria para *${submittedLead.servicoDesejado}* (Regime: ${submittedLead.regimeTributario}) e gostaria de agilizar o atendimento.`;

    return (
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="w-12 h-12 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-700 mb-4">
          <CheckCircle2 className="w-6 h-6" />
        </div>
        <h3 className="font-display text-2xl font-bold text-[#081B33]">
          Solicitação registrada com sucesso
        </h3>
        <p className="text-slate-600 mt-2 text-sm leading-relaxed">
          Recebemos os dados de <strong>{submittedLead.empresa}</strong> em nossa base comercial. Um sócio-consultor da A M analisará seu perfil ({submittedLead.regimeTributario} · {submittedLead.servicoDesejado}) e entrará em contato.
        </p>

        <div className="mt-6 p-4 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-600 space-y-1 font-mono">
          <div>Protocolo de Atendimento: AM-{Math.floor(100000 + Math.random() * 900000)}</div>
          <div>E-mail Oficial: {config.email}</div>
          <div>Central Direta: {config.telefonePrincipal}</div>
        </div>

        <div className="mt-6 flex flex-col sm:flex-row gap-3">
          <button
            type="button"
            onClick={() => onOpenWhatsApp(customWppText)}
            className="px-5 py-3 bg-emerald-600 hover:bg-emerald-700 text-white text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer"
          >
            <MessageSquare className="w-4 h-4" />
            <span>Agilizar atendimento no WhatsApp agora</span>
          </button>
          <button
            type="button"
            onClick={() => {
              setSubmittedLead(null);
              setNome('');
              setEmpresa('');
              setCnpj('');
              setMensagem('');
            }}
            className="px-4 py-3 border border-slate-300 hover:bg-slate-50 text-slate-700 text-sm font-medium rounded-xl transition-colors cursor-pointer"
          >
            Enviar outra solicitação
          </button>
        </div>
      </div>
    );
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5"
      noValidate
    >
      <div className="border-b border-slate-100 pb-4">
        <div className="text-xs text-[#1769AA] font-semibold">
          Proposta Personalizada · Resposta Rápida
        </div>
        <h3 className="font-display text-xl sm:text-2xl font-bold text-[#081B33] mt-1">
          Solicite uma avaliação e orçamento para sua empresa
        </h3>
        <p className="text-sm text-slate-600 mt-1">
          Preencha os dados abaixo para receber um diagnóstico contábil e tributário sem compromisso.
        </p>
      </div>

      {errorMsg && (
        <div className="p-3.5 bg-red-50 border border-red-200 rounded-xl text-xs font-medium text-red-700">
          {errorMsg}
        </div>
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Seu Nome Completo *
          </label>
          <input
            type="text"
            required
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            placeholder="Ex.: João Paulo Mendes"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Nome da Empresa
          </label>
          <input
            type="text"
            value={empresa}
            onChange={(e) => setEmpresa(e.target.value)}
            placeholder="Razão Social ou Nome Fantasia"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            CNPJ (opcional se empresa nova)
          </label>
          <input
            type="text"
            value={cnpj}
            onChange={(e) => setCnpj(formatCnpjOrPhone(e.target.value, 'cnpj'))}
            placeholder="00.000.000/0001-00"
            className="w-full px-3.5 py-2.5 text-sm font-mono bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            WhatsApp com DDD *
          </label>
          <input
            type="tel"
            required
            value={whatsapp}
            onChange={(e) => setWhatsapp(formatCnpjOrPhone(e.target.value, 'phone'))}
            placeholder="(92) 99999-9999"
            className="w-full px-3.5 py-2.5 text-sm font-mono bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            E-mail Corporativo *
          </label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="voce@suaempresa.com.br"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Cidade / UF
          </label>
          <input
            type="text"
            value={cidadeUf}
            onChange={(e) => setCidadeUf(e.target.value)}
            placeholder="Manaus/AM"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Regime Tributário Atual
          </label>
          <select
            value={regimeTributario}
            onChange={(e) => setRegimeTributario(e.target.value)}
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          >
            <option value="Simples Nacional">Simples Nacional</option>
            <option value="Lucro Presumido">Lucro Presumido</option>
            <option value="Lucro Real">Lucro Real</option>
            <option value="Não sei">Não sei informar</option>
            <option value="Empresa nova">Empresa nova (Em abertura)</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Serviço Desejado
          </label>
          <select
            value={servicoDesejado}
            onChange={(e) => setServicoDesejado(e.target.value)}
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
          >
            <option value="Contabilidade">Contabilidade Mensal</option>
            <option value="Fiscal">Fiscal e Tributário</option>
            <option value="Departamento Pessoal">Departamento Pessoal</option>
            <option value="Consultoria">Consultoria Contábil / Financeira</option>
            <option value="Auditoria">Auditoria Contábil e Tributária</option>
            <option value="Troca de contador">Troca de contador</option>
            <option value="Abertura de empresa">Abertura de empresa</option>
            <option value="Outro">Outro objetivo</option>
          </select>
        </div>
      </div>

      <div>
        <label className="block text-xs font-semibold text-slate-700 mb-1.5">
          Conte brevemente sobre a necessidade da sua empresa
        </label>
        <textarea
          rows={3}
          value={mensagem}
          onChange={(e) => setMensagem(e.target.value)}
          placeholder="Ex.: Quantidade aproximada de notas fiscais/mês, número de funcionários ou dúvidas sobre impostos..."
          className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] focus:bg-white text-[#081B33]"
        />
      </div>

      <div className="flex items-start gap-2.5 pt-1">
        <input
          id="lgpd-consent"
          type="checkbox"
          checked={lgpdAccepted}
          onChange={(e) => setLgpdAccepted(e.target.checked)}
          className="mt-1 rounded border-slate-300 text-[#1769AA] focus:ring-[#1769AA]"
        />
        <label htmlFor="lgpd-consent" className="text-xs text-slate-600 leading-relaxed">
          Concordo com o tratamento dos meus dados exclusivamente para retorno comercial da{' '}
          <strong>A M Consultoria e Auditoria Contábil Ltda</strong>, nos termos da Lei Geral de Proteção de Dados (Lei nº 13.709/2018 — LGPD).
        </label>
      </div>

      <div className="pt-2 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <button
          type="submit"
          className="px-6 py-3.5 bg-[#081B33] hover:bg-[#1769AA] text-white text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer whitespace-nowrap"
        >
          <Send className="w-4 h-4 text-[#F59E0B]" />
          <span>Solicitar proposta</span>
        </button>

        <div className="flex items-center gap-1.5 text-xs text-slate-500">
          <ShieldCheck className="w-4 h-4 text-[#1769AA] shrink-0" />
          <span>Seus dados estão protegidos por sigilo contábil e HTTPS.</span>
        </div>
      </div>
    </form>
  );
};

interface ScheduleMeetingSectionProps {
  config: SiteConfig;
  onAddAppointment: (app: Omit<AppointmentRecord, 'id' | 'criadoEm' | 'status'>) => void;
  onOpenWhatsApp: (customMessage?: string) => void;
}

export const ScheduleMeetingSection: React.FC<ScheduleMeetingSectionProps> = ({
  config,
  onAddAppointment,
  onOpenWhatsApp
}) => {
  const [assunto, setAssunto] = useState('Diagnóstico para Troca de Contador');
  const [data, setData] = useState('2026-09-30');
  const [horario, setHorario] = useState('10:00');
  const [nome, setNome] = useState('');
  const [empresa, setEmpresa] = useState('');
  const [whatsapp, setWhatsapp] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const [confirmed, setConfirmed] = useState(false);

  const timeSlots = ['09:00', '10:00', '11:00', '14:30', '16:00', '17:00'];

  const handleSchedule = (e: React.FormEvent) => {
    e.preventDefault();
    if (!nome.trim() || !whatsapp.trim() || !email.trim() || !data) {
      setError('Preencha nome, WhatsApp, e-mail e escolha uma data para confirmar a reunião.');
      return;
    }
    setError('');
    onAddAppointment({
      assunto,
      data,
      horario,
      nome: nome.trim(),
      empresa: empresa.trim() || 'Empresa não informada',
      whatsapp: whatsapp.trim(),
      email: email.trim()
    });
    setConfirmed(true);
  };

  if (confirmed) {
    const msg = `Olá! Agendei pelo site uma conversa sobre *${assunto}* para o dia ${data} às ${horario}. Meu nome é ${nome} (${empresa || 'Empresa'}).`;
    return (
      <div className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
        <div className="w-12 h-12 rounded-xl bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-700 mb-4">
          <Calendar className="w-6 h-6" />
        </div>
        <h3 className="font-display text-2xl font-bold text-[#081B33]">
          Reunião pré-agendada com sucesso
        </h3>
        <p className="text-sm text-slate-600 mt-2">
          Reservamos o horário de <strong>{horario}</strong> na data <strong>{data}</strong> para tratar sobre <strong>{assunto}</strong>. Você pode optar por reunião online (Google Meet) ou presencial em nossa sede no Dom Pedro I, Manaus/AM.
        </p>
        <div className="mt-6 flex flex-col sm:flex-row gap-3">
          <button
            type="button"
            onClick={() => onOpenWhatsApp(msg)}
            className="px-5 py-3 bg-emerald-600 hover:bg-emerald-700 text-white text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 cursor-pointer"
          >
            <MessageSquare className="w-4 h-4" />
            <span>Confirmar link da reunião via WhatsApp</span>
          </button>
          <button
            type="button"
            onClick={() => setConfirmed(false)}
            className="px-4 py-3 border border-slate-300 text-slate-700 text-sm font-medium rounded-xl hover:bg-slate-50 cursor-pointer"
          >
            Alterar horário
          </button>
        </div>
      </div>
    );
  }

  return (
    <form
      onSubmit={handleSchedule}
      className="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5"
    >
      <div className="border-b border-slate-100 pb-4">
        <div className="text-xs text-[#1769AA] font-semibold">
          Atendimento Consultivo · Online ou Presencial em Manaus
        </div>
        <h3 className="font-display text-xl sm:text-2xl font-bold text-[#081B33] mt-1">
          Agendar uma conversa com um especialista
        </h3>
        <p className="text-sm text-slate-600 mt-1">
          Escolha o assunto, a data e o melhor horário para conversar diretamente com os sócios da A M.
        </p>
      </div>

      {error && (
        <div className="p-3.5 bg-red-50 border border-red-200 rounded-xl text-xs font-medium text-red-700">
          {error}
        </div>
      )}

      <div>
        <label className="block text-xs font-semibold text-slate-700 mb-1.5">
          Pauta / Assunto da Reunião
        </label>
        <select
          value={assunto}
          onChange={(e) => setAssunto(e.target.value)}
          className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] text-[#081B33]"
        >
          <option value="Diagnóstico para Troca de Contador">Diagnóstico para Troca de Contador</option>
          <option value="Planejamento de Abertura de Empresa">Planejamento de Abertura de Empresa</option>
          <option value="Revisão e Planejamento Tributário">Revisão e Planejamento Tributário</option>
          <option value="Auditoria Contábil e Fiscal">Auditoria Contábil e Fiscal</option>
          <option value="Organização Contábil e Financeira">Organização Contábil e Financeira</option>
        </select>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Data Preferencial *
          </label>
          <input
            type="date"
            value={data}
            onChange={(e) => setData(e.target.value)}
            className="w-full px-3.5 py-2.5 text-sm font-mono bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA] text-[#081B33]"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Horário (Manaus GMT-4) *
          </label>
          <div className="grid grid-cols-3 gap-1.5">
            {timeSlots.map((slot) => (
              <button
                key={slot}
                type="button"
                onClick={() => setHorario(slot)}
                className={`py-2 text-xs font-mono rounded-lg border transition-colors cursor-pointer ${
                  horario === slot
                    ? 'bg-[#081B33] text-white border-[#081B33] font-semibold'
                    : 'bg-slate-50 text-slate-700 border-slate-200 hover:border-slate-400'
                }`}
              >
                {slot}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Seu Nome *
          </label>
          <input
            type="text"
            required
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            placeholder="Nome completo"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA]"
          />
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            Empresa
          </label>
          <input
            type="text"
            value={empresa}
            onChange={(e) => setEmpresa(e.target.value)}
            placeholder="Nome da empresa"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA]"
          />
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            WhatsApp *
          </label>
          <input
            type="tel"
            required
            value={whatsapp}
            onChange={(e) => setWhatsapp(e.target.value)}
            placeholder="(92) 99999-9999"
            className="w-full px-3.5 py-2.5 text-sm font-mono bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA]"
          />
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1.5">
            E-mail *
          </label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="contato@empresa.com.br"
            className="w-full px-3.5 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:border-[#1769AA]"
          />
        </div>
      </div>

      <div className="pt-2 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <button
          type="submit"
          className="px-6 py-3.5 bg-[#1769AA] hover:bg-[#081B33] text-white text-sm font-semibold rounded-xl inline-flex items-center justify-center gap-2 transition-colors cursor-pointer"
        >
          <Clock className="w-4 h-4" />
          <span>Confirmar agendamento</span>
        </button>
        <span className="text-xs text-slate-500">
          Atendimento: {config.horarioAtendimento}
        </span>
      </div>
    </form>
  );
};

interface TaxDiagnosticSimulatorProps {
  onSelectQuoteWithContext: (service: string, regime: string) => void;
}

export const TaxDiagnosticSimulator: React.FC<TaxDiagnosticSimulatorProps> = ({
  onSelectQuoteWithContext
}) => {
  const [faturamentoMensal, setFaturamentoMensal] = useState(85000);
  const [folhaMensal, setFolhaMensal] = useState(25000);
  const [segmento, setSegmento] = useState<'servicos' | 'comercio' | 'engenharia'>('servicos');

  const fatorR = faturamentoMensal > 0 ? (folhaMensal / faturamentoMensal) * 100 : 0;
  const enquadraAnexoIII = fatorR >= 28;

  // Estimativa orientativa transparente
  const aliquotaSimplesSemPlanejamento =
    segmento === 'comercio' ? 0.088 : enquadraAnexoIII ? 0.095 : 0.165;
  const aliquotaOtimizadaAM =
    segmento === 'comercio'
      ? 0.068
      : enquadraAnexoIII
        ? 0.082
        : 0.105;

  const custoAtual = Math.round(faturamentoMensal * aliquotaSimplesSemPlanejamento);
  const custoOtimizado = Math.round(faturamentoMensal * aliquotaOtimizadaAM);
  const diferencaAnual = Math.max(1200, (custoAtual - custoOtimizado) * 12);

  return (
    <div className="bg-[#081B33] text-white rounded-2xl p-6 sm:p-8 border border-white/10">
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-6 border-b border-white/10">
        <div>
          <div className="text-xs text-[#F59E0B] font-semibold">
            Ferramenta Interativa · Inteligência Tributária A M
          </div>
          <h3 className="font-display text-2xl font-bold text-white mt-1">
            Diagnóstico Preliminar de Enquadramento Tributário
          </h3>
          <p className="text-sm text-slate-300 mt-1">
            Simule o impacto do Fator R, segregação de receitas e escolha entre Simples Nacional e Lucro Presumido.
          </p>
        </div>
        <div className="flex items-center gap-2 text-xs text-slate-300 font-mono">
          <Calculator className="w-4 h-4 text-[#F59E0B]" />
          <span>Cálculo paramétrico orientativo</span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 pt-6 items-center">
        <div className="lg:col-span-7 space-y-5">
          <div>
            <label className="block text-xs font-medium text-slate-300 mb-2">
              Segmento Principal da Empresa
            </label>
            <div className="grid grid-cols-3 gap-2">
              {[
                { id: 'servicos', label: 'Serviços / Saúde / TI' },
                { id: 'engenharia', label: 'Engenharia / B2B' },
                { id: 'comercio', label: 'Comércio / Manaus' }
              ].map((seg) => (
                <button
                  key={seg.id}
                  type="button"
                  onClick={() => setSegmento(seg.id as 'servicos' | 'comercio' | 'engenharia')}
                  className={`py-2.5 px-3 text-xs font-medium rounded-lg border transition-colors cursor-pointer ${
                    segmento === seg.id
                      ? 'bg-[#1769AA] text-white border-[#38bdf8]'
                      : 'bg-white/5 text-slate-300 border-white/10 hover:bg-white/10'
                  }`}
                >
                  {seg.label}
                </button>
              ))}
            </div>
          </div>

          <div>
            <div className="flex justify-between text-xs mb-1.5">
              <span className="text-slate-300">Faturamento Bruto Mensal Estimado</span>
              <span className="font-mono font-semibold text-white tabular-nums">
                R$ {faturamentoMensal.toLocaleString('pt-BR')}
              </span>
            </div>
            <input
              type="range"
              min={15000}
              max={400000}
              step={5000}
              value={faturamentoMensal}
              onChange={(e) => setFaturamentoMensal(Number(e.target.value))}
              className="w-full accent-[#F59E0B] cursor-pointer"
            />
          </div>

          <div>
            <div className="flex justify-between text-xs mb-1.5">
              <span className="text-slate-300">Folha de Pagamento + Pró-Labore Mensal</span>
              <span className="font-mono font-semibold text-white tabular-nums">
                R$ {folhaMensal.toLocaleString('pt-BR')} ({fatorR.toFixed(1)}% Fator R)
              </span>
            </div>
            <input
              type="range"
              min={2000}
              max={120000}
              step={1000}
              value={folhaMensal}
              onChange={(e) => setFolhaMensal(Number(e.target.value))}
              className="w-full accent-[#1769AA] cursor-pointer"
            />
          </div>
        </div>

        <div className="lg:col-span-5 bg-[#0D2544] border border-white/15 rounded-xl p-5 space-y-4">
          <div className="text-xs text-slate-300">
            Diagnóstico Técnico Recomendado:
          </div>
          <div className="text-sm font-semibold text-white">
            {segmento === 'comercio'
              ? 'Revisão de ICMS-AM, NCM Monofásico e Benefícios ZFM'
              : enquadraAnexoIII
                ? 'Enquadramento Anexo III (Fator R >= 28%) vs. Lucro Presumido'
                : 'Alerta de Alíquota Elevada (Anexo V) · Oportunidade de Planejamento'}
          </div>

          <div className="grid grid-cols-2 gap-3 pt-2 border-t border-white/10">
            <div>
              <div className="text-[11px] text-slate-400">Índice Fator R Atual</div>
              <div className="text-lg font-mono font-semibold text-white tabular-nums">
                {fatorR.toFixed(1)}%
              </div>
            </div>
            <div>
              <div className="text-[11px] text-slate-400">Potencial Revisão Anual</div>
              <div className="text-lg font-mono font-semibold text-[#F59E0B] tabular-nums">
                R$ {diferencaAnual.toLocaleString('pt-BR')}
              </div>
            </div>
          </div>

          <button
            type="button"
            onClick={() =>
              onSelectQuoteWithContext(
                'Fiscal',
                faturamentoMensal > 180000 ? 'Lucro Presumido' : 'Simples Nacional'
              )
            }
            className="w-full py-3 px-4 bg-[#F59E0B] hover:bg-[#fbbf24] text-[#081B33] text-xs font-semibold rounded-lg inline-flex items-center justify-center gap-2 transition-colors cursor-pointer"
          >
            <span>Solicitar estudo tributário completo</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};
