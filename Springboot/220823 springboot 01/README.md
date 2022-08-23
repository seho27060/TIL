# springboot_01

## Controller - Service

### Controller

- Dispatch Servlet 을 통해 url을 요청받고, Controller에 전달

- Controlloer에서는 url을 분석하여 매칭되는 서비스 호출

```java
// src/main/java/come/ssafy/project/Controller/ChallengeController.java
@RestController
@RequestMapping("/challenge") //
@RequiredArgsConstructor // 필수 args 생성자 : final(상수)인 멤버변수의 생성자
// final 은 생성자에서 처리해줘야함
public class ChallengeController 

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

    @GetMapping("/save")
    public void saveChallenge(){

    }
}
```

- 어노테이션
  
  - RestController = Controller + ResponseBody : Json 형태로 객체 데이터를 반환함
  
  - RequiredArgsConstructor : 필수 args 생성자, final(상수)인 멤버변수의 생성자역할
  
  - GetMapping("url") : `GET` method이면서 해당 url인 요청을 처리
  
  - PostMapping("url") : `Post` method이면서 해당 url인 요청을 처리

```java
    @PostMapping("/save")
    public void saveChallenge(@RequestBody CRDTO challenge){
        someService.saveChallenge(challenge); // 정의한 someService에서 saveChallenge 호
    }
```

- someService라는 `Service`인터페이스에 선언한 `saveChallenge`메서드를 호출한다.

### Service

- Interface 형식의 `Service` 선언

```java
// src/main/java/com/ssafy/project/Service/SomeService
package com.ssafy.specificPJ.Service;

import com.ssafy.specificPJ.Domain.DTO.CRDTO; // 데이터 전달을 위해 정의한 DTO 가져오

public interface SomeService {

    public void saveChallenge(CRDTO crdto); // 매개변수로 정의한 DTO 대입
    public void getChallenge();
    public void deleteChallenge();

}
```

- Interface를 구현하기 위해 `SomeServiceImpl` 생성

#### Domain

- `Entity`클래스를 생성한다.

```java
@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder // build 패턴.
public class Challenge {

    @Id // primary key
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 생성 값에 대한 strategy 할당, 데이터가 생성될 수록 index 증가
    private Long id;

    private String name;

    private int level;

    private String content;

}
```

- 사용하려는 `Entity`를 정의하고, @Builder를 통해 build패턴을 부여한다.

- #### Domain-DTO

```java
// src/main/java/com/ssafy/project/Domain/DTO/CRDTO

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class CRDTO {
    private String name;
    private int level;
    private String content;
}
```

- 전달할 `Challenge`객체의 정보를 DTO로 선언한다.
- Lombok 어노테이션
  - Getter : 클래스에 접근 할수 있는 `getter`메서드 제공
  - AllArgsConstructor : 모든 인자의 생성자를 생성
  - NoArgsConstructor : 기본 빈 생성자 생성

#### ServiceImpl

- Interface인 Service의 구현

```java
// src/main/java/com/ssafy/project/Service/SomeServiceImpl

@Service
@RequiredArgsConstructor
public class SomeServiceImpl implements SomeService{

    private final ChallengeRepository challengeRepository; // 레포지터리를 상수로 
    @Override
    public void saveChallenge(CRDTO crdto){
        // 1. CRDTO -> Challenge 변환 작업
        // 2. 레포지토리에서 디비에 저장

        // build 패턴, 명시하지 않은 컬럼은 기본값으로 할당됨
        Challenge challenge = Challenge.builder()
                .name(crdto.getName())
                .content(crdto.getContent())
                .level(crdto.getLevel())
                .build();
        challengeRepository.save(challenge);
    }
```

- final(상수)로 불러와진 레포지터리는 @RequiredArgsConstructor의 생성자에 포함된다.
- @Override를 통해 Interface에서 선언된 `saveChallenge`메서드의 실행을 구현한다.
- "build" 패턴을 통해 데이터가 저장된다.

#### Repository

```java
public interface ChallengeRepository extends JpaRepository<Challenge, Long> {
    // 엔티티 클래스를 디비의 테이블로 바꾸는 작업을 유저들이 알아야하는가?
    // 그럴 필요 없으니, 인터페이스 생성하면 CRUD 관련 메서드는 spring에서 자동 생성해줌
    //

    Challenge findById(int id);
}
```

- `JpaRepository`를 상속받는 레포지터리 Interface를 생성하면 spring에서 자동으로 생성해준다.

- 또한 정해진 키워드(`findById`와 같은)를 통해 매개변수와 반환타입에 적합한 기능을 수행할 수 있다.

# 
