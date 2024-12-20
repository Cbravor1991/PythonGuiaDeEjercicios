import java.util.Scanner;
import java.util.regex.*;

public class Solution
{
 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        
        while (testCases-- > 0) {
            String pattern = in.nextLine();
            try {
                // Try compiling the pattern
                Pattern.compile(pattern);
                System.out.println("Valid");
            } catch (PatternSyntaxException e) {
                // Catch the exception and print Invalid if pattern is invalid
                System.out.println("Invalid");
            }
        }
    }
}


