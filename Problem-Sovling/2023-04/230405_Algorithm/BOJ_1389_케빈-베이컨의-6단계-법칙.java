import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230404 1389
public class Ex2 {
    static int n;
    static int m;
    static ArrayList<Integer>[] board;

    static int bfs(int start){
        int result = 0;

        Deque<Integer> deque = new ArrayDeque<>();
        int[] check = new int[n];
        Arrays.fill(check,-1);
        check[start] = 0;
        int now;
        deque.push(start);
        while (!deque.isEmpty()){
            now = deque.poll();
            for(int nxt: board[now]){
                if(check[nxt] == -1 || check[nxt] >= check[now] + 1){
                    deque.push(nxt);
                    check[nxt] = check[now]+1;
                }
            }
        }
        for(int res:check){
            result += res;
        }
        return result;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new ArrayList[n];
        for(int row = 0; row < n; row++){
            board[row] = new ArrayList<>();
        }

        int s,e;
        for(int idx = 0; idx < m; idx++){
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            board[s-1].add(e-1);
            board[e-1].add(s-1);
        }

        int kevinBacon = Integer.MAX_VALUE;
        int answer = -1;
        int result;
        for(int start = 0; start < n; start ++){
            result = bfs(start);
            if(kevinBacon > result){
                kevinBacon = result;
                answer = start;
            }
        }
        System.out.println(answer+1);
    }
}
