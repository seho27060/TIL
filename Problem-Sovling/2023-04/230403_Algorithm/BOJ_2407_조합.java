import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

//        230403 2407
public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        BigInteger ans = new BigInteger("1");
        BigInteger wer = new BigInteger("1");
        int limit = m;
        for(int j = 1; j <= limit; j ++){
            ans = ans.multiply(new BigInteger(Integer.toString(n)));
            wer = wer.multiply(new BigInteger(Integer.toString(m)));
            n -= 1;
            m -= 1;
        }
        System.out.println(ans.divide(wer));
    }
}
