import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the initial list
        int n = scanner.nextInt(); // Read the size of the list
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(scanner.nextInt()); // Add each element to the list
        }
        
        // Read the number of queries
        int q = scanner.nextInt(); // Read number of queries
        
        // Process each query
        for (int i = 0; i < q; i++) {
            String queryType = scanner.next(); // Read the query type ("Insert" or "Delete")
            
            if (queryType.equals("Insert")) {
                int index = scanner.nextInt(); // Read the index
                int value = scanner.nextInt(); // Read the value to insert
                list.add(index, value); // Insert the value at the specified index
            } else if (queryType.equals("Delete")) {
                int index = scanner.nextInt(); // Read the index to delete
                list.remove(index); // Delete the element at the specified index
            }
        }
        
        // Print the final list as a space-separated string
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + (i == list.size() - 1 ? "" : " ")); // Print the list
        }
    }
}