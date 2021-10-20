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


