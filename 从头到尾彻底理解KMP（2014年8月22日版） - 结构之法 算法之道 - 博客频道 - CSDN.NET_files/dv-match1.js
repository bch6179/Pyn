window.dv=window.dv||{};window.dv.match=window.dv.match||{};
window.dv.match.service=function(){function n(b){var c={a:b,content:null};switch(b){case 23483290480:c.content={b:h,c:p}}return c}function q(b){function c(a,b){b.start();b.addEventListener("message",q,!1);-1===r.indexOf(a)&&(r.push(a),z.push(b))}function t(a){var b=new MessageChannel;c(a,b.port1);a.postMessage(n(23483290480),"*",[b.port2])}function g(a){c(a.source.parent,a.ports[0]);(a=a.content||a.data.content)&&a.b<h&&(h=a.b,p=a.c)}function a(a){return-1<k.indexOf(a)?!1:-1<l.indexOf(a)?!0:!function(a){function b(a,
e,c){return c(f.compareDocumentPosition(a))?(k.push(e),!0):!1}function e(a,c){var d=Array.prototype.slice.call(a).filter(function(a){try{return a.contentWindow===c}catch(b){}return!1})[0];if(d)return d.parentNode===f||b(d.parentNode,c,function(a){return a&u||a&v})}var c=d.document.querySelectorAll("iframe[data-dv-frm]");if(function(a,e){var c=Array.prototype.slice.call(a).filter(function(a){var b;a:{try{var c=a.contentWindow;for(a=e;a!==window.top;)if(a=a.parent,a===c){b=!0;break a}}catch(d){}b=!1}return b})[0];
if(c)return b(c,e,function(a){return a&u})}(f.querySelectorAll("iframe:not([data-dv-frm])"),a)||e(c,a))return!0;l.push(a);return!1}(a)}if(b&&b.data&&b.data.a){var e=b.data.a;if(!m||!a(b.source))switch(e){case 17381297349:t(b.source.parent);break;case 23483290480:g(b)}}}function A(){function b(a){var e=[];m?(a=f.querySelectorAll("iframe:not([data-dv-frm])"),a=Array.prototype.slice.call(a),a.forEach(function(a){e.push(a.contentWindow)})):e=a.frames;a=0;for(var c=e.length;a<c&&!(50<++t);a++)e[a].postMessage(g,
"*"),0<e[a].frames.length&&b(e[a])}function c(){(function(a){var b=d.document.querySelectorAll("iframe[src='about:blank'][data-dv-frm]"),b=Array.prototype.slice.call(b);b.splice(b.indexOf(a),1);return b})(w).forEach(function(a){var b=a.parentNode,c=f.compareDocumentPosition(b);b===f||c&v||c&u?(a.contentWindow.postMessage(g,"*"),-1===k.indexOf(a.contentWindow)&&k.push(a.contentWindow)):-1===l.indexOf(a.contentWindow)&&l.push(a.contentWindow)})}var t=0,g=n(17381297349);d.addEventListener("message",
q,!1);m&&(c(),x.addEventListener("message",q,!1));(function(a){for(;a!==window.top;)a=a.parent,a.postMessage(g,"*")})(d);b(d)}function B(){function b(){if(0<r.length&&!y){y=!0;try{$dv.messages.registerMsg(window,{mascid:h})}catch(b){}}}d.addEventListener("beforeunload",b,!1);setTimeout(b,5E3);setTimeout(b,14E3)}var p=(new Date).getTime().toString(16),h=p+function(){function b(){var b=new Uint32Array(4);window.crypto.getRandomValues(b);var d=[];b.forEach(function(b){d.push(("00000000"+b.toString(36)).substr(-6))});
return d.join("")}return window.crypto?b():(Math.random().toString(36)+"000000000000").substr(2,12)+(Math.random().toString(36)+"000000000000").substr(2,12)}(),d=window.parent,x=window,w=x.frameElement,f=w.parentNode,m=d===window.top,k=[],l=[],r=[],z=[],y=!1,v=Node.DOCUMENT_POSITION_CONTAINS,u=Node.DOCUMENT_POSITION_CONTAINED_BY;this.start=function(){var b=m&&f===d.document.body;window.MessageChannel&&!b&&(A(),B())}};try{(new window.dv.match.service).start()}catch(n){};
