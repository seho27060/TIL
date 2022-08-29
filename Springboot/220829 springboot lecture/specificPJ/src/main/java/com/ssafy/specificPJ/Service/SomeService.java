package com.ssafy.specificPJ.Service;

// 다형성
// 인터페이스 vs 클래스
// 인터페이스 : 사용법 설정
// 클래스 :

// 기본형 참조형
// 기본형 - 데이터의 크기를 **사전**에 알고 있음
// 참조형 - 그렇지 않은것 예) 클래스
// 클래스 형성시, 실행 전에는 어떠한 구성인지 컴퓨터는 알 수 있는 방법이 없음(사전에 알지 못함)
// 해당 클래스에 대한 적절한 메모리를 할당하고, 참조형 변수에 그 메모리의 주소를 할당함.

// 클래스 : 변수와 메서드로 구성됨.
// 클래스의 각 인스턴스마다 다른 변수값을 갖는다/ 메서드는 공유하게됨
// 변수는 각 다른 메모리에 할당/ 메서드는 공통된 메모리에 할당되어 사용됨.


import com.ssafy.specificPJ.Domain.Challenge;
import com.ssafy.specificPJ.Domain.DTO.CRDTO;
import com.ssafy.specificPJ.Domain.DTO.ChallengeResponseDTO;
import com.ssafy.specificPJ.Domain.DTO.PageCDTO;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

public interface SomeService {

    public void saveChallenge(CRDTO crdto);
    public void getChallenge();
    public List<ChallengeResponseDTO> findByName(String name);

    public void deleteChallenge(Long index);

    public PageCDTO findAll(Pageable pageable);

}
