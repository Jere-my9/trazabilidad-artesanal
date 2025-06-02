// frontend/src/pages/Home.jsx
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
      // MODIFICACIÓN CLAVE AQUÍ: Acceder a response.data
      const response = await listarProductos();
      const productsData = response.data; // <-- ¡Accede a la propiedad 'data' del objeto de respuesta!

      // Asegurarse de que productsData es un array antes de establecerlo
      if (Array.isArray(productsData)) {
        setProducts(productsData);
        console.log("Home: Productos cargados:", productsData);
      } else {
        // Manejar el caso si response.data no es un array (aunque no debería pasar si el backend es RESTful)
        console.error("Home: La respuesta de la API no es un array:", productsData);
        setErrorProducts('Formato de datos de productos inesperado del servidor.');
      }

    } catch (err) {
      console.error("Home: Error al cargar productos:", err.response ? err.response.data : err.message);
      setErrorProducts('No se pudieron cargar los productos del servidor.');
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


  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    product.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
    product.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase())) // También busca por etiquetas
  );

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

        {loadingProducts && <p>Cargando productos...</p>} {/* Muestra mensaje de carga */}
        {errorProducts && <p className="error-message" style={{ color: 'red' }}>{errorProducts}</p>} {/* Muestra mensaje de error */}

        {!loadingProducts && !errorProducts && filteredProducts.length === 0 ? (
          <p className="no-products-message">No se encontraron productos.</p>
        ) : (
          // Solo muestra el grid si no hay carga ni error y hay productos
          !loadingProducts && !errorProducts && (
            <div className="product-cards-grid">
              {filteredProducts.map(product => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          )
        )}
      </section>
    </div>
  );
}

export default Home;