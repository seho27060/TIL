import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//        230406 1931
public class Ex3 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int s, e;
        ArrayList<int[]> rooms = new ArrayList<>();
        for(int idx=0;idx <n; idx++){
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            int[] room = {s,e};
            rooms.add(room);
        }

        rooms.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] != o2[1] ? o1[1] - o2[1] : o1[0] - o2[0];
            }
        });

        int result = -1;
        int answer = 0;

        for(int[] room:rooms){
            if(result == -1){
                result = room[1];
                answer ++;
            } else if(result <= room[0]){
                result = room[1];
                answer ++;
            }
        }
        System.out.println(answer);
    }
}
