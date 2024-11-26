import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Convert both strings to lowercase
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        // If the lengths are different, they cannot be anagrams
        if (a.length() != b.length()) {
            return false;
        }
        
        // Convert the strings to character arrays
        char[] arrA = a.toCharArray();
        char[] arrB = b.toCharArray();
        
        // Sort the arrays
        java.util.Arrays.sort(arrA);
        java.util.Arrays.sort(arrB);
        
        // Compare the sorted arrays
        return java.util.Arrays.equals(arrA, arrB);
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}