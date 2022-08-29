package com.ssafy.specificPJ.Service;

import com.ssafy.specificPJ.Domain.DTO.MRDTO;
import com.ssafy.specificPJ.Domain.Member;
import com.ssafy.specificPJ.Repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
public class MemberServiceImpl implements MemberService{
    private final MemberRepository memberRepository;

    @Override
    public void saveMember(MRDTO mrdto) {
        Member member = Member.builder()
                .name(mrdto.getName())
                .age(mrdto.getAge())
                .description(mrdto.getDescription())
                .build();
        memberRepository.save(member);
    }

    @Override
//    @Transactional
    public void updateMember(Long index, MRDTO member) {
        // 반환값이 null일수 있으니 Optional 객체로 참조변수 선언
        Optional<Member> updatedMember = memberRepository.findById(index);
        // .get()을 통해 값을 불러온다(값이 null일수있으니 사전에 방지)
        updatedMember.get().updateMember(member);
    }

}

