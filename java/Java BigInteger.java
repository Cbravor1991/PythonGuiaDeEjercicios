import java.io.*;
import java.math.BigInteger;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        // Read input
        Scanner sc = new Scanner(System.in);
        BigInteger a = new BigInteger(sc.next());
        BigInteger b = new BigInteger(sc.next());
        sc.close();

        // Perform addition and multiplication
        BigInteger sum = a.add(b);
        BigInteger product = a.multiply(b);

        // Print results
        System.out.println(sum);
        System.out.println(product);
    }
}