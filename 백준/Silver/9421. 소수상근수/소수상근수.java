import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Main {

  // 1 상근수 , 0 암것도 안해봄, -1 상근수 아님
  static int[] isPrime = new int[1000001];

  public static void calculate() {
    isPrime[0] = 1;
    isPrime[1] = 1;


    for (int i = 2; i < 1000001; i++) {
      List<Integer> stack = new ArrayList<Integer>();

      if (isPrime[i] == 0) {
        stack.add(i);

        int tmp = i;
        while (true) {
          tmp = getNextNum(tmp);

          // 상근 수 발견
          if (isPrime[tmp] == 1) {
            stack.forEach(e -> isPrime[e] = 1);
            break;
          }

          // 상근 수 아님 싸이클 발생
          if (isPrime[tmp] == -1 || stack.contains(tmp)) {
            stack.forEach(e -> isPrime[e] = -1);
            break;
          }

          stack.add(tmp);
        }
      }
    }
  }

  public static int getNextNum(int num) {
    int result = 0;

    while (num != 0) {
      int tmp = num % 10;
      result += tmp * tmp;
      num = num / 10;
    }

    return result;
  }

  public static void main(String[] args) throws Exception {
    calculate();

    BufferedReader br = new BufferedReader(
        new InputStreamReader(System.in));

    int input = Integer.parseInt(br.readLine());

    for (int i = 2; i <= input; i++) {
      if(isPrime[i] == 1){
        int flag = 0;
        for (int j=2; j<=Math.sqrt(i); j++) {
          if (i % j == 0){
            flag = 1;
            break;
          }
        }
        if (flag == 0) {
          System.out.println(i);
        }

      }
    }


  }


}