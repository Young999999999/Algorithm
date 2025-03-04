import java.util.*;
import java.io.*;

public class Main {

	static int[] dx = {0,0,-1,1};
	static int[] dy = {1,-1,0,0};
	static int result = 0;
	static int n;
	
	public static void main(String[] args) throws IOException{
		//--------------솔루션 코드를 작성하세요.--------------------------------
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		n = Integer.parseInt(br.readLine());
		
		int[][] matrix = new int[n][n];
		
		//2차원 매트릭스 입력
		for (int i=0; i<n ;i++) {
			String[] input = br.readLine().split(" ");
			for (int j=0;j<n;j++) {
				matrix[i][j] = Integer.parseInt(input[j]);	
			}
		}
		
		for (int cut=0;cut<100;cut++) {
			boolean[][] visited = new boolean[n][n];
			int cnt = 0;
			for(int i=0; i<n;i++) {
				for (int j=0; j<n;j++) {
					if(!visited[i][j] && matrix[i][j] > cut) {
						cnt++;
						bfs(j,i,visited,cut,matrix);
					}
				}
			}
			
			result = Math.max(result,cnt);
			
		}	
		System.out.println(result);
	}
	
	
	//cut 보다 큰놈들 bfs
	public static void bfs(int x, int y , boolean[][] visited, int cut,int[][] matrix) {
		LinkedList<int[]> q = new LinkedList<>();
		
		q.offer(new int[]{x,y});
		visited[y][x] = true;
		
		while(!q.isEmpty()) {
			int[] now = q.pollFirst();
			x = now[0]; y = now[1];
			
			for(int i=0; i<4;i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				
				if(0<=nx && nx<n && 0<=ny && ny<n) {
					if(!visited[ny][nx] && matrix[ny][nx] > cut) {
						visited[ny][nx] = true;
						q.offer(new int[] {nx,ny});
						
					}
				}
			}
			
		}
	}
	
	
	
	
}
    