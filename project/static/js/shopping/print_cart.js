$(document).ready(function () {
    $('#print_cart').click(function () {
        //hide the button for printing
        $('#print_cart').hide();
        //print dialog
        window.print();
        $('#print_cart').show();
    });
    setTimeout(function () {
        //same but with a timeout
        $('#print_cart').hide();
        window.print();
        $('#print_cart').show();
    }, 500);
});