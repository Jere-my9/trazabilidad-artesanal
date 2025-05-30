import React from 'react';

function ProductCard({ product }) {
  const { name, description, imageUrl, tags, iaVerified, averageConfidence, producer } = product;

  return (
    <div className="product-card"> {/* Clase CSS estándar */}
      <img src={imageUrl} alt={name} className="product-card-image" /> {/* Clase CSS estándar */}
      <div className="product-card-content"> {/* Clase CSS estándar */}
        <h3 className="product-card-title">{name}</h3> {/* Clase CSS estándar */}
        <p className="product-card-description">{description}</p> {/* Clase CSS estándar */}
        
        <div className="product-card-badges"> {/* Clase CSS estándar */}
          {tags.map((tag, index) => (
            <span key={index} className="badge"> {/* Clase CSS estándar */}
              {tag}
            </span>
          ))}
        </div>

        {iaVerified && (
          <div className="badge-verified"> {/* Clase CSS estándar */}
            <span className="emoji-icon">✅</span> {/* Emoji */}
            <span>Verificado por IA</span>
          </div>
        )}

        <div className="product-card-footer"> {/* Clase CSS estándar */}
          <p className="product-card-ia">Confianza IA: {averageConfidence}%</p> {/* Clase CSS estándar */}
          <p className="product-card-producer">{producer}</p> {/* Nueva clase si necesitas estilizar el productor */}
        </div>
      </div>
    </div>
  );
}

export default ProductCard;