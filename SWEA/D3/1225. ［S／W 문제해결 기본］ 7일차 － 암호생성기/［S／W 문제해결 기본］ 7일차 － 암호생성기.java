import java.util.*;

public class Solution {
    public static boolean cycle(LinkedList<Integer> num) {
        for (int cnt = 1; cnt <= 5; cnt++) {
            int tmp = num.removeFirst();
            tmp -= cnt;
            if (tmp > 0) {
                num.add(tmp);
            } else {
                num.add(0); 
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 10; i++) {
            sc.nextLine();
            int[] num = new int[8];
            LinkedList<Integer> queue = new LinkedList<>();

            String[] input = sc.nextLine().split(" ");
  
            for (int j = 0; j < 8; j++) {
                num[j] = Integer.parseInt(input[j]);
            }

            for (int val : num) {
                queue.add(val);
            }

            while (true) {
                if (!cycle(queue)) { 
                    System.out.print("#" + (i + 1) + " ");
                    for (int val : queue) {
                        System.out.print(val + " ");
                    }
                    System.out.println();
                    break;
                }
            }
        }

        sc.close();
    }
}
