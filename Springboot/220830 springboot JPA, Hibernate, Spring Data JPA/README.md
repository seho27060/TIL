# Springboot_06

## JPA, Hibernate, Spring Data JPA

- JPA(Java Persistence API) : 자바 어플리케이션에서 관계형 데이터베이스를 사용하는 방식을 **정의한 인터페이스**. 특정기능을 하는 라이브러리가 아닌 **인터페이스**이다.
  
  - `javax.persistence.EntityManager`...와 같은 인터페이스

- Hibernate : JPA라는 명세(인터페이스)의 구현체. JPA와 Hibernate는 마치 자바의 interface와 해당 interface를 구현한 class와 같은 관계이다. 

![jpa_hibernate_relationship.png](Springboot/220830 springboot JPA, Hibernate, Spring Data JPA/images/jpa_hibernate_relationship.png)

-  위 사진은 JPA와 Hibernate의 상속 및 구현 관계를 나타낸 것이다. JPA의 핵심인 `EntityManagerFactory`, `EntityManager`, `EntityTransaction`을 Hibernate에서는 각각 `SessionFactory`, `Session`, `Transaction`으로 상속받고 각각 `Impl`로 구현하고 있음을 확인할 수 있다.

#### Spring Data JPA

- 그럼 Spring Data JPA는 뭘까?.. 계속 써오던 `@Repository`는 뭐였나?..

- **Spring Data JPA**는 JPA를 쓰기 편하게 만들어놓은 모듈이다.
  
  - `Repository`라는 한 단계 더 추상화된 인터페이스/ 추상화된 규칙에 따라 메서드를 입력하면 Spring이 알아서 메서드 이름에 적합한 쿼리를 날리는 구현체를 만들어 Bean으로 등록한다.

- Spring Data JPA의 `@Repository`의 구현에는 JPA를 사용하고 있다. `@Repository`의 기본 구현체인 `SimpleJpaRepository`를 살펴보면, 내부적으로 JPA의 `@EntityManager`를 사용하는 것을 확인할 수 있다.

### 데이터베이스 초기화

- 스프링부트에서 스프링 데이터 JPA를 사용할때, 데이터베이스의 스키마를 초기화한다.

- 아무런 설정을 하지 않을 시, 스프링은 스키마를 생성하는 쿼리를 수행하지 않는다.

- 설정파일에서 작성하여 초기화 방법을 선택할 수 있다.`

- `application.yml`상에서 할당해보자.

```yml
spring:
  datasource:
    url: jdbc:h2:~/test
    username: sa
    password:
    driver-class-name: org.h2.Driver

  jpa:
    hibernate:
      ddl-auto: none // ddl-auto 옵션, 데이터베이스 초기화 방
    properties:
      hibernate:
        show_sql: true
        format_sql: true
  h2:
    console:
      enabled: true

logging.level:
  org.hibernate.SQL: debug
```

- 위 예시에서 `jpa: hibernate: ddl-auto: 옵션`을 살펴보자

- 할당 옵션(Hibernate 전략)은 아래와 같다.
  
  - `update`: 기존의 스키마를 유지하며 JPA에 의해 변경된 부분만 추가한다.
  
  - `valiadate` : 엔티티와 테이블이 정상적으로 매핑되어있는지만 검증한다.
  
  - `create`: 기존에 존재하는 스키마를 삭제하고 새로 생성한다.
  
  - `create-drop` : 스키마를 생성하고, 애플리케이션이 종료될 때, 삭제한다.
  
  - `none` : 초기화 동작을 하지 않는다.

- 기존에는 `create`옵션이 할당되어, 수정사항에 대한 빌드를 다시 할때마다, H2 데이터베이스가 초기화되었다. 이 때문에 빌드할때마다 새로운 데이터값을 할당해줘야 해서 귀찮았다.

- `none`으로 값을 바꿔주니, 기존의 데이턱 살아있음이 확인되었다.

## Controller에서 데이터를 받는법.

```java
@RestController
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

    @PostMapping("/save")
    public void saveMember(@RequestBody MemberReqDTO member){
        memberService.saveMember(member);
    }

    @PutMapping("/update/{index}")
    public void updateMember(@PathVariable("index") Long index, @RequestBody MemberReqDTO updatedInput){ memberService.updateMember(index,updatedInput); }

    @DeleteMapping("/delete/{index}")
    public void deleteMember(@PathVariable("index") Long index){memberService.deleteMember(index);}

    @GetMapping("/read/{index}")
    public MemberResDTO readMember(@PathVariable("index") Long index){
        return memberService.readMember(index);
    }
}
```

- 위 코드를 토대로 살펴보자

#### @RequestMapping

- `@GetMapping`와 같은 메서드에 따른 메서드매핑 어노테이션이 나오기전에 메서드 방식과 url경로를 입력하여 사용하는 어노테이션..이였지만 이제는 위와같이 통틀어서 사용한다.

- 하위 클래스로 컨트롤러에 메서드를 할당할때는 메서드에 따라 다른 어노테이션을 할당한다.

#### @RequestParam, @PathVariable

- GET, DELETE 요청에 따른 매핑인 `@GetMapping`, `@DeleteMapping`을 사용할때 변수를 받는 어노테이션

##### @RequestParam

```java
@GetMapping("/read")
    public MemberResDTO readMember(@RequestParam(value="index", required = false) Long index){
        return memberService.readMember(index);
    }
```

##### @PathVariable

```java
 @GetMapping("/read/{index}")
    public MemberResDTO readMember(@PathVariable("index") Long index){
        return memberService.readMember(index);
    }
```

- 위와 같이 **`@GetMapping`과 `@DeleteMapping`** 어노테이션에 사용한다.
- GET과 DELETE http 메서드에 대해서는 url로 변수값을 받아 사용함에 유의하자.

#### @RequestBody

```java
    @PostMapping("/save")
    public void saveMember(@RequestBody MemberReqDTO member){
        memberService.saveMember(member);
    }

    @PutMapping("/update/{index}")
    public void updateMember(@PathVariable("index") Long index, @RequestBody MemberReqDTO updatedInput){ memberService.updateMember(index,updatedInput); }
```

- 위와 같이 `PostMapping`과 `PutMapping`처럼 요청 바디가 필요할때 사용된다.
- `@PathVariable`로 데이터를 동시에 받는것도 가능하다.
