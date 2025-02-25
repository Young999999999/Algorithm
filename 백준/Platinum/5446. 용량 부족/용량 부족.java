import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;

class Node {
    boolean isEnd = false;
    boolean isWildCard = true;
    HashMap<Character, Node> children = new HashMap<>();
}

public class Main {
    static Node root;
    static int cnt=0;
    static HashSet<String> set  ;
    static boolean flag;

    public static void removeWildCard(String s){
        Node pre = root;
        pre.isWildCard = false;

        for(int i =0; i<s.length();i++){
            pre = pre.children.get(s.charAt(i));
            //브랜치가 없을 때도 있음.
            if(pre == null) return;

            pre.isWildCard = false;
        }
    }

    public static void searchWord(String s){
        Node pre = root;
        if (root.isWildCard) {
            flag = true;
            return;
        }

        for(int i =0; i<s.length();i++){
            pre = pre.children.get(s.charAt(i));

            //와일드 카드를 찾은 경우
            if(pre.isWildCard) {
                String e = s.substring(0,i+1);

                //와일드 카드가 아직 등록 안돼있다면
                if(!set.contains(e)){
                    set.add(e);
                    cnt++;
                }
                return;
            }
        }
        //이때까지 와일드카드가 없었으면
     //   System.out.println(s);
        cnt++;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int t = 0; t<tc;t++){
            // build trie
            set = new HashSet<>();
            root = new Node();
            cnt = 0;
            flag = false;
            String[] removeFileNames = new String[2000];
            int n = Integer.parseInt(br.readLine());
            for (int i=0; i<n;i++){
                String s = br.readLine();
                removeFileNames[i] = s;
                Node pre = root;

                //word를 트라이에 삽입
                for (int j=0; j<s.length();j++){
                    char c = s.charAt(j);
                    pre.children.putIfAbsent(c,new Node());
                    pre = pre.children.get(c);
                }
                pre.isEnd = true;
            }

            // removeWildCard
            int m = Integer.parseInt(br.readLine());
            for (int i=0; i<m ; i++){
                String s = br.readLine();
                removeWildCard(s);
            }

            for(int i=0; i<2000;i++){
                if(removeFileNames[i] == null) break;
                searchWord(removeFileNames[i]);
                if (flag) break;
            }
            if(flag){
                System.out.println(1);
            } else{
                System.out.println(cnt);
            }

        }
    }
}


