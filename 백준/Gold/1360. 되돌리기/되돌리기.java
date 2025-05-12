import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        var ops = new LinkedList<Object[]>();
        for (int i=0 ;i<n ;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            Object[] op = new Object[]{ st.nextToken(),st.nextToken(),st.nextToken()};
            ops.offer(op);
        }
        StringBuilder sb = new StringBuilder();
        int undoTime = Integer.MAX_VALUE;
        for (int i=0; i<n;i++){
            Object[] op = ops.pollLast();
            String command = String.valueOf(op[0]);
            int atTime = Integer.parseInt(String.valueOf(op[2]));
            if(atTime >= undoTime) continue;

            if(command.equals("type")){
                sb.append(op[1]);
            }

            if (command.equals("undo")){
                int excuteTime = Integer.parseInt(String.valueOf(op[1]));
                undoTime = atTime - excuteTime;
            }
        }

        System.out.println(sb.reverse());


    }

}