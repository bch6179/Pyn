try{window.CHITIKA&&top.CHITIKA&&top.CHITIKA!==window.CHITIKA&&(top.CHITIKA.units=top.CHITIKA.units.append(window.CHITIKA.units),delete window.CHITIKA),window.CHITIKA=window.CHITIKA?window.CHITIKA:top.CHITIKA,window.CHITIKA_ADS=window.CHITIKA_ADS?window.CHITIKA_ADS:top.CHITIKA_ADS}catch(a){}if(window.CHITIKA=window.CHITIKA?window.CHITIKA:{},window.CHITIKA_ADS=window.CHITIKA_ADS?window.CHITIKA_ADS:function(){"use strict";function r(a,b){if(void 0===b&&(b=document),"string"==typeof a){var c=b.getElementsByTagName("head")[0];if(c){var d=b.createElement("script");return d.type="text/javascript",d.src=a,c.appendChild(d),d}}}function s(a,b,c,d){t(a,1,b,c,d)()}function t(a,b,c,d,e){return function(){for(var f in e){var g=e[f],h=d[f],i=g-h,j=i*(Math.pow(b,4)/Math.pow(c,4)),k=h+j;"l"==f?a.style.left=k+"px":"t"==f?a.style.top=k+"px":"r"==f?a.style.right=k+"px":"b"==f&&(a.style.bottom=k+"px")}b<c&&(b++,setTimeout(t(a,b,c,d,e),20))}}function u(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent("on"+b,c)}function v(a,b,c,d){void 0===d&&(d=document);var e=d.createElement("a");e.href="#chitika_close_button",e.style.background="url(//images.chitika.net/buttons/close_round_white_on_red.png)",e.style["background-repeat"]="no-repeat",e.style.height="14px",e.style.position="absolute",e.style.right="0px",e.style.top="0px",e.style.width="16px",e.style.zIndex="999999","object"==typeof b&&ga(e.style,b),u(e,"click",c),a.appendChild(e)}function w(){var a=window;if(void 0!==a.ch_client){var b={};if("mobile"==a.ch_type){CHITIKA.publisher=ch_client;var c=W();return void(c>=1&&c<=3&&(r("//cdn.chitika.net/apps/adhesion.js"),CHITIKA_ADS.already_adhesion=!0))}for(var d in l){var e=l[d],f=a[d];"function"!=typeof f&&(b[e]=f)}b.impsrc=D(a.ch_impsrc,"amm-getads-bridge");var g=CHITIKA.units.length;if(CHITIKA.units[g]=b,document.write('<div id="chitikaAdBlock-'+g+'" class="chitikaAdContainer"></div>'),(250==b.width&&250==b.height||120==b.width&&600==b.height)&&(250==b.width&&250==b.height&&(b.width=300),120==b.width&&600==b.height&&(b.width=160)),"salary"==b.publisher&&b.third_party_tracker&&(b.third_party_tracker=decodeURIComponent(decodeURIComponent(b.third_party_tracker))),"thirdage"==b.publisher&&1==a.ch_hq&&(delete b.hq,K().url.indexOf(/\/d\//)===-1?CHITIKA.snippet_priority.unshift("h1"):CHITIKA.snippet_priority.unshift("h3")),"epodunk"==b.publisher){var h=window.location.hostname.match(/([^\.]+)\.(com|net|org|info|mobi|co\.uk|org\.uk|ac\.uk|uk)$/);h&&(b.sid="epodunk_"+h[1])}else b.publisher.match(/^epodunk_/)&&(b.sid=b.publisher,b.publisher="epodunk");if("yellowbook"==b.publisher&&1==a.ch_hq){var i=document.getElementById("related-categories");i&&(i=i.getElementsByTagName("a")),i&&(i=i[0].innerHTML),b.query=i}a.ch_alternate_ad_url=void 0,a.ch_alternate_css_url=void 0,a.ch_cid=void 0,a.ch_city=void 0,a.ch_fluidH=void 0,a.ch_height=void 0,a.ch_impsrc=void 0,a.ch_metro_id=void 0,a.ch_nump=void 0,a.ch_query=void 0,a.ch_sid=void 0,a.ch_state=void 0,a.ch_where=void 0,a.ch_width=void 0,a.ch_zip=void 0}}function x(a,b,c){void 0===c&&(c=document);var d=c.createElement("div");return d.id=a,d.className="chitikaAdContainer",ga(d.style,{backgroundColor:D(b.bgColor,"#FFFFFF"),border:D(b.border,"none"),borderRadius:D(b.borderRadius,"none"),boxShadow:D(b.boxShadow,"none"),padding:D(b.padding,"none"),position:"fixed",zIndex:"99999"}),b.close_handler&&v(d,b.close_config,b.close_handler,c),d}function z(a,b,c,d){void 0===d&&(d=document);var e={allowTransparency:"allowTransparency",border:"0",className:"chitikaAdBlock",frameBorder:"0",height:"string"==typeof c?0:c,hspace:"0",id:a,marginHeight:"0",marginWidth:"0",padding:"0",scrolling:"no",src:"about:blank",style:{margin:"0",padding:"0"},vspace:"0",width:"string"==typeof b?0:b},f=d.createElement("iframe");return ga(f,e),f}function A(a){return function(){for(var b=0;b<a.frames.length;b++)a.frames[b].contentWindow.postMessage("close","*")}}function B(a,b){return function(){var c=a.frames[b];if(!a.frames_loaded[b]){a.frames_loaded[b]=!0,a.message_handlers[b]=D(a.message_handlers[b],y(c.contentWindow));var f,d=a.message_handlers[b],e=c.contentWindow,g=!1;try{e.CHITIKA=CHITIKA,e.CHITIKA_ADS=CHITIKA_ADS,e.handle_message=a.message_handlers[b],e.lightbox=O,e.lightbox_config=n,e.render_ad=a.callback}catch(a){fa("getads_except_sic1",null,{message:a.message}),g=!0}g&&void 0===window.postMessage?f="window.postMessage = "+d.toString()+"; ":void 0===window.postMessage?e.postMessage=d:g?(f="var handle_message = "+d.toString()+"; ",f+=window.addEventListener?'window.addEventListener("message", handle_message, true);':'window.attachEvent("onmessage", handle_message);'):(e.handle_message=d,u(e,"message",d)),f&&(f="javascript:(function() { "+f+" }())",c.src=f),0===b&&navigator.userAgent&&navigator.userAgent.match(/MSIE [5-8]/)&&e.postMessage("write|<!DOCTYPE html><html><head></head><body></body></html>","*"),a.frames_ready++}}}function C(a,b,c,d){d||(d="//images.chitika.net/spinner.gif");var e=a.createElement("div");e.id=b,ga(e,c);var f=a.createElement("img");return f.src=d,f.style.margin="auto",f.style.display="block",e.appendChild(f),e}function D(a,b){return null!==a&&void 0!==a?a:b}function E(a){return null!==a?'"'+a+'"':'""'}function F(a){if(a){var b=CHITIKA.units[a.unit_id],c=b.frames[0];if(b.ad_url_params&&c){if(a.extra_params)for(var d in a.extra_params){var e=a.extra_params[d];b.ad_url_params=Y(b.ad_url_params,d,e)}var f="//"+CHITIKA.host+"/minimall"+b.ad_url_params;c.contentWindow.postMessage("script|"+f,"*")}}}function G(){if(CHITIKA.enable_one_call){for(var a=[],b=0;b<CHITIKA.units.length;b++){var c=CHITIKA.units[b],d={calltype:c.calltype,cid:c.cid,h:c.height,product:c.product,nump:c.nump,sid:c.sid,w:c.width};a.push(d)}return void 0!==typeof JSON&&void 0!==typeof JSON.stringify?JSON.stringify(a):ha(a)}}function H(){return void 0!==d?d:d={h:screen.height,w:screen.width}}function I(){if(void 0!==e)return e;var a=p.top_accessible?top.document:window.document;return e={h:a.documentElement.scrollHeight||a.body.scrollHeight,w:a.documentElement.scrollWidth||a.body.scrollWidth}}function J(){if(g)return g;g={};for(var a=p.top_accessible?top.document:window.document,b=a.getElementsByTagName("meta"),c=0;c<b.length;c++){var d=b[c].getAttribute("name"),e=b[c].getAttribute("content");d&&e&&(g[d.toLowerCase()]=e)}for(var f=0;f<CHITIKA.snippet_priority.length;f++){var h=CHITIKA.snippet_priority[f].match(/^([^\/]+)(?:\/(\d+))?/),c=h[2]?parseInt(h[2],10):0,i=a.getElementsByTagName(h[1]);i.length<=c||(g[h[1]]=i[c].textContent||i[c].innerText)}return g}function K(){if(void 0!==j)return j;var a,b,c,d;return p.top_same?(b=document.referrer,d=document.location.href):p.top_accessible?(a=1,b=top.document.referrer,d=top.document.location.href,c=document.location.href):(a=2,d=document.referrer,c=document.location.href),c&&d&&c==d&&(c=void 0),c&&c.match(/^javascript:/)&&(c=void 0),b&&b.length>500&&(b=b.replace(/[?#].*/,""),b.length>500&&(b=b.match(/.*\/\/[^\/]*\//)[0])),j={frm:a,url:d,ref:b,serveUrl:c}}function L(){if(void 0!==f)return f;var a=p.top_accessible?top:window;return f={h:a.innerHeight||a.document.documentElement.clientHeight||a.document.body.clientHeight,w:a.innerWidth||a.document.documentElement.clientWidth||a.document.body.clientWidth}}function M(){f=void 0;for(var a=0;a<CHITIKA.units.length;a++){var c=CHITIKA.units[a];if(c.already_rendered){if(c.fluidH)for(var d=0;d<c.frames.length;d++){var e=c.frames[d];if(e&&e.contentWindow&&e.contentWindow.document){var g=e.contentWindow.document.body?e.contentWindow.document.body.scrollHeight:e.contentWindow.document.documentElement.scrollHeight,h=c.height;g!=h&&(c.height=g,e.style.height=g+"px")}}!p.top_accessible||c.already_visible||c.disable_vcpm||(c.loc=S(c.container))}}b&&"block"==b.style.display&&Q()}function N(){for(var a=0;a<arguments.length;a++)if(void 0!==arguments[a])return arguments[a]}function O(c,d,e){var f={hc1:e,lc1:d};if(fa("lightbox_click",c,f),p.top_accessible){if(CHITIKA.lightbox_config&&ga(n,CHITIKA.lightbox_config),!n.height||!n.width)for(var g=["height","width"],h=L(),i=0;i<2;i++){var j=g[i];n[j]||(n[j]=Math.floor(h["width"==j?"w":"h"]*n[j+"_percent"]),n[j]>n[j+"_max"]?n[j]=n[j+"_max"]:n[j]<n[j+"_min"]&&(n[j]=n[j+"_min"]))}void 0===top.lightbox_units&&(top.lightbox_units={});var k=top.lightbox_units;if(a=top.document.getElementById("chitika-modal"),null===a&&(a=top.document.createElement("div"),a.id="chitika-modal",ga(a.style,{allowTransparency:"allowTransparency",backgroundColor:n.modal_color,bottom:"0",display:"none",filter:"alpha(opacity="+100*n.modal_opacity+")",left:"0",opacity:n.modal_opacity,position:"fixed",right:"0",top:"0",zIndex:"9999",zoom:"1"}),u(a,"click",R),top.document.body.appendChild(a),b=x("chitika-container-lightbox",n,top.document),b.style.margin="auto auto",top.document.body.appendChild(b),b.appendChild(C(top.document,"chitika-spinner-lightbox",void 0,n.spinner_url))),b=top.document.getElementById("chitika-container-lightbox"),void 0===k[c]&&(k[c]={}),void 0===k[c][d]){top.document.getElementById("chitika-spinner-lightbox").style.display="block";var l="chitikaLightbox-"+c+"-"+d,m={callback:P,cid:n.cid,container_id:"chitika-container-lightbox",container_document:top.document,disable_vcpm:!0,frame_id:l,height:n.height,impId:c,product:"lightbox",query:e,sid:n.sid,skip_one_call:1,width:n.width};k[c][d]=m,CHITIKA.units.push(m),U()}else k[c][d].frames[0].style.display="block";Q()}}function P(a){void 0!==a&&(a.output||a.alturl)||R();var b=CHITIKA.units[a.unit_id],c=b.frames[0];top.document.getElementById("chitika-spinner-lightbox").style.display="none",ba(a),ca(a),c.style.display="block"}function Q(){var c=L(),d=(c.w-n.width)/2,e=(c.h-n.height)/2;b.style.left=d+"px",b.style.top=e+"px",b.style.display="block",a.style.display="block"}function R(){for(var c in top.lightbox_units)for(var d in top.lightbox_units[c])top.lightbox_units[c][d].frames[0].style.display="none";return b.style.display="none",a.style.display="none",!1}function S(a){var b=0,c=0,d=0,e=0;for(d=a.offsetWidth,e=a.offsetHeight;a;)try{if(b+=a.offsetLeft,c+=a.offsetTop,"BODY"==a.tagName){var f=a.ownerDocument.defaultView||a.ownerDocument.parentWindow;a=f.frameElement}else a=a.offsetParent}catch(a){return fa("getads_except_locate_obj",null,{message:a.message}),{}}return{x:b,y:c,w:d,h:e}}function T(){for(var a="//"+CHITIKA.host+"/minimall",b=0;b<CHITIKA.units.length;b++){var c=CHITIKA.units[b],d=c.frames[0],e=a;!c.already_fired&&c.ad_url_params&&d&&c.frames_ready===c.hasClones+1&&(1!==CHITIKA.enable_one_call||c.skip_one_call||0===b)&&((c.force_rtb||!c.disable_rtb&&(c.cpm_floor||Math.random()<0))&&(e="http://ss.chitika.net/chitika/decision"),e+=c.ad_url_params,c.already_fired=!0,c.frame_autoclose_timeout=setTimeout(A(c),1e4),d.contentWindow.postMessage("script|"+e,"*"))}}function U(){i&&(clearTimeout(i),i=null),CHITIKA.mmu0_initial||(CHITIKA.mmu0_initial=1);try{aa()}catch(a){}try{_()}catch(a){}try{$()}catch(a){}try{T()}catch(a){}for(var a=!1,b=0;b<CHITIKA.units.length;b++)if(!CHITIKA.units[b].already_fired){a=!0;break}a&&(i=setTimeout(U,250))}function V(a){if(void 0!==a){if(0===a.unit_id,a.apps){for(var b in a.apps)void 0!==o[b]&&o[b]();aa(),$(),T()}if(0===a.unit_id&&CHITIKA.enable_one_call){for(var c=1;c<CHITIKA.units.length;c++)CHITIKA.enable_one_call&&!CHITIKA.units[c].skip_one_call&&(CHITIKA.units[c].impId=a.impId);CHITIKA.enable_one_call=2,$(),T()}ba(a);try{ca(a)}catch(a){fa("getads_except_render_inject",null,{message:a.message})}da(a),ea(a),setTimeout(M,30),setTimeout(M,60),setTimeout(M,180)}}function W(){return void 0!==c?c:c=/i[Pp]ad/.test(navigator.userAgent)?1:/i[Pp]od/.test(navigator.userAgent)?4:/i[Pp]hone/.test(navigator.userAgent)?2:/[Aa]ndroid/.test(navigator.userAgent)?3:/BlackBerry|RIM/.test(navigator.userAgent)?5:0}function X(a,b,c){return c||0===c?a+"&"+b+"="+c:a}function Y(a,b,c){return c||0===c?a+"&"+b+"="+encodeURIComponent(c):a}function Z(a,b,c){return c||0===c?(c=c.replace(/[\W]+/,"_"),a+"&"+b+"="+encodeURIComponent(c)):a}function $(){var a=[],b={},c={},d={},e={},f={};try{a=G()}catch(a){fa("getads_except_pau_1",null,{message:a.message})}try{b=H()}catch(a){fa("getads_except_pau_2",null,{message:a.message})}try{c=I()}catch(a){fa("getads_except_pau_3",null,{message:a.message})}try{d=J()}catch(a){fa("getads_except_pau_4",null,{message:a.message})}try{e=K()}catch(a){fa("getads_except_pau_5",null,{message:a.message})}try{f=L()}catch(a){fa("getads_except_pau_6",null,{message:a.message})}for(var g=0;g<CHITIKA.units.length;g++){var h=CHITIKA.units[g];if(!(!h.already_fixup||h.ad_url_params||1===CHITIKA.enable_one_call&&g>0)){var i="?output="+h.output;i=Y(i,"publisher",h.publisher),i=Y(i,"altsid",h.altsid),i=X(i,"unit_id",g),i=Y(i,"impId",h.impId),i=Y(i,"extra_subid_info",h.extra_subid_info),i=Y(i,"cpm_floor",h.cpm_floor),CHITIKA.enable_one_call&&!h.skip_one_call&&void 0!==a&&"string"==typeof a?i=Y(i,"adspec",a):(i=Y(i,"sid",h.sid),i=Z(i,"cid",h.cid),i=Y(i,"calltype",h.calltype),i=Y(i,"product",h.product),i=Y(i,"w",h.width),i=Y(i,"h",h.height),i=Y(i,"nump",h.nump));for(var j in e){var m,l=e[j];void 0!==h.omg&&(m=h.omg[j],m&&m!=l&&(i=X(i,"omg_"+j,1),l=m)),i=Y(i,j,l)}i=Y(i,"altcss",h.alternate_css_url),i=Y(i,"alturl",h.alternate_ad_url),i=Y(i,"cttarget",h.target),i=Y(i,"tptracker",h.third_party_tracker),i=Y(i,"query",h.query),i=Y(i,"where",h.where),i=Y(i,"city",h.city),i=Y(i,"state",h.state),i=Y(i,"zip",h.zip),h.queries&&h.queries.constructor.toString().indexOf("Array")!==-1&&(i=Y(i,"mquery",h.queries.join("|"))),i=Y(i,"cl_border",h.color_border),i=Y(i,"cl_button",h.color_button),i=Y(i,"cl_button_text",h.color_button_text),i=Y(i,"cl_bg",h.color_bg),i=Y(i,"cl_title",h.color_title),i=Y(i,"cl_text",h.color_text),i=Y(i,"cl_site_link",h.color_site_link),i=Y(i,"fn_title",h.font_title),i=Y(i,"fn_text",h.font_text),i=X(i,"dpr",window.devicePixelRatio),i=Y(i,"impsrc",h.impsrc);try{i=Y(i,"history",window.history.length)}catch(a){fa("getads_except_pau_7",null,{message:a.message})}if(i=Y(i,"size_screen",b.w+"x"+b.h),i=Y(i,"size_scroll",c.w+"x"+c.h),i=Y(i,"size_viewport",f.w+"x"+f.h),i=Y(i,"vsn",k),p.top_accessible&&"CSS1Compat"!=top.document.compatMode&&(i=X(i,"quirks",1)),void 0!==h.extra_params)for(var j in h.extra_params)i=Y(i,j,h.extra_params[j]);navigator.userAgent.match(/Chrome/)&&void 0!==document.webkitVisibilityState&&"prerender"==document.webkitVisibilityState&&(i=X(i,"prerender",1));for(var n=0,o=0;o<CHITIKA.snippet_priority.length&&n<CHITIKA.snippet_count;o++){var q=CHITIKA.snippet_priority[o].match(/^([^\/]+)(?:\/(\d+))?/)[1];d[q]&&(i=Y(i,"snip_"+q,d[q].substring(0,CHITIKA.snippet_length)),++n)}i=i.substring(0,2048),i=i.replace(/%\w?$/,""),void 0!==h.adurl_fixup&&(i=h.adurl_fixup(i)),h.ad_url_params=i}}}function _(){for(var a=0;a<CHITIKA.units.length;a++){var b=CHITIKA.units[a];if(b.already_fixup&&!b.container)for(var c=b.container_document?b.container_document:document,d=0;d<=b.hasClones;d++){var e=D(b.container_id,"chitikaAdBlock-"+a);0!==d&&(e+="-"+d);var f=b.frame_id?b.frame_id:"ch_ad"+a+"-"+d,g=c.getElementById(e);if(g){0===d&&(b.container=g),g.className?g.className.indexOf("chitikaAdContainer")==-1&&(g.className+=" chitikaAdContainer"):g.className="chitikaAdContainer";var h=z(f,b.width,b.height);b.frames.push(h),u(h,"load",B(b,d)),b.defer_show&&(h.style.display="none"),g.appendChild(h)}}}}function aa(){for(var a=0;a<CHITIKA.units.length;a++){var b=CHITIKA.units[a];if(!b.already_fixup){b.client&&(b.publisher=b.client,delete b.client),CHITIKA.publisher=D(CHITIKA.publisher,b.publisher),b.publisher||(b.publisher=CHITIKA.publisher),b.cid||(b.sid&&"Chitika Default"!=b.sid?b.cid=b.sid:b.cid="unit-"+a),b.impsrc=D(b.impsrc,"getads"),(250==b.width&&250==b.height||120==b.width&&600==b.height)&&(250==b.width&&250==b.height&&(b.width=300),120==b.width&&600==b.height&&(b.width=160));for(var c in m){var d=m[c];b[c]&&b[c].match(new RegExp(d,"i"))&&delete b[c]}!b.fluidH&&b.nump&&delete b.nump,b.frames=D(b.frames,[]),b.frames_loaded={},b.hasClones=D(b.hasClones,0),b.message_handlers=D(b.message_handlers,[]),b.output=D(b.output,"jsonp"),b.callback=D(b.callback,V),b.already_fixup=!0,b.frames_ready=0}}}function ba(a){var b=a.unit_id,c=CHITIKA.units[b];a.alturl&&(c.alternate_ad_url=a.alturl),a.disable_vcpm&&(c.disable_vcpm=!0),a.fluidH&&(c.fluidH=!0),c.impId=a.impId,c.navajo=a.navajo,p.top_accessible&&!c.disable_vcpm&&(c.loc=S(c.container))}function ca(a){for(var b=a.unit_id,c=CHITIKA.units[b],d=0;d<c.frames.length;d++){var e=c.frames[d],f=e.contentWindow;a.output?(f.postMessage("write|"+a.output,"*"),a.dont_close||(f.postMessage("close","*"),clearTimeout(CHITIKA.units[d].frame_autoclose_timeout)),c.already_rendered=!0,c.disable_vcpm||ja()):c.alternate_ad_url?(e.src=c.alternate_ad_url,c.disable_vcpm=!1):a.altjs?(c.disable_vcpm=!1,f.postMessage("script|"+a.altjs,"*")):(void 0!==window.jQuery?window.jQuery(e).slideUp():e.style.display="none",f.postMessage("close","*"),clearTimeout(CHITIKA.units[d].frame_autoclose_timeout),c.disable_vcpm=!1),c.defer_show&&(a.output||a.alternate_ad_url||a.altjs)&&(void 0!==window.jQuery?window.jQuery(e).slideDown():e.style.display="block")}}function da(a){if(a.js)for(var b=p.top_accessible?top.document:window.document,c=0;c<a.js.length;c++){var d=a.js[c];r(d,b)}}function ea(a){if(a.pixels)for(var b=0;b<a.pixels.length;b++){var c=a.pixels[b],d=document.createElement("img");d.border=0,d.style.border="none",d.style.display="none",d.width=1,d.height=1,d.src=c,document.body.appendChild(d)}}function fa(a,b,c){if("imp_visible"==a){for(var d=c.unit_id,e=CHITIKA.units[d],f=e.container_document?e.container_document:document,g="chitikaAdBlock-"+d,h=f.getElementById(g),i=h.parentNode,j=1;j;)"DIV"==i.tagName||"BODY"==i.tagName?j=0:i=i.parentNode;var l=i.getBoundingClientRect(),m=l.width,n=l.height}var o=K(),p="//mm.chitika.net/chewey?event="+a;if(p=Y(p,"publisher",CHITIKA.publisher),p=Y(p,"impId",b),p=Y(p,"url",o.url),p=Y(p,"vsn",k),"imp_visible"==a&&(p=Y(p,"container_height",n),p=Y(p,"container_width",m)),c)for(var q in c){var r=c[q];p=Y(p,q,r)}var s=new Image(1,1);s.src=p,s.style.display="none"}function ga(a,b){if(a&&b)for(var c in b){var d=b[c];void 0!==d&&"function"!=typeof d&&("object"==typeof d?ga(a[c],d):a[c]=d)}}function ha(a){if(a instanceof Object){var b="";if(a.constructor===Array){for(var c=0;c<a.length;b+=ha(a[c])+",",c++);return"["+b.substr(0,b.length-1)+"]"}if(a.toString!==Object.prototype.toString)return'"'+a.toString().replace(/"/g,"\\$&")+'"';for(var d in a)void 0!==a[d]&&(b+='"'+d.replace(/"/g,"\\$&")+'":'+ha(a[d])+",");return"{"+b.substr(0,b.length-1)+"}"}return"string"==typeof a?'"'+a.replace(/"/g,"\\$&")+'"':String(a)}function ia(){var b,c,a="";for(b=0;b<32;b++)c=16*Math.random()|0,a+=(12==b?4:16==b?3&c|8:c).toString(16);return a}function ja(){if(p.top_accessible)for(var a=document.documentElement.scrollTop||document.body.scrollTop,b=L(),c=0;c<CHITIKA.units.length;c++){var d=CHITIKA.units[c];if(d.already_rendered&&!d.already_visible&&!d.disable_vcpm){var e=d.height,f=d.loc.y;if(!(f<a-.5*e||f>a+b.h-.5*e)){var g={unit_id:c,h:e,offset_h:a,sid:d.sid,viewport_h:b.h,viewport_w:b.w,xargs:d.navajo,w:d.width,y:f};fa("imp_visible",d.impId,g),d.already_visible=!0}}}}function ka(a,b){setTimeout(function(){document.getElementById(a).contentWindow.document.write(b)},1)}var a,b,c,d,e,f,g,i,j,k=(new Date,"8.1"),l={ch_alternate_ad_url:"alternate_ad_url",ch_alternate_css_url:"alternate_css_url",ch_cid:"cid",ch_city:"city",ch_client:"publisher",ch_color_bg:"color_bg",ch_color_border:"color_border",ch_color_site_link:"color_site_link",ch_color_text:"color_text",ch_color_title:"color_title",ch_fluidH:"fluidH",ch_font_text:"font_text",ch_font_title:"font_title",ch_height:"height",ch_nump:"nump",ch_queries:"queries",ch_query:"query",ch_sid:"sid",ch_state:"state",ch_target:"target",ch_third_party_tracker:"third_party_tracker",ch_where:"where",ch_width:"width",ch_zip:"zip"},m={color_bg:"^#?ffffff",color_border:"^#?ffffff",color_site_link:"^#?0000cc",color_text:"^#?000000",color_title:"^#?0000cc"},n={border:"1px solid #acacac",borderRadius:"1px",boxShadow:"0px 0px 10px 5px #a2a2a2",cid:void 0,close_config:{background:"url(//images.chitika.net/buttons/close_metro.png)",height:"18px",right:"5px",top:"5px",width:"18px"},close_handler:R,height_max:500,height_min:180,height_percent:.6,modal_color:"#888888",modal_opacity:.4,padding:"20px 10px 10px 10px",sid:"lightbox",spinner_url:"//images.chitika.net/spinner.gif",width_max:700,width_min:300,width_percent:.65},o={},p={top_accessible:!1,top_same:!1};try{window===top&&(p.top_same=!0);top.document.location;p.top_accessible=!0}catch(a){}var y=function(a){var b=a.document,c=function(c,d){if(c){var e="object"==typeof c?c.data:c,f=e.match(/^([^\|]*)\|?([\s\S]*)/),g=f[1],h=f[2];if("close"==g)try{b.close()}catch(a){}else if("script"==g&&h){var i=b.getElementsByTagName("head")[0];if(!i)return;var j=b.createElement("script");j.src=h,i.appendChild(j)}else if("write"==g&&h){for(var k=["CHITIKA","CHITIKA_ADS","handle_message","lightbox","lightbox_config","render_ad"],l={},m=0;m<k.length;m++){var n=k[m];l[n]=a[n]}b.write(h);try{0==b.body.innerHTML.length&&a.parent.CHITIKA_ADS.rewrite_iframe(a.frameElement.id,h)}catch(a){}for(var m=0;m<k.length;m++){var n=k[m];a[n]=l[n]}void 0===a.postMessage?a.postMessage=l.handle_message:a.addEventListener?a.addEventListener("message",a.handle_message,!1):a.attachEvent("onmessage",a.handle_message)}}};return c};return u(p.top_accessible?top:window,"resize",M),p.top_accessible&&u(top,"scroll",ja),{add_script:r,already_adhesion:!1,animate:s,append_func:u,attach_close:v,bridge_amm:w,create_container:x,create_spinner:C,def:D,dq:E,drop_it_like_its_hot:F,get_screen_size:H,get_scroll_size:I,get_snippet_data:J,get_url_data:K,get_viewport_size:L,ldef:N,locate_obj:S,make_it_so:U,mobile_type:W,param_concat_escape:Y,param_concat:X,param_concat_words:Z,render_ad_basic:ba,render_ad_inject_content:ca,rewrite_iframe:ka,send_event:fa,set_properties:ga,uuid:ia,window_data:p}}(),CHITIKA_ADS.window_data.top_accessible&&!top.CHITIKA&&(top.CHITIKA=CHITIKA,top.CHITIKA_ADS=CHITIKA_ADS),CHITIKA.host=CHITIKA_ADS.def(CHITIKA.host,"mm.chitika.net"),CHITIKA.publisher=CHITIKA_ADS.def(CHITIKA.publisher,void 0),CHITIKA.snippet_count=CHITIKA_ADS.def(CHITIKA.snippet_count,1),CHITIKA.snippet_length=CHITIKA_ADS.def(CHITIKA.snippet_length,100),CHITIKA.snippet_priority=CHITIKA_ADS.def(CHITIKA.snippet_priority,["title","h1","keywords","description"]),CHITIKA.units=CHITIKA_ADS.def(CHITIKA.units,[]),void 0!==window.chitika_units)for(var c=0;c<window.chitika_units.length;c++){var unit=window.chitika_units[c];unit&&(CHITIKA.units.push(unit),window.chitika_units[c]=null)}CHITIKA_ADS.bridge_amm(),CHITIKA.no_adhesion||CHITIKA_ADS.already_adhesion||0===CHITIKA_ADS.mobile_type()||(!CHITIKA.publisher&&CHITIKA.units[0]&&CHITIKA.units[0].publisher&&(CHITIKA.publisher=CHITIKA.units[0].publisher),CHITIKA.publisher&&(CHITIKA_ADS.add_script("//cdn.chitika.net/apps/adhesion.js"),CHITIKA_ADS.already_adhesion=!0));var DNC={publiceduonline:1,olgalevin:1,tehatin:1,gamefus:1,popstore:1,gameajax:1,revogame:1,phonecall:1,gopalakrishna811:1,medialooker:1,mobilega:1,musicall:1,upgamesnow:1,gamenexon:1,amusespot:1,howsthat:1,movietop:1,revelone:1,alteredgamer:1,daily9ames:1,arcadegrounds:1,prashanthellina:1,mhoang14122:1,banglachotis:1,caovuong:1,limdee8:1,gamesbaby:1,hassannisar:1};void 0!==CHITIKA.publisher?"undefined"==typeof DNC[CHITIKA.publisher]&&(CHITIKA_ADS.make_it_so(),CHITIKA_ADS.append_func(window,"load",CHITIKA_ADS.make_it_so)):(CHITIKA_ADS.make_it_so(),CHITIKA_ADS.append_func(window,"load",CHITIKA_ADS.make_it_so));
