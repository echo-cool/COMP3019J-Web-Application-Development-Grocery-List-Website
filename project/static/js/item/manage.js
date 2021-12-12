$(document).ready(function () {
    $("a[id^=remove-item-button-]").click(function () {
        let item_id = $(this).attr("id").split("-").pop();
        $.ajax({
            url: "/item/delete/" + item_id,
            type: "GET",
            success: function (data) {
                $("#manage-items-box-table-data")[0].innerHTML = $(data).find("#manage-items-box-table-data")[0].innerHTML;
            }
        });
    });
});