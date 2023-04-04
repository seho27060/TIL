import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230404 1206
public class Ex1 {

    static int n, m, v;
    static ArrayList<Integer>[] board;
    static int[] check;

    static void dfs(int start){
        Stack<Integer> stack = new Stack<>();
        stack.push(start);
        int now;
        while(!stack.isEmpty()){
            now = stack.pop();
            if(check[now] == 0){
                check[now] = 1;
                System.out.printf("%d ",now+1);
                if(!board[now].isEmpty()){
                    for(int nxt:board[now]){
                        if(check[nxt] == 0){
                            dfs(nxt);
                            stack.add(nxt);
                        }
                    }
                }
            }
        }
    }

    static void bfs(int start){
        Deque<Integer> deque = new ArrayDeque<>();
        deque.push(start);
        int now;

        while (!deque.isEmpty()){
            now = deque.poll();
            if(check[now] == 0){
                check[now] = 1;
                System.out.printf("%d ",now+1);
                if(!board[now].isEmpty()){
                    for(int nxt:board[now]){
                        deque.offer(nxt);
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());
        board = new ArrayList[n];
        for(int idx=0; idx < n; idx++){
            board[idx] = new ArrayList<>();
        }
        int s;
        int e;
        for(int idx = 0; idx < m; idx ++){
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            board[s-1].add(e-1);
            board[e-1].add(s-1);
        }
        for(int idx =0; idx < n; idx++){
            Collections.sort(board[idx]);
        }
        check = new int[n];
        Arrays.fill(check,0);
        dfs(v-1);
        System.out.println();

        Arrays.fill(check,0);
        bfs(v-1);
    }
}

