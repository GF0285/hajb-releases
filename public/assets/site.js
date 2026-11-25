(function(){
  var root=document.documentElement;
  var btn=document.querySelector('.theme');
  function current(){var t=root.getAttribute('data-theme');if(t)return t;return matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
  function sync(){btn&&btn.setAttribute('aria-pressed',current()==='dark'?'true':'false');}
  if(btn){sync();btn.addEventListener('click',function(){var n=current()==='dark'?'light':'dark';root.setAttribute('data-theme',n);try{localStorage.setItem('hajb-theme',n);}catch(e){}sync();});}
  document.querySelectorAll('.copy').forEach(function(b){
    var orig=b.textContent;
    b.addEventListener('click',function(){
      var v=b.getAttribute('data-copy');
      var done=function(){b.textContent=b.getAttribute('data-done');b.classList.add('ok');setTimeout(function(){b.textContent=orig;b.classList.remove('ok');},1800);};
      if(navigator.clipboard){navigator.clipboard.writeText(v).then(done,function(){});}
    });
  });
  // Tabs (progressive: without JS every panel is visible)
  document.querySelectorAll('[data-tabs]').forEach(function(box){
    var tabs=[].slice.call(box.querySelectorAll('[role=tab]'));
    var panels=tabs.map(function(t){return document.getElementById(t.getAttribute('aria-controls'));});
    box.classList.add('js');
    function show(i,focus,push){
      tabs.forEach(function(t,j){var on=i===j;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;panels[j].hidden=!on;});
      if(focus)tabs[i].focus();
      if(push&&history.replaceState)history.replaceState(null,'','#'+panels[i].id);
    }
    tabs.forEach(function(t,i){
      t.addEventListener('click',function(ev){ev.preventDefault();show(i,false,true);});
      t.addEventListener('keydown',function(ev){
        var rtl=getComputedStyle(box).direction==='rtl';
        var k=ev.key, n=null;
        if(k==='ArrowRight')n=rtl?i-1:i+1; else if(k==='ArrowLeft')n=rtl?i+1:i-1; else if(k==='Home')n=0; else if(k==='End')n=tabs.length-1;
        if(n!==null){ev.preventDefault();n=(n+tabs.length)%tabs.length;show(n,true,true);}
      });
    });
    // in-page links to a panel (e.g. "see Chrome")
    function fromHash(){var h=location.hash.slice(1);var i=panels.findIndex(function(p){return p.id===h;});if(i>=0){show(i,false,false);return true;}return false;}
    if(!fromHash())show(0,false,false);
    window.addEventListener('hashchange',function(){if(fromHash()){box.scrollIntoView({block:'start'});}});
  });
})();
