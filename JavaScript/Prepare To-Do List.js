function addtodo(){
    var int=document.getElementById('input')
    var ulist=document.getElementById('list')
    var in_t=document.getElementById('input').value
    var li=document.createElement('li')
    li.textContent=in_t
    var button=document.createElement('button')
    button.textContent='Delete'
    li.appendChild(button)
    ulist.appendChild(li)
    button.addEventListener('click',()=>{ulist.removeChild(li)})
    int.value=''
}

button.addEventListener('click',addtodo())

document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        addtodo()
    }
})