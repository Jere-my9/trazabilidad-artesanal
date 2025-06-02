// frontend/src/components/ProductCard.jsx

import React from 'react';
// Importa cualquier otra cosa que necesites, como PropTypes si los usas

function ProductCard({ product }) {
  // Asegúrate de que 'product' y sus propiedades necesarias existan
  if (!product) {
    console.warn("ProductCard: 'product' prop es undefined o null. No se puede renderizar.");
    return null; // O un placeholder de error
  }

  // Proporciona valores por defecto para evitar errores si las propiedades no existen
  const { 
    id, 
    nombre, 
    descripcion, 
    precio, // si lo tienes
    imagen, 
    etiquetas, // <-- ¡Aquí está el foco!
    iaVerified, 
    averageConfidence 
  } = product;

  // Asegurarse de que 'etiquetas' sea un array antes de mapear
  const safeEtiquetas = Array.isArray(etiquetas) ? etiquetas : [];

  return (
    <div className="product-card">
      <img src={imagen} alt={nombre} className="product-card-image" />
      <div className="product-card-content">
        <h3 className="product-card-title">{nombre}</h3>
        <p className="product-card-description">{descripcion}</p>

        {/* Aplica la defensa aquí también para etiquetas/badges */}
        {safeEtiquetas.length > 0 && ( // Solo renderiza si hay etiquetas
            <div className="product-badges">
              {safeEtiquetas.map((etiqueta, index) => (
                // Usa un key único, como el índice si la etiqueta no tiene un ID único,
                // pero si las etiquetas pueden cambiar de orden, usa un ID real.
                // Para cadenas simples, el índice puede ser suficiente si no hay reordenamientos
                <span key={index} className="badge">{etiqueta}</span>
              ))}
            </div>
        )}

        <div className="badge-verified">
          {iaVerified && (
            <>
              <span className="emoji-icon">✅</span>
              <span>Verificado por IA</span>
            </>
          )}
        </div>
        <div className="product-card-footer">
          <p className="product-card-ia">Confianza IA: {averageConfidence ? averageConfidence.toFixed(0) : 'N/A'}%</p>
          {/* Añade el campo productor aquí si lo tienes */}
          {/* <p className="product-card-producer">Productor: {productorNombre}</p> */}
        </div>
      </div>
    </div>
  );
}

export default ProductCard;