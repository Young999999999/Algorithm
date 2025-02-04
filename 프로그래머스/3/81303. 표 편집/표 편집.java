import java.util.*;

class Solution {
    
     class Node{
            int value;
            boolean edge = false;
            Node prev;
            Node next;

            Node(int value){
                this.value = value;
            }
         
            @Override
            public String toString(){
                return String.valueOf(value) + " " + next;
            }
        }

    class MyLinkedList{
        Node lastNode;
        Node firstNode;
        Node now;
        Stack<Node> stack = new Stack<>();

        void moveLeft(int idx){
            for(int i =0 ;i<idx;i++){
                now = now.prev;
            }
        }

        void moveRight(int idx){
            for (int i=0;i<idx;i++){
                now = now.next;
            }
        }

        void deleteNode(){
            if (now.edge){
                return;
            }
            
            stack.add(now);
            now.prev.next = now.next;
            now.next.prev = now.prev;

            if (now.next.edge){
                now = now.prev;
            } else {
                now = now.next;
            }
        }

        void recover(){
            Node recoverNode = stack.pop();
            recoverNode.prev.next = recoverNode;
            recoverNode.next.prev = recoverNode;

        }

        void add(Node node){
            if(now == null){
                now = node;
                firstNode = node;
                lastNode = node;
            } else {
                lastNode.next = node;
                node.prev = lastNode;
                lastNode = node;
            }
        }
        
    }

    public String solution(int n, int k, String[] cmd) {
        
        String answer = "";
        
        MyLinkedList list = new MyLinkedList();

        // 링크드 리스트 초기화
        for (int i=0; i<n+2; i++){
            Node node = new Node(i);
            list.add(node);
        }
        
        list.now.edge = true;
        list.lastNode.edge = true;
        list.moveRight(k+1);

        for (int i=0;i<cmd.length;i++){
            String op = cmd[i];
            char command = op.charAt(0);

            if (command == 'D' || command == 'U'){
                String[] s = op.split(" ");
                int idx = Integer.parseInt(s[1]);
               
                switch (command){
                    case 'D':
                        list.moveRight(idx);
                        break;
                    case 'U':
                        list.moveLeft(idx);
                        
                }
                
            } else if (command == 'C') {
                list.deleteNode();
            } else {
                list.recover();
            }
        }
        
        Node node = list.firstNode.next;
        
        char[] ans = new char[n+2];
        Arrays.fill(ans,'X');
        
        int v = 1;
        while(true){
            if (node.edge) break;
            ans[node.value] = 'O';
            node = node.next;
            
        }

        char[] trimmed = Arrays.copyOfRange(ans, 1, ans.length - 1);
        
        // char 배열을 문자열로 변환
        String finalStr = new String(trimmed);

        return finalStr;

    }
}