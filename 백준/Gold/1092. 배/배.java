import java.util.*;
import java.io.*;

class Crain{
    int limitWeight;
    LinkedList<Box> candidates = new LinkedList<>();
    Crain(int limitWeight){
        this.limitWeight = limitWeight;
    }
    void add(Box box){
        if(this.limitWeight >= box.weight){
            this.candidates.offer(box);
        }
    }

    boolean carry(){
        while(!candidates.isEmpty()) {
            Box box = candidates.pollFirst();
            if(box.isVisited) continue;

            //방문하지 않은 박스라면
            box.isVisited = true;
            return true;
        }
        return false;
    }
}
class Box {
    boolean isVisited = false;
    int weight;

    Box(int weight){
        this.weight = weight;
    }
}

public class Main {
    static int size;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Crain> crains = new ArrayList<>();
        String[] input = br.readLine().split(" ");
        for(int i=0; i<n ; i++){
            crains.add(new Crain(Integer.parseInt(input[i])));
        }

        int m = Integer.parseInt(br.readLine());
        String[] input2 = br.readLine().split(" ");
        for(int i=0; i<m; i++){
            Box box = new Box(Integer.parseInt(input2[i]));
            for(int j=0; j <n; j++){
                crains.get(j).add(box);
            }
        }

        for(int i=0; i<n; i++){
            crains.get(i).candidates.sort((o1,o2)-> {return -1*Integer.compare(o1.weight,o2.weight);});
        }

        crains.sort((o1,o2) -> {
            return o1.limitWeight - o2.limitWeight;
        });

        int t=1;
        while(true){
            for(int i=0; i<n; i++){
                if(crains.get(i).carry()) size++;
            }

            if(size == m){
                System.out.println(t);
                break;
            }

            if(t > 10000){
                System.out.println(-1);
                break;
            }

            t++;
        }




    }
}
