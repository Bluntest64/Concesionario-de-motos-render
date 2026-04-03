/* ============================================================
   reportes.js  —  Gráficos y lógica del módulo de reportes
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // Gráfico simple de barras con canvas nativo (sin librerías externas)
  const canvas = document.getElementById('grafico-ventas');
  if (!canvas) return;

  const datos = JSON.parse(canvas.dataset.ventas || '[]');
  if (!datos.length) return;

  const ctx = canvas.getContext('2d');
  const W = canvas.width  = canvas.offsetWidth;
  const H = canvas.height = 220;
  const pad = { top: 20, right: 20, bottom: 40, left: 60 };
  const maxVal = Math.max(...datos.map(d => d.valor), 1);

  ctx.clearRect(0, 0, W, H);

  const barW = Math.min(40, (W - pad.left - pad.right) / datos.length - 8);
  const chartW = W - pad.left - pad.right;
  const chartH = H - pad.top - pad.bottom;

  datos.forEach((d, i) => {
    const x = pad.left + (chartW / datos.length) * i + (chartW / datos.length - barW) / 2;
    const h = (d.valor / maxVal) * chartH;
    const y = pad.top + chartH - h;

    ctx.fillStyle = '#C1121F';
    ctx.beginPath();
    ctx.roundRect(x, y, barW, h, [3, 3, 0, 0]);
    ctx.fill();

    ctx.fillStyle = '#888';
    ctx.font = '10px Barlow, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(d.mes || d.label, x + barW / 2, H - pad.bottom + 16);
  });

  // Línea base
  ctx.strokeStyle = '#2E2E2E';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(pad.left, pad.top + chartH);
  ctx.lineTo(W - pad.right, pad.top + chartH);
  ctx.stroke();
});
