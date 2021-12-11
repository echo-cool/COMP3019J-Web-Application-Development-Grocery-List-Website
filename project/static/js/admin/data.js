let btn = document.querySelector('.btn');

// the following codes are partly adapted from this link:
// no. 42
// https://pan.baidu.com/s/1XCmR5eGgKZJTYQN08779xw#list/path=%2Fsharelink2789904698-143656889326290%2Fsrc&parentPath=%2Fsharelink2789904698-143656889326290

function btnFront() {
    let mx = event.clientX - btn.offsetLeft,
        my = event.clientY - btn.offsetTop;

    let w = btn.offsetWidth,
        h = btn.offsetHeight;

    let directions = [
        {id: 'top', x: w / 2, y: 0},
        {id: 'right', x: w, y: h / 2},
        {id: 'bottom', x: w / 2, y: h},
        {id: 'left', x: 0, y: h / 2}
    ];

    directions.sort(function (a, b) {
        return distance(mx, my, a.x, a.y) - distance(mx, my, b.x, b.y);
    });

    btn.setAttribute('data-direction', directions.shift().id);
    btn.classList.add('is-open');
}

// click yes
function btnYes() {
    btn.classList.remove('is-open');
}

// click no
function btnNo() {
    btn.classList.remove('is-open');
}

// calculate the correct position
function distance(x1, y1, x2, y2) {
    let dx = x1 - x2;
    let dy = y1 - y2;
    return Math.sqrt(dx * dx + dy * dy);
}    
    