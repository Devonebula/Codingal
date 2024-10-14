var d= new Date()
var year=d.getFullYear()
var month = d.getMonth()
var day = d.getDay()
var date = d.getDate() 
var day2=''
var days=["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]
// if(day==0){
//     day2='Sunday'
// }
// else if(day==1){
//     day2='Monday'
// }
// else if(day==2){
//     day2='Tuesday'
// }
// else if(day==3){
//     day2='Wednesday'
// }
// else if(day==4){
//     day2='Thursday'
// }
// else if(day==5){
//     day2='Friday'
// }
// else if(day==6){
//     day2='Saturday'
// }
var m=["jan","Feb","March", "April","may","June","July","Aug","September"]

document.write('Today is'+date+'/'+days[day]+'/'+'in the month of '+m[month]+'/'+'in the year of'+year)