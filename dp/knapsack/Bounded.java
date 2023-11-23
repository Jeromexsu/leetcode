package dp.knapsack;
/*
 * Given N items where each item has some weight and profit associated with it 
 * and also given a bag with capacity W. 
 * The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 
 */
public class Bounded {
    private int[] weights;
    private int[] profits;
    private int N;
    public Bounded(int[] weights, int[] profits) {
        this.weights = weights;
        this.profits = profits;
        this.N = weights.length;
    }
    public int maxValue(int C) {
        int[][] dp = new int[N][C+1];

        for(int c = 0; c <= C; c++) {
            dp[0][c] = c >= weights[0] ? profits[0] : 0;
        }

        for(int i = 1; i < N; i++) {
            for(int c = 0; c <= C; c++) {
                int skip = dp[i-1][c];
                int pick = -1;
                if(c >= weights[i]) pick = dp[i-1][c-weights[i]] + profits[i];
                dp[i][c] = Math.max(skip,pick);
            }
        }
        return dp[N-1][C];
    }

    public static void main(String[] args) {
        int[] weights = new int[] {4,2,3};
        int[] profits = new int[] {4,2,3};
        Bounded bounded = new Bounded(weights,profits);
        
        System.out.println(bounded.maxValue(5));
    }
}
