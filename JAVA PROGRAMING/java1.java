// public class java1{
//     public static void main(String args[]){
//         int a=10;
//         int b=25;
//         int c=30;
//         float average=(a+b+c)/3;
//         System.out.println(average);
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         float side= sc.nextFloat();
//         float area= side * side;
//         System.out.println(area);

//     }
// }



// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         Scanner sc= new Scanner(System.in);
//         float pen=sc.nextFloat();
//         float pencil=sc.nextFloat();
//         float eraser=sc.nextFloat();
//         float totalcost=(pen + pencil + eraser);
//         System.out.println("bill cost:" + totalcost);

//         float new_total= totalcost + (0.18f * totalcost);
//         System.out.println("totalbill:" + new_total);

//     }
// }


// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         int income=sc.nextInt();
//         int tax;

//         if(income<500000){
//             tax=0;
//         }
//         else if(income>500000 && income<100000){
//             tax=(int)(income * (0.2));
//         }
//         else{
//             tax=(int)(income * (0.3));
//         }

//         System.out.println("tax is:" + tax);
//     }
// }


// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//        Scanner sc=new Scanner(System.in);
//        System.out.println("enter a:");
//        int a=sc.nextInt();
//        System.out.println("enter b:");
//        int b=sc.nextInt();

//        System.out.println("enter operator:");
//        char operator=sc.next().charAt(0);
//        switch(operator) {
//         case '+':
//             System.out.println(a+b);
//             break;
//         case '-':
//             System.out.println(a-b);
//             break;
//         case '*':
//             System.out.println(a*b);
//             break;
//         case '/':
//             System.out.println(a/b);
//             break;
//         case '%':
//             System.out.println(a%b);
//             break;
       
//         default:System.out.println("wrong operator");
//             break;
//        }
//     }
       
// }

// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         int num=1;
//         while(num<=10){
//             System.out.println(num);
//             num++;
//         }
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         int n=sc.nextInt();
//         int num=1;
//         while(num<=n){
//             System.out.println(num);
//             num++;
//         }
//     }
// }


// import java.util.*;
// public class java1{
//     public static void main(String args[]){
//         Scanner sc=new Scanner(System.in);
//         int n=sc.nextInt();
//         int sum=0;
//         int i=1;
//         while(i<=n){
//             sum+=i;
//             i++;
//         }
//         System.out.println(sum);
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         for(int i=1;i<5;i++){
//             System.out.println("* * * *");
//         }
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         int num=2218;
//         while(num>0){
//             int last_digit=num%10;
//             System.out.print(last_digit);
//             num=num/10;
//         }
//         System.out.println();
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         int num=22180409;
//         int reverse=0;
//         while(num>0){
//             int last_digit=num%10;
//             reverse=(reverse*10) + last_digit;
//             num=num/10;
//         }
//         System.out.println(reverse);
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         int N=sc.nextInt();
//         int i=1;
//         while (i<11){
//             System.out.println(N*i);
//             i++;
//         }
//     }
// } 

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         int fact=1;
    

//         System.out.println("enter the number:");
//         int num=sc.nextInt();

//         for(int i=1;i<=num;i++){
//             fact*=i;
//         }

//         System.out.println("the factorila is:" + fact);
//     }
// } 

// import java.util.*;
// public class java1 {
//     public static void main(String[] args) {
//         for(int line=1;line<=5;line++){
//              for(int star=1;star<=line;star++){
//                 System.out.print("*");
//              }
//              System.out.println();
//         }
//     }
// }

// import java.util.*;
// public class java1 {
//     public static void main(String[] args) {
//         int n=5;
//         for(int line=1;line<=n;line++){
//             for(int star=1;star<=n-line+1;star++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }
// }

// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         Scanner sc=new Scanner(System.in);
//         System.out.println("enter 1st number:");
//         int a=sc.nextInt();

//         System.out.println("enter 2nd number:");
//         int b=sc.nextInt();
//         int sum=a+b;

//         System.out.println("the sum is:");
//         System.out.println(sum);
//     }
// }


// import java.util.*;
// public class java1{
//     public static void main(String[] args) {
//         int n=5;
//         for(int line=1;line<=n;line++){
//             for(int number=1;number<=line;number++){
//                 System.out.print(number);
//             }
//             System.out.println();
//         }
//     }
// }

// import java.util.*;
// public class java1 {

//     public static void main(String[] args) {
//         int n=5;
//         char ch='A';

//         for(int line=1;line<=n;line++){
//             for(int chars=1;chars<=line;chars++){
//                 System.out.print(ch);
//                 ch++;
//             }
//             System.out.println();
//         }

//     }
// }

// import java.util.*;
// public class java1 {
//     public static int multiply(int a,int b){
//         int product=a*b;
//         return product;
//     } 
//     public static void main(String[] args) {
        
//         int a=10;
//         int b=4;
//         int prod=multiply(a,b);
//         System.err.println("a*b is:"+prod);
//     }
// }

// import java.util.*;
// public class java1 {

//     public static int factorial(int n){
//         int f=1;
//         for(int i=1;i<=n;i++){
//             f*=i;
//         }
//         return f;
//     }
//     public static void main(String[] args){
//         System.out.println(factorial(5));
//     }
// }


// import java.util.*;
// public class java1{
//     public static int factorial(int n){
//         int f=1;
//         for(int i=1;i<=n;i++){
//             f*=i;
//         }
//         return f;
//     }

//     public static int binomialcoeff(int n,int r){
//         int fact_n=factorial(n);
//         int fact_r=factorial(r);
//         int fact_n_minus_r=factorial(n-r);

//         int binomialcoeff=fact_n/(fact_r * fact_n_minus_r);
//         return binomialcoeff;
//     }
//     public static void main(String[] args) {
//         System.out.println(binomialcoeff(6, 2));
//     }
// }


// import java.util.*;
// public class java1{
//     public static boolean isprime(int n){
//         boolean isprime=true;
//         for(int i=2;i<=Math.sqrt(n);i++){
//             if(n%i==0){
//                 isprime=false;            }
//         }
//         return isprime;
//     }
//     public static void primeinrange(int n){
//         for(int i=2;i<=n;i++){
//             if(isprime(i)){
//                 System.out.print(i+" ");
//             }
//         }
//     }
//     public static void main(String[] args) {
//         // System.out.println(isprime(2));

//     primeinrange(10);
//        }
// }


// import java.util.*;
// public class java1{
//     public static void dectobin(int dec){
//         int mynum=dec;
//         int power=0;
//         int bin=0;

//         while (dec>0){
//             int rem=dec%2;
//             bin=bin+(rem*(int)Math.pow(10,power));
            
//             power++;
//             dec=dec/2;
//         }
//          System.out.println("the binary of " + mynum + " is: " + bin);
//     }    
//     public static void main(String[] args) {
//         dectobin(7);
//     }
// }

