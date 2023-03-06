- [Flow of Controller in Spring MVC](#flow-of-controller-in-spring-mvc)
  - [Flow of Controller in Spring MVC](#flow-of-controller-in-spring-mvc-1)
      - [Controller](#controller)
      - [Service](#service)
        - [ServiceImpl](#serviceimpl)
      - [Domain](#domain)
        - [Domain-DTO](#domain-dto)
      - [Repository](#repository)
---
# Flow of Controller in Spring MVC

## Flow of Controller in Spring MVC

- `Spring MVC pattern`에서의 `Controller` 영역의 작동 과정과 관련 어노테이션의 역할을 알아보자.

#### Controller

- `Dispatch Servlet` 을 통한 `URL` 요청을 실질적으로 처리하는 영역
  
  - 백엔드 컨트롤러(Backend Controller)라고 한다.

- `Controller`에서는 url을 분석하여 매칭되는 `Service`를 호출한다.

```java
// src/main/java/come/ssafy/project/Controller/ChallengeController.java
@RestController
@RequestMapping("/challenge")
@RequiredArgsConstructor 
public class ChallengeController 

    private final SomeService someService;

    @PostMapping("/save")
    public void saveChallenge(@RequestBody CRDTO challenge){
        someService.saveChallenge(challenge);

    }
}
```

#### Service

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

##### ServiceImpl

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

#### Domain

- 실제 DB테이블과 매핑되는 `Entity`클래스를 생성한다.

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

- 사용하려는 `Entity`를 정의하고, `@Builder`를 통해 build패턴을 부여한다. 이를 통해 객체 생성 시점에 값을 할당할 수 있다.
- `@Setter`를 여러 Domain에서 사용하면 일관성을 보장하게 못하게 되므로, `@Builder`어노테이션을 애용하도록 하자. 

##### Domain-DTO

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

- DB에 접근하여 데이터에 대한 CRUD를 실행 가능한 Layer이다. 필요한 기능을 쿼리 메서드 규칙에 따라 작성하거나, 커스터마이징한 쿼리 메서드를 등록할수도 있다.

---

- 레퍼런스

> https://velog.io/@h220101/SpringBoot-%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-spring-MVC-%ED%8C%A8%ED%84%B4-%EB%8F%99%EC%9E%91
> 
> [Spring MVC Framework | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/web-knowledge/spring-knowledge/Spring%20MVC.html)
