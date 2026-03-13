import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hour = scanner.nextInt();
        int min = scanner.nextInt();
        int add = scanner.nextInt();
        int total = min + add;
        int count = 0;
        while (total > 59) {
            count++;
            total -= 60;
        }
        hour = hour + count;
        if(hour >= 24)
            hour -= 24;
        System.out.println((hour) + " " + total);
    }
}
