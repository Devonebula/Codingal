class student{
    constructor(name,pen){
        this.name=name
        this.pen=pen

    }
    static greeting_1(){
        return("Hello, my name is"+ this.name)
    }
    return(){
        return(this.name +'have a'+ this.pen)
    }
    }
    class teacher extends student{
        constructor(name,pen,book){
            super(name,pen)
            this.book=book
        }
        static greeting_2(){
            return('Hello, I am the teacher of'+ this.name)
        }
        return(){
            return('My student,'+this.name +'have a'+ this.book)
        }
    }
    let student=new student("Keshav","parker")
    let teacher=new teacher("story book")
    document.write(student.greeting_1()+'<br>')
    document.write(student.return()+'<br>')
    document.write(teacher.greeting_2()+'<br>')
    document.write(teacher.return()+'<br>')
