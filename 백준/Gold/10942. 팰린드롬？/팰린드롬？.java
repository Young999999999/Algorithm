import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] sequence;
    static boolean[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n =Integer.parseInt(br.readLine());
        sequence = new int[n];
        String[] input = br.readLine().split(" ");
        for(int i=0; i<n; i++){
            sequence[i] = Integer.parseInt(input[i]);
        }
        int m = Integer.parseInt(br.readLine());
        dp = new boolean[n][n];
        for(int i=0;i<n;i++){
            dp[i][i] = true;
        }

        if (n>=2)
        {
            for(int i=0; i<n-1;i++) {
                dp[i][i + 1] = sequence[i] == sequence[i + 1];
            }

            for(int dist=2; dist<n;dist++){
                for (int s=0;s<n-dist;s++){
                    int e = s+dist;
                    if(sequence[s] == sequence[e] && dp[s+1][e-1]){
                        dp[s][e] = true;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i=0; i<m; i++){
            String[] input2 = br.readLine().split(" ");
            int s = Integer.parseInt(input2[0])-1, e = Integer.parseInt(input2[1])-1;
            sb.append(dp[s][e] ? "1" : "0").append("\n");
        }
        System.out.println(sb);
    }
}
