import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 230328 2163 초콜릿 자르기
public class Ex2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int a;
        int b;

        if( n >= m){
            a = n;
            b = m;
        } else{
            a = m;
            b = n;
        }

        System.out.println((a-1)+a*(b-1));
    }
}
