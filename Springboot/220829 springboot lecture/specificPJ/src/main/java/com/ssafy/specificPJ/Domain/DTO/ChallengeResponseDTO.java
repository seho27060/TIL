package com.ssafy.specificPJ.Domain.DTO;


import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class ChallengeResponseDTO {
    private Long id;
    private String name;
    private int level;
    private String content;
    private MemberResponseDTO member;
}
