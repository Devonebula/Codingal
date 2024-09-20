var dices = ['&#9856;', '&#9857;', '&#9858;', '&#9859;', '&#9860;', '&#9861;'];
var stop = true;
var c;
document.getElementById('roll').addEventListener('click', rolldice);
function rolldice() {
    if (stop) {
        stop = false
        c = setInterval(change, 100)
    }
    else {
        stop = true
        clearInterval(c)
    }

}
function change() {
    var r = Math.floor(Math.random() * 6)
    document.getElementById('dice').innerHTML = dices[r]
}