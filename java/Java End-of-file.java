import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lineNumber = 1;
        
        while (sc.hasNext()) {
            System.out.println(lineNumber + " " + sc.nextLine());
            lineNumber++;
        }
        
        sc.close();
    }
}
