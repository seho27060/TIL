import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
// 230403 1003


public class Ex1 {
    static Integer[][] memo = new Integer[41][2];

    static Integer[] fibo(int n){
        if(memo[n][0] == null || memo[n][1] == null){
            memo[n][0] = fibo(n-1)[0] + fibo(n-2)[0];
            memo[n][1] = fibo(n-1)[1] + fibo(n-2)[1];
        }

        return memo[n];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        memo[0][0] = 1;
        memo[0][1] = 0;
        memo[1][0] = 0;
        memo[1][1] = 1;

        int t = Integer.parseInt(br.readLine());
        int n;
        Integer[] answer = new Integer[2];
        for(int tc = 0; tc < t; tc ++){
            n = Integer.parseInt(br.readLine());
            answer = fibo(n);
            System.out.printf("%d %d \n",answer[0], answer[1]);
        }
    }
}
