package search.binary;

// [1,2,           2,2,3] target = 2
//    lowerbound       upperbound
public class SimpleBinarySearch {
    private static int binarySearch(int[] arr,int target) {
        int left = 0, right = arr.length - 1;
        while(left <= right) {
            int mid = left + (right-left) / 2;
            if(arr[mid] == target) return mid;
            if(target < arr[mid]) right = mid - 1;
            else left = mid + 1; 
        }
        return -1;     
    }

    private static int firstGreater(int[]arr, int target) {
        int left = 0, right = arr.length - 1;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            if(target == arr[mid]) left = mid + 1;
            else if(target < arr[mid]) right = mid - 1; // skip a mid, right is not reliable
            else left = mid + 1;
        }
        return left;
    }

    public static void main(String[] args) { 
        int[] arr = new int[] {1,2,44};
        int target = 45;
        int pos = binarySearch(arr,target);
        System.out.println(pos);

    }
    
}
