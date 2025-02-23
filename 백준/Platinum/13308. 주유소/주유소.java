import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Edge{
    int s;
    int e;
    int dist;

    public Edge(int s, int e, int dist) {
        this.s = s;
        this.e = e;
        this.dist = dist;
    }
}

class Node {
    int e;
    int dist;

    int cost;

    int preCost;
    public Node(int e, int dist, int cost, int preCost) {
        this.e = e;
        this.dist = dist;
        this.cost = cost;
        this.preCost = preCost;
    }

    @Override
    public String toString(){
        return "e " + e + "  dist " + dist + " cost " + cost;
    }
}




public class Main {
    static int[] cost = new int[2500];
    static int n;
    static int m;
    static List<Edge>[] graph;

    static List<Node> miniDijkstra(int s,int preCost) {

        List<Node> nodes = new ArrayList<>();
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.dist));
        pq.offer(new Node(s,0,cost[s],cost[s]));
        int[] distance = new int[n];
        Arrays.fill(distance,Integer.MAX_VALUE);
        distance[s] = 0;

        while (!pq.isEmpty()) {

            Node now = pq.poll();
            if(now.dist > distance[now.e]) continue;

            for (Edge e : graph[now.e]){
                if( now.dist + e.dist < distance[e.e]){
                    distance[e.e] = now.dist + e.dist;
                    pq.offer(new Node(e.e,now.dist + e.dist,cost[s],cost[s]));
                }
            }
        }

        for(int i=0; i<n; i++){
            if(distance[i] != Integer.MAX_VALUE && distance[i] != 0)
                nodes.add(new Node(i,distance[i]*preCost,preCost,preCost));
        }

        return nodes;

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        String[] costInput = br.readLine().split(" ");

        for (int i=0; i<n;i++){
            cost[i] = Integer.parseInt(costInput[i]);
        }

        graph = new ArrayList[n];

        for (int i =0 ; i<n ; i++){
            graph[i] = new ArrayList<>();
        }

        for (int i =0; i<m; i++){
            String[] edgeInput = br.readLine().split(" ");
            int s = Integer.parseInt(edgeInput[0]) , e = Integer.parseInt(edgeInput[1]) , c = Integer.parseInt(edgeInput[2]);
            graph[s-1].add(new Edge(s-1,e-1,c));
            graph[e-1].add(new Edge(e-1,s-1,c));
        }

        PriorityQueue<Node> pq = new PriorityQueue<>((o1,o2) -> o1.dist-o2.dist);
        pq.offer(new Node(0,0,cost[0],2500));
        int[] distance = new int[n];
        Arrays.fill(distance,Integer.MAX_VALUE);
        distance[0] = 0;

        while(!pq.isEmpty()){
            Node now = pq.poll();

            if (now.e == n-1) {
                System.out.println(now.dist);
                break;
            }

            if (now.dist > distance[now.e]) continue;

            //미니 다익 돌려
            if (now.preCost > now.cost){
                List<Node> nodes = miniDijkstra(now.e,now.cost);

                //미니 다익 결과를 distance에서 비교해서 값 넣어야함
                for (Node node : nodes){
                    if(distance[node.e] > node.dist + now.dist){
                        distance[node.e] = node.dist + now.dist;
                        pq.offer(new Node(node.e,node.dist + now.dist,cost[node.e],now.cost));
                    }
                }
            } // 일반 다익 돌려
            else{
                for(Edge node : graph[now.e]){
                    if(distance[node.e] > now.preCost * node.dist + now.dist){
                        distance[node.e] = now.preCost * node.dist + now.dist;
                        pq.offer(new Node(node.e,now.preCost*node.dist + now.dist,now.preCost,now.preCost));
                    }
                }
            }

        }
    }
}
