import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanners = new Scanner(System.in);
        int num = scanners.nextInt();
        int[] arr = new int[num];
        int rep = scanners.nextInt();
        for (int i = 0; i < rep; i++) {
            int a = scanners.nextInt();
            int b = scanners.nextInt();
            int c = scanners.nextInt();
            for (int j = a - 1; j < b; j++) {
                arr[j] = c;
            }
        }
        for (int i = 0; i < num; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}
