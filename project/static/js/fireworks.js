var canvasEl = document.querySelector('.fireworks')
if (canvasEl) {
    var ctx = canvasEl.getContext('2d')
    var pointerX = 0
    var pointerY = 0
    var tap = 'mousedown' //click event
    var colors = ['#FF1461', '#18FF92', '#5A87FF', '#FBF38C', '#FBF38C'] //colors

    //set canvas same as window
    canvasEl.width = window.innerWidth
    canvasEl.height = window.innerHeight
    canvasEl.style.width = window.innerWidth + 'px'
    canvasEl.style.height = window.innerHeight + 'px'
    canvasEl.getContext('2d').scale(1, 1)

    //click listener
    document.addEventListener(tap, function (e) {
        if (e.target.id !== 'sidebar' && e.target.id !== 'toggle-sidebar' && e.target.nodeName !== 'A' && e.target.nodeName !== 'IMG') {
            updateCoords(e) //update position
            animateParticules(pointerX, pointerY) //draw
        }
    }, false)
}

function updateCoords(e) {
    pointerX = (e.clientX || e.touches[0].clientX) - canvasEl.getBoundingClientRect().left
    pointerY = e.clientY || e.touches[0].clientY - canvasEl.getBoundingClientRect().top
}

function animateParticules(x, y) {

    // canvasEl.style = "animation: Fadeout 0.5s ease-in 0s backwards;"
    var run_color = new Array();
    for (let count = 0; count < 40; count++) {
        run_color[count] = colors[Number.parseInt(Math.random() * 5)]; //gen color of each particle
    }

    for (let i = 0; i < 100; i++) {

        setTimeout(function () {
            clearCanvas(); //clear
            var radious1 = i * 2;
            var radious2 = i * 3;

            count = 0;
            for (let r = 0.0; r < 2 * Math.PI; r += Math.PI / 10) {
                var delta_x = Math.sin(r);
                var delta_y = Math.cos(r);

                // ctx.arc(x + radious1 * delta_x, y + radious1 * delta_y, 10 - i / 10, 0, Math.PI * 2, true);
                // ctx.closePath();
                // ctx.fillStyle = "green";
                // ctx.fill();
                ctx.fillStyle = run_color[count];
                // ctx.fillText("O", x + radious1 * delta_x, y + radious1 * delta_y)
                ctx.fillRect(x + radious1 * delta_x, y + radious1 * delta_y, 10 - i / 10, 10 - i / 10);
                ctx.fillRect(x + radious2 * delta_x, y + radious2 * delta_y, 20 - i / 5, 20 - i / 5);
                count += 1;
            }

        }, i * 5); //move the particle
    }
    setTimeout(function () {
        clearCanvas();
        // canvasEl.style = "animation: none;"
    }, 99 * 5)


}

function clearCanvas() {
    var cxt = canvasEl.getContext("2d");
    cxt.clearRect(0, 0, canvasEl.width, canvasEl.height);
}