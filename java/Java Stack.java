import java.util.*;

class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Loop through all input lines
        while (sc.hasNext()) {
            String input = sc.next();  // Read the next string
            
            if (isBalanced(input)) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
        }
        
        sc.close();
    }

    // Helper function to check if a string of parentheses is balanced
    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        
        // Loop through each character in the string
        for (char c : s.toCharArray()) {
            // If the character is an opening parenthesis, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            // If it's a closing parenthesis, check if it matches the stack's top
            else if (c == ')' || c == '}' || c == ']') {
                // If the stack is empty or top doesn't match, it's unbalanced
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if (!isMatchingPair(top, c)) {
                    return false;
                }
            }
        }
        
        // If stack is empty, it means all parentheses matched correctly
        return stack.isEmpty();
    }

    // Helper function to check if two parentheses are matching
    public static boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
    }
}
