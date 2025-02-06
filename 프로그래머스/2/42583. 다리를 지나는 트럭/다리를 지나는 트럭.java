import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.


class Solution {
    ArrayDeque<int[]> q = new ArrayDeque<>();
    int bridge_length;
    int weight;
    int answer;
    int sum;
    int time = 0;
    int[] insertTime;

    public int solution(int bridge_length, int weight, int[] truck_weights) {

//         bridge_length = 10;
//         weight = 100;
//         truck_weights = new int[]{50, 30, 10, 10, 30, 10, 40};
      
        this.bridge_length =bridge_length;
        this.weight = weight;
        insertTime = new int[truck_weights.length];
        int idx =0 ;
        for (int t : truck_weights){

            addTruck(t,idx++);

        }

        return insertTime[idx-1] + bridge_length;
    }


    private void addTruck(int t,int idx){

        //단순 append
        int[] node = {t,idx};
        time++;
        
        if (sum + t <=weight){
            
            if (!q.isEmpty()){
                int[] p = q.poll();
                sum-=p[0];
                if(insertTime[p[1]] +bridge_length > time){
                    q.addFirst(p);
                    sum+=p[0];
                }
            }
            
            q.add(node);
            insertTime[idx] = time;
            sum += t;
            
        } else {

            while(sum+t > weight){
                int[] pollNode = q.poll();
                sum -= pollNode[0];
                time = insertTime[pollNode[1]] + bridge_length ;
            }

            q.add(node);
            insertTime[idx] = time;
            sum += t;  
        }        
    }
}

