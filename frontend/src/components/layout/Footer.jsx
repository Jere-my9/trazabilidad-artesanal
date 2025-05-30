import React from 'react';

function Footer() {
  return (
    <footer className="footer"> {/* Clase CSS estándar */}
      <div className="footer-content">
        <p>© {new Date().getFullYear()} Tinkuy Platform. Todos los derechos reservados.</p>
        <p>Impulsando la trazabilidad y confianza en la artesanía.</p>
      </div>
    </footer>
  );
}

export default Footer;