const timeout = 10;
let closeTimer = 0;
let oldLayer = 0;

// open hidden layer
function layer_open(id) {
    // cancel the close timer
    cancel_close_timer();

    // close the old layer (hidden)
    if (oldLayer) oldLayer.style.visibility = 'hidden';

    // make new layer visible by displaying it
    oldLayer = document.getElementById(id);
    oldLayer.style.visibility = 'visible';

}

// close the layer by making it hidden
function close_layer() {
    if (oldLayer) oldLayer.style.visibility = 'hidden';
}

// call the close timer
function close_timer() {
    closeTimer = window.setTimeout(close_layer, timeout);
}

// cancel the close timer
function cancel_close_timer() {
    if (closeTimer) {
        window.clearTimeout(closeTimer);
        closeTimer = null;
    }
}

// close the layer when the mouse moves away
document.onclick = close_layer;