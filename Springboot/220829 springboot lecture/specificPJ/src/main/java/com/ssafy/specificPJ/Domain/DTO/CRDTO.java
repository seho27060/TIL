package com.ssafy.specificPJ.Domain.DTO;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;

// 캡슐화 - 정보의 은닉 -> private
// 그럼 private에 접근할때는? ->
// private를 설정할때는?

// @Data 로 모든 어노테이션 적용이가능하나
// 예상치못한 작동을 방지하기위해, 필요한 어노테이션만 사용하낟.

// @AllArgsConstructor : 모든 인자의 생성자를 생성
// @NoArgsConstructor : AllArgsContructor로 빈 생성자가 생성이 안되므로 생성해줌
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class CRDTO {
    private String name;
    private int level;
    private String content;
    private Long member_id;
}


