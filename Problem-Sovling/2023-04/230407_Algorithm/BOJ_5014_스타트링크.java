import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230407 5014
public class Ex1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int f, s, g, u, d;
        f = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        g = Integer.parseInt(st.nextToken());
        u = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        int[] stairs = new int[f+1];
        Arrays.fill(stairs, -1);
        Deque<Integer> deque = new ArrayDeque<>();

        stairs[s] = 0;
        deque.add(s);

        int now;
        int nxt;
        while(!deque.isEmpty()){
            now = deque.poll();

            nxt = now + u;
            if(nxt <= f && nxt != 0){
                if(stairs[nxt] == -1 || stairs[nxt] > stairs[now] + 1){
                    stairs[nxt] = stairs[now] + 1;
                    deque.add(nxt);
                }
            }

            nxt = now - d;
            if(1 <= nxt){
                if(stairs[nxt] == -1 || stairs[nxt] > stairs[now] + 1){
                    stairs[nxt] = stairs[now] + 1;
                    deque.add(nxt);
                }
            }
        }

        String answer;
        if(stairs[g] == -1){
            answer = "use the stairs";
        }else {
            answer = String.valueOf(stairs[g]);
        }

        System.out.println(answer);
    }
}

