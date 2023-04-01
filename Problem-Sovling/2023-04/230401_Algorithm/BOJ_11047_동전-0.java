import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230401 11047
public class Ex2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] coins = new int[n];

        for(int idx = 0; idx < n; idx++){
            coins[idx] = Integer.parseInt(br.readLine());
        }

        int answer = 0;
        int result = k;
        for(int i = coins.length-1; i >= 0; i -- ){
            if(result >= coins[i]){
                int cnt = 1;
                while(true){
                    if(result - coins[i]*cnt >= 0){
                        cnt += 1;
                    } else{
                        cnt -= 1;
                        break;
                    }
                }
                result -= coins[i]*cnt;
//                System.out.printf("%d %d %d %d \n",coins[i],result,answer,cnt);
                answer += cnt;
            }
        }

        System.out.println(answer);
    }
}
