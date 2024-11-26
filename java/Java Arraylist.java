import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of lists
        int n = scanner.nextInt();
        scanner.nextLine(); // Move to the next line
        
        // Create a list of lists to store the data
        ArrayList<ArrayList<Integer>> lists = new ArrayList<>();
        
        // Read the lists
        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            String[] parts = line.split(" ");
            int size = Integer.parseInt(parts[0]);
            ArrayList<Integer> list = new ArrayList<>();
            for (int j = 1; j <= size; j++) {
                list.add(Integer.parseInt(parts[j]));
            }
            lists.add(list);
        }
        
        // Read number of queries
        int q = scanner.nextInt();
        
        // Process each query
        for (int i = 0; i < q; i++) {
            int x = scanner.nextInt();  // The list number (1-based index)
            int y = scanner.nextInt();  // The position within the list (1-based index)
            
            // Check if the list number and the position are valid
            if (x <= n && x > 0 && y <= lists.get(x - 1).size() && y > 0) {
                System.out.println(lists.get(x - 1).get(y - 1));
            } else {
                System.out.println("ERROR!");
            }
        }
        
        scanner.close();
    }
}
