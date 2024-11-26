import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Leer la longitud del array
        int n = scanner.nextInt();
        
        // Leer los elementos del array
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        scanner.close();
        
        // Contar subarrays con suma negativa
        int negativeCount = 0;
        
        for (int i = 0; i < n; i++) {
            int currentSum = 0;
            for (int j = i; j < n; j++) {
                currentSum += arr[j]; // Sumar elementos del subarray
                if (currentSum < 0) {
                    negativeCount++; // Contar si la suma es negativa
                }
            }
        }
        
        // Imprimir el resultado
        System.out.println(negativeCount);
    }
}
