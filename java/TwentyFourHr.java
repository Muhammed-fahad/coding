import java.util.Scanner;

public class TwentyFourHr {

    public static String TimeChange(String time) {
        String[] parts = time.split(" ");
        String hhmm = parts[0];
        String ampm = parts[1].toLowerCase();

        String[] timeParts = hhmm.split(":");
        int hour = Integer.parseInt(timeParts[0]);
        String minute = timeParts[1];

        if (ampm.equals("am")) {
            if (hour == 12) {
                hour = 0;
            }
        } else {
            if (hour != 12) {
                hour += 12;
            }
        }

        return String.format("%02d:%s", hour, minute);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter time in 12hr format (hh:mm am/pm): ");
        String time = sc.nextLine();

        String result = TimeChange(time);
        System.out.println("24hr Format: " + result);
    }
}
