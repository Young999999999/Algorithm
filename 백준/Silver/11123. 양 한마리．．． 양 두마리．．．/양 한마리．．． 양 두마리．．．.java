import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {

  static int w;
  static int h;

  static char[][] matrix;
  public static void dfs(int[] now, int[][] visited){
    int nowX = now[0], nowY = now[1];
    visited[nowY][nowX] = 1;
    int[][] vectors = {{0,1},{0,-1},{1,0},{-1,0}};

    for (int[] vector :vectors){
      int nx = nowX+vector[0];
      int ny = nowY+vector[1];

      if (0<=nx && nx<w && 0<=ny&& ny<h) {
        if (visited[ny][nx] == 0 && matrix[ny][nx] == '#') {
          dfs(new int[]{nx, ny}, visited);
        }
      }

    }
  }


  public static void main(String[] args) throws  Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int t = Integer.parseInt(br.readLine());

    for (int i=0; i<t; i++) {
      var tmp = br.readLine().split(" ");
      h = Integer.parseInt(tmp[0]);
      w = Integer.parseInt(tmp[1]);

      matrix = new char[h][w];

      for (int y = 0; y < h; y++) {
        String l = br.readLine();
        for (int x = 0; x < w; x++) {
          matrix[y][x]= l.charAt(x);
        }
      }

      int [][] visited = new int[h][w];
      int result = 0;
      for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
          if(visited[y][x] == 0 && matrix[y][x] == '#') {
            dfs(new int[]{x, y}, visited);
            result++;
          }
        }
      }

      System.out.println(result);


    }
  }
}
