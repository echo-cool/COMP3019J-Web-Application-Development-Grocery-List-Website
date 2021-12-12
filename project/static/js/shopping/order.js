function alertNotConfirmedBySeller() {
    alert("Sorry you cannot confirm this order\nbecause it has not been confirmed by the seller!")
}

function alertConfirmedBySeller() {
    // alert("That is fine!")
}

let btn = document.querySelector('.dialogue-message-box');

$(".message-button-action-new").on("click", function (e) {

    //get x,y corrdinates of the button
    let mx = e.clientX - btn.offsetLeft,
        my = e.clientY - btn.offsetTop;

    //get the button's width and height
    let w = $(this).offsetWidth,
        h = $(this).offsetHeight;

    //get the button's position
    let directions = [
        {id: 'top', x: w / 2, y: 0},
        {id: 'right', x: w, y: h / 2},
        {id: 'bottom', x: w / 2, y: h},
        {id: 'left', x: 0, y: h / 2}
    ];

    directions.sort(function (a, b) {
        return distance(mx, my, a.x, a.y) - distance(mx, my, b.x, b.y);
    });
   //The shift() method removes the first element from an array and returns that removed element. This method changes the length of the array.
    $(this).parent().attr('data-direction', directions.shift().id);
    $(this).parent().addClass('is-open');
});

// click yes
$(".dialogue-message-yes-button").on("click", function () {
    console.log("yes");
    //close the dialogue box
    $(this).parent().parent().removeClass('is-open');

})
;

// function btnYes() {
//     btn.classList.remove('is-open');
// }

// click no
$(".dialogue-message-no-button").on("click", function () {
    console.log("no");
    //close the dialogue box
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
