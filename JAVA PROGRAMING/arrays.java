// import java.util.*;
// public class arrays {

//     public static void main(String[] args){
//         int marks[]=new int[50];
//         System.out.println("length is:" + marks.length);

//         Scanner sc=new Scanner(System.in);
//         marks[0]=sc.nextInt();
//         marks[1]=sc.nextInt();
//         marks[2]=sc.nextInt();

//         System.out.println("phy:" + marks[0]);
//         System.out.println("chem:" + marks[1]);
//         System.out.println("maths:" + marks[2]);

//         int percentage=(marks[0] +marks[1] + marks[2])/3;
//         System.out.println("percentage of pcm is:"+percentage+"%");
//         marks[1]=marks[1] + 2;
//         System.out.println("chem marks is changed into:" +marks[1]);
//         int percent=(marks[0] +marks[1] + marks[2])/3;
//         System.out.println("new percentage is:"+percent+"%");
//     }
// }




// import java.util.*;
// public class arrays {
//     public static int linearsearch(int menu[],int key){
//         for(int i=0;i<menu.length;i++){
//             if(menu[i]==key){
//                 return i;
//             }
//         }
//         return -1;
//     }
//     public static void main(String[] args) {
//         int menu[]={2,14,56,18,22};
//         int key=22;
//         int index=linearsearch(menu, key);
//         if(index==-1){
//             System.out.println("not found");
//         }else{
//              System.out.println("22 found at index:" + index);
//         }
//     }
// }

// import java.util.*;
// public class arrays {
//     public static int getlargest(int num[]){
//         int largest=Integer.MIN_VALUE;
//         int smallest=Integer.MAX_VALUE;

//         for(int i=0;i<num.length;i++){
//             if(largest<num[i]){
//                 largest=num[i];
//             }
//                 if(smallest>num[i]){
//                     smallest=num[i];
//                 }
//         }
//         System.out.println("smallest is:" +smallest);
//             return largest;
//     }
//     public static void main(String[] args) {
//         int num[]={1,6,2,9,22,18};
//         System.out.println("largest is:" + getlargest(num));


//     }
// }

// import java.util.*;
// public class arrays {
//     public static int binarysearch(int num[],int key){
//         int start=0;
//         int end=num.length-1;

//         while(start<=end){
//             int mid=(start +end)/2;

//             if(num[mid]==key){
//                 return mid;
//             }
//             if(num[mid]>key){
//                 end=mid-1;
//             }
//             if(num[mid]<key){
//                 start=mid+1;
//             }
//         }
//         return -1;
//     }
//     public static void main(String[] args){
//         int num[]={2,5,6,8,9,22};
//         int key=8;

//         System.out.println("the key is found at index:" + binarysearch(num, key));
//     }
// }

// import java.util.*;
// public class arrays {
//     public static void reverse(int num[]){
//         int start =0;
//         int end=num.length -1;

//         while(start<end){
//             int temp=num[end];
//             num[end]=num[start];
//             num[start]=temp;
//             start++;
//             end--;
//         }
//     }
//     public static void main(String[] args) {
//         int num[]={2,3,4,7,9,1,22,18};

//         reverse(num);

//         for(int i=0;i<num.length;i++){
//             System.out.print(num[i]+" ");
//         }
//         System.out.println();
//     }
// }

// import java.util.*;
// public class arrays {
//     public static void print_pairs(int num[]){
//         int tp=0;
//         for(int i=0;i<num.length;i++){
//             int curr=num[i];
//             for(int j=i+1;j<num.length;j++){
//                 System.out.print("(" + curr + ","+ num[j]+")");
//             }
//             System.out.println();
//             tp++;
//         }
//         System.out.print("total pairs:"+ tp);
//     }
//     public static void main(String[] args) {
//         int num[]={2,5,7,8,3,5,6};
//         print_pairs(num);
//     }
// }


