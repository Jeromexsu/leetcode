public class _isValidSudoku {
    public static void main(String[] args) {
        String boardString = """
            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        """; 
        char[][] board = LeetCodeUtils.readCharMatrix(boardString);
        boolean res = new _isValidSudoku().isValidSudoku(board);
        System.out.println(res);

    }
    public boolean isValidSudoku(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == '.') continue;
                char num = board[i][j];
                // System.out.println("cur:" + num);
                for(int k = 0; k < n; k++) {
                    char num1 = board[i][k];
                    if(num1 == '.' || k == j) continue;
                    if(num1 == num) return false;
                }
                for(int k = 0; k < m; k++) {
                    char num1 = board[k][j];
                    if(num1 == '.' || k == i) continue;
                    if(num1 == num) return false;
                }
                int m1 = i/3*3;
                int n1 = j/3*3;
                for(int k = 0; k < 3; k++ ) {
                    for(int l = 0; l < 3; l++) {
                        char num1 = board[k+m1][l+n1];
                        if(num1 == '.' || k+m1 == i) continue;
                        if(num1 == num) return false;
                    }
                }

                board[i][j] = '.';
            }
        }
        return true;
    }
}