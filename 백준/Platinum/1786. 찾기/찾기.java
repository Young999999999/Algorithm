import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        char[] T = br.readLine().toCharArray();
        char[] P = br.readLine().toCharArray();

        if(P.length > T.length){
            System.out.println(0);
            System.exit(0);
        }
        int cnt =0;
        StringBuilder sb = new StringBuilder();

        long MOD = 1_000_000_007;
        long BASE = 31;
        long pHash = 0;
        long tHash = 0;
        long power = 1;

        for(int i=0 ;i< P.length;i++){
            pHash = (BASE * pHash + P[i]) % MOD;
            tHash = (BASE * tHash + T[i]) % MOD;

            if(i>0) {
                power = (power * BASE) % MOD;
            }
        }

        for(int i=0; i< T.length-P.length+1;i++){
            if(tHash == pHash){
                cnt++;
                sb.append(i+1).append(' ');
            }

            if (i >= T.length - P.length) break;

            long removed = (T[i] * power) % MOD;
            tHash = (tHash - removed + MOD) % MOD;
            tHash = (BASE * tHash + T[i+P.length]) % MOD;

        }

        System.out.println(cnt);
        System.out.println(sb);

    }
}
