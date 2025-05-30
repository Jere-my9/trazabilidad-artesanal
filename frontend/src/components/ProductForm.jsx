import React, { useState } from 'react';

function ProductForm({ addProduct }) {
  const [productName, setProductName] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');
  const [imageUrl, setImageUrl] = useState(null); // Para almacenar el objeto File o URL temporal
  const [formMessage, setFormMessage] = useState({ type: '', text: '' }); // {type: 'success'|'error', text: 'Mensaje'}

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!productName || !description || !tags || !imageUrl) {
      setFormMessage({ type: 'error', text: 'Por favor, completa todos los campos.' });
      return;
    }

    const newProduct = {
      name: productName,
      description,
      tags: tags.split(',').map(tag => tag.trim()).filter(tag => tag !== ''),
      imageUrl: typeof imageUrl === 'string' ? imageUrl : URL.createObjectURL(imageUrl), // Usar URL temporal si es un File
      iaVerified: Math.random() > 0.5, // Simular verificación IA
      averageConfidence: Math.floor(Math.random() * 40) + 60, // Simular confianza 60-100
      producer: "Artesano Ejemplo" // Puedes hacer que esto sea un input si es necesario
    };

    addProduct(newProduct);

    // Resetear formulario
    setProductName('');
    setDescription('');
    setTags('');
    setImageUrl(null);
    setFormMessage({ type: 'success', text: 'Producto registrado exitosamente. ¡Gracias por confiar en Tinkuy!' });

    // Opcional: Limpiar mensaje después de un tiempo
    setTimeout(() => setFormMessage({ type: '', text: '' }), 5000);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageUrl(file);
    } else {
      setImageUrl(null);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {formMessage.type === 'success' && (
        <div className="form-message-success">{formMessage.text}</div>
      )}
      {formMessage.type === 'error' && (
        <div className="form-message-error">{formMessage.text}</div>
      )}

      <div className="form-grid">
        <div>
          <label htmlFor="productName" className="form-label">
            Nombre del Producto
          </label>
          <input
            type="text"
            id="productName"
            className="form-input"
            placeholder="Ej: Manta Andina de Alpaca"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
          />
        </div>
        <div className="full-width"> {/* Clase para que ocupe todo el ancho en móvil, o 2 columnas en md */}
          <label htmlFor="description" className="form-label">
            Descripción del Producto
          </label>
          <textarea
            id="description"
            rows="4"
            className="form-textarea"
            placeholder="Describe las características, materiales, y técnicas usadas."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <div>
          <label htmlFor="tags" className="form-label">
            Etiquetas (separadas por comas)
          </label>
          <input
            type="text"
            id="tags"
            className="form-input"
            placeholder="Ej: tejido, alpaca, peruano, artesanal"
            value={tags}
            onChange={(e) => setTags(e.target.value)}
          />
        </div>
        <div className="full-width"> {/* Este div ya tenía la clase "full-width" correctamente */}
          <label htmlFor="imageUrl" className="form-label">
            Imagen del Producto
          </label>
          {/* INICIO DEL CÓDIGO ACTUALIZADO PARA IMAGEN DEL PRODUCTO */}
          <div className="file-input-wrapper">
            <input
              type="file"
              id="imageUrl"
              className="form-file-input"
              accept="image/*"
              onChange={handleFileChange}
            />
            {imageUrl ? ( // Si hay imagen, muestra su nombre
              <p className="file-selected-text">
                {typeof imageUrl === 'string' ? imageUrl : imageUrl.name}
              </p>
            ) : ( // Si no hay imagen, muestra el texto por defecto
              <p className="file-selected-text">Sin archivos seleccionados</p>
            )}
          </div>
          {/* FIN DEL CÓDIGO ACTUALIZADO */}
        </div>
      </div>
      <div className="submit-button-wrapper">
        <button
          type="submit"
          className="submit-button"
        >
          Registrar Producto
        </button>
      </div>
    </form>
  );
}

export default ProductForm;
