// public class advance_sort{
//     public static void printele(int arr[]){
//         for(int i=0;i<arr.length;i++){
//             System.out.print(arr[i] + " ");
//         }
//         System.out.println();
//     }
//     public static void mergesort(int arr[],int si,int ei){
//         if(si>=ei){
//             return ;
//         }
//         int mid=si+(ei-si)/2;
//         mergesort(arr, si, mid);//left 
//         mergesort(arr, mid+1, ei);//right
//         //calling to merge
//         merge(arr, si, mid, ei);
//     }

//     public static void merge(int arr[],int si,int mid,int ei){
//         int temp[]=new int[ei-si+1];//[1,3]=3elements and [3,5]=2 now for ei-si+1 we get 5 index
//         int i=si;
//         int j=mid+1;
//         int k=0;

//         while(i<=mid && j<=ei){
//             if(arr[i]<arr[j]){
//                 temp[k]=arr[i];
//                 i++;
//             }
//             else{
//                 temp[k]=arr[j];
//                 j++;
//             }
//             k++;
//         }

//         while (i<=mid) {
//             temp[k++]=arr[i++];//left part for the left over right side elements
//         }

//         //right part
//         while (j<=ei) {
//             temp[k++]=arr[j++];
//         }


//         //copy to original
//         for(k=0, i=si; k<temp.length;k++,i++){
//             arr[i]=temp[k];
//         }
//     }
//     public static void main(String[] args) {
//         int arr[]={3,5,2,4,8,9};
//         mergesort(arr, 0, arr.length-1);
//         printele(arr);
//     }
// }


// public class advance_sort{
//     public static void printele(int arr[]){
//         for(int i=0;i<arr.length;i++){
//             System.out.print(arr[i] + " ");
//         }
//         System.out.println();
//     }

//     public static void quicksort(int arr[],int si,int ei){
//         if(si>=ei){
//             return;
//         }

//         int pidx=partition(arr,si,ei);
//         quicksort(arr, si, pidx-1);
//         quicksort(arr, pidx+1, ei);
//     }


//     public static int partition(int arr[],int si,int ei){
//         int pivot=arr[ei];
//         int i=si-1;

//         for(int j=si;j<ei;j++){
//             if(arr[j]<=pivot){
//                 i++;
//                 //swap
//                 int temp=arr[j];
//                 arr[j]=arr[i];
//                 arr[i]=temp;
//             }
//         }
//         i++;
//         int temp=pivot;
//         arr[ei]=arr[i];
//         arr[i]=temp;
//         return i;
//     }
//     public static void main(String[] args) {
//         int arr[]={9,5,6,3,2,4};
//         quicksort(arr, 0, arr.length-1);
//         printele(arr);
//     }
// }


// public class advance_sort{
//     public static int sort_rotatearray(int arr[],int target,int si,int ei){
//         if(si>ei){
//             return -1;
//         }
//         int mid=si+(ei-si)/2;
//         //case 1
//         if(arr[mid]==target){
//             return mid;
//         }

//         //case 2 on L1
//         if (arr[si]<=arr[mid]) {
//             //case left
//             if(arr[si]<=target && target<=arr[mid]){
//                 return sort_rotatearray(arr, target, si, mid-1);
//             }//case right
//             else{
//                 return sort_rotatearray(arr, target, mid+1, ei);
//             }
//         }

//         //case 3 on L2
//         else{
//             //case right
//             if (arr[mid]<=target && target<=arr[ei]) {
//                 return sort_rotatearray(arr,target,mid+1,ei);
//             }else{//case left
//                 return sort_rotatearray(arr,target,si,mid-1);
//             }
//         }
        
//     }
//     public static void main(String[] args) {
//         int arr[]={4,5,6,7,0,1,2};//arr should be sorted half and half like
//         int tarr=0;
//         int targetidx=sort_rotatearray(arr,tarr,0,arr.length-1);
//         System.out.print(targetidx);
//     }
// }

   