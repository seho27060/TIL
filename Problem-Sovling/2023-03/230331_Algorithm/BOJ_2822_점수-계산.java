import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

// 230330 11557 Yangjojang of The Year
// ㅋㅋㅋㅋ 반복문 범위를 잘 설정하자 ^^...
public class Ex2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int tc = Integer.parseInt(st.nextToken());
        for(int tcNum = 0; tcNum < tc;tcNum++){
            int n = Integer.parseInt(br.readLine());
            String result = "";
            int maxValue = -1;

            for(int idx = 0;idx < n; idx++){
                String[] input = br.readLine().split(" ");
                String univ = input[0];
                int value = Integer.parseInt(input[1]);
                if(maxValue <= value){
                    result = univ;
                    maxValue = value;
                }
            }
            System.out.println(result);
        }
    }
}
