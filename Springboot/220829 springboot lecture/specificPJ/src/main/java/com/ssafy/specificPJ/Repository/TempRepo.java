package com.ssafy.specificPJ.Repository;

import org.springframework.stereotype.Repository;

import java.util.HashMap;

@Repository
public class TempRepo {
    // Repository -> db와 연관된 작업 실행하는 컴포넌트
    //
    private HashMap<String, Long> repo = new HashMap<>();

    public void add(String str, Long id) {
        System.out.println(str + "    -----------------------------  "+id);
        repo.put(str, id);
        System.out.println(repo.get(str));

    }
    public void delete(String str){
        repo.remove(str);
    }
}
