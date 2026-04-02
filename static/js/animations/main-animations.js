// Main Animations Initialization
document.addEventListener('DOMContentLoaded', () => {
  // Add class to body when GSAP is loaded
  document.body.classList.add('gsap-loaded');
  
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('GSAP or ScrollTrigger not loaded, animations disabled');
    document.querySelectorAll('.reveal-element').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  const heroTimeline = gsap.timeline({ delay: 0.3 });

  heroTimeline
    .from('.orb', {
      scale: 0,
      opacity: 0,
      duration: 1,
      stagger: 0.2,
      ease: "back.out(1.7)"
    })
    .from('.reveal-element', {
      opacity: 0,
      y: 30,
      duration: 0.8,
      stagger: 0.15,
      ease: "power2.out"
    }, "-=0.5");

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#' || href === '#!') return;
      
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        gsap.to(window, {
          duration: 1,
          scrollTo: { y: target, offsetY: 80 },
          ease: "power2.inOut"
        });
      }
    });
  });

  const interactiveElements = document.querySelectorAll('a, button, input, textarea, select, [role="button"]');
  
  interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
      document.body.style.cursor = 'none';
    });
    
    el.addEventListener('mouseleave', () => {
      document.body.style.cursor = '';
    });
  });

  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (sections.length && navLinks.length) {
    sections.forEach(section => {
      ScrollTrigger.create({
        trigger: section,
        start: "top 50%",
        end: "bottom 50%",
        onEnter: () => updateActiveNav(section.id),
        onEnterBack: () => updateActiveNav(section.id)
      });
    });

    function updateActiveNav(id) {
      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.includes(id)) {
          link.classList.add('text-primary');
        } else {
          link.classList.remove('text-primary');
        }
      });
    }
  }

  ScrollTrigger.refresh();
});

window.addEventListener('load', () => {
  ScrollTrigger.refresh();
});
