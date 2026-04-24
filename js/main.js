(function(){
  'use strict';

  // Mobile nav
  var toggle = document.getElementById('nav-toggle');
  var mobile = document.getElementById('nav-mobile');
  if(toggle && mobile){
    toggle.addEventListener('click', function(){
      var open = mobile.classList.toggle('open');
      toggle.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    mobile.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        mobile.classList.remove('open');
        toggle.classList.remove('open');
        toggle.setAttribute('aria-expanded','false');
      });
    });
  }

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = this.getAttribute('href');
      if(id === '#') return;
      var t = document.querySelector(id);
      if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'})}
    });
  });

  // Parallax: pin bg to viewport. Lazy-loads image and only listens to scroll
  // while the section is actually in view (huge perf save on long pages)
  var parallaxBg = document.querySelector('[data-parallax-bg]');
  var parallaxSection = document.querySelector('[data-parallax]');
  var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (parallaxBg && parallaxSection && !reducedMotion) {
    var ticking = false;
    var inView = false;
    var imgLoaded = false;
    var bgUrl = parallaxBg.getAttribute('data-bg');
    function updateParallax() {
      var rect = parallaxSection.getBoundingClientRect();
      parallaxBg.style.transform = 'translate3d(0,' + (-rect.top).toFixed(1) + 'px,0)';
      ticking = false;
    }
    function requestTick() {
      if (!ticking && inView) { ticking = true; window.requestAnimationFrame(updateParallax); }
    }
    if ('IntersectionObserver' in window) {
      var pObs = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          inView = e.isIntersecting;
          if (inView && !imgLoaded && bgUrl) {
            parallaxBg.style.backgroundImage = "url('" + bgUrl + "')";
            imgLoaded = true;
          }
          if (inView) requestTick();
        });
      }, { rootMargin: '200px' });
      pObs.observe(parallaxSection);
    } else {
      inView = true;
      if (bgUrl) parallaxBg.style.backgroundImage = "url('" + bgUrl + "')";
    }
    window.addEventListener('scroll', requestTick, { passive: true });
    window.addEventListener('resize', requestTick, { passive: true });
  }

  // Marquee: pause animation when the testimonial section is off-screen
  var marqueeTrack = document.querySelector('.marquee-track');
  var marqueeSection = document.querySelector('.testimonial-marquee');
  if (marqueeTrack && marqueeSection && 'IntersectionObserver' in window) {
    var mObs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        marqueeTrack.classList.toggle('paused', !e.isIntersecting);
      });
    }, { rootMargin: '100px' });
    mObs.observe(marqueeSection);
  }

  // Form
  var form = document.getElementById('quote-form');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var btn = form.querySelector('.btn-submit');
      var txt = btn.textContent;
      if(!form.querySelector('#name').value.trim() || !form.querySelector('#phone').value.trim() || !form.querySelector('#service').value) return;
      btn.textContent = 'Sending...';
      btn.disabled = true;
      setTimeout(function(){
        btn.textContent = 'Sent!';
        btn.style.background = '#22863a';
        setTimeout(function(){
          form.reset();
          btn.textContent = txt;
          btn.style.background = '';
          btn.disabled = false;
        },2500);
      },600);
    });
  }
})();
