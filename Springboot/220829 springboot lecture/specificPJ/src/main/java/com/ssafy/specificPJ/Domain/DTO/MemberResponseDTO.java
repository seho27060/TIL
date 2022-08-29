package com.ssafy.specificPJ.Domain.DTO;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class MemberResponseDTO {
    private Long id;
    private String description;
    private int age;
    private String name;
//    private List<Cha>
}
