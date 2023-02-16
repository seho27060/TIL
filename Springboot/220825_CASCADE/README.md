[TOC]

# Springboot_03

## JPA 영속성 전이(CASCADE)

- 영속성전이(CASCADE) : 부모 엔티티가 영속화될 때, 자식 엔티티도 같이 영속화되고/ 부모 엔티티가 삭제될 때 자식 엔티티도 삭제된다. 특정 엔티티를 영속 상태로 만들 때 연관된 엔티티도 함께 영속 상태로 전이되는 것을 의미한다.

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
