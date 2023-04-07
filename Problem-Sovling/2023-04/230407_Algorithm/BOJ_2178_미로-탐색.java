import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230404 1206
public class Ex1 {
    static int n,m;
    static int[][] board;
    static void bfs(int start){

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for(int row = 0; row < n; row++){
            String input = br.readLine().strip();
            for(int col = 0; col < m; col++){
                board[row][col] = Integer.parseInt(input.substring(col,col+1));
            }
        }

        Deque<int[]> deque = new ArrayDeque<>();
        int[][] check = new int[n][m];
        for(int row = 0; row < n; row ++){
            Arrays.fill(check[row],-1);
        }
        deque.push(new int[] {0,0});
        check[0][0] = 1;
        int[] now;
        int nxtR, nxtC;
        int[] mX = new int[] {0,0,1,-1};
        int[] mY = new int[] {1,-1,0,0};

        while (!deque.isEmpty()){
            now = deque.poll();
            for(int mIdx = 0; mIdx < 4; mIdx ++){
                nxtR = now[0] + mX[mIdx];
                nxtC = now[1] + mY[mIdx];
                if ((0 <= nxtR && nxtR < n) &&(0 <= nxtC && nxtC < m)) {
                    if (board[nxtR][nxtC] == 1){
                        if(check[nxtR][nxtC] == -1 || check[nxtR][nxtC] > check[now[0]][now[1]] + 1){
                            check[nxtR][nxtC] = check[now[0]][now[1]] + 1;
                            deque.push(new int[]{nxtR,nxtC});
                        }
                    }
                }
            }
        }
        int answer = check[n-1][m-1];
        System.out.println(answer);
    }
}

