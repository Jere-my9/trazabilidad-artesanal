import React, { useState } from 'react';
import { crearProducto } from '../services/api'; // <--- Importa crearProducto

// El prop addProduct ahora se usará para notificar al padre (Home.jsx) que se registró
// pero la lógica de guardado la manejará este componente con la API.
function ProductForm({ addProduct }) {
  const [productName, setProductName] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');
  const [imageFile, setImageFile] = useState(null); // Renombrado a imageFile para claridad
  const [formMessage, setFormMessage] = useState({ type: '', text: '' });
  const [loading, setLoading] = useState(false); // Nuevo estado para indicar carga

  const handleSubmit = async (e) => { // <--- Haz la función asíncrona
    e.preventDefault();

    if (!productName || !description || !tags || !imageFile) { // Usa imageFile
      setFormMessage({ type: 'error', text: 'Por favor, completa todos los campos (incluida la imagen).' });
      return;
    }

    setLoading(true); // Inicia el estado de carga
    setFormMessage({ type: '', text: '' }); // Limpia mensajes anteriores

    try {
        // Crea un objeto FormData para enviar datos y el archivo
        const formData = new FormData();
        formData.append('nombre', productName); // Asegúrate que coincida con el campo de tu modelo Django
        formData.append('descripcion', description);
        formData.append('etiquetas', tags); // Si Django espera un string separado por comas
        formData.append('imagen', imageFile); // ¡Aquí adjuntas el archivo real!

        // Llama a la función de la API para crear el producto
        const response = await crearProducto(formData); // <--- ¡Esta es la llamada crucial!

        // Si la respuesta es exitosa, el backend ya guardó el producto en la DB
        // Ahora actualiza el frontend y limpia el formulario
        setFormMessage({ type: 'success', text: 'Producto registrado exitosamente. ¡Gracias por confiar en Tinkuy!' });

        // Llama a la prop addProduct para que el componente padre (Home.jsx)
        // sepa que un nuevo producto fue añadido y pueda recargar la lista
        addProduct(response.data); // Pasa los datos del producto que devuelve el backend

        // Resetear formulario
        setProductName('');
        setDescription('');
        setTags('');
        setImageFile(null); // Limpia el estado del archivo de imagen
        // Para limpiar visualmente el input de archivo, necesitarías una ref
        e.target.reset(); // Esto puede funcionar para limpiar todos los inputs del form

    } catch (error) {
        console.error('Error al registrar producto:', error.response ? error.response.data : error.message);
        setFormMessage({ type: 'error', text: `Error al registrar el producto: ${error.response ? (JSON.stringify(error.response.data)) : error.message}` });
    } finally {
        setLoading(false); // Finaliza el estado de carga
        setTimeout(() => setFormMessage({ type: '', text: '' }), 5000);
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file); // Guarda el objeto File directamente
    } else {
      setImageFile(null);
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
            required
          />
        </div>
        <div className="full-width">
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
            required
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
        <div className="full-width">
          <label htmlFor="imageUrl" className="form-label"> {/* Este label puede ser solo "Imagen" */}
            Imagen del Producto
          </label>
          <div className="file-input-wrapper">
            <input
              type="file"
              id="imageUrl"
              className="form-file-input"
              accept="image/*"
              onChange={handleFileChange}
              required
            />
            {imageFile ? ( // Muestra el nombre del archivo seleccionado
              <p className="file-selected-text">{imageFile.name}</p>
            ) : (
              <p className="file-selected-text">Sin archivos seleccionados</p>
            )}
          </div>
        </div>
      </div>
      <div className="submit-button-wrapper">
      <button
        type="submit"
        className="submit-button"
        disabled={loading} // Deshabilita el botón mientras se está enviando
      >
        {loading ? 'Registrando...' : 'Registrar Producto'}
      </button>
      </div>
    </form>
  );
}

export default ProductForm;
