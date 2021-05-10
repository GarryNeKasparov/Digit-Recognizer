window.addEventListener("load", function onWindowLoad() {
    var canvas = document.getElementById("input");
    var context = canvas.getContext("2d");
    
    //context.fillStyle = "white";
    context.lineCap = "round";
    context.lineWidth = 8;
    //context.fillRect(0, 0, canvas.width, canvas.height)


    document.getElementById("clear").onclick = function c() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        var status = document.getElementById("status");
        status.innerHTML = "Hello";
    };
    document.getElementById("predict").onclick = function pred() {
        //var image = context.toDataURL("image.png");
        //document.querySelector('.image').src = image;
        var status = document.getElementById("status")
        status.innerHTML = "I think it's"
        //console.log("hello");
    };
    canvas.onmousemove = function drawIfPressed (e) {
        var x = e.offsetX;
        var y = e.offsetY;
        var dx = e.movementX;
        var dy = e.movementY;

        if (e.buttons > 0) {
            context.beginPath();
            context.moveTo(x, y);
            context.lineTo(x - dx, y - dy);
            context.stroke();
            context.closePath();
        }
    };
});
