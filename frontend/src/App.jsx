import React from 'react';
import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import Home from './pages/Home';

function App() {
  return (
    <div id="root"> {/* Este es el contenedor principal con el fondo claro y el flex-column */}
      <Header />
      <main className="main-content section-spacing"> {/* Aplica clases CSS estándar para el contenido principal */}
        <Home />
      </main>
      <Footer />
    </div>
  );
}

export default App;