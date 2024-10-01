function validation() {
    var a = document.getElementById('no')

    if (!a.checkValidity()) {
        document.getElementById('result').innerHTML = a.validationMessage;
    }
    else
        document.getElementById('result').innerHTML = "input is Valid"
}