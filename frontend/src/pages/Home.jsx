import React, { useState, useEffect } from 'react';
import ProductForm from '../components/ProductForm';
import ProductCard from '../components/ProductCard';
import { listarProductos } from '../services/api';

function Home() {
  const [products, setProducts] = useState([]);
  const [loadingProducts, setLoadingProducts] = useState(true);
  const [errorProducts, setErrorProducts] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  const fetchProducts = async () => {
    setLoadingProducts(true);
    setErrorProducts(null);
    try {
      console.log("Home: Intentando listar productos del backend...");
      const response = await listarProductos();
      const productsData = response.data;
    
      console.log("Home: Respuesta de la API (productsData):", productsData); // Debug log
      if (Array.isArray(productsData)) {
        setProducts(productsData);
        console.log("Home: Productos cargados y establecidos:", productsData); // Debug log
      } else {
        console.error("Home: La respuesta de la API no es un array:", productsData);
        setErrorProducts('Formato de datos de productos inesperado del servidor.');
        setProducts([]); // Asegurarse de que 'products' siempre sea un array
      }
    
    } catch (err) {
      console.error("Home: Error al cargar productos:", err.response ? err.response.data : err.message);
      setErrorProducts('No se pudieron cargar los productos del servidor.');
      setProducts([]); // Asegurarse de que 'products' siempre sea un array
    } finally {
      setLoadingProducts(false);
    }
  };

  // *** EFECTO PARA CARGAR PRODUCTOS AL MONTAR EL COMPONENTE ***
  useEffect(() => {
    fetchProducts();
  }, []); // El array vacío [] asegura que se ejecuta solo una vez al montar

  // *** FUNCIÓN PARA MANEJAR EL REGISTRO EXITOSO DESDE PRODUCTFORM ***
  // Esta función ahora solo gatillará una recarga de los productos desde el backend
  const handleProductRegistered = (newProductData) => { // newProductData es el producto devuelto por el backend
    console.log("Home: Producto registrado exitosamente. Recargando lista...");
    // Podrías añadir el newProductData directamente, pero recargar es más seguro
    // para reflejar cualquier cambio o procesamiento en el backend.
    fetchProducts();
  };


  // REVISIÓN DE LA FUNCIÓN filteredProducts
  const filteredProducts = Array.isArray(products) // Asegurarse que 'products' sea un array antes de filtrar
    ? products.filter(product => {
        const nombre = product.nombre ? String(product.nombre).toLowerCase() : ''; // String() para asegurar que es un string
        const descripcion = product.descripcion ? String(product.descripcion).toLowerCase() : ''; // String() para asegurar que es un string
        const term = String(searchTerm || '').toLowerCase(); // String() y || '' para asegurar que searchTerm es un string

        return (
          nombre.includes(term) ||
          descripcion.includes(term)
        );
      })
    : []; // Si 'products' no es un array, devuelve un array vacío para filteredProducts

  console.log("Home: Estado actual de products (antes del render):", products); // Debug log
  console.log("Home: Estado actual de filteredProducts (antes del render):", filteredProducts); // Debug log

  return (
    <div className="section-spacing">

      {/* Sección de Bloques de Información */}
      <section>
        <h2 className="section-title">Nuestra Plataforma en Cifras</h2>
        <div className="info-blocks-grid">
          <div className="info-block info-block-blue">
            <h3 className="info-block-title">Productos Registrados</h3>
            {/* Asegúrate que esto muestre la cantidad real de productos cargados */}
            <p className="info-block-value">{products.length}</p>
            <span className="emoji-icon">📦</span>
          </div>

          <div className="info-block info-block-green">
            <h3 className="info-block-title">Verificados con IA</h3>
            {/* Asegúrate que iaVerified y averageConfidence vengan del backend */}
            <p className="info-block-value">{products.filter(p => p.iaVerified).length}</p>
            <span className="emoji-icon">✅</span>
          </div>

          <div className="info-block info-block-orange">
            <h3 className="info-block-title">Confianza Promedio</h3>
            <p className="info-block-value">
              {products.length > 0
                ? (products.reduce((sum, p) => sum + p.averageConfidence, 0) / products.length).toFixed(0)
                : 'N/A'}%
            </p>
            <span className="emoji-icon">📈</span>
          </div>
        </div>
      </section>

      {/* Sección del Formulario de Registro */}
      <section>
        <div className="product-form-container">
          <h2 className="form-title">Registrar Nuevo Producto Artesanal</h2>
          {/* ¡Pasa la nueva función handleProductRegistered como prop! */}
          <ProductForm addProduct={handleProductRegistered} />
        </div>
      </section>

      {/* Sección de Productos Recientes */}
      <section className="recent-products-section">
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
              <span className="emoji-icon">🔍</span>
            </div>
          </div>
        </div>

        {loadingProducts && <p>Cargando productos...</p>}
        {errorProducts && <p className="error-message" style={{ color: 'red' }}>{errorProducts}</p>}

        {/* Solo renderiza si no está cargando y no hay errores */}
        {!loadingProducts && !errorProducts && (
          filteredProducts && filteredProducts.length > 0 ? ( // Asegura que filteredProducts no sea undefined y tenga elementos
            <div className="product-cards-grid">
              {filteredProducts.map(product => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          ) : (
            <p className="no-products-message">No se encontraron productos.</p>
          )
        )}
      </section>
    </div>
  );
}

export default Home;