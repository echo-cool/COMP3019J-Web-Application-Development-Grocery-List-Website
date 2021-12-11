$(document).ready(function () {

    $(".shopping-cart").on("click", function (e) {

        let itemID = $("#item-id-hidden").val();
        let quantity = $("#quantity-hidden").val();

        $("#shopping-cart-text-nav")

        $.ajax({
            url: "/cart/add",
            type: "POST",
            data: {
                itemID: itemID,
                itemCount: quantity,
                csrf_token: $("meta[name='csrf-token']").attr("content")
            },
            success: function (data) {
                alert("Item added to cart!");
            }
        });
    });
});