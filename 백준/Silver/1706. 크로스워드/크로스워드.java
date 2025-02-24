import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] input = sc.nextLine().split(" ");
		char[][] matrix = new char[Integer.parseInt(input[0])][Integer.parseInt(input[1])];
		
		int r = Integer.parseInt(input[0]);
		int c = Integer.parseInt(input[1]);
		
		for (int i=0; i<Integer.parseInt(input[0]);i++) {
			matrix[i] = sc.nextLine().toCharArray();
		}
		
		List<String> dict = new ArrayList<String>();
		
		for (int j =0; j<c ;j++) {
			StringBuilder sb= new StringBuilder();
			for (int i=0;i<r;i++) {
				if(matrix[i][j] == '#') {
					
					if(sb.length() >=2)
						dict.add(sb.toString());
					
					sb.setLength(0);
				} else {
					sb.append(matrix[i][j]);
				}
				
				//세로 마지막
				if (i==r-1) {
					if(sb.length() >=2)
						dict.add(sb.toString());
				}
			}
		}
	
		for (int i =0; i<r ;i++) {
			StringBuilder sb= new StringBuilder();
			for (int j=0;j<c;j++) {
				if(matrix[i][j] == '#') {
					
					if(sb.length() >=2)
						dict.add(sb.toString());
					
					sb.setLength(0);
				} else {
					sb.append(matrix[i][j]);
				}
				
				//세로 마지막
				if (j==c-1) {
					if(sb.length() >=2)
						dict.add(sb.toString());
				}
			}
		}
		
		dict.sort((o1,o2) -> o1.compareTo(o2));
		
		System.out.println(dict.get(0));
		
		
	}

}
