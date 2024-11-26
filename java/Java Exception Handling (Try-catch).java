import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        // Create a scanner object to read inputs
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Read first integer a
            int a = scanner.nextInt();
            // Read second integer b
            int b = scanner.nextInt();
            
            // Perform the division and print the result
            System.out.println(a / b);
        } 
        catch (InputMismatchException e) {
            // Handle invalid integer inputs
            System.out.println("java.util.InputMismatchException");
        } 
        catch (ArithmeticException e) {
            // Handle division by zero
            System.out.println("java.lang.ArithmeticException: / by zero");
        }
        
        scanner.close();
    }
}