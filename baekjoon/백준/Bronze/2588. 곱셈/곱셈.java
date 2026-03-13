import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int hun = b / 100;
        int ten = (b - (hun * 100)) / 10;
        int one = (b - (hun * 100) - ten * 10);
        System.out.println(a * one);
        System.out.println(a * ten);
        System.out.println(a * hun);
        System.out.println(a * b);
    }
}
