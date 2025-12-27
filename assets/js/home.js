document.addEventListener('DOMContentLoaded', function() {
  // Tabs: Overview / Activity
  var tabs = document.querySelectorAll('.hf-tab');
  var panels = document.querySelectorAll('.hf-panel');
  tabs.forEach(function(tab) {
    tab.addEventListener('click', function() {
      var target = this.dataset.target;
      tabs.forEach(t=>t.classList.remove('active'));
      panels.forEach(p=>p.classList.remove('active'));
      this.classList.add('active');
      document.querySelector('#' + target).classList.add('active');
    });
  });

  // Search filter for projects and posts
  var search = document.getElementById('home-search');
  if (search) {
    search.addEventListener('input', function(e) {
      var q = e.target.value.toLowerCase().trim();
      // filter project cards
      document.querySelectorAll('.project-card').forEach(function(card){
        var text = card.textContent.toLowerCase();
        card.style.display = text.indexOf(q) !== -1 ? '' : 'none';
      });
      // filter post list items
      document.querySelectorAll('.home-post-item').forEach(function(li){
        var text = li.textContent.toLowerCase();
        li.style.display = text.indexOf(q) !== -1 ? '' : 'none';
      });
    });
  }

  // Simple entrance animation for cards
  var cards = document.querySelectorAll('.project-card');
  cards.forEach(function(c, i){
    c.style.opacity = 0;
    c.style.transform = 'translateY(8px)';
    setTimeout(function(){
      c.style.transition = 'opacity 360ms ease, transform 360ms ease';
      c.style.opacity = 1;
      c.style.transform = 'translateY(0)';
    }, 80 * i);
  });
});
