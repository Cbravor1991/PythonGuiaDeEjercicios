import java.util.*;
interface AdvancedArithmetic{
  int divisor_sum(int n);
}

// Write MyCalculator class here
class MyCalculator implements AdvancedArithmetic {
    // Implement the divisor_sum method to calculate the sum of divisors of n
    public int divisor_sum(int n) {
        int sum = 0;
        // Loop through all numbers from 1 to n to find divisors
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) { // If i is a divisor of n
                sum += i;
            }
        }
        return sum;
    }
}

class Solution{
    public static void main(String []args){
        MyCalculator my_calculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(my_calculator.divisor_sum(n) + "\n");
      	sc.close();
    }
    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o){
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++){
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}

