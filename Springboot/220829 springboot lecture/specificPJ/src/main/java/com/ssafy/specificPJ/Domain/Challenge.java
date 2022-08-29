package com.ssafy.specificPJ.Domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

// ORM - object relational mapping
// 객체와 디비 테이블을 매핑
// 디비의 challenge 테이블
// 자바의 challenge 클래스
// 자바의 형태의 challenge 클래스를 디비에 적용하면 알아서 쿼리로 변환되어 날아간다.
// 그 역 도 성립 (디비 테이블 -> 자바 클래스, 객체)

// sql을 작성하지 않고는 db 작성불가
// java code 내에서 작성하도록 클래스 - 테이블을 1:1 매핑후, java code -> sql 변환 과정을 자동화하자.
// 이때 매핑되는 클래스를 **Entity**라고 한다.

// Spring DATA JPA

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder // build 패턴.
public class Challenge {

    @Id // primary key
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 생성 값에 대한 strategy 할당, 데이터가 생성될 수록 index 증가
    private Long id;

    private String name;

    private int level;

    private String content;

    // 연관관계
    // 일대일/ 일대다/ 다대일/ 다대다/
    // *다대다 일때는 다 대 일 대 다 로 구성
    // *중개테이블을 만들어준다.

    // 일대다 관계 설정
    // 일대다 에서 다인 엔티티가 외래키를 갖는다.
    // 외래키를 갖는 쪽이 "주인"

    @ManyToOne(fetch = FetchType.LAZY)
    // Challenge 객체를 조회하는데 Member객체까지 오는문제를 위해 설정
    // 순환참조
    // -> 프론트 반환용 DTO를 만들ㅇ자
    @JoinColumn(name = "member_id")
    // member_id라는 이름의 Member객체를 갖는다.
    // 객체 - 객체 간 연관관계를 맺는 방법
    // 디비에서 member의 id를 외래키로 갖게된다.
    private Member member;

    public void updateNameWhenLevelChanged(String name){
        this.name = name;
    }

}
