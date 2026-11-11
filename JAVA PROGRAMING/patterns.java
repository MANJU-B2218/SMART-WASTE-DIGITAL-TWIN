// public class patterns {
//     public static void hollow_rectangle(int totalrws,int totalclms){
//         for(int i=1;i<=totalrws;i++){
//             for(int j=1;j<=totalclms;j++){
//                 if(i==1 || i==totalrws || j==1 || j==totalclms){
//                     System.out.print("*");
//                 }else{
//                     System.out.print(" ");
//                 }
//             }
//             System.out.println();
//         }
//     }

//     public static void main(String[] args) {
//         hollow_rectangle(7, 8);
//     }
// }


// public class patterns{
//     public static void inverted_rotated_pyramid(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=n-i;j++){
//                 System.out.print(" ");
//             }
            
//             for(int stars=1;stars<=i;stars++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         inverted_rotated_pyramid(5);
//     }
//}

// public class patterns {
//     public static void inverted_halfpyramid(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=n-i+1;j++){
//                 System.out.print(j + " ");
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         inverted_halfpyramid(7);
//     }
// }

// public class patterns{
//     public static void floid_triangle(int n){
//         int count=1;
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=i;j++){
//                 System.out.print(count + " ");
//                 count++;
//             }
//             System.out.println();
//         }
//     }    
//     public static void main(String[] args) {
//         floid_triangle(5);
//     }
// }

// public class patterns{
//     public static void zero_onetriangle(int n ){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=i;j++){
//                 if((i+j)%2==0){
//                     System.out.print("1");
//                 }else{
//                     System.out.print("0");
//                 }
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         zero_onetriangle(5);
//     }
// }

// public class patterns{
//     public static void butterfly(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=i;j++){
//                 System.out.print("*");
//             }
//             for(int j=1;j<=2*(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=i;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
        
//         for(int i=n;i>=1;i--){
//             for(int j=1;j<=i;j++){
//                 System.out.print("*");
//             }
//             for(int j=1;j<=2*(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=i;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
    
//     } 

//     public static void main(String[] args) {
//         butterfly(5);
//     }
// }

// public class patterns {
//     public static void solid_rhombus(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=n;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         solid_rhombus(6);
//     }
// }

// public class patterns {
//     public static void hollow_rhombus(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=n;j++){
//                 if(i==1 || i==n || j==1 || j==n){
//                     System.out.print("*");
//                 }else{
//                     System.out.print(" ");
//                 }
//             }

//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         hollow_rhombus(5);
//     }
// }



// public class patterns {
//     public static void diamond(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=(2*i)-1;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//          for(int i=n;i>=1;i--){
//             for(int j=1;j<=(n-i);j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<=(2*i)-1;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         diamond(5);
//     }
// }

