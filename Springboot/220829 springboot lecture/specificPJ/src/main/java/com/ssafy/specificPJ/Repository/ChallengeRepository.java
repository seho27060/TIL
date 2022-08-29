package com.ssafy.specificPJ.Repository;

import com.ssafy.specificPJ.Domain.Challenge;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ChallengeRepository extends JpaRepository<Challenge, Long> {

    List<Challenge> findByName(String name);
    // 찾는값이 없으면  null 반환
    // *null은 size가 없다

    // 컴파일러는 실제 데이터공간이 어떻든 가리키는 대상의 타입으로 본다.
    // 부모클래스가 자식 클래스를 가리키면, 데이터 공간은 자식 클래스임에도 부모 클래스인것처럼 자비는 인식한다.
    // null은 아무것도 가리키지 않음(null pointer)

    // <> 제네릭
    // 엔티티 클래스를 디비의 테이블로 바꾸는 작업을 유저들이 알아야하는가?
    // 그럴 필요 없으니, 인터페이스 생성하면 CRUD 관련 메서드는 spring에서 자동 생성해줌

    // 1.
    List<Challenge> findByNameAndContent(String name, String content);

    // 2.
//    List<Challenge> findByIndex(String index1);
    List<Challenge> findByIdIn(List<Long> ids);
    // 3.
    List<Challenge> readByOrderByIdDesc();

    // 4.
    Integer countByName(String name);

    // 5.
    List<Challenge> findByNameContaining(String search);

    // 페이지네이션
    Page<Challenge> findAll(Pageable pageable);
//    @Query를 통해 sql문을 수정하여 할당가능

    Challenge findById(int id);
    // List<Challenge> findByName(String name);
    // 쿼리문으로 자동변환

}
