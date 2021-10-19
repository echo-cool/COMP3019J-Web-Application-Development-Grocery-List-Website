$(window).scroll(function () {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var window_height = $(window).height()
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