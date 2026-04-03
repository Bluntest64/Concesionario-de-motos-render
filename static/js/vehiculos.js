/* ============================================================
   vehiculos.js  —  Lógica específica del módulo de vehículos
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // Vista previa de precio formateado
  const precioInput = document.getElementById('precio');
  const precioPreview = document.getElementById('precio-preview');
  if (precioInput && precioPreview) {
    const formatCOP = v => new Intl.NumberFormat('es-CO', {
      style: 'currency', currency: 'COP', maximumFractionDigits: 0
    }).format(v);

    precioInput.addEventListener('input', () => {
      const val = parseFloat(precioInput.value);
      precioPreview.textContent = isNaN(val) ? '' : formatCOP(val);
    });
  }

  // Resaltar fila al hacer hover (accesibilidad visual)
  document.querySelectorAll('tbody tr').forEach(row => {
    row.addEventListener('mouseenter', () => row.classList.add('row-hover'));
    row.addEventListener('mouseleave', () => row.classList.remove('row-hover'));
  });
});
