import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//        230330 5635 생일
//        생일이 주어졌을때, 가장 어린/늙은 사람 출력
class BirthDate implements Comparable<BirthDate>{
    private String name;
    private Calendar calendar;

    public BirthDate(String name, Calendar calendar){
        this.name = name;
        this.calendar = calendar;
    }

    public String getName() {
        return name;
    }

    public Calendar getCalendar() {
        return calendar;
    }

    @Override
    public int compareTo(BirthDate o) {
        return calendar.compareTo(o.getCalendar());
    }
}

public class Ex3 {
    public static void main(String[] args) throws IOException {



        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int n = Integer.parseInt(st.nextToken());
        List<BirthDate> birthList = new ArrayList<>();
        for(int student = 0; student < n; student ++){
            String[] input = br.readLine().split(" ");
            Calendar birth = Calendar.getInstance();
            birth.set(Integer.parseInt(input[3]),Integer.parseInt(input[2]),Integer.parseInt(input[1]));
            birthList.add(new BirthDate(input[0],birth));
        }
        Collections.sort(birthList);
        System.out.println(birthList.get(birthList.size()-1).getName());
        System.out.println(birthList.get(0).getName());
    }
}
