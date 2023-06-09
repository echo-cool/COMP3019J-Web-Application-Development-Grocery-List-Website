// function expandSelect() {
//     let box = document.querySelector(".search-result-list")
//     box.setAttribute("class", "test")
// }
const csrf_token = $("meta[name=csrf-token]").attr("content");
$(document).ready(function () {
    console.log("ready!")
    // $(".index-search-text").on("focusout", function () {
    //
    //     $(".search-result-list").empty();
    //
    // });
    $(".index-search-text").on("input focus", function (e) {

        const input_data = $(this).val();
        //ajax search
        $.ajax({
            url: "/search_ajax",
            type: "POST",
            data: {
                "keyword": input_data,
            },
            headers: {"X-CSRFToken": csrf_token},
            success: function (data) {
                console.log(data)
                //empty the list
                $(".search-result-list").empty();
                //load the data to the list
                for (let item_name in data) {
                    $(".search-result-list").append(
                        "<li class='search-list-item'>" +
                        "<a href='/search" + "?csrf_token=" + csrf_token + "&keyword=" + data[item_name] + "'" + ">" +
                        data[item_name] +
                        "</a>" +
                        "</li>"
                    );
                }
            }
        });

    });


    $(".index-item-image-big").on("mouseover", function () {
        //mouse over the iframe then show the iframe
        console.log($(this))
        let url = $(this).parent().attr("href");
        console.log(url);
        const iframe = $('<iframe id="mainIframe" name="mainIframe" src="' + url + '" frameborder="0" scrolling="no" ></iframe>');
        //scale it to fit the screen
        iframe.css({
            "position": "absolute",
            "width": "1190px",
            "height": "800px",
            "z-index": "999999999",
            "transform": "translate(-58%, -15%) scale(0.2)",
        });
        $(this).parent().append(iframe.clone().addClass("index-item-image-clone"));
    });
    $(".index-item-image-big").on("mouseleave", function () {
        $(".index-item-image-clone").remove();
    });

    //lower page image
    $(".index-item-image").on("mouseover", function () {
        console.log($(this))
        let url = $(this).parent().attr("href");
        console.log(url);
        const iframe = $('<iframe id="mainIframe" name="mainIframe" src="' + url + '" frameborder="0" scrolling="no" ></iframe>');
        //same as the upper page image
        iframe.css({
            "position": "absolute",
            "width": "1190px",
            "height": "800px",
            "z-index": "999999999",
            "transform": "translate(-58%, -15%) scale(0.2)",
        });
        $(this).parent().append(iframe.clone().addClass("index-item-image-clone"));
    });
    $(".index-item-image").on("mouseleave", function () {
        //mouse leave the image, remove the iframe.
        $(".index-item-image-clone").remove();
    });

})

function clear_search_result() {
    $(".search-result-list").empty();
}