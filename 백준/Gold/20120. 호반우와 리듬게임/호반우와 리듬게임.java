import java.util.*;
import java.io.*;

public class Main {

    static long[][] dp = new long[1000][1001];

    private static long getMax(int idx){

        long MAX = Long.MIN_VALUE;
        for(int i =1; i<idx+2;i++){
            MAX = Math.max(MAX,dp[idx][i]);
        }

        return MAX;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int[] notes = new int[n];

        for (int i =0; i<n;i++){
            notes[i] = Integer.parseInt(input[i]);
            dp[i][0] = -10000000000L;
        }

        dp[0][0] = 0;
        dp[0][1] = notes[0];

        for(int i=1;i<n;i++){
            //combo => j
            if(i-1>=0) dp[i][0] = Math.max(dp[i][0],getMax(i-1));
            if(i-2>=0) dp[i][0] = Math.max(dp[i][0],getMax(i-2));


            for(int j=1;j<i+2;j++){
                dp[i][j] = dp[i-1][j-1] + j * notes[i];
            }
        }
//
//        for(int i=0;i<10;i++){
//            System.out.println(Arrays.toString(dp[i]));
//        }

        long result = Long.MIN_VALUE;
        for(int i=0;i<n+1;i++){
            result = Math.max(dp[n-1][i],result);
        }

        System.out.println(Math.max(0,result));


    }
}
