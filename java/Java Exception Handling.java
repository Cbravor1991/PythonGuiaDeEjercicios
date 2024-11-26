import java.util.Scanner;
class MyCalculator {
      /*
    * Create the method long power(int, int) here.
    * This method computes n^p and handles exceptions as needed.
    */
    public long power(int n, int p) throws Exception {
        // Check if both n and p are zero
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        
        // Check if either n or p is negative
        if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        }
        
        // Return n raised to the power of p
        return (long) Math.pow(n, p);
    }
}

public class Solution {
    public static final MyCalculator my_calculator = new MyCalculator();
    public static final Scanner in = new Scanner(System.in);
    
    public static void main(String[] args) {
        while (in .hasNextInt()) {
            int n = in .nextInt();
            int p = in .nextInt();
            
            try {
                System.out.println(my_calculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}