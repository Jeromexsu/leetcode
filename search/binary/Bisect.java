package search.binary;

public class Bisect {
    private static int lowerbound(int[] arr, int left, int right, int target) {
        left--;
        while(left + 1 < right) {
            //invariance : left < target <= right
            int mid = left + (right - left) / 2;
            if(arr[mid] < target) left = mid;
            else right = mid;
        }
        return right;
    }
}
