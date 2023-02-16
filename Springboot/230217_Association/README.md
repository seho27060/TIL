[TOC]

# Association

## 연관관계 매핑

- 방향(Direction) : [단방향, 양방향]으로 구분된다. 
  
  - 관계에서 A에서 B를 참조하는 것을 단방향
  
  - A와 B가 서로 단방향으로 참조하는 것을 양방향

- 다중성(Multiplicity) : `N:1`, `1:N`, `1:1`, `N:N` 등의 형태

- 연관관계의 주인(owner) : 객체를 양방향 연관관계를 만들면 `N`의 위치의 `Entity`가 연관관계의 주인이 된다.

- **객체 연관관계**와 **테이블 연관관계**는 명백히 다름을 이해하자.
  
  - 객체 연관관계의 경우 관계는 단방향 관계로 구성된다. `Entity.getField()`와 같은 방식으로 참조
    
    - 이때 **양방향 관계**는 결국 **단방향 관계가 서로를 마주보는 것**을 구현된다.
  
  - 테이블 연관관계의 경우 관계는 양방향 관계로 구성된다. 
    
    ```sql
    select * from tableA
    join tableB on a.id = b.id
    
    select * from tableB
    join tableA on a.id = b.id
    ```
    
    위와 같은 방식으로 `SQL` 상에서는 `JOIN`을 활용하여 서로 참조가 가능하다.

### 객체 관계 매핑

- `JPA`를 활용하여 연관관계에 따른 객체 관계 매핑을 알아보자.

- `Entity`의 필드에 "어노테이션"을 붙여 여러 옵션을 부여할 수 있다.

#### @ManyToOne

- 다대일(`N:1`) 관계 매핑 어노테이션

- `optional`, `fetch`, `cascade`, `targetEntity` 등의 속성으로 옵션 부여가 가능하다.

- ```java
  @ManyToOne(
    optional=연관 Entity 여부,
    fetch = FetchType.Lazy,
    cascade = CascadeType.영속성정의) 
  ```

#### @JoinColumn

- 외래 키를 매핑할 때 사용한다.
- ```java
  @JoinColumn(
      name="필드명_기본키",
      referecedColumnName = "외래 키가 참조하는 대상 테이블의 컬럼명",
      foreignKey(DDL) = 외래 키 제약 조건 실행,
      등등등
  )
  ```

#### detail-index1

---

- 레퍼런스

> 
