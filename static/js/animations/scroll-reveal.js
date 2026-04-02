// GSAP Scroll Reveal Animations
document.addEventListener('DOMContentLoaded', () => {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not loaded, skipping scroll animations');
    document.querySelectorAll('.reveal-element').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  gsap.utils.toArray('.reveal-element').forEach((el) => {
    gsap.from(el, {
      opacity: 0,
      y: 50,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
        toggleActions: "play none none none"
      }
    });
  });

  gsap.utils.toArray('.orb').forEach(orb => {
    gsap.to(orb, {
      y: -100,
      ease: "none",
      scrollTrigger: {
        trigger: orb.parentElement,
        start: "top bottom",
        end: "bottom top",
        scrub: 1
      }
    });
  });

  gsap.utils.toArray('[data-animate-grid]').forEach(grid => {
    const items = grid.querySelectorAll('.animate-item');
    gsap.from(items, {
      opacity: 0,
      y: 60,
      duration: 0.8,
      stagger: 0.15,
      ease: "power2.out",
      scrollTrigger: {
        trigger: grid,
        start: "top 80%",
        toggleActions: "play none none none"
      }
    });
  });

  gsap.utils.toArray('[data-counter]').forEach(counter => {
    const target = parseInt(counter.dataset.counter);
    const suffix = counter.dataset.suffix || '+';
    
    ScrollTrigger.create({
      trigger: counter,
      start: "top 85%",
      onEnter: () => {
        gsap.to(counter, {
          innerHTML: target,
          duration: 2,
          ease: "power2.out",
          snap: { innerHTML: 1 },
          onUpdate: function() {
            counter.innerHTML = Math.round(this.targets()[0].innerHTML) + suffix;
          }
        });
      },
      once: true
    });
  });

  gsap.utils.toArray('.split-text').forEach(text => {
    const chars = text.textContent.split('');
    text.innerHTML = chars.map(char => 
      `<span class="char inline-block">${char === ' ' ? '&nbsp;' : char}</span>`
    ).join('');

    gsap.from(text.querySelectorAll('.char'), {
      opacity: 0,
      y: 50,
      rotationX: -90,
      stagger: 0.02,
      duration: 0.8,
      ease: "back.out(1.7)",
      scrollTrigger: {
        trigger: text,
        start: "top 85%",
        toggleActions: "play none none none"
      }
    });
  });

  gsap.utils.toArray('.parallax-section').forEach(section => {
    const content = section.querySelector('.parallax-content');
    if (content) {
      gsap.to(content, {
        yPercent: -20,
        ease: "none",
        scrollTrigger: {
          trigger: section,
          start: "top bottom",
          end: "bottom top",
          scrub: 1
        }
      });
    }
  });

  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      ScrollTrigger.refresh();
    }, 250);
  });
});
