import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        BitSet bitSet1 = new BitSet(n);
        BitSet bitSet2 = new BitSet(n);

        for (int j = 0; j < m; j++) {
            String operation = sc.next();
            
            if (operation.equals("AND")) {
                int a = sc.nextInt() - 1;
                int b = sc.nextInt() - 1;
                if (a == 0 && b == 1) {
                    bitSet1.and(bitSet2);
                } else if (a == 1 && b == 0) {
                    bitSet2.and(bitSet1);
                }
            } else if (operation.equals("OR")) {
                int a = sc.nextInt() - 1;
                int b = sc.nextInt() - 1;
                if (a == 0 && b == 1) {
                    bitSet1.or(bitSet2);
                } else if (a == 1 && b == 0) {
                    bitSet2.or(bitSet1);
                }
            } else if (operation.equals("XOR")) {
                int a = sc.nextInt() - 1;
                int b = sc.nextInt() - 1;
                if (a == 0 && b == 1) {
                    bitSet1.xor(bitSet2);
                } else if (a == 1 && b == 0) {
                    bitSet2.xor(bitSet1);
                }
            } else if (operation.equals("FLIP")) {
                int a = sc.nextInt() - 1;
                int index = sc.nextInt();
                if (a == 0) {
                    bitSet1.flip(index);
                } else if (a == 1) {
                    bitSet2.flip(index);
                }
            } else if (operation.equals("SET")) {
                int a = sc.nextInt() - 1;
                int index = sc.nextInt();
                if (a == 0) {
                    bitSet1.set(index);
                } else if (a == 1) {
                    bitSet2.set(index);
                }
            }
            
            System.out.println(bitSet1.cardinality() + " " + bitSet2.cardinality());
        }
        
        sc.close();
    }
}
