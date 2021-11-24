// identify the element
let enter_product_name = document.querySelector("#enter_product_name");
// register event
enter_product_name.onclick = function () {
    // onfocus
    enter_product_name.onfocus = function () {
        console.log(this.value);
        if (this.value === "Enter the product name") {
            this.value = "";
        }
    }
    // onblur
    enter_product_name.onblur = function () {
        this.value = "Enter the product name";
    }
}