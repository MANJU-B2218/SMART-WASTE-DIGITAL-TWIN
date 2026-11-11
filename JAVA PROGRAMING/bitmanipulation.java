
// import java.util.*;
// public class bitmanipulation {
//     public static void oddoreven(int num){
//         int bitmask=1;
//         if((num & bitmask)==0){
//             System.out.println("it is even number");
//         }else{
//             System.out.println("it is odd number");
//         }
//     }
//     public static void main(String[] args) {
//         oddoreven(18);
//         oddoreven(22);
//         oddoreven(7);
//     }
// }


// import java.util.*;
// public class bitmanipulation{
//     public static int getith(int n,int i){
//         int bitmask=1<<i;
//         if((n & bitmask)==0){
//             return 0;
//         }else{
//             return 1;
//         }
//     }
//     public static void main(String[] args) {
//         System.out.println(getith(6, 3));
//     }
// }

// public class bitmanipulation {
//     public static int setith(int n,int i){
//         int bitmask=1<<i;
//         return n|bitmask;
//     }
//     public static void main(String[] args) {
//         System.out.println(setith(6, 3));
//     }
// }

// public class bitmanipulation {
//     public static int clearith(int n,int i){
//         int bitmask=~(1<<i);
//         return n & bitmask;
//     }
//     public static void main(String[] args) {
//         System.out.println(clearith(10, 1));
//     }
// }



// public class bitmanipulation {
//     public static int setith(int n,int i){
//         int bitmask=1<<i;
//         return n|bitmask;
//     }

//     public static int clearith(int n,int i){
//         int bitmask=~(1<<i);
//         return n & bitmask;
//     }    

//     public static int updateith(int n,int i,int newbit){
//         if(newbit==0){
//             return clearith(n,i);
//         }else{
//             return setith(n,i);
//         }
//     }
//     public static void main(String[] args) {
//         System.out.println(updateith(10, 2, 1));
//     }
// }

// public class bitmanipulation {
//     public static int clearlastith(int n,int i){
//         int bitmask=(~0)<<i;
//         return n & bitmask;
//     }
//     public static void main(String[] args) {
//         System.out.println(clearlastith(12, 2));
//     }
// }

// import java.util.*;
// public class bitmanipulation{
//     public static boolean powerof_two(int n){
//         return (n & (n-1))==0;
//     }
//     public static void main(String[] args) {
//        System.out.println(powerof_two(5));
//     }

// }


// import java.util.*;
// public class bitmanipulation{
//     public static int setofbits(int n){
//         int count=0;
//         while(n>0){
//             if((n&1)!=0){
//                 count++;
//             }
//             n=n>>1;
//         }
//         return  count;
//     }
//     public static void main(String[] args) {
//        System.out.println(setofbits(16));
//     }

// }

// import java.util.*;
// public class bitmanipulation{
//     public static int fast_exponential(int a,int n){
//         int ans=1;
//         while(n>0){
//             if((n & 1)!=0){
//                 ans=ans*a;
//             }
//             a=a*a;
//             n=n>>1;
//         }
//         return ans;
//     }
//     public static void main(String[] args) {
//        System.out.println(fast_exponential(3, 5));
//     }

// }
