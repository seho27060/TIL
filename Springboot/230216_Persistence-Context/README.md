[TOC]

# Persistence Context

## 영속성 컨텍스트

> `Spring` 에서 `Entity`를 영구저장하는 환경
> 
> 애플리케이션과 데이터베이스 사이에서 객체를 보관하는 **가상의 데이터베이스** 역할

- `JPA`를 이해하기 위한 가장 중요한 개념

- `Application` 별로 하나의 `EntityManagerFactory`가 존재한다.
  
  - `EntityManagerFactory` : 하나의 데이터베이스에 연결되어  `EntityManager`를 관리하는 관리자. 생성시에 비용이 매우 크며, 여러개의 쓰레드에도 동시성이 보장된다.
  
  - `EntityManger` : `EntityManagerFactory`로 생성되는 `Entity`를 관리하는 관리자. 수정, 삭제, 생성, 조회 등의 기능을 수행한다. 생성 비용이 적으며, 동시성 보장이 안된다.

- `EntityManagerFactory`는 디비 접근 트랜잭션 별로 `EntityManager`를 생성한다.

- `EntityManager`로 `Entity`를 저장, 조회하면 영속성 컨텍스트 `Entity`를 보관한다.

- **영속성 컨텍스트**는 논리적인 개념에 가까워 실제적으로 관찰하기 어렵다.

#### 영속성의 생명주기

- `Entity`의 상태에 따라 영속성의 생명주기를 4가지로 분류된다.
  
  1. 비영속(new/transient): 영속성 컨텍스트와 전혀 관계 없음
     
     - `Entity` 객체를 이제 막 생성하면 비영속 상태이다.
  
  2. 영속(managed) : 영속성 컨텍스트에 저장됨
     
     - `EntityManager`를 통해 `Entity`를 영속성 컨텍스트에 저장한 상태
     
     - 비영속 상태에서 **영속**되어 영속 상태로서 **영속성 컨텍스트에 의해 관리**된다.
  
  3. 준영속(detached) : 영속성 컨텍스트에 저장되었다가 분리됨
     
     - 또는 영속성 컨텍스트를 초기화할 시, 영속 상태의 `Entity`는 준영속 상태가 된다.
  
  4. 삭제(removed):  `Entity`를 영속성 컨텍스트와 데이터베이스에서 삭제할 경우.

### 영속성 컨텍스트의 특징

- 영속 상태의 `Entity`는 무조건 식별자 값을 갖는다.

- 영속성 컨텍스트에 저장된 `Entity`는 `JPA`가 `Transaction`을 `commit`하는 순간 데이터베이스에 변경내용을 저장한다.
  
  - 이를 **플러시(flush)** 라고 한다.

#### 영속성 컨텍스트의 장점

1. 1차 캐시 :영속성 컨텍스트 내부에 1차 캐시가 존재한다. 이곳에 영속 상태의 엔티티를 `key-value`의 `map`의 형태로 저장한다.
   
   - 조회 흐름
     
     1. 1차 캐시에서 식별자값(`key`)로 `Entity`를 찾는다.
     
     2. 1차 캐시에 있으면 캐시에서 조회/ 없으면 디비에서 조회한다.
     
     3. 조회 데이터로 `Entity`를 생성해 1차 캐시에 저장 
     
     4. 조회 `Entity`를 영속상태로 반환

2. 동일성 보장 : 영속 상태의 `Entity`를 다른 인스턴스로 호출할때, 1차 캐시의 값을 반환함으로 동일한 값의 다른 인스턴스가 생성된다.

3. 트랙잭션을 지원하는 쓰기 지연
   
   - 쓰기 지연(transactional write-behind) : 트랜잭션의 쿼리들을 **내부 쿼리 저장소**에 임시로 저장하여 **트랜잭션을 커밋**할때 내부 쿼리 저장소의 쿼리들을 **일괄적**으로 데이터베이스에 보낸다.

