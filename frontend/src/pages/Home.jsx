import { listarProductos } from '../services/api';
import React, { useState } from 'react';
import ProductForm from '../components/ProductForm';
import ProductCard from '../components/ProductCard';

function Home() {
  const [products, setProducts] = useState([
    {
      id: 1,
      name: "Cerámica Artesanal 'Flor Andina'",
      description: "Jarrón de cerámica pintado a mano con motivos florales andinos, ideal para decoración.",
      imageUrl: "https://via.placeholder.com/150/FF5733/FFFFFF?text=Ceramica1", // Reemplaza con tus imágenes reales
      tags: ["Cerámica", "Decoración", "Andino"],
      iaVerified: true,
      averageConfidence: 95,
      producer: "Artesanías del Valle"
    },
    {
      id: 2,
      name: "Tejido Alpaca 'Caminos del Sol'",
      description: "Manta de alpaca tejida a mano con patrones geométricos, suave y abrigadora.",
      imageUrl: "https://via.placeholder.com/150/33FF57/FFFFFF?text=Tejido1",
      tags: ["Textil", "Alpaca", "Cultura"],
      iaVerified: false,
      averageConfidence: 70,
      producer: "Textiles Quillabamba"
    },
    {
      id: 3,
      name: "Joyería Plata 'Laguna Azul'",
      description: "Collar de plata 950 con incrustaciones de piedra turquesa, diseño inspirado en lagunas andinas.",
      imageUrl: "https://via.placeholder.com/150/5733FF/FFFFFF?text=Joyer%C3%ADa1",
      tags: ["Joyería", "Plata", "Turquesa"],
      iaVerified: true,
      averageConfidence: 88,
      producer: "Orfebrería Andina"
    },
    {
      id: 4,
      name: "Escultura Madera 'Guardían Inca'",
      description: "Figura tallada en madera de cedro, representa un guardián de la antigua civilización Inca.",
      imageUrl: "https://via.placeholder.com/150/FFBD33/FFFFFF?text=Escultura1",
      tags: ["Escultura", "Madera", "Inca"],
      iaVerified: true,
      averageConfidence: 92,
      producer: "Talla Ayacuchana"
    }
  ]);
  const [searchTerm, setSearchTerm] = useState('');

  const addProduct = (newProduct) => {
    setProducts([...products, { ...newProduct, id: products.length + 1 }]);
  };

  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    product.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="section-spacing"> {/* Contenedor principal con espaciado entre secciones */}

      {/* Sección de Bloques de Información */}
      <section>
        <h2 className="section-title">Nuestra Plataforma en Cifras</h2>
        <div className="info-blocks-grid"> {/* Grid para los bloques de información */}
          
          <div className="info-block info-block-blue">
            <h3 className="info-block-title">Productos Registrados</h3>
            <p className="info-block-value">{products.length}</p>
            <span className="emoji-icon">📦</span> {/* Emoji */}
          </div>

          <div className="info-block info-block-green">
            <h3 className="info-block-title">Verificados con IA</h3>
            <p className="info-block-value">{products.filter(p => p.iaVerified).length}</p>
            <span className="emoji-icon">✅</span> {/* Emoji */}
          </div>

          <div className="info-block info-block-orange">
            <h3 className="info-block-title">Confianza Promedio</h3>
            <p className="info-block-value">
              {products.length > 0
                ? (products.reduce((sum, p) => sum + p.averageConfidence, 0) / products.length).toFixed(0)
                : 'N/A'}%
            </p>
            <span className="emoji-icon">📈</span> {/* Emoji */}
          </div>

        </div>
      </section>

      {/* Sección del Formulario de Registro */}
      <section>
        <div className="product-form-container"> {/* Contenedor del formulario */}
          <h2 className="form-title">Registrar Nuevo Producto Artesanal</h2>
          <ProductForm addProduct={addProduct} />
        </div>
      </section>

      {/* Sección de Productos Recientes */}
      <section className="recent-products-section"> {/* Contenedor para productos recientes */}
        <div className="recent-products-header">
          <h2 className="recent-products-title">Productos Recientes</h2>
          <div className="search-input-wrapper">
            <input
              type="text"
              placeholder="Buscar productos..."
              className="search-input"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
            <div className="search-icon">
              <span className="emoji-icon">🔍</span> {/* Emoji de búsqueda */}
            </div>
          </div>
        </div>
        
        {filteredProducts.length === 0 ? (
          <p className="no-products-message">No se encontraron productos.</p>
        ) : (
          <div className="product-cards-grid"> {/* Grid para las tarjetas de producto */}
            {filteredProducts.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default Home;