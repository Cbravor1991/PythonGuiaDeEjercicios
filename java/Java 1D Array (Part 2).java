import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] game) {
        // Create a boolean array to track visited indices
        boolean[] visited = new boolean[game.length];
        return dfs(0, leap, game, visited);
    }

    private static boolean dfs(int currentIndex, int leap, int[] game, boolean[] visited) {
        // If we are beyond the last index, we win the game
        if (currentIndex >= game.length) {
            return true;
        }

        // If we're at an invalid position or already visited this position, return false
        if (currentIndex < 0 || visited[currentIndex] || game[currentIndex] == 1) {
            return false;
        }

        // Mark this index as visited
        visited[currentIndex] = true;

        // Explore moves: backward (-1), forward (+1), and leap (+leap)
        return dfs(currentIndex - 1, leap, game, visited) ||
               dfs(currentIndex + 1, leap, game, visited) ||
               dfs(currentIndex + leap, leap, game, visited);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
