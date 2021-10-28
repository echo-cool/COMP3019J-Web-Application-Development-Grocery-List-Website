var csrftoken = $("meta[name=csrf-token]").attr("content");

function cart_add(itemID) {
    var itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value) + 1;
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
    var itemCount = Number.parseInt($("#item-quantity-id-" + itemID)[0].value) - 1;
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

// $(".minus-page-button-area").addEventListener("click", function () {
//
// })