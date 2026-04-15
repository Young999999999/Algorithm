import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

class Main {
  static boolean[] ban = new boolean[100001];
  static boolean[][] visited = new boolean[10001][1000];

  static Queue<int[]> q = new ArrayDeque<>();

  static int[] vector = {1,0,-1};

  static void bfs(int end) {
    q.offer(new int[]{1,0,0});

    while(!q.isEmpty()){
      int[] tmp = q.poll();
      int now = tmp[0], step = tmp[1], cnt = tmp[2];
      
      if (now == end) {
        System.out.println(cnt);
        System.exit(0);
        return;
      }

      for (int dx: vector){
        int nStep = step + dx;
        if (nStep > 0){
          int next = now + nStep;

          //bound check
          if (!ban[next] && next <= end && !visited[next][nStep]) {
            q.offer(new int[]{next,nStep,cnt+1});
            visited[next][nStep] = true;
          }
        }
      }
    }
  }


  public static void main(String[] args) throws Exception{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] line = br.readLine().split(" ");
    int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]);

    for (int i=0; i<m ;i++){
      int tmp = Integer.parseInt(br.readLine());
      ban[tmp] = true;
    }

    bfs(n);
    System.out.println(-1);

  }
}
