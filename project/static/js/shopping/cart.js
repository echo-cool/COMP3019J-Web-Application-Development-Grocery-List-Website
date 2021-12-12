const csrf_token = $("meta[name=csrf-token]").attr("content");

function cart_add(itemID) {
    var item_inventory = Number.parseInt($("#item-inventory-id-" + itemID)[0].textContent);
    var itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value) + 1;
    if (item_inventory - itemCount < 0) {
        alert("You can't have more then inventory !")
        itemCount = item_inventory;
    }
    console.log(itemID, itemCount)
    console.log(csrf_token)
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrf_token},
        success: function (data) {
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
                let trs = $(".shopping-cart-box-table tr");
                for (let i = 0; i < trs.length; i++) {
                    if (i + 1 < trs.length) {
                        if (trs[i].className == "shopping-cart-seller" && trs[i].className == trs[i + 1].className) {
                            trs[i].remove();
                        }
                    }
                }
                calc_price();
                if ($("tr[id^='item-entry-id-']").length == 0) {
                    // location.reload();
                    $.ajax({
                        url: "/cart",
                        type: "GET",
                        success: function (data) {
                            $("#shopping-cart-box").html($(data).find("#shopping-cart-box")[0].innerHTML);
                        }
                    })

                }
            } else {
                $("#item-quantity-id-" + itemID)[0].value = itemCount;
                $("#item-total_price-id-" + itemID)[0].textContent = Number.parseInt($("#item-price-id-" + itemID)[0].textContent) * itemCount;
                const price_array = $(".item-total-perice");
                var cart_total_price = 0;
                for (let i = 0; i < price_array.length; i++) {
                    cart_total_price += Number.parseFloat(price_array[i].textContent);
                }
                $(".checkout-total-payment")[0].textContent = "Total Price: " + cart_total_price;
                $("#shopping-cart-box-head-price")[0].textContent = "Total Price: " + cart_total_price;
            }
        },
        error: function (data) {
            console.log("Error")
        }
    });
}

function cart_minus(itemID) {
    var item_inventory = Number.parseInt($("#item-inventory-id-" + itemID)[0].textContent);
    var itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value) - 1;
    if (item_inventory - itemCount < 0) {
        alert("You can't have more then inventory !")
        itemCount = item_inventory;
    }
    console.log(itemID, itemCount)
    console.log(csrf_token)
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrf_token},
        success: function (data) {
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
                let trs = $(".shopping-cart-box-table tr");
                for (let i = 0; i < trs.length; i++) {
                    if (i + 1 < trs.length) {
                        if (trs[i].className == "shopping-cart-seller" && trs[i].className == trs[i + 1].className) {
                            trs[i].remove();
                        }
                    }
                }
                calc_price();
                if ($("tr[id^='item-entry-id-']").length == 0) {
                    // location.reload();
                    $.ajax({
                        url: "/cart",
                        type: "GET",
                        success: function (data) {
                            $("#shopping-cart-box").html($(data).find("#shopping-cart-box")[0].innerHTML);
                        }
                    })

                }
            } else {
                $("#item-quantity-id-" + itemID)[0].value = itemCount;
                $("#item-total_price-id-" + itemID)[0].textContent = Number.parseInt($("#item-price-id-" + itemID)[0].textContent) * itemCount;
                const price_array = $(".item-total-perice");
                var cart_total_price = 0;
                for (let i = 0; i < price_array.length; i++) {
                    cart_total_price += Number.parseFloat(price_array[i].textContent);
                }
                $(".checkout-total-payment")[0].textContent = "Total Price: " + cart_total_price;
                $("#shopping-cart-box-head-price")[0].textContent = "Total Price: " + cart_total_price;
            }
        },
        error: function (data) {
            console.log("Error")
        }
    });
}

function calc_price() {
    trs = $("tr[id^='item-entry-id-']");
    var total_price = 0;
    for (let i = 0; i < trs.length; i++) {
        const tr = trs[i];
        const itemID = tr.id.split("-")[3];
        const itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value);
        total_price += Number.parseInt($("#item-price-id-" + itemID)[0].textContent) * itemCount;
    }
    $(".checkout-total-payment")[0].textContent = "Total Price: " + total_price;
    $("#shopping-cart-box-head-price")[0].textContent = "Total Price: " + total_price;
}

