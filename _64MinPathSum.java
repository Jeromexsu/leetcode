public class _64MinPathSum {
    public static void main(String[] args) {
        String gridString = "[[1,3,1],[1,5,1],[4,2,1]]";
        int[][] grid = LeetCodeUtils.readMatrix(gridString);
        int ret = new _64MinPathSum().minPathSum(grid);
        System.out.println(ret);
    }
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i==0 && j==0) dp[i][j] = grid[i][j];
                else if(i==0) dp[i][j] = dp[i][j-1]+grid[i][j];
                else if(j==0) dp[i][j] = dp[i-1][j]+grid[i][j];
                else dp[i][j] = Math.min(dp[i][j-1],dp[i-1][j])+grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
}
