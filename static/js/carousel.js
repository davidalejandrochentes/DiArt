class Carousel {
  constructor(container) {
    this.container = container;
    this.track = container.querySelector('.carousel-track');
    this.slides = container.querySelectorAll('.carousel-slide');
    this.prevBtn = document.getElementById('carousel-prev');
    this.nextBtn = document.getElementById('carousel-next');
    this.dotsContainer = document.getElementById('carousel-dots');
    
    this.currentIndex = 0;
    this.slidesPerView = this.getSlidesPerView();
    this.totalSlides = this.slides.length;
    this.maxIndex = Math.max(0, Math.ceil(this.totalSlides - this.slidesPerView));
    this.autoplayInterval = null;
    this.autoplayDelay = 4000;
    
    this.init();
  }
  
  getSlidesPerView() {
    const width = window.innerWidth;
    if (width >= 1024) return 4;
    if (width >= 768) return 3;
    if (width >= 640) return 2;
    return 1;
  }
  
  init() {
    this.createDots();
    this.updateCarousel();
    this.setupEventListeners();
    this.startAutoplay();
  }
  
  createDots() {
    this.dotsContainer.innerHTML = '';
    const dotsCount = Math.ceil(this.totalSlides / this.slidesPerView);
    
    for (let i = 0; i < dotsCount; i++) {
      const dot = document.createElement('button');
      dot.className = 'w-2 h-2 rounded-full bg-slate-300 hover:bg-primary transition-all duration-300';
      dot.setAttribute('aria-label', `Ir a slide ${i + 1}`);
      dot.addEventListener('click', () => this.goToSlide(i * this.slidesPerView));
      this.dotsContainer.appendChild(dot);
    }
    
    this.dots = this.dotsContainer.querySelectorAll('button');
  }
  
  updateCarousel() {
    const slideWidth = 100 / this.slidesPerView;
    this.track.style.transform = `translateX(-${this.currentIndex * slideWidth}%)`;
    
    this.slides.forEach((slide, index) => {
      slide.style.width = `${slideWidth}%`;
    });
    
    this.updateDots();
  }
  
  updateDots() {
    const activeDotIndex = Math.floor(this.currentIndex / this.slidesPerView);
    this.dots.forEach((dot, index) => {
      if (index === activeDotIndex) {
        dot.classList.remove('bg-slate-300');
        dot.classList.add('bg-primary', 'w-6');
      } else {
        dot.classList.remove('bg-primary', 'w-6');
        dot.classList.add('bg-slate-300');
      }
    });
  }
  
  goToSlide(index) {
    this.currentIndex = Math.max(0, Math.min(index, this.maxIndex));
    this.updateCarousel();
    this.resetAutoplay();
  }
  
  nextSlide() {
    if (this.currentIndex >= this.maxIndex) {
      this.currentIndex = 0;
    } else {
      this.currentIndex++;
    }
    this.updateCarousel();
  }
  
  prevSlide() {
    if (this.currentIndex <= 0) {
      this.currentIndex = this.maxIndex;
    } else {
      this.currentIndex--;
    }
    this.updateCarousel();
  }
  
  setupEventListeners() {
    this.prevBtn.addEventListener('click', () => {
      this.prevSlide();
      this.resetAutoplay();
    });
    
    this.nextBtn.addEventListener('click', () => {
      this.nextSlide();
      this.resetAutoplay();
    });
    
    this.container.addEventListener('mouseenter', () => this.stopAutoplay());
    this.container.addEventListener('mouseleave', () => this.startAutoplay());
    
    this.container.addEventListener('touchstart', (e) => {
      this.touchStartX = e.touches[0].clientX;
      this.stopAutoplay();
    });
    
    this.container.addEventListener('touchend', (e) => {
      const touchEndX = e.changedTouches[0].clientX;
      const diff = this.touchStartX - touchEndX;
      
      if (Math.abs(diff) > 50) {
        if (diff > 0) {
          this.nextSlide();
        } else {
          this.prevSlide();
        }
      }
      
      this.startAutoplay();
    });
    
    window.addEventListener('resize', () => {
      this.slidesPerView = this.getSlidesPerView();
      this.maxIndex = Math.max(0, Math.ceil(this.totalSlides - this.slidesPerView));
      this.currentIndex = Math.min(this.currentIndex, this.maxIndex);
      this.createDots();
      this.updateCarousel();
    });
  }
  
  startAutoplay() {
    this.stopAutoplay();
    this.autoplayInterval = setInterval(() => {
      this.nextSlide();
    }, this.autoplayDelay);
  }
  
  stopAutoplay() {
    if (this.autoplayInterval) {
      clearInterval(this.autoplayInterval);
      this.autoplayInterval = null;
    }
  }
  
  resetAutoplay() {
    this.stopAutoplay();
    this.startAutoplay();
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const carouselContainer = document.getElementById('team-carousel');
  if (carouselContainer) {
    new Carousel(carouselContainer);
  }
});
