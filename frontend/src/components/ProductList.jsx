import React, { useEffect, useState } from 'react';
import { listarProductos } from '../services/api';
import ProductCard from './ProductCard';

export default function ProductList() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/productos/') // Ajusta la URL si es necesario
      .then(res => res.json())
      .then(data => setProductos(data));
  }, []);

  return (
    <div className="max-w-7xl mx-auto p-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-6">Productos Registrados</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {productos.map(producto => (
          <ProductCard key={producto.id} producto={producto} />
        ))}
      </div>
    </div>
  );
}
