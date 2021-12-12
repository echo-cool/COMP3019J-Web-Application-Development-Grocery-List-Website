$(document).ready(function () {
    $('#print_cart').click(function () {
        $('#print_cart').hide();
        window.print();
        $('#print_cart').show();
    });
    setTimeout(function () {
        $('#print_cart').hide();
        window.print();
        $('#print_cart').show();
    }, 300);
});