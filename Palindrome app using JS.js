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
for(i=0;i<s1/2;i++){
    if(s[i]!==s[s1-1-i]){
        alert("not a palindrome")
        break
    }
    alert("palindrome")     
    }
