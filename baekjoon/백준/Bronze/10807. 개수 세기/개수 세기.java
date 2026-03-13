import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanners = new Scanner(System.in);
        int num = scanners.nextInt();
        int count = 0;
        int [] array = new int[num];
        for(int i = 0; i < num ; i++){
            array[i] = scanners.nextInt();
        }
        int target = scanners.nextInt();
        for(int i = 0 ; i < num; i ++){
            if( array[i] == target)
                count ++;
        }
        System.out.println(count);

    }
}
