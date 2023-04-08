import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 230408 1107
public class Ex2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int[] numbers = new int[10];

        int number;
        if(m > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()){
                number = Integer.parseInt(st.nextToken());
                numbers[number] = 1;
            }
        }

        boolean check;
        int cnt;
        int answer = Math.abs(n - 100);
        for(int num = 0; num <= 999999; num++){
            check = true;
            String numString = String.valueOf(num);
            for(int idx=0;idx < numString.length(); idx++){
                if(numbers[Integer.parseInt(numString.substring(idx,idx+1))] == 1){
                    check = false;
                    break;
                }
            }

            if(check){
                cnt = numString.length() + Math.abs(n - num);
                answer = Math.min(answer,cnt);
            }
        }

        System.out.println(answer);
    }
}
