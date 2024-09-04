function validation(){
    var email=document.getElementById("email").value;
    var password=document.getElementById("pass").value

    if((email=="" ) && (password==""))
    {
        alert("Please fill all the fields")
    }
    else if(!email.includes("@")){
        alert("Please enter valid email")
    }
    else if(password.length<8){
        alert("Password should be more than 8 characters")
    }
    else{
        alert("Form Submitted")
    }}