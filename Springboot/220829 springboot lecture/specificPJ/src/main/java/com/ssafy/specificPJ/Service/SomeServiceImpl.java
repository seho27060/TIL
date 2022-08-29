package com.ssafy.specificPJ.Service;

import com.ssafy.specificPJ.Domain.Challenge;
import com.ssafy.specificPJ.Domain.DTO.CRDTO;
import com.ssafy.specificPJ.Domain.DTO.ChallengeResponseDTO;
import com.ssafy.specificPJ.Domain.DTO.MemberResponseDTO;
import com.ssafy.specificPJ.Domain.DTO.PageCDTO;
import com.ssafy.specificPJ.Domain.Member;
import com.ssafy.specificPJ.Repository.ChallengeRepository;
import com.ssafy.specificPJ.Repository.MemberRepository;
import com.ssafy.specificPJ.Repository.TempRepo;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;

// 스프링이 클래스를 싱글톤으로 관리하도록 등록
@Service
@RequiredArgsConstructor
public class SomeServiceImpl implements SomeService{

    private final Logger logger = LoggerFactory.getLogger(SomeServiceImpl.class);
    private final TempRepo tempRepo;
    private final ChallengeRepository challengeRepository;
    private final MemberRepository memberRepository;

    @Override
    public void saveChallenge(CRDTO crdto){
        // 1. CRDTO -> Challenge 변환 작업
        // 2. 레포지토리에서 디비에 저장
        Member member = memberRepository.getById(crdto.getMember_id());

        // build 패턴, 명시하지 않은 컬럼은 기본값으로 할당됨
        Challenge challenge = Challenge.builder()
                .name(crdto.getName())
                .content(crdto.getContent())
                .level(crdto.getLevel())
                .member(member)
                .build();
        logger.debug("지금 레포 어너를 한번 테스트중입낟.");
        logger.warn("지금 레포 어너를 한번 테스트중입낟.");
        logger.info("지금 레포 어너를 한번 테스트중입낟.");
        logger.error("지금 레포 어너를 한번 테스트중입낟.");

        tempRepo.add(challenge.getName(), 1L);
        challengeRepository.save(challenge);

    }
    @Override
    public void getChallenge() {
    }

    @Override
    @Transactional
    public List<ChallengeResponseDTO> findByName(String name){
        List<Challenge> challengeList = challengeRepository.findByName(name);
        List<ChallengeResponseDTO> challengeResponseDTOList = new ArrayList<>();

        for(Challenge challenge : challengeList){
            Member member = challenge.getMember();
            MemberResponseDTO memberResponseDTO = MemberResponseDTO.builder()
                    .age(member.getAge())
                    .name(member.getName())
                    .id(member.getId())
                    .description(member.getDescription())
                    .build();

            ChallengeResponseDTO challengeResponseDTO = ChallengeResponseDTO.builder()
                    .id(challenge.getId())
                    .content(challenge.getContent())
                    .member(memberResponseDTO)
                    .name(challenge.getName())
                    .level(challenge.getLevel())
                    .build();

            challengeResponseDTOList.add(challengeResponseDTO);
        }

        System.out.println(challengeResponseDTOList);

        return challengeResponseDTOList;
    }
    @Override
    public void deleteChallenge(Long index) {
        challengeRepository.deleteById(index);
//        challengeRepository.
    }

    @Override
    public PageCDTO findAll(Pageable pageable) {
        Page<Challenge> results = challengeRepository.findAll(pageable);
        List<ChallengeResponseDTO> challengeResponseDTOList = new ArrayList<>();

        for(Challenge challenge: results.getContent()){
            Member member = challenge.getMember();
            MemberResponseDTO memberResponseDTO = MemberResponseDTO.builder()
                    .age(member.getAge())
                    .name(member.getName())
                    .id(member.getId())
                    .description(member.getDescription())
                    .build();

            ChallengeResponseDTO challengeResponseDTO = ChallengeResponseDTO.builder()
                    .id(challenge.getId())
                    .content(challenge.getContent())
                    .member(memberResponseDTO)
                    .name(challenge.getName())
                    .level(challenge.getLevel())
                    .build();
            challengeResponseDTOList.add(challengeResponseDTO);
        }

        PageCDTO pageCDTO = PageCDTO.builder()
                .currentPage(results.getNumber())
                .size(results.getSize())
                .hasNext(results.hasNext())
                .totalPages(results.getTotalPages())
                .challengeResponseDTOList(challengeResponseDTOList)
                .build();

        return pageCDTO;
    }
}
