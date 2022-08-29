package com.practice.prac1.Service;


import com.practice.prac1.Domain.DTO.MemberReqDTO;
import com.practice.prac1.Domain.DTO.MemberResDTO;
import com.practice.prac1.Domain.Member;
import com.practice.prac1.Domain.MemberStage;
import com.practice.prac1.Domain.Stage;
import com.practice.prac1.Repository.MemberRepository;
import com.practice.prac1.Repository.MemberStageRepository;
import com.practice.prac1.Repository.StageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.swing.text.html.Option;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
public class MemberServiceImpl implements MemberService{
    private final MemberRepository memberRepository;
    private final MemberStageRepository memberStageRepository;
    private final StageRepository stageRepository;

    @Override
    public void saveMember(MemberReqDTO MemberReqDTO) {
        Member member = Member.builder()
                .name(MemberReqDTO.getName())
                .build();
        memberRepository.save(member);
    }
    @Override
    public void updateMember(Long index, MemberReqDTO updatedInput) {
        Optional<Member> member = memberRepository.findById(index);
        if(member.isPresent()){
            Member innerMember = member.get();
            innerMember.updateMember(updatedInput);
        }
    }
    @Override
    public Long deleteMember(Long index) {
        Optional<Member> member = memberRepository.findById(index);
        Optional<MemberStage> memberStage = memberStageRepository.findByMember_id(index);
        Optional<Stage> stage = stageRepository.findById(memberStage.get().getStage().getId());
        if(member.isPresent()){
            memberRepository.deleteById(index);
            return index;
        }
        return null;
    }

    @Override
    public MemberResDTO readMember(Long index) {
        Optional<Member> member = memberRepository.findById(index);
        if(member.isPresent()){
            Member innerMember = member.get();
            MemberResDTO memberResDTO = MemberResDTO.builder()
                    .id(innerMember.getId())
                    .name(innerMember.getName())
                    .build();
            return memberResDTO;
        }
        return null;
    }
}
