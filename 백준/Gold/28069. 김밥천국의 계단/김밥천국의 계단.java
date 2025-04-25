import java.io.*;
import java.util.*;

public class Main {

    static class Node{
        int now;
        int cost;

        Node(int now, int cost){
            this.now = now;
            this.cost = cost;
        }
    }

    public static int bfs(int n){
        boolean[] visited = new boolean[1000001];
        LinkedList<Node> q = new LinkedList<>();
        q.offer(new Node(0,0));

        while (!q.isEmpty()){
            Node cur = q.poll();
            if(cur.now == n) return cur.cost;

            for(int next: new int[]{cur.now+1,cur.now + cur.now/2}){
                if(next <= n && !visited[next] ) {
                    visited[next] = true;
                    q.offer(new Node(next,cur.cost + 1));
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        int minDist = bfs(n);

        if(minDist <= k ){
            System.out.println("minigimbob");
        } else{
            System.out.println("water");
        }

    }

}