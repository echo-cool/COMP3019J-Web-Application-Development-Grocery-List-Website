let btn = document.querySelector('.dialogue-message-box');

$(".message-button-action").on("click", function (e) {

    let mx = e.clientX - btn.offsetLeft,
        my = e.clientY - btn.offsetTop;

    let w = $(this).offsetWidth,
        h = $(this).offsetHeight;

    let directions = [
        {id: 'top', x: w / 2, y: 0},
        {id: 'right', x: w, y: h / 2},
        {id: 'bottom', x: w / 2, y: h},
        {id: 'left', x: 0, y: h / 2}
    ];

    directions.sort(function (a, b) {
        return distance(mx, my, a.x, a.y) - distance(mx, my, b.x, b.y);
    });

    $(this).parent().attr('data-direction', directions.shift().id);
    $(this).parent().addClass('is-open');
});

// click yes
$(".dialogue-message-yes-button").on("click", function () {
    console.log("yes");
    $(this).parent().parent().removeClass('is-open');
});

// function btnYes() {
//     btn.classList.remove('is-open');
// }

// click no
$(".dialogue-message-no-button").on("click", function () {
    console.log("no");
    $(this).parent().parent().removeClass('is-open');
});

// function btnNo() {
//     btn.classList.remove('is-open');
// }

// calculate the correct position
function distance(x1, y1, x2, y2) {
    let dx = x1 - x2;
    let dy = y1 - y2;
    return Math.sqrt(dx * dx + dy * dy);
}    
    