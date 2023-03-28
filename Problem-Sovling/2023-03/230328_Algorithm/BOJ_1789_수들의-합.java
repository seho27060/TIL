import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Ex3 {
    public static void main(String[] args) throws IOException {
//        230328 2163 초콜릿 자르기
//        서로 "다른" n개 자연수의 합이 s, 자연수 n의 최댓값은?

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long s = Long.parseLong(st.nextToken());
        long sum = 0;
        long cnt = 0;

        for(long num = 1;num<=s;num++){
            sum += num;
            cnt += 1;
            if(sum > s){
                cnt -= 1;
                break;
            }else if(sum == s){
                break;
            }
        }
        System.out.println(cnt);
    }
}
