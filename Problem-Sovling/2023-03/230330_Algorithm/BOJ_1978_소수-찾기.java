import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 230330 1978 소수 찾기
public class Ex1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int answer = 0;
        while (st.hasMoreTokens()){
            int number = Integer.parseInt(st.nextToken());
            boolean check = true;

            for(int div = 2;div < (int)Math.sqrt(number)+1;div ++){
                if(number % div == 0){
                    check = false;
                    break;
                }
            }
            if(check && number > 1){
                answer ++;
            }
        }

        System.out.println(answer);
    }
}