// import java.util.*;
// public class arrays {
//     public static void sub_arrays(int num[]){
//         int sum=0;
//         for(int i=0;i<num.length;i++){
//             int start=i;
//             for(int j=i;j<num.length;j++){
//                 int end=j;
//                 for(int k=start;k<=end;k++){
//                     System.out.print(num[k] + " ");
//                     sum+=num[k];
//                 }
//                 System.out.println();
//             }
//             System.out.println();
//         }
//         System.out.print("sum:" + sum);
//     }
//     public static void main(String[] args) {
//         int num[]={2,4,6,8,10};
//         sub_arrays(num);
//     }
// }


// import java.util.*;
// public class arrays {
//     public static void sum_sub_arrays(int num[]){
//         int currentsum=0;
//         int max=Integer.MIN_VALUE;
//         for(int i=0;i<num.length;i++){
//             int start=i;
//             for(int j=i;j<num.length;j++){
//                 int end=j;
//                 currentsum=0;
//                 for(int k=start;k<=end;k++){
//                     currentsum+=num[k];
//                 }
//                 System.out.println(currentsum);
//                 if(max<currentsum){
//                     max=currentsum;
//                 }
//             }
//             System.out.println();
//         }
//         System.out.print("maxsum is:"+ max);
//     }
//     public static void main(String[] args) {
//         int num[]={2,4,6,8,10};
//         sum_sub_arrays(num);
//     }
// }

//sorting.......

//bubble_sort

// import java.util.*;
// public class arrays {
//     public static void bubble_sort(int num[]){
//         for(int turn=0;turn<num.length-1;turn++){
//             for(int j=0;j<num.length-1-turn;j++){
//                 if(num[j]>num[j+1]){
//                     //swap
//                     int temp=num[j+1];
//                     num[j+1]=num[j];
//                     num[j]=temp;
//                 }
//             }
//         }
//     }

//     public static void print_sort(int num[]){
//         for(int i=0;i<num.length;i++){
//             System.out.print(num[i] + " ");
//         }
//         System.out.println();
//     }
//     public static void main(String[] args) {
//         int num[]={2,5,3,1,4};
//         bubble_sort(num);
//         print_sort(num);
//     }
// }

//if array is already sorted then the count will be always 0

// import java.util.*;
// public class arrays {
//     public static void bubble_sort(int num[]){
//         int count=0;
//         for(int turn=0;turn<num.length-1;turn++){
//             for(int j=0;j<num.length-1-turn;j++){
//                 if(num[j]>num[j+1]){
//                     //swap
//                     int temp=num[j+1];
//                     num[j+1]=num[j];
//                     num[j]=temp;
//                     count++;
//                 }
//                 System.out.println("count is:" + count);
//             }
//         }
//     }

//     public static void print_sort(int num[]){
//         for(int i=0;i<num.length;i++){
//             System.out.print(num[i] + " ");
//         }
//         System.out.println();
//     }
//     public static void main(String[] args) {
//         int num[]={1,2,3,4,5};
//         bubble_sort(num);
//         print_sort(num);
//     }
// }



// public class arrays {
//     public static void selection_sort(int num[]){
//         for(int i=0;i<num.length-1;i++){
//             int min_pos=i;
//             for(int j=i+1;j<num.length;j++){
//                 if(num[min_pos]>num[j]){
//                     min_pos=j;
//                 }
//             }
//              //swap
//             int temp=num[min_pos];
//             num[min_pos]=num[i];
//             num[i]=temp;
//         }
//     }
//     public static void print_sort(int num[]){
//         for(int i=0;i<num.length;i++){
//             System.out.print(num[i] + " ");
//         }
//         System.out.println();
//     }  
    
//     public static void insertion_sort(int num[]){
//         for(int i=1;i<num.length;i++){
//             int curr=num[i];
//             int prev=i-1;

//             while(prev>=0 && num[prev]>curr){
//                 num[prev+1]=num[prev];
//                 prev--;
//             }
//             num[prev+1]=curr;
//         }
//     }
//     public static void main(String[] args) {
//         int num[]={1,2,1,3,4,6,2};
//         insertion_sort(num);
//         print_sort(num);

//     }
// }


