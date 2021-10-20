//This is for scroll fade in animation
$(window).scroll(function () {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var window_height = $(window).height();
    var index_images = $(".scroll-fade-in");
    for (let i = 0; i < index_images.size(); i++) {
        if (index_images[i].offsetTop < scrollTop + window_height) {
            if (index_images[i] != null) {
                index_images[i].style.animation = "blurFadeIn 0.5s ease-in 0s backwards";
                // index_images[i].style.opacity = 1;
                // index_images[i].style.scale = 1;
            }
        } else {
            if (index_images[i] != null) {
                index_images[i].style.animation = "";
                // index_images[i].style.opacity = 0;
                // index_images[i].style.scale = 1.3;
            }
        }
    }
});

//Save the original value of the block
var counters = $(".anim-counter");
var orgi_number = new Array();
for (let i = 0; i < counters.size(); i++) {
    var number = Number(counters[i].innerText);
    orgi_number[i] = number;
    counters[i].innerText=0;
}

//start timer to add the value to the original value
var timer = setInterval(() => {
        var counters = $(".anim-counter");
        for (let i = 0; i < counters.size(); i++) {
            var number = Number(counters[i].innerText);
            if(number < orgi_number[i]){
                counters[i].innerText = number + parseInt(orgi_number[i]/100);
            }
            if(number > orgi_number[i]){
                 counters[i].innerText = orgi_number[i];
            }
        }
    },
    10
);


function co() {
  var colorElements = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f";
  var colorArray = colorElements.split(",");
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += colorArray[Math.floor(Math.random() * 16)];
  }
  return color;
};
var a_idx = 0;
jQuery(document).ready(function ($) {
  $("body").click(function (e) {

    var config = new Array(["Hi", "Welcome"]);
    var a = config.text.split(",");
    var $i = $("<span/>").text(a[a_idx]);
    a_idx = (a_idx + 1) % a.length;
    var x = e.pageX,
      y = e.pageY;
    $i.css({
      "z-index": 150,
      "top": y - 20,
      "left": x - 40,
      "position": "absolute",
      "font-weight": "bold",
      "color": co(),
      "cursor": "default",
      "font-size": config.fontSize || "inherit"
    });
    $("body").append($i);
    $i.animate({
      "top": y - 180,
      "opacity": 0
    },
      1500,
      function () {
        $i.remove();
      });
  });
});