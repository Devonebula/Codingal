class gf{
    constructor(bike,house){
        this.bike=bike
        this.house=house
    }
    display_gf(){
        return ("GF have a "+this.bike+" and a "+this.house)
    }
}
class f extends gf{
    constructor(bike,house,car){
        super(bike,house)
        this.car=car
    }
    display_f(){
        return("F have a "+this.bike+" and a "+this.house+" and a "+this.car)
    }
}
var f1=new f ("BMW","mansion","Car")
document.write(f1.display_gf())