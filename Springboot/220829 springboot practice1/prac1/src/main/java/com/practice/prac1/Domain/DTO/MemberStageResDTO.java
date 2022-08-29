package com.practice.prac1.Domain.DTO;

import com.practice.prac1.Domain.MemberStage;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class MemberStageResDTO {
    private Long memberid;
    private Long stageid;

    private Long state;

    public MemberStageResDTO(MemberStage memberStage, Long state){
        this.memberid = memberStage.getMember().getId();
        this.stageid = memberStage.getStage().getId();
        this.state = state;
    }
    public MemberStageResDTO(MemberStage memberStage){
        this.memberid = memberStage.getMember().getId();
        this.stageid = memberStage.getStage().getId();
        this.state = memberStage.getState();
    }
}
