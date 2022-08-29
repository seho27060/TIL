package com.practice.prac1.Domain.DTO;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class MemberStageReqDTO {
    private Long memberId;
    private Long stageId;
}
