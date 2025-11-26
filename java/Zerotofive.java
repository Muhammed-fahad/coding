import java.util.Scanner;

public class Zerotofive {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter a number: ");
            int n = sc.nextInt();
            
            int ans = 0;
            int multi = 1;
            
            while (n > 0) {
                int k = n % 10;
                if (k == 0) {
                    ans += 5 * multi;
                } else {
                    ans += k * multi;
                }
                n /= 10;
                multi *= 10;
            }
            
            System.out.println(ans);
        }
    }
}
