import java.util.*;

public class Test {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int m = in.nextInt();
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        int maxUnique = 0;
        
        for (int i = 0; i < n; i++) {
            int count = map.containsKey(arr[i]) ? map.get(arr[i]) : 0;
            map.put(arr[i], count + 1);
            
            if (i >= m - 1) {
                maxUnique = Math.max(maxUnique, map.size());
                
                int elementToRemove = arr[i - m + 1];
                int elementCount = map.get(elementToRemove) - 1;
                map.put(elementToRemove, elementCount);
                
                if (elementCount == 0) {
                    map.remove(elementToRemove);
                }
            }
        }
        
        System.out.println(maxUnique);
    }
}
