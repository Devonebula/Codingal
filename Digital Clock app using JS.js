function gettime(){
    var date=new Date();
    var h=date.getHours();
    var m=date.getMinutes();
    var s=date.getSeconds();
   var session='AM';
   if(h>12){
    h=h-12;
    session='PM';
   }
   if(h==0){
    h=12;
    session='PM';
   }
   if(h<10){
    h='0'+h;
   }
   
   if(m<10){
    h='0'+m;
   }
   
   if(s<10){
    h='0'+s;
   }

   var time=h+':'+m+':'+s+' '+ session;
   document.getElementById('clock').innerText=time;
   setTimeout(gettime,1000)
}
gettime()