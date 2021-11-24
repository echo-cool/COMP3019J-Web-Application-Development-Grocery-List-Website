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

let index_banner_left = document.querySelector(".index-banner-button-left")
let index_banner_right = document.querySelector(".index-banner-button-right")
let index_banner_min = document.querySelectorAll(".index-banner-min-image")
let index_banner_images = document.querySelector(".index-banner-images-box")
// First set an index to calculate and control the position of the image, and then set a time as a timer
let index = 0
let time

// Here first create a position as a reuse function, the role is to combine index to define the current image position
function getPosition() {
    index_banner_images.style.top = (index * -100) + "%"
}

// Then create a reuse function add as an add function, if the current image position value index is
// greater than or equal to the current number of images,
// it means that the calculation range is exceeded, so we have to clear zero, if not index will be added one
function increaseTime() {
    if (index >= index_banner_min.length - 1) {
        index = 0
    } else {
        index++
    }
}

// Conversely desc is a minus function, if the current image position value index is less than 1,
// then his value will bounce to the top, that is, the last of the rotation map, if not index will be minus one
function decreaseTime() {
    if (index < 1) {
        index = index_banner_min.length - 1
    } else {
        index--
    }
}

// Create a timer to be used as a function of reuse time,, index every 3 seconds to add one,
// and then add add add function and desc function to determine a bit, and then add the positioning function
function timeCalc() {
    time = setInterval(() => {
        index++
        decreaseTime()
        increaseTime()
        getPosition()
    }, 1200)
}

// Set the button, left for the left button, because when you click the picture will be backwards in the opposite direction,
// so set into the desc minus function into, positioning
index_banner_left.addEventListener("click", () => {
    decreaseTime()
    getPosition()
    clearInterval(time)
    timeCalc()
})
// similar for the right button
index_banner_right.addEventListener("click", () => {
    increaseTime()
    getPosition()
    clearInterval(time)
    timeCalc()
})
// When you get the left and right buttons, you also need to take effect the small picture button below.
// First iterate through it, then get the value of the currently clicked small image button and assign it to index, then jump
for (let i = 0; i < index_banner_min.length; i++) {
    index_banner_min[i].addEventListener("click", () => {
        index = i
        getPosition()
        clearInterval(time)
        timeCalc()
    })
}
// Turn the timer on
timeCalc()