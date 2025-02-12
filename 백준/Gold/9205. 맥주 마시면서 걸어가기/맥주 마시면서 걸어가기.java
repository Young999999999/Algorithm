import java.util.*;
import java.io.*;

public class Main{

    private static boolean canWalk(String[] a,String[] b){
        int dx = Math.abs(Integer.parseInt(a[0]) - Integer.parseInt(b[0]));
        int dy = Math.abs(Integer.parseInt(a[1]) - Integer.parseInt(b[1]));
        return dx+dy <= 1000;
    }

    private static int[][] floid(int[][] graph){

        for(int j=0;j<graph.length;j++){
            for(int i=0;i<graph.length;i++){
                for (int k=0;k<graph.length;k++){
                    graph[i][k] = Math.min(graph[i][k], graph[i][j] + graph[j][k]);
                }
            }
        }

        return graph;
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        for (int t=0;t<tc;t++){
            int n =Integer.parseInt(br.readLine());
            String[][] locate = new String[n+2][2];
            int[][] graph = new int[n+2][n+2];
            for(int i=0;i<n+2;i++){
                Arrays.fill(graph[i],100);
            }
            String[] house = br.readLine().split(" ");
            locate[0] = house;

            for (int j=1; j<n+1; j++){
                locate[j] = br.readLine().split(" ");
            }

            String[] festival = br.readLine().split(" ");
            locate[n+1] = festival;

            for(int i=0; i<n+2;i++){
                for(int j=0;j<n+2;j++){
                    if(canWalk(locate[i],locate[j])) {
                        graph[i][j] = 0;
                        graph[j][i] = 0;
                    }
                }
            }

            graph = floid(graph);

            if(graph[0][n+1] ==0){
                System.out.println("happy");
            } else{
                System.out.println("sad");
            }

        }


    }
}
