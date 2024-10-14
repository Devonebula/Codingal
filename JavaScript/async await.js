async function party(){try{
    var msg=await cakePromise
    console.log(msg)
    console.log('party time')
}
catch(error){
    console.log(error)
}
}
let cakePromise=new Promise((resolve,reject )=>{
    let cakearrived=true
    if (cakearrived){
        resolve('cake is arrived')

    }
    else{
        reject('cake is not arrived')
    }
    
});
cakePromise.then((msg)=> {
    console.log(msg)
})
cakePromise.catch((error)=> {
    console.log(error)

})
party()