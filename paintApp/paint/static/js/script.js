window.addEventListener("load", function onWindowLoad() {
    var canvas = document.getElementById("input");
    var context = canvas.getContext("2d");

    context.fillStyle = "white";
    context.lineCap = "round";
    context.lineWidth = 8;
    context.fillRect(0, 0, canvas.width, canvas.height)


    document.getElementById("clear").onclick = function clear() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        var status = document.getElementById("status");
        status.innerHTML = "Draw a digit";
    };
    canvas.onmousemove = function drawIfPressed (e) {
        var x = e.offsetX;
        var y = e.offsetY;
        var dx = e.movementX;
        var dy = e.movementY;

        if (e.button > 0) {
            context.beginPath();
            context.moveTo(x, y);
            context.lineTo(x - dx, y - dy);
            context.stroke();
            context.closePath();
        }
    };

});
