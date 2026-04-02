// Magnetic Buttons & Tilt Effect
document.addEventListener('DOMContentLoaded', () => {
  if (typeof gsap === 'undefined') {
    console.warn('GSAP not loaded, magnetic effects disabled');
    return;
  }

  const magneticElements = document.querySelectorAll('.magnetic-btn');

  magneticElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;

      gsap.to(el, {
        x: x * 0.3,
        y: y * 0.3,
        duration: 0.3,
        ease: "power2.out"
      });
    });

    el.addEventListener('mouseleave', () => {
      gsap.to(el, {
        x: 0,
        y: 0,
        duration: 0.5,
        ease: "elastic.out(1, 0.3)"
      });
    });
  });

  const tiltCards = document.querySelectorAll('[data-tilt]');

  tiltCards.forEach(card => {
    const inner = card.querySelector('[data-tilt-inner]') || card;

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = (y - centerY) / 20;
      const rotateY = (centerX - x) / 20;

      gsap.to(inner, {
        rotateX: -rotateX,
        rotateY: rotateY,
        duration: 0.5,
        ease: "power2.out",
        transformPerspective: 1000
      });

      const shine = card.querySelector('.tilt-shine');
      if (shine) {
        const percentX = (x / rect.width) * 100;
        const percentY = (y / rect.height) * 100;
        shine.style.background = `radial-gradient(circle at ${percentX}% ${percentY}%, rgba(255,255,255,0.3) 0%, transparent 60%)`;
      }
    });

    card.addEventListener('mouseleave', () => {
      gsap.to(inner, {
        rotateX: 0,
        rotateY: 0,
        duration: 0.5,
        ease: "power2.out"
      });

      const shine = card.querySelector('.tilt-shine');
      if (shine) {
        shine.style.background = 'transparent';
      }
    });
  });
});
