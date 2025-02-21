import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node{
	
	boolean isEnd = false;
	HashMap<Character,Node> child = new HashMap<>();
	
	public Node(boolean end) {
		this.isEnd = end;
	}
	
	public Node() {
	}
	
	@Override
	public String toString() {
		return "Node [isEnd=" + isEnd + ", child=" + child.keySet() + "]";
	}
	
	
}


public class Main {
	
	static int[] dx = {0,0,1,-1,1,1,-1,-1};
	static int[] dy = {1,-1,0,0,-1,1,-1,1};
	static HashSet<String> result = new HashSet<>();
	
	static void recursive(char[][] board, int x, int y, Node now, char[] str,int idx,boolean[][] visited) {
		
		if(now.isEnd) {
			result.add(Arrays.toString(str));
		}
		
		for(int i=0; i<8 ;i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(0<=nx && nx<4 && 0<=ny && ny<4) {
				//자식중에 다음 좌표 값이 있다면 재귀
				if(!visited[ny][nx] && now.child.containsKey(board[ny][nx])){
					Node next = now.child.get(board[ny][nx]);
					
					str[idx] = board[ny][nx];
					visited[ny][nx] = true;
					recursive(board,nx,ny,next,str,idx+1,visited);
					visited[ny][nx] = false;
					str[idx] = '\0';
				}
			}
		}
	}

	static String wordToString(Object e) {
		StringBuilder sb = new StringBuilder();
		
		for (char c : ((String)e).toCharArray()) {
			if(65 <= c && c <= 90)sb.append(c);
		}
		return sb.toString();
	}
	static int[] getResult() {
		int value = 0;
		Object[] words = result.toArray();
		
		for (Object e : words) {
			String s = wordToString(e);
			
			switch(s.length()) {
				case 1:
				case 2:
					value +=0;
					break;
				case 3:
				case 4:
					value +=1;
					break;
				case 5:
					value +=2;
					break;
				case 6:
					value += 3;
					break;
				case 7:
					value += 5;
					break;
				case 8:
					value += 11;
					break;
			
			}
		}
		
		return new int[] {value,result.size()};
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int w = Integer.parseInt(br.readLine()); 
		
		Node root = new Node();
		char[] str = new char[8];
		boolean[][] visited = new boolean[4][4];
		
		//make Trie
		for (int i = 0; i < w; i++) {
			char[] words = br.readLine().toCharArray();
			Node pre = root;
			
			for (int j = 0; j < words.length; j++) {
				char c = words[j];
				
				pre.child.putIfAbsent(c, new Node());
				pre = pre.child.get(c);
				
			}
			pre.isEnd = true;
		}
		br.readLine();
		
		int b = Integer.parseInt(br.readLine());
		for (int i = 0; i < b; i++) {
			result.clear();
			char[][] board = new char[4][4];
			
			for(int j=0;j<4;j++) {
				board[j] = br.readLine().toCharArray();
			}
			
			for(int r=0; r<4; r++) {
				for (int c=0; c<4; c++) {
					
					if(root.child.containsKey(board[r][c])){
						Node next = root.child.get(board[r][c]);
						
						str[0] = board[r][c];
						visited[r][c] = true;
						recursive(board,c,r,next,str,1,visited);
						visited[r][c] = false;
						str[0] = '\0';
					}
					
					
				}
			}
			
			List<String> words = new ArrayList<>();
			for (Object e : result.toArray()) {
				words.add(wordToString(e));
			}
	
			words.sort((o1,o2) -> {
				String s1 = (String)o1;
				String s2 = (String)o2;
				
				if (s1.length() != s2.length()) {
					return -1 * (s1.length() - s2.length()); 
				} 
				
				return	 s1.compareTo(s2);
			});
			
			int[] a = getResult();
	
			System.out.printf("%d %s %d\n",a[0],words.get(0),a[1]);
			
			br.readLine();
		}

	}
}

