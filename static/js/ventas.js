/* ============================================================
   ventas.js  —  Lógica específica del módulo de ventas
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  const vehiculoSelect = document.getElementById('id_vehiculo');
  const precioSugerido = document.getElementById('precio-sugerido');
  const valorInput     = document.getElementById('valor');
  const precios        = {};

  // Construir mapa precio por vehiculo desde data-attributes
  if (vehiculoSelect) {
    vehiculoSelect.querySelectorAll('option[data-precio]').forEach(opt => {
      precios[opt.value] = parseFloat(opt.dataset.precio);
    });

    vehiculoSelect.addEventListener('change', () => {
      const precio = precios[vehiculoSelect.value];
      if (precio && precioSugerido) {
        precioSugerido.textContent = 'Precio de catálogo: ' +
          new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP',
            maximumFractionDigits: 0 }).format(precio);
        if (valorInput && !valorInput.value) valorInput.value = precio;
      } else if (precioSugerido) {
        precioSugerido.textContent = '';
      }
    });
  }

  // Fecha de venta por defecto = hoy
  const fechaInput = document.getElementById('fecha_venta');
  if (fechaInput && !fechaInput.value) {
    const hoy = new Date().toISOString().split('T')[0];
    fechaInput.value = hoy;
  }
});