//BRUTE FORCE APPROACH
// import java.util.*;
// public class arrays {
//     public static void sum_sub_arrays(int num[]){
//         int cursum=0;
//         int maxsum=Integer.MIN_VALUE;
//         for(int i=0;i<num.length;i++){
//             int start=i;
//             for(int j=i;j<num.length;j++){
//                 int end=j;
//                 cursum=0;
//                 for(int k=start;k<=end;k++){
//                     cursum+=num[k];
//                 }
//                 System.out.println(cursum);
//                 if(maxsum<cursum){
//                     maxsum=cursum;
//                 }
//             }
//         }
//         System.out.print("maxsum is:" + maxsum);
//     }
//     public static void main(String[] args) {
//         int num[]={2,4,6,8,10};
//         sum_sub_arrays(num);
//     }
// }



//PREFIX SUM OPTIMISED APPROACH
// import java.util.*;
// public class arrays {
//     public static void sum_sub_arrays(int num[]){
//         int cursum=0;
//         int maxsum=Integer.MIN_VALUE;
//         int prefix[]=new int[num.length];

//         prefix[0]=num[0];
//         for(int i=1;i<prefix.length;i++){
//             prefix[i]=prefix[i-1]+num[i];
//         }
//         for(int i=0;i<num.length;i++){
//             int start=i;
//             for(int j=i;j<num.length;j++){
//                 int end=j;
//                 cursum=start==0?prefix[end]:prefix[end] - prefix[start-1];
            
//                 if(maxsum<cursum){
//                     maxsum=cursum;
//                 }
//             }
//         }
//         System.out.print("maxsum is:" + maxsum);
//     }
//     public static void main(String[] args) {
//         int num[]={2,4,6,8,10};
//         sum_sub_arrays(num);
//     }
// }

// kadaanes method
// import java.util.*;
// public class arrays{
//     public static void kadanes(int num[]){
//         int cursum=0;
//         int maxsum=Integer.MIN_VALUE;

//         for(int i=0;i<num.length;i++){
//             cursum+=num[i];
//             if(cursum<0){
//                 cursum=0;
//             }
//             maxsum=Math.max(cursum,maxsum);
//         }   
//         System.out.println("maximum sum is:" + maxsum);
//     }
//     public static void main(String[] args){
//         int num[]={-1,4,6,-5,10};
//         kadanes(num);
//     }
// } 

//TRAPPING RAINWATER
// import java.util.*;
// public class arrays{
//     public static int trapped_rainwater(int height[]){
//         int n=height.length;
//         //left max
//         int leftmax[]=new int[height.length];
//         leftmax[0]=height[0];
//         for(int i=1;i<n;i++){
//             leftmax[i]=Math.max(height[i],leftmax[i-1]);
//         }

//         //right max
//         int rightmax[]=new int[height.length];
//         rightmax[n-1]=height[n-1];
//         for(int i=n-2;i>=0;i--){
//             rightmax[i]=Math.max(height[i],rightmax[i+1]);
//         }

//         int trappedwater=0;
//         for(int i=0;i<n;i++){
//             int waterlevel=Math.min(leftmax[i], rightmax[i]);
//             trappedwater+=waterlevel-height[i];
//         }
//         return trappedwater;

//     }
//     public static void main(String[] args){
//         int height[]={4,2,0,6,3,2,5};
//         System.out.println(trapped_rainwater(height));
//     }
// }

// BUYING AND SELLING STOCKS
// import java.util.*;
// public class arrays {
//     public static int buy_sellstoccks(int prices[]){
//         int buyingprice=Integer.MAX_VALUE;
//         int maxprofit=0;
//         for(int i=0;i<prices.length;i++){
//             if(buyingprice<prices[i]){
//                 int profit=prices[i]-buyingprice;
//                 maxprofit=Math.max(maxprofit,profit);
//             }
//             else{
//                 buyingprice=prices[i];
//             }
//         }
//         return maxprofit;
//     }
//     public static void main(String[] args) {
//         int prices[]={5,2,3,6,4};
//         System.out.println(buy_sellstoccks(prices));
//     }
// }



//assignments
public class arrays {
    public static boolean duplicates(int num[]){
        for(int i=0;i<num.length-1;i++){
            for(int j=i+1;j<num.length;j++){
                if(num[i]==num[j]){
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int num[]={1,2,3,4,2};
        System.out.println(duplicates(num));
    }
}