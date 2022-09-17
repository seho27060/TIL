- [Springboot_03](#springboot_03)
  - [연관관계](#연관관계)
    - [JPA 영속성 전이(CASCADE)](#jpa-영속성-전이cascade)
      - [Entity의 상태](#entity의-상태)
      - [CascadeType](#cascadetype)
    - [Wrapper class](#wrapper-class)
    - [Generic](#generic)
    - [NullPointerException(NPE)](#nullpointerexceptionnpe)
      - [Optional](#optional)
    - [더티체킹(Dirty Checking)](#더티체킹dirty-checking)
# Springboot_03

## 연관관계

- 연관관계의 테이블에서 특정 엔티티가 삭제되면 그에 연관된 다른 테이블의 엔티티는 어떻게 처리해야 할까? 삭제?/ 그대로 두기?

### JPA 영속성 전이(CASCADE)

- 영속성전이(CASCADE) : 부모 엔티티가 영속화될 때, 자식 엔티티도 같이 영속화되고/ 부모 엔티티가 삭제될 때 자식 엔티티도 삭제된다. 특정 엔티티를 영속 상태로 만들 때 연관된 엔티티도 함께 영속 상태로 전이되는 것을 의미한다.

#### Entity의 상태

1. `Transient`: 객체를 생성하고, 값을 주어도 JPA나 hibernate가 그 객체에 관해 아무것도 모르는 상태. 즉, 데이터베이스와 매핑된 것이 아무것도 없다.  
2. `Persistent`: 저장을 하고나서, JPA가 아는 상태(관리하는 상태)가 된다. 그러나 .save()를 했다고 해서, 이 순간 바로 DB에 이 객체에 대한 데이터가 들어가는 것은 아니다. JPA가 persistent 상태로 관리하고 있다가, 후에 데이터를 저장한다.(1차 캐시, Dirty Checking(변경사항 감지), Write Behind(최대한 늦게, 필요한 시점에 DB에 적용) 등의 기능을 제공한다)  
3. `Detached`: JPA가 더이상 관리하지 않는 상태. JPA가 제공해주는 기능들을 사용하고 싶다면, 다시 persistent 상태로 돌아가야한다.  
4. `Removed`: JPA가 관리하는 상태이긴 하지만, 실제 commit이 일어날 때, 삭제가 일어난다.

#### CascadeType

- 영속성 전이와 같은 엔티티간의 의존성을 설정하기 위해 jpa에서 제공하는 타입

- 연관관계를 명시하는 `@OneToMany`나 `@ManyToOne` 어노테이션에 옵션으로 줄 수 있다.
  
  ```java
  @Entity
  @Getter
  @NoArgsConstructor
  @AllArgsConstructor
  @Builder
  public class Member {
  
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
  
      private String name;
  
      private int age;
  
      private String description;
  
      @OneToMany(mappedBy = "member", cascade =CascadeType.REMOVE) // CascadeType 부
      private List<Challenge> challengeList;
  
      public void updateMember(MRDTO member){
          this.age = member.getAge();
          this.description = member.getDescription();
          this.name = member.getName();
      }
  }
  ```

- 위 예시에서는 일대다 관계인 `Member`와 `Challenge`에서 `Member`엔티티가 삭제되면 연관관계에 있는 `Challenge`도 삭제된다.

- 다양한 operation 들

- `CascadeType.ALL` : 모든 Cascade를 적용한다

- `CascadeType.PERSIST`: 엔티티를 영속화할 때, 연관된 엔티티도 함께 유지한다

- `CascadeType.MERGE`: 엔티티 상태를 병합(Merge)할 때, 연관된 엔티티도 모두 병합

- `CascadeType.REMOVE`:엔티티를 제거할 때, 연관된 엔티티도 모두 제거한다.

- `CascadeType.DETACH`: 부모 엔티티를 detach() 수행하면, 연관 엔티티도 detach된다.

- `CascadeType.REFRESH`: 상위 엔티티를 새로고침할때, 연관된 엔티티도 모두 새로고침한다.

### 쿼리 메서드

- 해당 레포지터리에 연관된 엔티티에 대한 sql 작업 가능

- 키워드를 자동으로 변환하여 sql을 할당한다.

- 그럼 다른 테이블간에 조인을 할때면?

#### @Query 사용

- `@Query(value = "sql 문작성, nativeQuery = true)`와 같은 구문으로 의도하는 기능을 하는 sql문을 작성하여 할당한다.

#### 페이지네이션

```java
Page<Challenge> findAll(Pageable pageable);
```

- 총 데이터의 개수, 다음 페이지 여부, 현재 페이지의 인덱스, 사이즈, 실행결과 갯수

### Wrapper class

- Wrapper 클래스(Long vs long) - 기본형을 객체로 표현할때 사용. 객체 주소를 갖게 되므로, 메서드(equals, compareTo와 같은걸로) 비교해야함

### Generic

- 데이터타입을 일반화한다. 클래스나 메서드에서 사용할 내부 데이터 타입을 미리 지정함(사용에서 타입의 불확정성을 제거)

- 이를 통해
  
  - 클래스나 메서드 내부에서 사용되는 객체의 타입 안정성을 높일 수 있다.
  
  - 반환값에 대한 타입 변환 및 타입 검사에 들어가는 노력을 줄일 수 있다.

- 제너릭의 선언 및 생성

```java
class MyArray<T>{
    T element;
    void setElement(T element){ this.element = element;}
    T getElement() {
    return element;
}
}
```

### NullPointerException(NPE)

- null 때문에 발생하는 Runtime Exception

- 실제 값이 아닌 null을 갖는 객체/변수를 호출할때 발생하는 예외

- null parameter를 넘기지 않거나, null 여부를 비교 처리후 추가하는 방법을 예방 가능하다.

- 그게 아니라면 **Optional**을 사용한다.

#### Optional

- "존재할 수도 있지만, 안 할 수도 있는 객체", "null이 될 수도 있는 객체"를 감싸는 일종의 Wrapper 클래스

- 장점
  
  - NPE를 유발하는 null을 직접 다루지 않아도 된다.
  
  - 수고롭게 null 체크를 안해도 된다.
  
  - 명시적으로 해당 변수가 **null일 수 있다는 가능성**을 표현 가능

```java
// Optional을 안쓰고 NPE를 방지하며 변수 사용하는 경우
Example ex1 = ...;
if (ex1 != null){
    System.out.println(ex1);
}

// Optional을 사용하는 경우
Optional<Example> ex2 = ...;
ex2.ifPresent(System.out::println);
```

### 더티체킹(Dirty Checking)

- 더티 체킹 : Transaction 안에서 엔티티의 변경이 일어나면, **변경 내용을 자동**으로 데이터베이스에 **반영**하는 JPA 특징

- JPA는 엔티티 매니저가 엔티티를 저장/조회/수정/삭제 한다.

- 엔티티 매니저의 메서드에는 저장(persist)/ 조회(find)/ 삭제(delete)로 수정에 해당하는 메서드는 없다.

- 수정 기능 대신 더티 체킹(dirty checking)을 지원한다.

-  JPA 영속성 컨텍스트

<img title="" src="https://blog.kakaocdn.net/dn/cokEKI/btqygTOISLW/TrI5hAUoR9wiVP92OJlIJ0/img.png" alt="" data-align="left">

- 더티체킹이 일어나는 환경
  
  - 영속 상태(Managed)안에 있는 엔티티인 경우
  
  - **Transaction** 안에서 엔티티를 변경하는 경우

- Transaction을 사용하는 방법
  
  - Service Layer에서 `@Transaction`을 사용하는 경우
  
  ```java
  @Service
  public class ExampleSercvice{
      @Transactional
      public void updateInfo(Logn id, String name){
          User user = userRepository.findById(id);
          user.setName(name);
      }
  }
  ```
  
  - EntityTransacton을 이용해서 트랜잭션을 범위를 지정하고 사용하는 경우
  
  ```java
  @Service
  public class ExampleService {
       public void updateInfo(Long id, String name) {
            EntityManager em = entityManagerFactory.createEntityManager();
            EntityTransaction tx = em.getTransaction();
            // 1. 트랜잭션 시작
            tx.begin();
            // 2.User 엔티티를 조회 & User 스냅샷 생성
            User user = em.find(User.class, id);
            // 3.User 엔티티의 name을 변경
            user.setName(name);
            // 4. 트랜잭션
            // 5.User 스냅샷과 최종 user의 내용을 비교해서 Dirty를 Checking 해서 Update Query 발생
            tx.commit();
       }
  }
  ```

- `@Transactional`을 사용했을때
  
  1. Table : User에서 PK id가 2인 엔티티 객체 조회
  
  2. user의 email을 examUpdate@mail.com으로 수정(**Dirty Checking**)
  
  3. 수정된 이메일 examUpdate@mail.com 을 가진 user엔티티 유무 확인, 2번과정에서 수정되었기에 true 출력

- `@Transactional`을 사용하지 않은 경우, 2번 과정의 더티체킹이 발생하지 않아 디비의 데이터가 수정되지 않는다.
