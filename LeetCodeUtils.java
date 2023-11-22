import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCodeUtils {
    public static void main(String[] args) {
        readMatrix("[[1,3,1],[1,5,1],[4,2,1]]");
    }
    public static int[][] readMatrix(String matrixString) {
        //[[1,3,1],[1,5,1],[4,2,1]]
        matrixString = matrixString.substring(1,matrixString.length()-1);
        String[] tokens = matrixString.split("],");
        int m = tokens.length;
        int[][] matrix = new int[m][];
        for(int i = 0; i < m; i++) {
            String token = tokens[i];
            // remove the extra [ in token and another trailing ] in the last token
            if(i == m-1) token = token.substring(1,token.length()-1);
            else token = token.substring(1);
            // after this: 1,2,3 ...

            String[] numStrings = token.split(",");
            int n = numStrings.length;
            matrix[i] = new int[n];
            for(int j = 0; j < n ; j++) {
                matrix[i][j] = Integer.parseInt(numStrings[j]);
            }
        }
        return matrix;
    }

    public static char[][] readCharMatrix(String matrixString) {
        matrixString = matrixString.substring(matrixString.indexOf('[') + 1,matrixString.lastIndexOf(']'));
        // System.out.println(matrixString);
        String[] tokens = matrixString.split("\n");
        // for(String token : tokens) System.out.println(token);
        int m = tokens.length;
        char[][] matrix = new char[m][];

        for(int i = 0; i < m; i++) {
            String token = tokens[i];
            // remove the extra [ in token and another trailing ] in the last token
            token = token.substring(token.indexOf('[')+1,token.lastIndexOf(']'));
            // after this: 1,2,3 ...

            String[] charStrings = token.split(",");
            int n = charStrings.length;
            matrix[i] = new char[n];
            for(int j = 0; j < n ; j++) {
                // System.out.println(charStrings[j].charAt(1));
                matrix[i][j] = charStrings[j].charAt(1);
            }
        }

        return matrix;

    }
}
