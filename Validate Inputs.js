function validation(){

    var name=document.getElementById("name").value
    var age=document.getElementById("age").value

    if((name=="" ) || (age=="")){
        alert("Please fill all the fields")
    }
    else if(age<18){
        alert("Age should be greater than 18")
    }
    else{
        alert("Form Submitted")
    }
}