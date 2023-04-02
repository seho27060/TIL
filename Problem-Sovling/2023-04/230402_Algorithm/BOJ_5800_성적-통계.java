import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//        230402 5800
public class Ex3 {
    public static void main(String[] args) throws IOException {



        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int num = 0; num < n; num ++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());

            int[] scores = new int[k];
            int idx = 0;
            while(st.hasMoreTokens()){
                scores[idx] = Integer.parseInt(st.nextToken());
                idx ++;
            }
            scores = Arrays.stream(scores).sorted().toArray();
            int gap = 0;
            for(int i=0;i < k-1;i++){
                if(gap < Math.abs((scores[i] - scores[i+1]))){
                    gap = Math.abs((scores[i] - scores[i+1]));
                }
            }
            System.out.printf("Class %d \n", num+1);
            System.out.printf("Max %d, Min %d, Largest gap %d \n", Arrays.stream(scores).max().getAsInt(), Arrays.stream(scores).min().getAsInt(),gap);
        }

    }
}
