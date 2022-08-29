package com.practice.prac1.Controller;

import com.practice.prac1.Domain.DTO.MemberResDTO;
import com.practice.prac1.Domain.DTO.MemberStageReqDTO;
import com.practice.prac1.Domain.DTO.MemberStageResDTO;
import com.practice.prac1.Repository.MemberStageRepository;
import com.practice.prac1.Service.MemberStageService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/memberstage")
@RequiredArgsConstructor
public class MemberStageController {
    private final MemberStageService memberStageService;

    private final Logger logger = LoggerFactory.getLogger(MemberStageController.class);

    @PostMapping("/join")
    public void joinStage(@RequestBody MemberStageReqDTO memberStageReqDTO){ memberStageService.joinStage(memberStageReqDTO);}

    @PutMapping("/complete")
    public MemberStageResDTO completeStage(@RequestBody MemberStageReqDTO memberStageReqDTO){ return memberStageService.comepleteStage(memberStageReqDTO);}

    @DeleteMapping("/delete") // deleteMapping 알아보기
    public Long deleteMemberStage(@RequestBody MemberStageReqDTO memberStageReqDTO){ return memberStageService.deleteMemberStage(memberStageReqDTO);}

    @GetMapping("/read/{memberId}/{stageId}")
    public MemberStageResDTO readMemberStage(@PathVariable("memberId") Long memberId, @PathVariable("stageId") Long stageId){
//        logger.debug("---------------------------");
//        System.out.println("여보세요");
        return memberStageService.readMemberStage(memberId,stageId);
    }
}
