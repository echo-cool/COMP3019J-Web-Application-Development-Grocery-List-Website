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
        $.ajax({
            url: "/search_ajax",
            type: "POST",
            data: {
                "keyword": input_data,
            },
            headers: {"X-CSRFToken": csrf_token},
            success: function (data) {
                console.log(data)
                $(".search-result-list").empty();
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
        })

    })
})

function clear_search_result() {
    $(".search-result-list").empty();
}