// public class OOPS {
//     public static void main(String[] args) {
//         Pen p1=new Pen();
//         p1.setcolor("red");
//         p1.setname("xo");
//         p1.settip(5);
//         System.out.println("penclr:"+ p1.color +" "+ "tipsize:" +p1.tip + " " + "pen name:" + p1.name);
//     }
// }

// class Pen{
//     String color;
//     String name;
//     int tip;
// //if we use private modifier then we cannot access the data from this class so even after not able acces the data we use getters to access the value
//     //private String color;
//     //private String name;
//     //private int tip;
// //we use now getter to access
//     String getcolor(){
//         return color;
//     }

//     String getname(){
//         return name;
//     }
//     int gettip(){
//         return tip;
//     }
// //now i can use this getters in main function to get the value    
//     void setcolor(String newcolor){
//         color=newcolor;
//     }
//     void  settip(int newtip){
//         tip=newtip;
//     }

//     void setname(String newname){
//         name=newname;
//     }
// }

public class OOPS {
    public static void main(String[] args) {
        eagle e1=new eagle();
        e1.attack();
        System.out.print(e1);
    }
    
}

class Animal{
    String breed;

    void walk(){
        System.out.println("walks");
    }
    void attack(){
        System.out.println("attacks");
    }
}

class dog extends Animal{
    void bark(){
        System.out.println("barks");
    }
}

class bird extends Animal{
    void fly(){
        System.out.println("flys");
    }
}

class eagle extends bird{
    void highfly(){
        System.out.println("flys high");
    }
}