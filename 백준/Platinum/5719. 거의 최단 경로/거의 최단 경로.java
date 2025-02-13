import java.util.*;
import java.io.*;

class Edge {

    int s;
    int e;
    int cost;

    Edge(int s,int e,int cost){
        this.s = s;
        this.e= e;
        this.cost=cost;
    }
}

public class Main {

    static int[] dijkstra(int[] distance,int s){
        Arrays.fill(distance,INF);
        distance[s]=0;
        PriorityQueue<Edge> pq = new PriorityQueue<>((o1,o2)-> o1.cost-o2.cost);
        pq.add(new Edge(0,s,0));

        while (!pq.isEmpty()){
            Edge edge = pq.poll();
            int now  = edge.e;
            int dist = edge.cost;

            if (distance[now] < dist) continue;

            for (Edge e : graph[now]){
                if(ban.contains(e)) continue;

                if(distance[e.e] > dist + e.cost){
                    distance[e.e] =  dist + e.cost;
                    pq.add(new Edge(0,e.e,distance[e.e]));
                }
            }
        }

        return distance;
    }

    static void banEdge(int e){
        for(int i =0; i< reverseGraph[e].size();i++){
            Edge edge =reverseGraph[e].get(i);
            if (distance[e] == distance[edge.s] + edge.cost){
                if (ban.contains(edge)) continue;

                ban.add(edge);
                banEdge(edge.s);

            }
        }
    }

    static int INF = 10000000;
    static List<Edge>[] graph;
    static List<Edge>[] reverseGraph;
    static HashSet<Edge> ban;
    static int[] distance;
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            String[] s1 = br.readLine().split(" ");
            int n=Integer.parseInt(s1[0]) , m =Integer.parseInt(s1[1]);
            if(n==0 && m==0) break;

            String[] s2 = br.readLine().split(" ");
            int s = Integer.parseInt(s2[0]), d = Integer.parseInt(s2[1]);

            graph = new ArrayList[n];
            reverseGraph = new ArrayList[n];
            ban = new HashSet<>();

            for(int i=0; i<n;i++){
                graph[i] = new ArrayList<>();
                reverseGraph[i] = new ArrayList<>();
            }

            distance = new int[n];


            //그래프 삽입
            for(int i=0;i<m;i++){
                String[] s3 = br.readLine().split(" ");
                int u = Integer.parseInt(s3[0]),v = Integer.parseInt(s3[1]),p = Integer.parseInt(s3[2]);
                Edge edge = new Edge(u,v,p);
                graph[u].add(edge);
                reverseGraph[v].add(edge);
            }

            dijkstra(distance,s);
            banEdge(d);
            dijkstra(distance,s);

            if(distance[d] == INF) System.out.println(-1);
            else System.out.println(distance[d]);

        }

    }




}
