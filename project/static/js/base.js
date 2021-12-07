//This is for scroll fade in animation
$(window).scroll(function () {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var window_height = $(window).height();
    var index_images = $(".scroll-fade-in");
    for (let i = 0; i < index_images.length; i++) {
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
for (let i = 0; i < counters.length; i++) {
    var number = Number(counters[i].innerText);
    orgi_number[i] = number;
    counters[i].innerText = 0;
}

//start timer to add the value to the original value
var timer = setInterval(() => {
        var counters = $(".anim-counter");
        for (let i = 0; i < counters.length; i++) {
            var number = Number(counters[i].innerText);
            if (number < orgi_number[i]) {
                counters[i].innerText = number + parseInt(orgi_number[i] / 100);
            }
            if (number > orgi_number[i]) {
                counters[i].innerText = orgi_number[i];
            }
        }
    },
    10
);

function gen_color() {
    var hex_numbers = "0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f";
    var colorArray = hex_numbers.split(",");
    var res = "#";
    for (var i = 0; i < 6; i++) {
        res += colorArray[Math.floor(Math.random() * 16)];
    }
    return res;
};
var a_idx = 0;
jQuery(document).ready(function ($) {
    $("body").click(function (e) {
        var text_data = "Hello,Welcome,Shopping";
        var a = text_data.split(",");
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
            "cursor": "default",
            "color": gen_color(),
            "font-size": "20px",
            "animation": "wiggle 1.5s ease-in 0s backwards"
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

$('#chooseImage').on('change', function () {
    var path_image, fileFormat, src;
    path_image = $(this).val();
    fileFormat = path_image.substring(path_image.lastIndexOf(".")).toLowerCase();
    src = window.URL.createObjectURL(this.files[0]);
    if (fileFormat.match(/.png|.jpg|.jpeg/)) {
        $('#upload_image_perivew').attr('src', src);
        $('#upload_image_perivew')[0].style.animation = "blurFadeIn 0.75s ease-in 0s backwards";
        setTimeout(function () {
            $('#upload_image_perivew')[0].style.animation = "none";
        }, 800);
    } else {
        alert('File type must be：png/jpg/jpeg');
        return;
    }
});

// $(document).ready(function () {
//
// });

// window.addEventListener("pageshow", new function () {
//
// });
document.onreadystatechange = function () {
    console.log(document.readyState)
    // if(document.readyState=="interactive"){
    //
    // }
    if (document.readyState == "complete") {
        console.log("Page complete")
        //Page ready hide load animation
        $(".background-image-loading-container").remove();

        //Page ready show content in body
        $(".content-body").show();
        document.getElementsByClassName("content-body")[0].hidden = false;
    }
}
// $(function () {
//
// });

function monitorEvents(element) {
    var log = function (e) {
        console.log(e);
    };
    var events = [];

    for (var i in element) {
        if (i.startsWith("on")) events.push(i.substr(2));
    }
    events.forEach(function (eventName) {
        element.addEventListener(eventName, log);
    });
}

// monitorEvents(document);

var brightness;
var isDarkMode = false;
if (window.sessionStorage.getItem("DarkMode") != null) {
    if (window.sessionStorage.getItem("DarkMode") == 1) {
        isDarkMode = true;
        darkMode(0.5)
    } else {
        isDarkMode = false;
        darkMode(0)
    }

} else {
    isDarkMode = false;
    darkMode(0);
}

let light = true;

function chooseTheme() {
    if (window.sessionStorage.getItem("DarkMode") != null) {
        if (window.sessionStorage.getItem("DarkMode") == 1) {
            light = false;
            darkMode(0)
        } else {
            light = true;
            darkMode(0.5)
        }
    } else {
        light = true;
        darkMode(0);
    }
}


function darkMode(brightness) {
    if (typeof (div) == 'undefined') {
        div = document.createElement('div');
        div.setAttribute('style', 'position:fixed;top:0;left:0;outline:5000px solid;z-index:99999;');
        document.body.appendChild(div);

    } else {
        div.style.display = '';
    }
    if (brightness == 0.5) {
        isDarkMode = true
        window.sessionStorage.setItem("DarkMode", "1")
    } else {
        isDarkMode = false
        window.sessionStorage.setItem("DarkMode", "0")
    }
    if (isDarkMode)
        $("*").each(function () {
            if (this.classList[0] != null)
                $(this).addClass(this.classList[0] + "-dark")
        });
    else
        $("*").each(function () {
            if (this.classList[0] != null)
                $(this).removeClass(this.classList[0] + "-dark")
        });
    div.style.outlineColor = 'rgba(0,0,0,' + brightness + ')';
}

let lis = document.querySelectorAll("li")
//console.log(lis)
for (let i = 0; i < lis.length; i++) {
    lis[i].onclick = function () {
        for (let k = 1; k < lis.length; k++) {
            lis[k].className = ""
            //console.log(lis[k])
        }
        this.className = "for-javascript"
        //alert(lis[i].className)
    }
}

