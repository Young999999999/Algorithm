import java.util.*;
import java.io.*;


public class Main {
    
	public static void floid(int[][] distance,int n) {
		
		for(int j=0;j<n;j++) {
			for (int i=0;i<n;i++) {
				for (int k=0;k<n;k++) {
					distance[i][k] = Math.min(distance[i][k], distance[i][j] + distance[j][k]);
				}
			}
		}
	
	}
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		var nm = br.readLine().split(" ");
		int n = Integer.parseInt(nm[0]), m = Integer.parseInt(nm[1]);
		
		var distance1 = new int[n][n];
		var distance2 = new int[n][n];
		int INF = 1000000000;
		for(int i=0;i<n;i++) {
			Arrays.fill(distance1[i], 1000000000);
			Arrays.fill(distance2[i], 1000000000);
		}
		var edges = new ArrayList<int[]>();
		
		for(int i=0 ;i<m;i++) {
			var input = br.readLine().split(" ");
			
			int from = Integer.parseInt(input[0]);
			int to = Integer.parseInt(input[1]);
			int cost = Integer.parseInt(input[2]);
			
			edges.add(new int[] {from,to,cost});
			distance1[from][to] = cost;
			distance1[to][from] = cost;
			
			distance2[from][to] = cost;
			distance2[to][from] = cost;
			
		}
		
		floid(distance1,n);

		StringBuilder sb = new StringBuilder();
		for (int i=0;i<m;i++) {
			var edge = edges.get(i);
			
			int from = edge[0], to = edge[1];
			
			int[][] distance3 = new int[n][n];

			
			for(int j=0; j<n;j++) {
				for(int k =0; k<n;k++) {
					distance3[j][k] = distance2[j][k];
				}
			}
				
			distance3[from][to] = INF;
			distance3[to][from] = INF;
			floid(distance3,n);
		
			int count = 0;
			
			for(int s=0;s<n;s++) {
				for(int e=0;e<n;e++) {
					if (s!=e && distance1[s][e] < distance3[s][e]) {
						count++;
					}
				}
			}
			
			sb.append(count/2).append(' ');
		}
		
		System.out.println(sb);
		
	}
}
