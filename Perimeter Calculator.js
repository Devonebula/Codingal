var choice=prompt('Welcome to Perimiter calculator app \n 1.Perimeter of Rectangle\n 2.Perimeter of Circle\n 3.Perimeter of square \n 4.Perimeter of triangle')
if(choice=='1'){
    var  l=prompt('Enter the length')
    var w=prompt('Enter the width')
    var result=2*(Number (l)+Number(w))
    alert('The Perimeter of rectangle is '+result)}
if(choice=='2'){
    var  r=prompt('Enter the radie')
    var P=Math.PI
    var result= 2*P*Number(r)
    alert('The Perimeter of circle is '+result)}

if(choice=='3'){
    var  s=prompt('Enter the side')
    var result=4*Number(s)
    alert('The Perimeter of square is '+result)}
if(choice=='4'){
    var  b=prompt('Enter the base')
    var h=prompt('Enter the height')
    var result=2*(Number (h)+Number (b))
    alert('The Perimeter of triangle is '+result)}