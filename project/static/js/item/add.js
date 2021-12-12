$("#item-name-input-text").on("focus input", function () {
    const input = $(this);
    const is_name = input.val();
    if (is_name.length > 0) {
        input.removeClass("invalid").addClass("valid");
    } else {
        input.removeClass("valid").addClass("invalid");
    }
});

$("#item-price-input-text").on("focus input", function () {
    const input = $(this);
    const is_price = input.val();
    if (is_price.length > 0 && is_price.match(/^[0-9\.]*$/)) {
        input.removeClass("invalid").addClass("valid");
    } else {
        input.removeClass("valid").addClass("invalid");
    }
});

$("#item-price-input-description").on("focus input", function () {
    const input = $(this);
    const is_description = input.val();
    if (is_description.length > 5) {
        input.removeClass("invalid").addClass("valid");
    } else {
        input.removeClass("valid").addClass("invalid");
    }
});

$("#item-price-input-inventory").on("focus input", function () {
    const input = $(this);
    const is_inventory = input.val();
    if (is_inventory.length > 0 && is_inventory.match(/^[0-9]*$/)) {
        input.removeClass("invalid").addClass("valid");
    } else {
        input.removeClass("valid").addClass("invalid");
    }
});