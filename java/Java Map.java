import java.util.*;
import java.io.*;

class Solution {
    public static void main(String []argh) {
        // Create a scanner to read input
        Scanner in = new Scanner(System.in);
        
        // Read the number of entries in the phone book
        int n = in.nextInt();
        in.nextLine();  // consume the leftover newline
        
        // Create a HashMap to store the phone book
        Map<String, Integer> phoneBook = new HashMap<>();
        
        // Read each entry in the phone book and store it
        for (int i = 0; i < n; i++) {
            String name = in.nextLine();  // Read the name
            int phone = in.nextInt();     // Read the phone number
            in.nextLine();  // consume the leftover newline
            
            // Store in the phone book
            phoneBook.put(name, phone);
        }
        
        // Process the queries
        while (in.hasNext()) {
            String query = in.nextLine();  // Read the query name
            
            // Check if the name exists in the phone book
            if (phoneBook.containsKey(query)) {
                System.out.println(query + "=" + phoneBook.get(query));  // Print the name and phone number
            } else {
                System.out.println("Not found");  // Print "Not found" if the name is not in the phone book
            }
        }
        
        // Close the scanner
        in.close();
    }
}