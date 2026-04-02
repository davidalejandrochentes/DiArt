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

	ScrollTrigger.config({
		limitCallbacks: true,
		ignoreMobileResize: true
	});

	gsap.utils.toArray('.reveal-element').forEach((el) => {
		gsap.from(el, {
			opacity: 0,
			y: 50,
			duration: 0.8,
			ease: "power2.out",
			scrollTrigger: {
				trigger: el,
				start: "top 90%",
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
				start: "top 85%",
				toggleActions: "play none none none"
			}
		});

		const counters = grid.querySelectorAll('[data-counter]');
		counters.forEach(counter => {
			const target = parseInt(counter.dataset.counter);
			if (isNaN(target)) return;

			const suffixMatch = counter.innerHTML.match(/\D+$/);
			const suffix = suffixMatch ? suffixMatch[0] : '+';

			ScrollTrigger.create({
				trigger: grid,
				start: "top 85%",
				onEnter: () => {
					gsap.fromTo(counter, 
						{ innerHTML: 0 },
						{
							innerHTML: target,
							duration: 2,
							ease: "power2.out",
							snap: { innerHTML: 1 },
							onUpdate: function() {
								counter.innerHTML = Math.round(this.targets()[0].innerHTML) + suffix;
							}
						}
					);
				},
				once: true
			});
		});
	});

	gsap.utils.toArray('[data-counter]').forEach(counter => {
		if (counter.closest('[data-animate-grid]')) return;

		const target = parseInt(counter.dataset.counter);
		if (isNaN(target)) return;

		const suffixMatch = counter.innerHTML.match(/\D+$/);
		const suffix = suffixMatch ? suffixMatch[0] : '+';

		ScrollTrigger.create({
			trigger: counter,
			start: "top 95%",
			onEnter: () => {
				gsap.fromTo(counter,
					{ innerHTML: 0 },
					{
						innerHTML: target,
						duration: 2,
						ease: "power2.out",
						snap: { innerHTML: 1 },
						onUpdate: function() {
							counter.innerHTML = Math.round(this.targets()[0].innerHTML) + suffix;
						}
					}
				);
			},
			once: true
		});
	});

	setTimeout(() => {
		ScrollTrigger.refresh();
	}, 100);

	let resizeTimer;
	window.addEventListener('resize', () => {
		clearTimeout(resizeTimer);
		resizeTimer = setTimeout(() => {
			ScrollTrigger.refresh();
		}, 250);
	});

	window.addEventListener('orientationchange', () => {
		setTimeout(() => {
			ScrollTrigger.refresh();
		}, 500);
	});
});
