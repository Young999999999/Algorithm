import java.util.*;
import java.io.*;

public class Main {
    static int[] arr;
    static long[] prefix;

    //전체범위중에서 조건 만족 가장 작은 인덱스 찾기
    private static int searchLeftIndex(int lowerBound, int n) {
        int l = 0;
        int r = n;
        for (int i = 0; i < 20; i++) {
            int mid = (l + r) / 2;
            if (arr[mid] < lowerBound) {
                l = mid;
                continue;
            }
            r = mid;
        }
        return r;
    }

    private static int searchRightIndex(int upperBound, int n) {
        int l = 0;
        int r = n;
        for (int i = 0; i < 20; i++) {
            int mid = (l + r) / 2;
            if (arr[mid] <= upperBound) {
                l = mid;
                continue;
            }
            r = mid;
        }
        return l;
    }


    private static long calCost(int s, int e, int now) {
        long leftCostSum = (long) (now - s) * arr[now] - (prefix[now] - prefix[s]);
        long rightCostSum = prefix[e + 1] - prefix[now + 1] - ((long) (e - now) * arr[now]);
        return leftCostSum + rightCostSum;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line1 = br.readLine().split(" ");
        int n = Integer.parseInt(line1[0]), q = Integer.parseInt(line1[1]);
        arr = new int[n];
        String[] line2 = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(line2[i]);
        }

        prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = arr[i] + prefix[i];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int lowerBound = Integer.parseInt(st.nextToken()), upperBound = Integer.parseInt(st.nextToken());
            int leftIdx = searchLeftIndex(lowerBound, n);
            int rightIdx = searchRightIndex(upperBound, n);

            if (lowerBound > arr[n - 1] || upperBound < arr[0] || leftIdx == rightIdx) {
                sb.append(0).append('\n');
                continue;
            }

            long max = -1, min = Long.MAX_VALUE;
            //max 구하기
            max = Math.max(max, calCost(leftIdx, rightIdx, leftIdx));
            max = Math.max(max, calCost(leftIdx, rightIdx, rightIdx));

            //min 구하기
            min = Math.min(min, calCost(leftIdx, rightIdx, (leftIdx + rightIdx) / 2));
            min = Math.min(min, calCost(leftIdx, rightIdx, (leftIdx + rightIdx) / 2 + 1));

            sb.append(max - min).append('\n');
        }

        System.out.println(sb);


    }

}