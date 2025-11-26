import java.util.HashMap;
import java.util.Scanner;

public class AnagramCheck {

    public static boolean isAnagram(String a, String b) {

        a = a.replaceAll("\\s", "").toLowerCase();
        b = b.replaceAll("\\s", "").toLowerCase();

        if (a.length() != b.length()) {
            return false;
        }

        HashMap<Character, Integer> aStore = new HashMap<>();
        HashMap<Character, Integer> bStore = new HashMap<>();

        for (int i = 0; i < a.length(); i++) {
            char ch1 = a.charAt(i);
            char ch2 = b.charAt(i);

            aStore.put(ch1, aStore.getOrDefault(ch1, 0) + 1);
            bStore.put(ch2, bStore.getOrDefault(ch2, 0) + 1);
        }

        return aStore.equals(bStore);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first string: ");
        String a = sc.nextLine();

        System.out.print("Enter second string: ");
        String b = sc.nextLine();

        if (isAnagram(a, b)) {
            System.out.println("Anagram");
        } else {
            System.out.println("Not anagram");
        }
    }
}
