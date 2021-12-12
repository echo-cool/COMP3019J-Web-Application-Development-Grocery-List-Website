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
                // alert("Item added to cart!");
                var imgtodrag = $("#product-image-file");
                var cart = $('#shopping-cart-text-nav');

                var imgclone = imgtodrag
                    .clone()
                    .offset({
                        top: imgtodrag.offset().top,
                        left: imgtodrag.offset().left
                    })
                    .css({
                        'opacity': '0.8',
                        'position': 'absolute',
                        'height': '150px',
                        'width': '150px',
                        'z-index': '100'
                    })
                    .appendTo($('body'));

                imgclone.attr("style",
                    "position:absolute;height:0px;width:0px;z-index:100;top:" + cart.offset().top + "px;left:" + cart.offset().left + "px;");
                // setInterval(function () {
                //     console.log(imgclone.attr("style"));
                // }, 100);
                // .animate({
                //     'top': cart.offset().top + 10,
                //     'left': cart.offset().left + 10,
                //     'width': 75,
                //     'height': 75
                // }, 1000, 'easeInOutExpo');
                // .animate({
                //     'top': cart.offset().top + 10,
                //     'left': cart.offset().left + 10,
                //     'width': 75,
                //     'height': 75
                // }, 1000, 'easeInOutExpo');

                // imgclone.animate({
                //     'width': 0,
                //     'height': 0
                // }, function () {
                //     $(this).detach()
                // });

                // setTimeout(function () {
                //     cart.effect("shake", {
                //         times: 2
                //     }, 200);
                // }, 1500);
            },
            error: function (){
                location.assign("/login");
            }
        });

    });
});

$