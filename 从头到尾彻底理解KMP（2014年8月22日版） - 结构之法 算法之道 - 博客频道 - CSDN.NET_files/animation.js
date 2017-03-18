'use strict';

$(document).ready(function() {
  var $stage = $('.stage');
  var stageW = $stage.width();
  var stageH = $stage.height();
  var $wall = $('.wall');
  
  var $text0 = $('.text0');
 
  var $cta = $('.cta');

  var isIE = /MSIE/.test(navigator.userAgent) || /Edge/.test(navigator.userAgent) || /Trident/.test(navigator.userAgent);
  var clickUrl = 'http://www.hrblock.com';
  $stage.on('click', function() {   
    if (typeof te_html !== 'undefined') {
      te_html.click('clickTAG', clickUrl);
    } else {
      window.location.href = clickUrl;
    }
  });

  var tl = new TimelineLite({'delay':1});
  tl.set($wall, {display:'none'});
  

  for (var i = 0; i < 100; i++) {
    tweenBox1(getBox(i), getRandom(0, 4), i);  }

  for (var j = 0; j < 100; j++) {
  tweenBox1(getBox(i+j), getRandom(5, 8), i+j);
  }
  
  for (var l = 0; l < 300; l++) {
    tweenBox1(getBox(i+j+l), getRandom(8, 13), i+j+l);
  }
         
  

  
  function tweenBox0(box, d, index) {
    var speed = getRandom(1, 1.5);

    tl.set(box, {x:stageW + 20, y:getRandom(0, stageH)}, 'start');

    tl.to(box, speed, {
        bezier:{autoRotate:true, 
          values:[
            {x:stageW+"px", y:box.position().top+getRandom(-10, 10)+"px"}, 
            {x:stageW/2+"px", y:box.position().top+getRandom(-10, 10)+"px"}, 
            {x:"-20px", y:box.position().top+getRandom(-10, 10)+"px"}
          ]},
        x: "-20px",
        rotation:getRandom(0, 360),
        ease:Linear.easeNone},'start+='+d);

    tl.to(box, speed, { skewX:getRandom(40, 180)},'start+='+d);
  }

  function tweenBox1(box, d, index) {
    var pp0 = [
      {x: 700, y:8},
      {x: 5, y:8}
    ];
         
    var pp1 = [
      {x: 700, y:75},
      {x: 5, y:75}
    ];

    var speed = getRandom(2.5, 4);
         
    var p0x0 = pp0[0].x + getRandom(-5, 5);
    var p0x1 = pp0[1].x + getRandom(-5, 5);
    var p0x2 = -10;
    var p0y0 = pp0[0].y + getRandom(-5, 5);
    var p0y1 = pp0[1].y + getRandom(-5, 5);
    var p0y2 = getRandom(0, stageH);
         
    var p1x0 = pp1[0].x + getRandom(-5, 5);
    var p1x1 = pp1[1].x + getRandom(-5, 5);
    var p1x2 = -10;
    var p1y0 = pp1[0].y + getRandom(-5, 5);
    var p1y1 = pp1[1].y + getRandom(-5, 5);
    var p1y2 = getRandom(0, stageH);
         
    tl.set(box, {x:stageW + 20, y:getRandom(0, stageH)}, 'start');
         
    if (index % 2 === 0) {
      tl.to(box, speed, {
      bezier:{autoRotate:true, values:[{x:p0x0, y:p0y0}, {x:p0x1, y:p0y1}, {x:p0x2, y:p0y2}]},
        rotation:getRandom(0, 360),
        ease:Linear.easeNone},'start+='+d);
    } else {
      tl.to(box, speed, {
        bezier:{autoRotate:true, values:[{x:p1x0, y:p1y0}, {x:p1x1, y:p1y1}, {x:p1x2, y:p1y2}]},
        rotation:getRandom(0, 360),
        ease:Linear.easeNone},'start+='+d);
      }
      tl.to(box, speed, { skewX:getRandom(40, 180)},'start+='+d);
  }


  function getRandom(min, max) {
    return Math.random() * (max - min) + min;
  }

  function getBox(i) {
    var size = getRandom(6, 9);
    var $square = $('#square').clone()
      .appendTo(".square-holder")
      .attr("id", "square"+i)
      .css({
        width: size + 'px',
        height: size + 'px'
      });
         
    return $square;
  }
});
