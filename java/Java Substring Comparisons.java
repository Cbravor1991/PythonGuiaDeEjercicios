import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
       String smallest = s.substring(0, k);  // Initialize smallest with the first substring
        String largest = s.substring(0, k);   // Initialize largest with the first substring
        
          // Iterate through the string to find all substrings of length k
        for (int i = 1; i <= s.length() - k; i++) {
            String substring = s.substring(i, i + k);
            
            // Update smallest and largest based on lexicographical comparison
            if (substring.compareTo(smallest) < 0) {
                smallest = substring;
            }
            if (substring.compareTo(largest) > 0) {
                largest = substring;
            }
        }
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}