package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.MemberStageReqDTO;
import com.practice.prac1.Domain.DTO.MemberStageResDTO;
import com.practice.prac1.Domain.Member;
import com.practice.prac1.Domain.MemberStage;
import com.practice.prac1.Domain.Stage;
import com.practice.prac1.Repository.MemberRepository;
import com.practice.prac1.Repository.MemberStageRepository;
import com.practice.prac1.Repository.StageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
public class MemberStageServiceImpl implements MemberStageService{
    private final MemberStageRepository memberStageRepository;
    private final MemberRepository memberRepository;
    private final StageRepository stageRepository;

    @Override
    public MemberStageResDTO joinStage(MemberStageReqDTO memberStageReqDTO) {
        Optional<Member> member = memberRepository.findById(memberStageReqDTO.getMemberId());
        Optional<Stage> stage = stageRepository.findById(memberStageReqDTO.getStageId());
        Optional<MemberStage> checkMemberStage= memberStageRepository.findByMember_idAndStage_id(memberStageReqDTO.getMemberId(),memberStageReqDTO.getStageId());

        if(checkMemberStage.isEmpty()) {
            MemberStage memberStage = MemberStage.builder()
                    .stage(stage.get())
                    .member(member.get())
                    .state(0L)
                    .build();
            memberStageRepository.save(memberStage);
            return new MemberStageResDTO(memberStage, 0L);
        }
        return null;
    }

    @Override
    public MemberStageResDTO comepleteStage(MemberStageReqDTO memberStageReqDTO) {
        Optional<Member> member = memberRepository.findById(memberStageReqDTO.getMemberId());
        Optional<Stage> stage = stageRepository.findById(memberStageReqDTO.getStageId());
        Optional<MemberStage> memberStage = memberStageRepository.findByMember_idAndStage_id(memberStageReqDTO.getMemberId(),memberStageReqDTO.getStageId());
        // 원래는..상태도 보고 분기처리해줘야..하나?
        if(memberStage.isPresent()){
            MemberStage innerMemberStage = memberStage.get();
            innerMemberStage.updateMemberStage(1L);
            return new MemberStageResDTO(innerMemberStage, 1L);
        }
        return null;
    }

    @Override
    public Long deleteMemberStage(MemberStageReqDTO memberStageReqDTO) {
        Optional<MemberStage> memberStage = memberStageRepository.findByMember_idAndStage_id(memberStageReqDTO.getMemberId(),memberStageReqDTO.getStageId());
        if(memberStage.isPresent()){
            Long index = memberStage.get().getId();
            memberStageRepository.deleteById(index);
            return index;
        }
        return null;
    }

    @Override
    public MemberStageResDTO readMemberStage(Long memberId, Long stageId) {
        Optional<MemberStage> memberStage = memberStageRepository.findByMember_idAndStage_id(memberId,stageId);
//        System.out.println(memberId, stageId);
        if (memberStage.isPresent()){
            MemberStage innerMemberStage = memberStage.get();
            MemberStageResDTO memberStageResDTO = new MemberStageResDTO(innerMemberStage);
            System.out.println(memberStageResDTO);
            return memberStageResDTO;
        }
        return null;
    }
}
