import java.util.*;

public class UniqueXOR {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers: ");

        String[] parts = sc.nextLine().split(" ");
        int result = 0;

        for (String p : parts) {
            result ^= Integer.parseInt(p);
        }

        System.out.println(result);
    }
}
