import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Ex1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());

            if(num == -1){
                break;
            } else{
                HashSet<Integer> numSet = new HashSet<>();

                for(int idx = 1; idx < Math.sqrt(num)+1; idx++){
                    if(num % idx == 0){
                        numSet.add(idx);
                        numSet.add(num/idx);
                    }
                }

                int result = numSet.stream().mapToInt(i->i).sum();
                if (result == num*2){
                    System.out.println(num + " = "+numSet.stream().sorted().limit(numSet.size()-1).map(Object::toString).collect(Collectors.joining(" + ")));
                } else{
                    System.out.println(num + " is NOT perfect.");
                }
            }
        }
    }
}
