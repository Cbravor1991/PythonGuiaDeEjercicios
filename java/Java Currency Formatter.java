import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        NumberFormat usFormatted = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usFormatted.format(payment);
        
        Locale indiaLocale = new Locale("en", "IN");
        NumberFormat indiaFormatted = NumberFormat.getCurrencyInstance(indiaLocale);
        String india = indiaFormatted.format(payment);
        
        Locale chinaLocale = Locale.CHINA;
        NumberFormat chinaFormatted = NumberFormat.getCurrencyInstance(chinaLocale);
        String china = chinaFormatted.format(payment);
        
        Locale franceLocale = Locale.FRANCE;
        NumberFormat franceFormatted = NumberFormat.getCurrencyInstance(franceLocale);
        String france = franceFormatted.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}