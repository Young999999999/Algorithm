import java.util.*;

class Solution {
    
    class Feature{
        int progress;
        int speed;
        
        Feature(int progress,int speed){
            this.progress = progress;
            this.speed= speed;
        }
        
        public void work(){
            this.progress += speed;
        }
        
        
    }
    
    
    public int[] solution(int[] progresses, int[] speeds) {
        Deque<Feature> q = new ArrayDeque<>();
        List<Integer> answer = new ArrayList<>();
        
        for(int i=0;i<progresses.length;i++){
            q.add(new Feature(progresses[i],speeds[i]));
        }
        
        while (!q.isEmpty()){
            int cnt= 0;
            for(Feature f : q){
                f.work();
            }

            while(!q.isEmpty()&& q.peek().progress >= 100){
                q.poll();
                cnt++;
            }  
            
            answer.add(cnt);
        }
        
        int[] result = answer.stream()
                .filter((cnt) -> cnt>0)
                .mapToInt((x) -> (int) x)
                .toArray();
        
        return result;
        
    }
     
}
