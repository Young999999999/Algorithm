import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.sql.SQLOutput;

public class Main {

    public static int GCD(int a, int b){
        if (a%b == 0){
            return b;
        }
        return GCD(b,a%b);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] P = br.readLine().split(" ");
        String[] T  =br.readLine().split(" ");

        long BASE = 31;
        long MOD = 1_000_000_007L;
        long pHash = 0;
        long tHash = 0;
        long power = 1;
        int cnt = 0;

        for(int i=0; i<n; i++){
            pHash = (BASE * pHash + P[i].charAt(0)) % MOD;
            tHash = (BASE * tHash + T[i].charAt(0)) % MOD;

            if(i>0){
                power = (power * BASE) % MOD;
            }
        }

        for (int i=0; i<n; i++){

            if(pHash == tHash){
                cnt++;
            }

            long removed = (power * T[i].charAt(0)) % MOD;
            tHash = (tHash - removed + MOD) % MOD;
            tHash = ((BASE * tHash) % MOD + T[i].charAt(0)) % MOD;

        }

        int gcd = GCD(n,cnt);
        System.out.printf("%d/%d",cnt/gcd ,n/gcd);

    }
}
