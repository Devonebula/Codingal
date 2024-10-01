function setScreenValue(value){
    document.getElementById("result").value += value;
}
function clearScreen(){
    document.getElementById("result").value = "";
}
function calculateResult(){
    var a=document.getElementById("result").value;
    var b=eval(a);
    document.getElementById("result").value = b;
}