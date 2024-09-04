var choice=prompt('Welcome to area calculator app \n 1.Area of Rectangle\n 2.Area of Circle\n 3.Area of square \n 4.area of triangle')
if(choice=='1'){
    var  l=prompt('Enter the length')
    var w=prompt('Enter the width')
    var result=Number (l)*Number (w)
    alert('The area of rectangle is '+result)}
if(choice=='2'){
    var  r=prompt('Enter the radie')
    var P=Math.PI
    var result= P*Number(r)*Number(r)
    alert('The area of circle is '+result)}

if(choice=='3'){
    var  s=prompt('Enter the side')
    var result=Math.pow(Number(s),2)
    alert('The area of square is '+result)}
if(choice=='4'){
    var  b=prompt('Enter the base')
    var h=prompt('Enter the height')
    var result=(Number (h)*Number (b))/2
    alert('The area of triangle is '+result)}