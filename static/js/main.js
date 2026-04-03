/* ============================================================
   main.js  —  Utilidades globales
   ============================================================ */

// Auto-cerrar alertas flash después de 4 segundos
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.alert[data-auto-close]').forEach(el => {
    setTimeout(() => {
      el.style.opacity = '0';
      el.style.transition = 'opacity 0.5s';
      setTimeout(() => el.remove(), 500);
    }, 4000);
  });

  // Marcar nav-link activo según la URL actual
  const path = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') && path.startsWith(link.getAttribute('href'))) {
      link.classList.add('active');
    }
  });
});

// Confirmación de eliminación reutilizable
function confirmarEliminar(form, mensaje) {
  if (confirm(mensaje || '¿Está seguro de que desea eliminar este registro?')) {
    form.submit();
  }
}
