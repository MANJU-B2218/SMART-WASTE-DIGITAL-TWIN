// public class recursion{
//     public static void numdec(int n){
//         if(n==1){
//             System.out.println(n);
//             return ;
//         }
//         System.out.println(n + " ");
//         numdec(n-1);
//     }
//     public static void main(String[] args) {
//         numdec(5);
//     }
// }

// public class recursion{
//     public static void numinc(int n){
//         if(n==1){
//             System.out.println(n + " ");
//             return ;
//         }
//         numinc(n-1);
//         System.out.println(n + " ");
//     }
//     public static void main(String[] args) {
//         int n=5;
//         numinc(n);
//     }
// }

// public class recursion{
//     public static int fact(int n){
//         if(n==0){
//             return 1;
//         }
//         int fn1=fact(n-1);
//         int fn=n*fact(n-1);
//         return fn;
//     }
//     public static void main(String[] args) {
//         System.out.println(fact(5));
//     }
// }


// public class recursion{
//     public static int calsum(int n){
//         if(n==1){
//             return 1;
//         }
//         int fm1=calsum(n-1);
//         int fm=n + calsum(n-1);
//         return fm;
//     }
//     public static void main(String[] args) {
//         System.out.println(calsum(5));
//     }
// }

// public class recursion{
//     public static int fibonacci(int n){
//         if(n==0 || n==1){
//             return n;
//         }
//         int fn1=fibonacci(n-1);
//         int fn2=fibonacci(n-2);

//         int fn=fn1+fn2;
//         return fn;
//     }
//     public static void main(String[] args) {
//         System.out.println(fibonacci(5));
//     }
// }

// public class recursion{
//     public static boolean issort(int arr[],int i){
//         if(i==arr.length-1){
//             return true;
//         }
//         if(arr[i]>arr[i+1]){
//             return false;
//         }
//         return issort(arr, i+1);
//     }
//     public static void main(String[] args) {
//         int arr[]={1,2,3,4,5};
//         System.out.print(issort(arr, 0));
//     }
// }

// public class recursion{
//     public static int firstoccurence(int arr[],int key,int i){
//         if(i==arr.length){
//             return -1;
//         }
//         if(arr[i]==key){
//             return i;
//         }
//         return firstoccurence(arr, key, i+1);
//     }
//     public static void main(String[] args) {
//         int arr[]={1,4,5,7,6,5,3,2};
//         System.out.println(firstoccurence(arr, 5, 0));
//     }
// }


// public class recursion{
//     public static int lastoccurence(int arr[],int key,int i){
//         if(i==arr.length){
//             return -1;
//         }
//         int isfound=lastoccurence(arr, key, i+1);
//         if(isfound==-1 && arr[i]==key){
//             return i;
//         }
//         return isfound;
//     }
//     public static void main(String[] args) {
//         int arr[]={1,4,5,7,6,5,3,2};
//         System.out.println(lastoccurence(arr, 5, 0));
//     }
// }

// public class recursion{
//     public static int power(int a,int n){
//         if(n==0){
//             return 1;
//         }
//         int p1=power(a, n-1);
//         int pn1=a*p1;
//         return pn1;
//     }
//     public static void main(String[] args) {
//         System.out.print(power(5, 3));
//     }
// }

// public class recursion{
//     public static int optpower(int a,int n){
//         if(n==0){
//             return 1;
//         }
//         int halfpower=optpower(a, n/2);
//         int halfpowersq=halfpower*halfpower;

//         if(n%2!=0){
//             halfpowersq=a*halfpowersq;
//         }
//         return halfpowersq;
//     }
//     public static void main(String[] args) {
//         System.out.print(optpower(5, 3));
//     }
// }

// public class recursion{
//     public static int tilingprblm(int n){
//         //base
//         if(n==0 || n==1){
//             return 1;
//         }
//         int vertical=tilingprblm(n-1);

//         int horizontal=tilingprblm(n-2);

//         int totways=vertical+horizontal;
//         return totways;
//     }
//     public static void main(String[] args) {
//         System.out.println(tilingprblm(4));
//     }
// }

// public class recursion{
//     public static void removeduplicates(String str,int idx,StringBuilder newstr,boolean map[]){
//         if(idx==str.length()){
//             System.out.println(newstr);
//             return ;
//         }
//         char currchar=str.charAt(idx);
//         if(map[currchar-'a'] == true){
//             //duplicate
//             removeduplicates(str, idx+1, newstr, map);
//         }else{
//             map[currchar-'a']=true;
//             removeduplicates(str, idx+1, newstr.append(currchar), map);
//         }
//     }
//     public static void main(String[] args) {
//         String str="racecar";
//         removeduplicates(str, 0, new StringBuilder(""), new boolean[26]);
//     }
// }


// public class recursion {
//     public static int friendspair(int n){
//         if(n==1 || n==2){
//             return n;
//         }
//         //single
//         int single=friendspair(n-1);

//         int pair=friendspair(n-2);
//         int pairways=(n-1) * pair;

//         int totalways=single+pairways;
//         return totalways;
//     }
//     public static void main(String[] args) {
//         System.out.println(friendspair(3));
//     }
// }


// public class recursion {
//     public static void printbstrings(int n,int lastplace,String str){
//         if(n==0){
//             System.out.println(str);
//             return ;
//         }
//         printbstrings(n-1,0, str+'0');
//         if(lastplace==0){
//             printbstrings(n-1,1, str+'1');
//         }
//     }
//     public static void main(String[] args) {
//         printbstrings(3, 0, "");
//     }
// }

// public class recursion {
//     static String digits[]={"zero","one","two","three","four","five","six","seven","eight","nine"};

//     public static void printdigits(int n){
//         if(n==0){
//             return;
//         }
//         int lastdigit=n%10;
//         printdigits(n/10);
//         System.out.print(digits[lastdigit] +" ");
//     }
//     public static void main(String[] args) {
//         printdigits(1822);
//     }
// }