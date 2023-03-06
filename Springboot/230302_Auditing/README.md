- [Auditing](#auditing)
  - [Auditing](#auditing-1)
    - [`Auditing` 적용하기](#auditing-적용하기)
      - [1. Configuration](#1-configuration)
      - [2. `Entity`에 생성 시각, 수정 시각 `field` 추가](#2-entity에-생성-시각-수정-시각-field-추가)

---

# Auditing

## Auditing

- `Entity`를 생성하고 수정하면서. 해당 `Entity`이 마지막으로 변경된 시간이나, 생성 시간을 알아야 할 때가 있다.

- 으레 그렇듯 기본적인 기능은 `Spring JPA`에 포함되어 있다.
  
  - 개발자가 직접, 필요한 사항에 따라 이러한 `field`를 생성할 수 있지만
  
  - 이미 구현된 기능을 사용할 수 있다.

- `Auditing` 기능을 적용하는 방법을 알아보자.

### `Auditing` 적용하기

#### 1. Configuration

- `Spring`에게 `JPA Auditing`을 사용함을 알리기 위해 어플리케이션 영역에 어노테이션을 추가해야 한다.

- 아래와 같이 `@SpringbootApplication`이 위치한 영역에 어노테이션을 추가한다.
  
  ```java
  @SpringBootApplication
  @EnableJpaAuditing
  public class BackendApplication {
  
      public static void main(String[] args) {
          SpringApplication.run(BackendApplication.class, args);
      }
  
  }
  ```

#### 2. `Entity`에 생성 시각, 수정 시각 `field` 추가

- `@CreateDate`와 `@LastModifiedDate`와 같은 생성 시각, 수정 시각을 나타내는 `field`를 추가하기 위해 `Entity`에 `Auditing`을 인지하기 위한 어노테이션을 추가해야 한다.
  
  - `@EntityListeners(AuditingEntityListener.class)` 와 같이 `Entity`의 변화를 감지하는 어노테이션을 추가한다. 
  
  - `AuditingEntityListener`의 `class`를 할당하였는데, 이는 `Spring Data JPA`에서 제공하는 **이벤트 리스너**로 `Entity`의 영속, 수정 이벤트를 감지한다.

- 생성일을 기록하기 위해 `LocalDateTime` 타입의 `field`에 `@CreateDate` 어노테이션을 적용한다.

- 수정일을 기록하기 위해 `LocalDateTime` 타입의 `field`에 `@LastModifiedDate` 어노테이션을 적용한다.

- ```java
  @Entity
  @AllArgsConstructor
  @NoArgsConstructor
  @Builder
  @Getter
  @EntityListeners(AuditingEntityListener.class)
  public class Diary {
  
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
  
      // ... 
  
      @CreatedDate
      private LocalDateTime created;
  
      @LastModifiedDate
      private LocalDateTime updated;
  ```

#### 3. `BaseEntity`로 분리

- `2.`까지의 방법으로는 생성 시간, 수정 시간이 필요한 `Entity` 모두에 위와 같은 `field`를 생성하고 적용시켜야 한다.

- `BaseEntity`라는 기본 `Entity`로 구현한다.
  
  - 필요에 따라 새로 생성한 `Entity`는 `BaseEntity`를 상속받는다.

- 아래와 같은 `BaseEntity`를 생성한다.
  
  ```java
  @Getter
  @EntityListeners(AuditingEntityListener.class)
  @MappedSuperclass
  public class BaseEntity {
  
      @CreatedDate
      @Column(updatable = false)
      private LocalDateTime created;
  
      @LastModifiedDate
      private LocalDateTime updated;
  }
  ```
  
  `@MappendSuperclass` 는 공통 매핑 정보가 필요할 때, 부모 클래스의 필드를 상속받는 클래스에서 그대로 사용할 때 적용한다.

- `created`와 `updated`를 따로 갖던 `Diary`는 아래와 같이 상속받도록 수정한다.
  
  ```java
  @Entity
  @AllArgsConstructor
  @NoArgsConstructor
  @Builder
  @Getter
  public class Diary extends BaseEntity{
  
      @Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
  ```
  
  이를 통해 **코드 중복**이 사라졌을 뿐 아니라, **관리가 용이**한 형태로 분리하여 사용할 수 있다.

---

- 레퍼런스

> https://hudi.blog/spring-data-jpa-auditing-create-update-date/
> 
> [Spring boot hibernate jpa에서 Auditing 사용 - update, create 시간 자동 변경 — wedul](https://wedul.site/455)
