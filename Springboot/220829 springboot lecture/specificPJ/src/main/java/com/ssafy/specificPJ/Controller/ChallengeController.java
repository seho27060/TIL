package com.ssafy.specificPJ.Controller;

// 컨트롤러는 무엇이
// 장고에서의 MTVV?
// 장고 template == 스프링 view(내장시에 사용, 프론트단이 존재하면 사용할일 X)
// 장고 model = 스프링, 데이터베이스와 관련된 단계 model
// 스프링에서 프론트의 요청을 받아 처리하고, 결과를 반환하는 단계를 controlloer
// 내장시에는 html or jsp(java servlet page : html 코드를 자바로 감싼 문서)
// 프론트에서 요청 -> dispatcher servlet -> 어떤 api인지 확인 -> 해당 controller 로 전송
// url을 보고 어떤 controller로 이동할지 결정한다.
// 특정 controlloer -> 특정 api에 해당하는 함수가 실행됨 -> api

// spring에서는 데이터베이스에 관련 코드들은 모두 repository 또는 model이라는 패키지(폴더)에서 관리하는게 일반적.
// controller : 요청이 어디로 왔고, 무엇을 원하는지, 원하는걸 반환해주면 됨
// service : controller에서 service를 호출, controller의 어떻게를 수행(요청 동작 수행)
// repository : 가장 단순한 도구 모음. db에 접근하는 쿼리 모음
// service가 데이터를 가지고 복잡한 일을 할때, 해당 데이터에 관련된 crud를 담당함.

// 왜 이런식으로 돌아가나 -> 복잡해 보이는 추상화 -> 유지보수, 개발의 용이성
//
// 오늘의 키워드!! : 스프링 mvc 패턴, 싱글톤, 객체지향프로그래밍 !!!
// singleton : 프로그램 내에서 중요한 역할을 하는 객체 = 관리 또는 제어 객체, 웹서버내에 실제일을 담당하는 객체

// CS
// 데드락
// 데이터 D에 대해 사용자 a와 b는 동시간대에 접근할 수 없다.
// 자원에 대한 접근 대원칙 : 동시간대에 단 하나만, 사용되고 있는 자원은 다른 사람은 사용할 수 없다. -> 락이 걸렸다.
// 데드락 : 데이터 접근 권한이 A,B 로 2개로 증가/ A는 B가 나와야 나올수 있고, B또한 그렇다. 동시에 A,B가 사용중이면, 둘다 나올수 있는 방법이 없으므로
// 데드락 발생. 시스템 정지

// 프로그램 - 프로세스
// 프로그램 : 실행가능한 파일의 형태로 저장되어 있는 것
// 프로세스 : 실행중인 프로그램
// 한 프로세스에는 여러개의 작업 흐름이 존재
// 쓰레드 Thread, 병렬처리의 가장 기본이 되는 존재
// cpu cache memory disk

// cpu - 중앙처리
// 프로세스 : 내가 지금 머릿속에 집중하고 있는 것.
// 병렬처리 - 순간을 매우 쪼개서 작동하기때문에 병렬처리되는 것 처럼 보임, 실제로는 순서에 따라 처리됨
// 프로세스 하위 작업 개념 = 쓰레드
// 현재 cpu에서 A프로세스 진행중 하위에 1 thread, 2 thread, 3 thread
// 1 thread 처리하다 2 thread를 처리하는 상황 -> Cpu 안에 있는 context switch

// cache - 단기기억 + 자주 사용하는 데이터
// cpu에서 하던 작업을 cache에 저장한다.
// cpu에서 접근하는데 매우 빠르게 가능하다.

// memory - cache에 비해 비교적 덜 중요한 작업 저장
// disk - 프로그램 저장소

// 객체지향 프로그래밍
// 이전 순차적 비구조적 실행
// 프로그램의 동작 방식이 객체 - 객체 간의 상호작용
// 객체 = 정보와 행위를 갖는것
import com.ssafy.specificPJ.Domain.Challenge;
import com.ssafy.specificPJ.Domain.DTO.CRDTO;
import com.ssafy.specificPJ.Domain.DTO.ChallengeResponseDTO;
import com.ssafy.specificPJ.Domain.DTO.PageCDTO;
import com.ssafy.specificPJ.Service.SomeService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

// 해당 태그/ 어노테이션의 의미 => rest api 전용 컨트롤러 == 요청을 받고. 그에 따른 데이터를 반환한다.
// 위의 내용에 관련된 실제 구현을 어노테이션 하나로 응축함.
// 컨트롤러 : 반환 데이터가 페이지의 이름, html
// responsebody 어노테이션 : 반환 데이터라고 인식을 바꿔줌
// RestController = Controlloer + responseBody


@RestController
@RequestMapping("/challenge") //
@RequiredArgsConstructor // 필수 args 생성자 : final(상수)인 멤버변수의 생성자
// final 은 생성자에서 처리해줘야함
public class ChallengeController {
    // 스프링에서는 클래스들을 싱글톤으로 관리한다.
    // 디스패처서블릿 -> url에 매칭되는 컨트롤러 -> 서비스호출 -> 레포짓토리 호출

    // interface SomeService 상수 선언

    // interface 상속 vs class 상속
    // 클래스 B가 A클래스를 상속 / A클래스의 성질을 물려받음
    // 클래스 B가 인터페이스 C를 상속 / B클래스를 C처럼 사용가능

    // 컴파일언어 : 컴파일 후 실행
    // 문법 언어, semantic error - 컴파일중 발생 , runtime error
    // 소스코드 -> 중간단계코드 -> 살행파일

    // 컴파일러는 참조형 데이터를 어떻게 보는가
    // Parent p = new child();
    // child 만큼의 메모리가 할당되지만, parent를 참조하기때문에 parent의 멤버변수를 사용가능하다.
    // 메서드는 가상 메서드로 실행된다.


    private final SomeService someService; //

    // @MethodnameMapping
    @GetMapping("/info")
    public void someApi() {

    }

    // Post 요청시의 데이터(body)를 클래스의 매개변수로 받는다
    // @RequestBody 어노테이션 사용시, 입력값을 매개변수의 타입으로 매핑시켜준다.
    // 예) 입력값 = { id : 1, content: "--", name :"name",level:3}

    // DTO, Data Transfer object :  데이터 전이 객체
    // VO, value object : 값 객체

    // (디스패처서블릿 ->) 컨트롤러 -> 서비스 (-> 레포짓)
    @PostMapping("/save")
    public void saveChallenge(@RequestBody CRDTO challenge){
        someService.saveChallenge(challenge);
    }

    // @RequestBody - 요청 바디
    // @ResponseBody - 반응 바디
    @GetMapping("/find")
    public ResponseEntity findByName(@RequestParam String name){
        List<ChallengeResponseDTO> challengeList = someService.findByName(name);
        // ResponseEntity - get요청에 따른 반환값 정의
//        ResponseEntity responseEntity = new ResponseEntity(challengeList, HttpStatus.OK);
//        return responseEntity;
        return new ResponseEntity(challengeList, HttpStatus.OK);
    }
    // 요청과 반환에 DTO를 사용하자, 안그러면 jpa에서 오류뒤지게뜸

    @DeleteMapping("/delete/{index}/")
    public void deleteChallenge(@PathVariable Long index){
        // 서비스 호출
        someService.deleteChallenge(index);
    }

    @GetMapping("/test")
    public ResponseEntity test(Pageable pageable){
        PageCDTO challengeResponseDTOPage = someService.findAll(pageable);
        return new ResponseEntity(challengeResponseDTOPage, HttpStatus.OK);
    }
}
