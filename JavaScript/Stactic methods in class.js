class person{
    constructor(name,age){
        this.name=name
        this.age=age
    }

    static greeting(){
        return("Hello, how are you")
    }

    name(){
        return("my name is Keshav")
    }
}
document.write(person.greeting())