4. **변경감지(Dirty Checking)**
   
   - `Entity`에서 변경 발생시, 변경을 감지하고 디비에 매핑되는 테이블에 업데이트 쿼리를 저장함(디비에 날리는거 아님)
     
     - `JPA`는 `Entity`를 영속성 컨테스트에 보관할 때, 최초 상태를 복사하여 **스냅샷**으로 저장한다. `flush()`가 발생하면 스냅샷과 `Entity`를 비교하여 변경을 감지한다.
   
   - 변경감지 흐름
     
     1. 트랜잭션 커밋시, `EntityManager`내부에 `flush()` 호출
     
     2. `Entity`와 스냅샷을 비교하여 변경된 엔티티를 찾는다.
     
     3. 변경 `Entity`발견시, 수정 쿼리를 생성하여 쓰기 지연 SQL저장소에 저장
     
     4. 수정과정에 문제가 없다면 쓰기 지연 저장소의 SQL을 데이터베이스에 쏜다.
     
     5. 데이터베이스 트랜잭션을 커밋한다.
   
   - 변경 감지는 영속성 컨테스트가 관리하는 **영속 상태**의 `Entity`에만 적용된다.
   
   - \*수정 쿼리는 단일 필드가 아닌 전체 필드에 적용된다. 규모가 큰 데이터 저장은 `@DynamicUpdate`와 같은 어노테이션으로 커스터마이징이 필요하다.

5. 지연 로딩
- 메서드에 `@Transaction`이 붙으면 저장된 쿼리를 디비에 날린다.

- `@Transactional` :`Service`의 구현에서 디비에 수정/삭제에 대해 신뢰성을 보장해주는 어노테이션
  
  - 디비와 소통한다.
  
  - 디비와 소통하기 전부터, 하고난 후까지 체크
  
  - 디비와 소통중 에러가 나면, 디비와 소통전으로 되돌리고
  
  - 정상적으로 소통이 끝나고 쿼리가 디비에 날아갔다면, 결과를 디비에 확정짓는다.
  
  - 메서드 하나에 붙여줄수도 있지만, 서비스 구현 전체에 달아줄수도 있다.

### Flush(플러시)

> **영속성 컨텍스트의 변경 내용을 데이터베이스에 반영한다.**
> 
> 엔티티를 지우는게 아닌, 변경 내용을 데이터베이스에 동기화한다.

- 플러시를 실행하면,
  
  1. 변경 감지(Dirty Checking)으로 영속성 컨테스트의 모든 `Entity`에 대한 수정 사항을 찾아 "쓰기 지연 `SQL` 저장소"에 등록한다.
  
  2. "쓰기 지연 `SQL` 저장소"의 쿼리를 데이터베이스에 쏜다.

- 영속성 컨텍스트는 플러시를 아래와 같이 호출한다.
  
  - `EntityManager` 인스턴스를 통한 직접 호출
  
  - 트랜잭션 커밋 시 자동 호출
  
  - `JPQL` 쿼리 실행 시 자동 호출

### 더티체킹(Dirty Checking)

- 더티 체킹 : Transaction 안에서 엔티티의 변경이 일어나면, **변경 내용을 자동**으로 데이터베이스에 **반영**하는 JPA 특징

- JPA는 엔티티 매니저가 엔티티를 저장/조회/수정/삭제 한다.

- 엔티티 매니저의 메서드에는 저장(persist)/ 조회(find)/ 삭제(delete)로 수정에 해당하는 메서드는 없다.

- 수정 기능 대신 더티 체킹(dirty checking)을 지원한다.

-  JPA 영속성 컨텍스트

![](https://blog.kakaocdn.net/dn/cokEKI/btqygTOISLW/TrI5hAUoR9wiVP92OJlIJ0/img.png)

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
  
  2. user의 email을 [examUpdate@mail.com](mailto:examUpdate@mail.com)으로 수정(**Dirty Checking**)
  
  3. 수정된 이메일 [examUpdate@mail.com](mailto:examUpdate@mail.com) 을 가진 user엔티티 유무 확인, 2번과정에서 수정되었기에 true 출력

- `@Transactional`을 사용하지 않은 경우, 2번 과정의 더티체킹이 발생하지 않아 디비의 데이터가 수정되지 않는다.

---

- 레퍼런스

> 자바 ORM 표준 JPA 프로그래밍 - p.89 영속성 관리
