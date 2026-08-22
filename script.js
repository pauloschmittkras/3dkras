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

// Carrega e exibe os produtos dinamicamente na galeria (apenas nome e descrição)
async function loadProducts() {
  const productGallery = document.getElementById('product-gallery');
  if (!productGallery) {
    return; // Não está na página galeria.html
  }

  try {
    const response = await fetch('products.json');
    if (!response.ok) {
      throw new Error(`Erro ao buscar products.json: ${response.statusText}`);
    }
    const products = await response.json();

    products.forEach(product => {
      const article = document.createElement('article');
      article.classList.add('work-card');

      article.innerHTML = `
        <div class="work-body">
          <h3>${product.name}</h3>
          <p>${product.description}</p>
        </div>
      `;
      productGallery.appendChild(article);
    });
  } catch (error) {
    console.error('Falha ao carregar produtos:', error);
  }
}

// Garante que a função loadProducts seja chamada apenas em galeria.html
// e após o DOM ser completamente carregado.
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('product-gallery')) {
    loadProducts();
  }
});