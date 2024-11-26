import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<List<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < 6; i++) {
            String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> arrRowItems = new ArrayList<>();

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowTempItems[j]);
                arrRowItems.add(arrItem);
            }

            arr.add(arrRowItems);
        }

        bufferedReader.close();

        // Write your code here
        int maxSum = Integer.MIN_VALUE;

        // Iterate over the possible starting points for hourglasses
        for (int i = 0; i <= 3; i++) {
            for (int j = 0; j <= 3; j++) {
                // Calculate the sum of the hourglass starting at (i, j)
                int currentSum = arr.get(i).get(j) + arr.get(i).get(j + 1) + arr.get(i).get(j + 2) // Top row
                               + arr.get(i + 1).get(j + 1)                                   // Middle
                               + arr.get(i + 2).get(j) + arr.get(i + 2).get(j + 1) + arr.get(i + 2).get(j + 2); // Bottom row
                
                // Update maxSum if the current hourglass sum is greater
                maxSum = Math.max(maxSum, currentSum);
            }
        }

        // Print the result
        System.out.println(maxSum);
    }
}
