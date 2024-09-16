// var s=prompt('Enter the string')
// s1=s.split('').reverse().join('')
// if(s==s1){
//     alert('palindrome')
// }
// else{
//     alert('not a palindrome')
// }

var s=prompt('Enter the string')
s1=s.length
var a=true;
for(i=0;i<s1/2;i++){
    if(s[i]!==s[s1-1-i]){
        a=false
    }
}
if(a==true){
    alert('palindrome')
}
else{
    alert('not a palindrome')
}