package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.MemberStageReqDTO;
import com.practice.prac1.Domain.DTO.MemberStageResDTO;

public interface MemberStageService {

    MemberStageResDTO joinStage(MemberStageReqDTO memberStageReqDTO);


    MemberStageResDTO comepleteStage(MemberStageReqDTO memberStageReqDTO);

    Long deleteMemberStage(MemberStageReqDTO memberStageReqDTO);

    MemberStageResDTO readMemberStage(Long memberId, Long stageId);
}
