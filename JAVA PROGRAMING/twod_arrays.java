// import java.util.*;
// public class twod_arrays{
//     public static void main(String[] args) {
//         int matrix[][]=new int[3][3];
//         int n=matrix.length;
//         int m=matrix[0].length;

//         Scanner sc=new Scanner(System.in);
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++){
//                 matrix[i][j]=sc.nextInt();
//             }
//         }
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++){
//                 System.out.print(matrix[i][j] + " ");
//             }
//             System.out.println();
//         } 
//     }
// }

// import java.util.*;
// public class twod_arrays{
//     public static boolean searching(int matrix[][],int key){
//         for(int i=0;i<matrix.length;i++){
//             for(int j=0;j<matrix[0].length;j++){
//                 if(matrix[i][j]==key){
//                     System.out.print("found at cell:" + "(" + i+","+ j +")");
//                     return true;
//                 }
//             }
//         } 
//         System.out.print("not found");
//             return  false;
//     }
//     public static void main(String[] args) {
//         int matrix[][]=new int[3][3];
//         int n=matrix.length;
//         int m=matrix[0].length;

//         Scanner sc=new Scanner(System.in);
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++){
//                 matrix[i][j]=sc.nextInt();
//             }
//         }
//         for(int i=0;i<n;i++){
//             for(int j=0;j<m;j++){
//                 System.out.print(matrix[i][j] + " ");
//             }
//             System.out.println();
//         } 
//         searching(matrix, 5);
//     }
// }

// import java.util.*;
// public class twod_arrays {
//     public static boolean staircase_search(int matrix[][],int key){
//         int row=0;
//         int col=matrix[0].length-1;
//         while (row<matrix.length && col>=0){
//             if(matrix[row][col]==key){
//                 System.out.println("key found at cell:" + "(" +row+","+col+")");
//                 return true;
//             }else if(key<matrix[row][col]){
//                 col--;
//             }else{
//                 row++;
//             }
//         }
//         System.out.println("key not found");
//             return false;
//     }
//     public static void main(String[] args) {
//         int matrix[][]={{10,20,30,40},
//                         {15,25,35,45},
//                         {27,29,37,48},
//                         {32,33,39,50}};
//         int key=33;
//         staircase_search(matrix, 48);
//     }
// }


// import java.util.*;
// public class twod_arrays {
//     public static void main(String[] args) {
//         int matrix[][]={{1,3,5,7},
//                        {4,6,7,2},
//                        {5,6,2,1},
//                        {2,7,5,6,1}};
//         int key=7;

//         int count=0;
//         int row=matrix.length;
//         int col=matrix[0].length;
        
//         for(int i=0;i<row;i++){
//             for(int j=0;j<col;j++){
//                 if(matrix[i][j]==key){
//                     count++;
//                 }
//             }
//         }
//         System.out.println("the count of key is :"+count);
//     }
// }


/////STRINGS.....
//palindrome
// import java.util.*;
// public class twod_arrays {
//     public static boolean palindrome(String str){
//         for(int i=0;i<str.length()/2;i++){
//             int n=str.length();
//             if(str.charAt(i)!=str.charAt(n-i-1)){
//                 return false;
//             }
//         }
//         return true;
//     }
//     public static void main(String[] args) {
//         String str="racecar";
//         System.out.println(palindrome(str));
//     }
// }

import java.util.Arrays;

////shortest path
// import java.util.*;
// public class twod_arrays {
//     public static float get_shortestpath(String path){
//         int x=0;
//         int y=0;
//         for(int i=0;i<path.length();i++){
//             char dir=path.charAt(i);
//             if(dir=='N'){
//                 y++;
//             }else if(dir=='S'){
//                 y--;
//             }else if(dir=='W'){
//                 x--;
//             }else if(dir=='E'){
//                 x++;
//             }
//         }
//         int x2=x*x;
//         int y2=y*y;
//         return (float)Math.sqrt(x2+y2);
//     }
//     public static void main(String[] args){
//         String path="WNEENESENNN";
//         System.out.println(get_shortestpath(path));
//     }
// }

// import java.util.*;
// public class twod_arrays {
//     public static String substring(String str,int si,int ei){
//         String substring="";
//         for(int i=si;i<ei;i++){
//             substring+=str.charAt(i);
//         }
//         return substring;
//     }
//     public static void main(String[] args) {
//         String str="Helloworld";
//         System.out.println(substring(str, 0, 5));
//     }
// }

// import java.util.*;
// public class twod_arrays {
//     public static void main(String[] args) {
//         String fruits[]={"apple","jackfruit","mango"};
//         String largest=fruits[0];
//         for(int i=0;i<fruits.length;i++){
//             if(largest.compareTo(fruits[i])<0){
//                 largest=fruits[i];
//             }
//         }
//         System.out.println(largest);
//     }
// }


// public class twod_arrays {
//     public static String compress(String str){
//         StringBuilder sb=new StringBuilder("");
//         for(int i=0;i<str.length();i++){
//             Integer count=1;
//             while (i<str.length()-1 && str.charAt(i)==str.charAt(i+1)) {
//                 count++;
//                 i++;
//             }
//             sb.append(str.charAt(i));
//             if(count>1){
//                 sb.append(count.toString());
//             }
//         }
//         return sb.toString();
//     }
//     public static void main(String[] args) {
//         String str="aaabbbbccd";
//         System.out.println(compress(str));
//     }
// }


// public class twod_arrays {
//     public static void counting_ele(int num[][],int key){
//         int count=0;
//         for(int i=0;i<num.length;i++){
//             for(int j=0;j<num[0].length;j++){
//                 if (num[i][j]==key) {
//                     count++;
//                 }
//             }
//         }
//         System.out.println("count of 8 is:"+ count);
//     }
//     public static void main(String[] args) {
//         int num[][]={{4,7,8},{8,8,7}};
//         int key=8;
//         counting_ele(num, key);
//     }
// }

// public class twod_arrays {
//     public static void summ(int num[][]){
//         int sum=0;
//         for(int i=0;i<num.length;i++){
//             for(int j=0;j<num[0].length;j++){
//                 if(i==1){
//                     sum+=num[i][j];
//                 }
//             }
//         }
//         System.out.println("sum of 2nd row is:"+sum);
//     }
//     public static void main(String[] args) {
//         int num[][]={{1,4,9},{11,4,3},{2,2,3}};  
//         summ(num);
//     }               
// }

public class twod_arrays {
    public static void transpose(int num[][]){
        int row=num.length;
        int col=num[0].length;
        int[][]temp=new int[col][row];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                temp[j][i]=num[i][j];
            }
        }
        for(int i=0;i<col;i++){
            for(int j=0;j<row;j++){
                System.out.print(temp[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int num[][]={{2,3,4},
                     {9,6,7}};
        transpose(num);
    }
}