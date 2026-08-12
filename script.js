// Efeito de "impressão" do título — o texto aparece como se estivesse sendo depositado pela extrusora
const typedEl = document.getElementById('typed-line');
const fullText = 'Imprimindo ideias, camada por camada.';
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function typeText(el, text, speed) {
  let i = 0;
  function step() {
    el.textContent = text.slice(0, i);
    i++;
    if (i <= text.length) {
      setTimeout(step, speed);
    }
  }
  step();
}

if (typedEl) {
  if (prefersReducedMotion) {
    typedEl.textContent = fullText;
  } else {
    typeText(typedEl, fullText, 45);
  }
}

// Anima as barras de progresso de impressão quando entram na tela
const progressBars = document.querySelectorAll('.print-progress-bar');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const bar = entry.target;
      const target = bar.getAttribute('data-progress') || '100';
      bar.style.width = target + '%';
      observer.unobserve(bar);
    }
  });
}, { threshold: 0.4 });

progressBars.forEach((bar) => observer.observe(bar));
