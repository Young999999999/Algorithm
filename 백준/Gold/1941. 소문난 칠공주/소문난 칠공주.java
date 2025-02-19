import java.util.*;

public class Main {

    static int[] dx = {-1,1,-5,5};
    static List<Integer>[] graph = new ArrayList[25];
    static void recursive(int x,LinkedList<Integer> path,int cnt){
        if(cnt>3) return;
        // 기저
        if(path.size() == 7){
            combinations.add(new ArrayList<>(path));
            return;
        }

        if(25 - x  < 7 - path.size()) return;

        for (int i=x+1 ; i<25;i++){
            path.add(i);
            if(matrix[i/5][i%5]=='Y') cnt++;
            recursive(i,path,cnt);
            if(matrix[i/5][i%5]=='Y') cnt--;
            path.removeLast();
        }
    }

    static char[][] matrix = new char[5][5];
    static List<List<Integer>> combinations = new ArrayList<>();

    static boolean isConnected(int start,int[] visited,List<Integer> c){
        int count = 1;
        int[] dx = {0,0,-1,1};
        int[] dy = {1,-1,0,0};

        ArrayDeque<Integer> q = new ArrayDeque<>();

        q.offerLast(start);
        visited[start] = 1;

        while (!q.isEmpty()){
            int now = q.pollFirst();
            int x = now%5;
            int y = now/5;

            for (int i=0;i<4;i++){
                int nx = x+dx[i], ny = y+dy[i];

                if (0<=nx && nx<5 && 0<=ny && ny<5) {
                    int num = ny * 5 + nx;

                    //아직 미방문이라면
                    if (c.contains(num) && visited[num] == 0) {
                        count++;
                        visited[num] = 1;
                        q.offerLast(num);
                    }
                }
            }
        }

        if (count == 7) return true;
        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        for(int i = 0; i<5;i++){
            matrix[i] = sc.nextLine().toCharArray();
        }
        int result =0;
        for (int i =0; i<25;i++) graph[i] = new ArrayList<>();

        //그래프 전처리
        for (int i =0; i<25;i++){
            for(int j = 0;j<4;j++){
                int nx = i+dx[j];
                if(0<=nx && nx<25){
                    graph[i].add(nx);
                }
            }
        }

        LinkedList<Integer> path = new LinkedList<>();
        recursive(-1, path,0);

        for(List<Integer> c : combinations){
            int[] visited=new int[25];
            if(isConnected(c.get(0),visited,c)) result++;

        }

        System.out.println(result);


    }
}
