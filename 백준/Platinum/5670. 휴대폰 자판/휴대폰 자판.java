import java.util.*;
import java.io.*;

class Node{
    boolean isEnd = false;

    Node[] child = new Node[26];
}

public class Main {

    static Node root;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String length;


        // 입력이 없을 때까지 반복 (EOF 처리)
        while ((length = br.readLine()) != null) {
            List<String> l = new ArrayList<>();
            root = new Node();
            float sum = 0;
            for (int i =0; i<Integer.parseInt(length); i++) {
                String word = br.readLine();
                l.add(word);
                Node pre = root;
                for (int j=0;j<word.length();j++) {
                    char c = word.charAt(j);

                    if (pre.child[c-'a'] == null) {
                        pre.child[c - 'a'] = new Node();
                    }
                    pre = pre.child[c-'a'];
                }
                pre.isEnd = true;

            }

            //입력이 끝나고 단어마다 몇 번 클릭을 해야하는지 구해야함
            for(String s : l) {
                sum += (float)searchWord(s);
            }
            System.out.printf("%.2f\n",sum/l.size());

        }
    }

    public static int searchWord(String word) {
        cnt = 0;
        Node now = root;
        int num =0;
        while(true) {
            num++;

            //현재 얻을 문자
            char c = word.charAt(cnt);
            now = now.child[c-'a'];
            Node result = getNextNode(now);

            //동일한 문자열이면 cnt 반환
            if(word.length() == cnt) {
                return num;
            }

            now = result;
        }

    }

    public static int getSize(Node node){
        int size= 0;
        for(int i=0; i<26;i++){
            if(node.child[i] != null) size++;
        }
        return size;
    }

    public static int getKey(Node node){
        for(int i=0;i<26;i++){
            if (node.child[i] != null) {
                return i;}
        }

        return 1;
    }
    public static Node getNextNode(Node now) {

        while (true) {
            //자식이 둘 이상
            if (getSize(now) >= 2 || now.isEnd) {
                cnt++;
                return now;
            }

            now = now.child[getKey(now)];
            cnt ++;
        }
    }

}




