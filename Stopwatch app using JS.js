var h=0
var m=0
var s=0
var ms=0
var timer=false
function start(){
    timer=true
    sw()
}
function stop(){
    timer=false
    sw()
}
function reset(){
    timer=false
    h=0
    m=0
    s=0
    ms=0
    document.getElementById("h").innerHTML='00'
    document.getElementById("s").innerHTML='00'
    document.getElementById('m').innerHTML='00'
    document.getElementById("ms").innerHTML='00'
}
function sw(){
    if(timer==true){
        ms++
        if(ms==100){
            s++
            ms=0
        }
        if(s==60){
            m++
            s=0
        }
        if(m==60){
            h++
            m=0
        }
        var hh=h
        var mm=m
        var ss=s
        var sss=ms
        if(h<10){
            hh='0'+h
        }
        if(m<10){
            mm='0'+m
        }
        if(s<10){
            ss='0'+s
        }
        if(ms<10){
            sss='0'+ms
        }
    
    document.getElementById("h").innerHTML=hh
    document.getElementById("s").innerHTML=ss
    document.getElementById('m').innerHTML=mm
    document.getElementById("ms").innerHTML=sss
    setTimeout(sw,10)
}}