function cart_set(itemID, itemCount) {
    var item_inventory = Number.parseInt($("#item-inventory-id-" + itemID)[0].textContent);

    console.log(itemID, itemCount)
    console.log(csrf_token)
    if (item_inventory - itemCount < 0) {
        alert("You can't have more then inventory !")
        itemCount = item_inventory;
    }
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrf_token},
        success: function (data) {
            console.log("success")
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
                let trs = $(".shopping-cart-box-table tr");
                for (let i = 0; i < trs.length; i++) {
                    if (i + 1 < trs.length) {
                        if (trs[i].className == "shopping-cart-seller" && trs[i].className == trs[i + 1].className) {
                            trs[i].remove();
                        }
                    }
                }
                calc_price();
                if ($("tr[id^='item-entry-id-']").length == 0) {
                    // location.reload();
                    $.ajax({
                        url: "/cart",
                        type: "GET",
                        success: function (data) {
                            $("#shopping-cart-box").html($(data).find("#shopping-cart-box")[0].innerHTML);
                        }
                    })

                }


            } else {
                $("#item-quantity-id-" + itemID)[0].value = itemCount;
                $("#item-total_price-id-" + itemID)[0].textContent = Number.parseInt($("#item-price-id-" + itemID)[0].textContent) * itemCount;
                const price_array = $(".item-total-perice");
                var cart_total_price = 0;
                for (let i = 0; i < price_array.length; i++) {
                    cart_total_price += Number.parseFloat(price_array[i].textContent);
                }
                $(".checkout-total-payment")[0].textContent = "Total Price: " + cart_total_price;
                $("#shopping-cart-box-head-price")[0].textContent = "Total Price: " + cart_total_price;
            }
        },
        error: function (data) {
            console.log("Error")
        }
    });
}

var input_quantity_array = $("input[id^='item-quantity-id-']");
for (let i = 0; i < input_quantity_array.length; i++) {
    var input_item = input_quantity_array[i];
    input_item.addEventListener("input", function (event) {
        var input_item = event.target;
        var itemID = input_item.id.split("-").pop();
        var itemCount = input_item.value;
        cart_set(itemID, itemCount)
    })
}

let selectAll = document.getElementById("select-all");
let selects = document.querySelectorAll("#select-one");
// add event to the selectAll
selectAll.onclick = function () {
    console.log(selects);
    for (let i = 0; i < selects.length; i++) {
        // get the current state: checked or not: this.checked
        selects[i].checked = this.checked;
    }
}

// add event to each selectOne
for (let i = 0; i < selects.length; i++) {
    // if one has been clicked
    selects[i].onclick = function () {
        // flag controls whether the selectAll has been clicked
        let flag = true;
        // check all: check whether they are selected --> effect the selected state of the selectAll
        for (let i = 0; i < selects.length; i++) {
            if (!selects[i].checked) {
                flag = false;
                break;
            }
        }
        selectAll.checked = flag;
    }
}

$(document).ready(function () {
    $(".removal-items-cart").on("click", function () {
        const itemID = $(this).attr("id").split("-").pop();
        console.log(itemID);

        cart_set(itemID, 0);
    })
})

// event handler: click button to remove items from the shopping cart
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

// event handler: click yes
$(".dialogue-message-yes-button").on("click", function () {
    console.log("yes");
    $(this).parent().parent().removeClass('is-open');

    const itemID = $(this).attr("id").split("-").pop();
    cart_set(itemID, 0);
});

// event handler: click no
$(".dialogue-message-no-button").on("click", function () {
    console.log("no");
    $(this).parent().parent().removeClass('is-open');
});

// event handler: calculate the correct position
function distance(x1, y1, x2, y2) {
    let dx = x1 - x2;
    let dy = y1 - y2;
    return Math.sqrt(dx * dx + dy * dy);
}
