function alertNotConfirmedBySeller(){
    alert("Sorry you cannot confirm this order\nbecause it has not been confirmed by the seller!")
}

function alertConfirmedBySeller(){
    // alert("That is fine!")
}

let btn = document.querySelector('.dialogue-message-box');

$(".message-button-action-new").on("click", function (e) {

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
    if (confirm("This action will clear **ALL** data from the **database**.\n Are you sure you want to continue?")) {
        let number1 = Math.floor(Math.random() * 10);
        let number2 = Math.floor(Math.random() * 10);
        const input_text = prompt("Please enter the result of this calculation\n\n" + number1 + " + " + number2 + "\n", "");
        if (input_text == (number1 + number2).toString()) {
            let timestamp = new Date().getTime();
            $.ajax({
                url: "/admin/del_all_tables?timestamp=" + timestamp,
                type: "GET",
                data: {},
                success: function (data) {
                    if (data.status === "success") {
                        alert("Delete all tables success");
                        $(this).parent().parent().removeClass('is-open');
                        location.assign("/");
                    }
                }
            });
        } else {
            alert("I don't think you are doing the right thing.\n\n**Please don't do this.**\n\nDatabase was not changed.");
        }
    }

})
;

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
