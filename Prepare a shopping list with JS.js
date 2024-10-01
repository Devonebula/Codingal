function additem(){
    var input=document.getElementById('input').value
    if(input.value ===  ''){
        alert('Enter the item')
    }
    else{
    var int=document.getElementById('input')
    var ulist=document.getElementById('list')

    var li=document.createElement('li')
    li.textContent=input
    var button=document.createElement('button')
    button.textContent='Delete'
    li.appendChild(button)
    ulist.appendChild(li)
    button.addEventListener('click',()=>{ulist.removeChild(li)})
    int.value=''
    }
}

button.addEventListener('click',additem())

document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        additem()
    }
})