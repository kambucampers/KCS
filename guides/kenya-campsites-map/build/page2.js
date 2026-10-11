(function(){
  'use strict';
  var root=document.querySelector('.kcm');
  if(!root||root.getAttribute('data-booted')) return;
  root.setAttribute('data-booted','1');
  function track(ev,p){try{if(window.dataLayer&&window.dataLayer.push){var o={event:ev};for(var k in p){o[k]=p[k];}window.dataLayer.push(o);}}catch(e){}}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  function fmt(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,',');}

  /* progress + scroll spy */
  var pb=document.createElement('div');pb.className='kcm__progress';pb.setAttribute('aria-hidden','true');root.appendChild(pb);
  window.addEventListener('scroll',function(){var h=document.documentElement,m=h.scrollHeight-h.clientHeight;pb.style.width=(m>0?(h.scrollTop/m*100):0)+'%';},{passive:true});
  var links=[].slice.call(root.querySelectorAll('[data-spy] a[href^="#"]'));
  if(links.length&&'IntersectionObserver' in window){
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a;});
    var regionIds=[].slice.call(root.querySelectorAll('section[id$="-campsites"]')).map(function(s){return s.id;});
    var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var id=e.target.id;var a=map[id]||(regionIds.indexOf(id)>=0?map.regions:null);if(!a)return;links.forEach(function(l){l.classList.remove('is-active');l.removeAttribute('aria-current');});a.classList.add('is-active');a.setAttribute('aria-current','true');});},{rootMargin:'-25% 0px -65% 0px'});
    Object.keys(map).concat(regionIds).forEach(function(id){var s=document.getElementById(id);if(s)obs.observe(s);});
  }
  root.addEventListener('toggle',function(e){var d=e.target;if(d.tagName==='DETAILS'&&d.open){track('disclosure_open',{section_id:d.id||(d.closest('[id]')||{}).id||''});}},true);
  root.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-evt]');if(a){track(a.getAttribute('data-evt'),{label:a.textContent.trim().slice(0,60)});}});

  /* gallery */
  [].forEach.call(root.querySelectorAll('[data-gal]'),function(g){
    var tr=g.querySelector('.kcm__track'),slides=tr.querySelectorAll('.kcm__slide'),cnt=g.querySelector('.kcm__gal-count'),nav=g.querySelector('.kcm__gal-nav');
    if(nav)nav.hidden=false;
    function idx(){var w=slides[0].getBoundingClientRect().width+16;return Math.min(slides.length-1,Math.round(tr.scrollLeft/w));}
    function upd(){if(cnt)cnt.textContent=(idx()+1)+' / '+slides.length;}
    function go(d){var i=Math.max(0,Math.min(slides.length-1,idx()+d));tr.scrollTo({left:slides[i].offsetLeft-slides[0].offsetLeft,behavior:'smooth'});track('gallery_nav',{index:i+1});}
    [].forEach.call(g.querySelectorAll('.kcm__arrow'),function(b){b.addEventListener('click',function(){go(parseInt(b.getAttribute('data-dir'),10));});});
    tr.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){e.preventDefault();go(1);}if(e.key==='ArrowLeft'){e.preventDefault();go(-1);}});
    tr.addEventListener('scroll',function(){window.requestAnimationFrame(upd);},{passive:true});upd();
  });

  var dataEl=document.getElementById('kcm-data');if(!dataEl)return;
  var D;try{D=JSON.parse(dataEl.textContent);}catch(e){return;}

  function overview(sid,withLink){
    var o=D.ov[sid];if(!o)return '';
    var h='<b class="kcm__mpop-n">'+esc(o.n)+'</b><p class="kcm__mpop-meta">'+esc(o.t)+' &middot; '+esc(o.r)+(o.co?' &middot; '+esc(o.co)+' County':'')+'</p>';
    if(o.st)h+='<p class="kcm__mpop-flag">'+esc(o.st)+'</p>';
    if(o.c)h+='<p><b>Cost:</b> '+esc(o.c)+'</p>';
    if(o.d)h+='<p><b>Drive:</b> '+esc(o.d)+'</p>';
    if(o.v)h+='<p><b>Vehicle:</b> '+esc(o.v)+'</p>';
    if(o.rv)h+='<p class="kcm__mpop-rev">'+esc(o.rv)+'</p>';
    if(withLink)h+='<a class="kcm__mpop-more" href="#'+sid+'" data-evt="map_read_more">Read more about '+esc(o.n)+' &rarr;</a>';
    return h;
  }
  /* static SVG maps: clickable pins with an overview popup */
  var pop=null,popPin=null;
  function closePop(){if(pop){pop.hidden=true;}if(popPin){popPin.classList.remove('is-on');popPin=null;}}
  function openPop(pin){
    var fig=pin.closest('.kcm__rmap,.kcm__fig');if(!fig)return;
    var sid=pin.getAttribute('data-sid');
    if(!pop){pop=document.createElement('div');pop.className='kcm__mpop';pop.setAttribute('role','dialog');pop.setAttribute('aria-label','Campsite overview');}
    if(pop.parentNode!==fig)fig.appendChild(pop);
    pop.innerHTML='<button type="button" class="kcm__mpop-x" aria-label="Close overview">&times;</button>'+overview(sid,true);
    pop.hidden=false;
    if(popPin)popPin.classList.remove('is-on');popPin=pin;pin.classList.add('is-on');
    var fr=fig.getBoundingClientRect(),pr=pin.getBoundingClientRect();
    var x=pr.left-fr.left+pr.width/2,y=pr.top-fr.top+pr.height/2;
    var pw=pop.offsetWidth,ph=pop.offsetHeight;
    var left=Math.min(Math.max(8,x-pw/2),fr.width-pw-8),top=y+16;
    if(top+ph>fr.height-8)top=Math.max(8,y-ph-16);
    pop.style.left=left+'px';pop.style.top=top+'px';
    pop.querySelector('.kcm__mpop-x').addEventListener('click',function(){var p=popPin;closePop();if(p&&p.focus)p.focus();});
    var more=pop.querySelector('.kcm__mpop-more');
    if(more)more.addEventListener('click',function(){var c=document.getElementById(sid);if(c){c.classList.add('is-flash');setTimeout(function(){c.classList.remove('is-flash');},2400);}closePop();});
    track('map_interaction',{location:D.ov[sid]?D.ov[sid].n:sid,from:'static_map'});
  }
  root.addEventListener('click',function(e){
    var pin=e.target.closest&&e.target.closest('.kcm__mpin');
    if(pin){e.preventDefault();openPop(pin);return;}
    if(pop&&!pop.hidden&&!e.target.closest('.kcm__mpop'))closePop();
  });
  root.addEventListener('keydown',function(e){
    var pin=e.target.closest&&e.target.closest('.kcm__mpin');
    if(pin&&(e.key==='Enter'||e.key===' ')){e.preventDefault();openPop(pin);var l=pop&&pop.querySelector('.kcm__mpop-more');if(l)l.focus();}
    if(e.key==='Escape'&&pop&&!pop.hidden){var p=popPin;closePop();if(p&&p.focus)p.focus();}
  });

  /* KWS calculator */
  (function(){
    var sel=document.getElementById('kcm-c-site');if(!sel)return;
    var ids=['kcm-c-site','kcm-c-vis','kcm-c-ad','kcm-c-ch','kcm-c-n','kcm-c-v'];
    var CUR=['KES','KES','USD','USD'];
    function num(id,min){var v=parseInt(document.getElementById(id).value,10);return isNaN(v)?min:Math.max(min,v);}
    function calc(){
      var k=D.kws[sel.value];if(!k)return;
      var vis=parseInt(document.getElementById('kcm-c-vis').value,10),ad=num('kcm-c-ad',1),ch=num('kcm-c-ch',0),n=num('kcm-c-n',1),veh=num('kcm-c-v',0);
      var entry=D.fees.entry[k[0]][vis],cur=CUR[vis],rows=[],tot=0,kes=0;
      var e=(entry[0]*ad+entry[1]*ch)*n;rows.push(['Park entry ('+k[3]+'), '+n+' x 24 h',e,cur]);tot+=e;
      if(k[1]!=='m'){
        var band=(k[0]==='premium')?'1':'0',cf=D.fees.camp[k[1]+band][vis];
        var c=(cf[0]*ad+cf[1]*ch)*n;rows.push(['Camping, '+n+' night'+(n>1?'s':''),c,cur]);tot+=c;
        if(k[1]==='s'){var w=Math.ceil(n/7);rows.push(['Special-site reservation, '+w+' week'+(w>1?'s':''),10000*w,'KES']);kes+=10000*w;}
      }else{rows.push(['Hut or camp fee','paid to operator','']);}
      if(veh>0){var vf=600*veh*n;rows.push(['Vehicle, '+veh+' x '+n+' day'+(n>1?'s':''),vf,'KES']);kes+=vf;}
      var tb=document.getElementById('kcm-c-rows');tb.innerHTML='';
      rows.forEach(function(r){var tr=document.createElement('tr');tr.innerHTML='<td>'+esc(r[0])+'</td><td>'+(typeof r[1]==='number'?r[2]+' '+fmt(r[1]):esc(r[1]))+'</td>';tb.appendChild(tr);});
      var t=cur+' '+fmt(tot);if(cur==='KES'){t='KES '+fmt(tot+kes);}else if(kes){t=t+' + KES '+fmt(kes);}
      document.getElementById('kcm-c-total').textContent=t;
      document.getElementById('kcm-c-label').textContent='Estimated KWS fees, '+k[2];
    }
    ids.forEach(function(id){var el=document.getElementById(id);el.addEventListener('input',calc);el.addEventListener('change',function(){calc();track('calculator_complete',{site:sel.value});});});
    calc();
  })();

  /* interactive map */
  var TYPES=D.types,REG=D.regions;
  var state={types:{},region:'all',veh:'all',priced:false,inactive:false,q:''};
  Object.keys(TYPES).forEach(function(t){if(t!=='kmc')state.types[t]=true;});
  var tries=0;
  function boot(){
    if(!window.L){if(++tries<60){setTimeout(boot,250);}return;}
    var box=document.getElementById('kcm-map');if(!box||box.getAttribute('data-ready'))return;
    box.setAttribute('data-ready','1');
    document.getElementById('kcm-mapui').hidden=false;
    var nj=document.getElementById('kcm-nojs');if(nj)nj.hidden=true;
    var L=window.L;
    var m=L.map(box,{scrollWheelZoom:false}).setView([0.2,37.9],6);
    var tok=box.getAttribute('data-mbtoken'),sty=box.getAttribute('data-mbstyle')||'mapbox/outdoors-v12';
    L.tileLayer('https://api.mapbox.com/styles/v1/'+sty+'/tiles/512/{z}/{x}/{y}@2x?access_token='+tok,{tileSize:512,zoomOffset:-1,maxZoom:18,attribution:'&copy; <a href="https://www.mapbox.com/about/maps/" target="_blank" rel="noopener">Mapbox</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> <a href="https://www.mapbox.com/map-feedback/" target="_blank" rel="noopener">Improve this map</a>'}).addTo(m);
    var wm=document.createElement('div');wm.className='kcm__mapwm';wm.setAttribute('aria-hidden','true');box.appendChild(wm);
    var wt=document.createElement('div');wt.className='kcm__mapwm-t';wt.setAttribute('aria-hidden','true');wt.textContent='@kambucampers.com';box.appendChild(wt);
    m.on('popupopen',function(ev){var a=ev.popup.getElement().querySelector('.kcm__mpop-more');if(a){a.addEventListener('click',function(){var c=document.getElementById(a.getAttribute('href').slice(1));if(c){c.classList.add('is-flash');setTimeout(function(){c.classList.remove('is-flash');},2400);}});}});
    m.on('focus',function(){m.scrollWheelZoom.enable();});m.on('blur',function(){m.scrollWheelZoom.disable();});
    var bl=L.layerGroup();
    D.bounds.forEach(function(b){
      var d=b.d.toLowerCase(),cons=d.indexOf('conservancy')>=0||d.indexOf('sector')>=0||(d.indexOf('sanctuary')>=0&&d.indexOf('national')<0),mar=d.indexOf('marine')>=0;
      var col=mar?'#2B6FA8':(cons?'#B67A18':'#3E7B4F');
      b.r.forEach(function(r){var ll=r.map(function(p){return[p[1],p[0]];});L.polygon(ll,{color:col,weight:1.6,fillColor:col,fillOpacity:.08,dashArray:cons?'5 4':null,interactive:true}).bindTooltip(esc(b.n)+' ('+esc(b.d)+')',{sticky:true}).addTo(bl);});
    });
    bl.addTo(m);
    var markers=[];
    D.sites.forEach(function(s,i){
      var T=TYPES[s.t];
      var mk=s.t==='kmc'?L.circleMarker([s.la,s.lo],{radius:10,color:'#C7A874',weight:3,fillColor:'#233A31',fillOpacity:1}):L.circleMarker([s.la,s.lo],{radius:7,color:'#FFFFFF',weight:2,fillColor:T.c,fillOpacity:s.s==='open'?.95:.45});
      mk.bindPopup('<div class="kcm__pop kcm__mpop" style="position:static;width:auto;box-shadow:none;border:0;padding:0">'+overview(s.i,true)+'</div>',{maxWidth:290});
      mk.on('click',function(){hl(i);track('map_interaction',{location:s.n});});
      markers.push(mk);
    });
    var cl=document.getElementById('kcm-count'),list=document.getElementById('kcm-results');
    function vis(s){
      if(s.t==='kmc'){if(state.q&&(s.n+' '+s.a).toLowerCase().indexOf(state.q)<0)return false;return state.region==='all'||state.region==='masai-mara-campsites';}
      if(!state.types[s.t])return false;
      if(state.region!=='all'&&s.g!==state.region)return false;
      if(!state.inactive&&s.s!=='open')return false;
      if(state.priced&&!s.p)return false;
      if(state.veh==='2wd'&&s.v!=='2WD ok')return false;
      if(state.veh==='4wd'&&s.v.indexOf('4WD')<0)return false;
      if(state.veh==='other'&&s.v!=='boat'&&s.v!=='on foot')return false;
      if(state.q){var h=(s.n+' '+s.a+' '+(REG[s.g]||'')+' '+s.c).toLowerCase();if(h.indexOf(state.q)<0)return false;}
      return true;
    }
    function render(fit){
      var shown=[],total=0;list.innerHTML='';
      D.sites.forEach(function(s,i){if(s.t!=='kmc')total++;var v=vis(s),mk=markers[i];if(v){if(!m.hasLayer(mk))mk.addTo(m);shown.push(i);}else if(m.hasLayer(mk)){m.removeLayer(mk);}});
      var n=shown.filter(function(i){return D.sites[i].t!=='kmc';}).length;
      cl.textContent='Showing '+n+' of '+total+' campsites';
      shown.sort(function(a,b){return D.sites[a].n.localeCompare(D.sites[b].n);});
      if(!shown.length){var li=document.createElement('li');li.className='kcm__empty';li.textContent='No campsite matches these filters. Widen the region or vehicle filter.';list.appendChild(li);}
      shown.forEach(function(i){
        var s=D.sites[i],li=document.createElement('li'),b=document.createElement('button');
        b.type='button';b.className='kcm__res';b.setAttribute('data-i',i);
        b.innerHTML='<b>'+esc(s.n)+'</b><span>'+esc(TYPES[s.t].l)+' &middot; '+esc(REG[s.g]||'')+'</span>';
        b.addEventListener('click',function(){m.flyTo([s.la,s.lo],Math.max(m.getZoom(),11),{duration:.8});markers[i].openPopup();hl(i);track('map_interaction',{location:s.n,from:'list'});});
        li.appendChild(b);list.appendChild(li);
      });
      if(fit&&shown.length){m.fitBounds(L.featureGroup(shown.map(function(i){return markers[i];})).getBounds().pad(.15),{maxZoom:11});}
    }
    function hl(i){[].forEach.call(list.querySelectorAll('.kcm__res'),function(b){var on=+b.getAttribute('data-i')===i;b.classList.toggle('is-on',on);if(on&&b.scrollIntoView){b.scrollIntoView({block:'nearest'});}});}
    [].forEach.call(root.querySelectorAll('[data-type]'),function(b){b.addEventListener('click',function(){var t=b.getAttribute('data-type');state.types[t]=!state.types[t];b.setAttribute('aria-pressed',state.types[t]?'true':'false');render(false);track('filter_use',{filter_category:'type',value:t});});});
    var sel=document.getElementById('kcm-region');sel.addEventListener('change',function(){state.region=sel.value;render(true);track('filter_use',{filter_category:'region',value:sel.value});});
    var vsel=document.getElementById('kcm-veh');vsel.addEventListener('change',function(){state.veh=vsel.value;render(false);track('filter_use',{filter_category:'vehicle',value:vsel.value});});
    ['priced','inactive'].forEach(function(k){var c=document.getElementById('kcm-f-'+k);c.addEventListener('change',function(){state[k]=c.checked;render(false);track('filter_use',{filter_category:k,value:c.checked});});});
    var bc=document.getElementById('kcm-f-bounds');bc.addEventListener('change',function(){if(bc.checked){bl.addTo(m);}else{m.removeLayer(bl);}track('map_interaction',{layer:'boundaries',on:bc.checked});});
    var qi=document.getElementById('kcm-q'),qt;qi.addEventListener('input',function(){clearTimeout(qt);qt=setTimeout(function(){state.q=qi.value.trim().toLowerCase();render(!!state.q);},180);});
    var all=L.featureGroup(markers).getBounds().pad(.04);
    document.getElementById('kcm-reset').addEventListener('click',function(){
      Object.keys(state.types).forEach(function(t){state.types[t]=true;});
      [].forEach.call(root.querySelectorAll('[data-type]'),function(b){b.setAttribute('aria-pressed','true');});
      state.region='all';sel.value='all';state.veh='all';vsel.value='all';state.priced=false;state.inactive=false;
      document.getElementById('kcm-f-priced').checked=false;document.getElementById('kcm-f-inactive').checked=false;
      state.q='';qi.value='';render(false);m.fitBounds(all);
    });
    render(false);m.fitBounds(all);
    setTimeout(function(){m.invalidateSize();m.fitBounds(all);},300);
  }
  if('IntersectionObserver' in window){
    var mb=document.getElementById('map'),io=new IntersectionObserver(function(es){if(es[0].isIntersecting){io.disconnect();boot();}},{rootMargin:'400px'});io.observe(mb);
  }else{boot();}
})();
