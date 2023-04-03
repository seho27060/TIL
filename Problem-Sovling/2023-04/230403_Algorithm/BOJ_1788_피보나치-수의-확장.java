import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230403 1788
public class Ex2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        ArrayList<Long> memo = new ArrayList<>();
        memo.add(0L);
        memo.add(1L);

        if(Math.abs(n) >= 2){
            for(int number = 2; number <= Math.abs(n); number++){
                memo.add((memo.get(number - 1) + memo.get(number - 2))%1000000000L);
            }
        }

        long result = 1;
        long answer = memo.get(Math.abs(n));
        if (n < 0 && Math.abs(n) % 2 ==0) {
            result = -1;
        } else if(n == 0){
            result = 0;
        }
        System.out.printf("%d \n%d",result,answer);
    }
}
