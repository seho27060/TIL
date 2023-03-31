import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 230331 10773

public class Ex1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine());

        ArrayList<Integer> numbers = new ArrayList<>();

        for(int idx = 0; idx < k; idx++){
            int num = Integer.parseInt(br.readLine());
            if(num == 0){
                numbers.remove(numbers.size()-1);
            } else{
                numbers.add(num);
            }
        }

        System.out.println(numbers.stream().mapToInt(o -> o).sum());
    }
}
