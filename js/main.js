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
