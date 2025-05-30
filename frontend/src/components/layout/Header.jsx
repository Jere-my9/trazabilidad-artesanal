import React from 'react';

function Header() {
  return (
    <header className="header"> {/* Clase CSS estándar */}
      <div className="header-container"> {/* Clase CSS estándar */}
        <div className="header-logo"> {/* Clase CSS estándar */}
          <span className="header-logo-icon">🛡️</span> {/* Emoji para el logo */}
          <p className="header-title">Tinkuy Platform</p> {/* Clase CSS estándar */}
        </div>
        {/* Eliminamos completamente la sección <nav> */}
        <span className="header-tagline">Trazabilidad y Confianza Artesanal</span> {/* Clase CSS estándar */}
      </div>
    </header>
  );
}

export default Header;
  
  