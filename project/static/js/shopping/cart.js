var csrftoken = $("meta[name=csrf-token]").attr("content");

function cart_add(itemID) {
    var item_inventory = Number.parseInt($("#item-inventory-id-" + itemID)[0].textContent);
    var itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value) + 1;
    if (item_inventory - itemCount < 0) {
        alert("You can't have more then inventory !")
        itemCount = item_inventory;
    }
    console.log(itemID, itemCount)
    console.log(csrftoken)
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrftoken},
        success: function (data) {
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
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
    console.log(csrftoken)
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrftoken},
        success: function (data) {
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
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

function cart_set(itemID, itemCount) {
    var item_inventory = Number.parseInt($("#item-inventory-id-" + itemID)[0].textContent);

    console.log(itemID, itemCount)
    console.log(csrftoken)
    if (item_inventory - itemCount < 0) {
        alert("You can't have more then inventory !")
        itemCount = item_inventory;
    }
    $.ajax({
        url: "/cart/set",
        type: "POST",
        dataType: "html",
        data: {"itemID": itemID, "itemCount": itemCount,},
        headers: {"X-CSRFToken": csrftoken},
        success: function (data) {
            console.log("success")
            if (itemCount <= 0) {
                $("#item-entry-id-" + itemID)[0].remove();
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

// function monitorEvents(element) {
//     var log = function (e) {
//         console.log(e);
//     };
//     var events = [];
//
//     for (var i in element) {
//         if (i.startsWith("on")) events.push(i.substr(2));
//     }
//     events.forEach(function (eventName) {
//         element.addEventListener(eventName, log);
//     });
// }

var input_quantity_array = $("input[id^='item-quantity-id-']");
for (let i = 0; i < input_quantity_array.length; i++) {
    var input_item = input_quantity_array[i];
    input_item.addEventListener("input", function (event) {
        var input_item = event.target;
        var itemID = input_item.id.split("-").pop();
        var itemCount = input_item.value;
        cart_set(itemID, itemCount)

    })
    // monitorEvents(input_item);
}

// $(".minus-page-button-area").addEventListener("click", function () {
//
// })