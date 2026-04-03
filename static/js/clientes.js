/* ============================================================
   clientes.js  —  Lógica específica del módulo de clientes
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // Validar formato de email en tiempo real
  const emailInput = document.getElementById('email');
  if (emailInput) {
    emailInput.addEventListener('blur', () => {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (emailInput.value && !re.test(emailInput.value)) {
        emailInput.style.borderColor = 'var(--color-danger)';
        let msg = emailInput.parentElement.querySelector('.field-error');
        if (!msg) {
          msg = document.createElement('span');
          msg.className = 'field-error';
          msg.style.cssText = 'color:var(--color-danger);font-size:0.78rem;margin-top:2px;';
          emailInput.parentElement.appendChild(msg);
        }
        msg.textContent = 'Correo electrónico inválido';
      } else {
        emailInput.style.borderColor = '';
        const msg = emailInput.parentElement.querySelector('.field-error');
        if (msg) msg.remove();
      }
    });
  }

  // Solo dígitos en campo documento y teléfono
  ['documento', 'telefono'].forEach(id => {
    const input = document.getElementById(id);
    if (input) {
      input.addEventListener('input', () => {
        input.value = input.value.replace(/\D/g, '');
      });
    }
  });
});
