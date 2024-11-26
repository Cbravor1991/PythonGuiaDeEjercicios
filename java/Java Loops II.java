class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        
        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int result = a;
            for (int j = 0; j < n; j++) {
                result += b * (1 << j);  // 1 << j es equivalente a 2^j
                System.out.print(result + " ");
            }
            System.out.println();
        }
        
        in.close();
    }
}