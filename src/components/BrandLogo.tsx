import React from 'react';

interface BrandLogoProps {
  variant?: 'dark' | 'light';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

/**
 * Reprodução vetorial de alta precisão da marca oficial
 * A.M CONSULTORIA CONTÁBIL (Gráfico ascendente dourado + tipografia geométrica A.M)
 * harmonizada com a paleta #081B33 (Azul Marinho Tecnológico), #F59E0B (Dourado) e #FFFFFF (Branco).
 */
export const BrandLogo: React.FC<BrandLogoProps> = ({
  variant = 'dark',
  size = 'md',
  className = ''
}) => {
  const isDarkBg = variant === 'dark';
  const textPrimary = isDarkBg ? '#FFFFFF' : '#081B33';
  const barColor = '#F59E0B';

  const dimensions = {
    sm: 'h-9',
    md: 'h-11',
    lg: 'h-16'
  }[size];

  return (
    <div className={`inline-flex items-center select-none ${className}`}>
      <svg
        viewBox="0 0 430 145"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className={`${dimensions} w-auto`}
        role="img"
        aria-label="A.M Consultoria Contábil"
      >
        {/* Seta curva de crescimento (dourada) */}
        <path
          d="M 12 85 Q 60 66 108 26"
          stroke={barColor}
          strokeWidth="6.5"
          strokeLinecap="round"
          fill="none"
        />
        <polygon points="93,18 125,13 114,42" fill={barColor} />

        {/* 4 Barras ascendentes douradas */}
        <rect x="18" y="96" width="18" height="36" rx="2" fill={barColor} />
        <rect x="46" y="80" width="18" height="52" rx="2" fill={barColor} />
        <rect x="74" y="63" width="18" height="69" rx="2" fill={barColor} />
        <rect x="102" y="45" width="18" height="87" rx="2" fill={barColor} />

        {/* Letra A geométrica */}
        <path
          d="M 188 22 C 191 16 199 16 202 22 L 240 102 C 242 106 239 110 234 110 L 220 110 C 217 110 215 108 214 105 L 209 93 L 181 93 L 176 105 C 175 108 173 110 170 110 L 156 110 C 151 110 148 106 150 102 L 188 22 Z M 195 48 L 186 74 L 204 74 L 195 48 Z"
          fill={textPrimary}
        />

        {/* Ponto central arredondado (pílula vertical entre A e M) */}
        <rect x="255" y="76" width="18" height="34" rx="5" fill={textPrimary} />

        {/* Letra M geométrica estilizada conforme a marca oficial */}
        <path
          d="M 288 24 C 288 19 294 17 298 21 L 336 63 L 374 21 C 378 17 384 19 384 24 L 384 104 C 384 108 381 110 377 110 L 363 110 C 359 110 356 108 356 104 L 356 61 L 340 79 C 337 82 333 82 330 79 L 292 37 L 288 24 Z"
          fill={textPrimary}
        />

        {/* Subtítulo CONSULTORIA CONTÁBIL */}
        <text
          x="152"
          y="134"
          fill={textPrimary}
          fontFamily="'Plus Jakarta Sans', 'Syne', sans-serif"
          fontWeight="700"
          fontSize="16.5"
          letterSpacing="1.6"
        >
          CONSULTORIA CONTÁBIL
        </text>
      </svg>
    </div>
  );
};
