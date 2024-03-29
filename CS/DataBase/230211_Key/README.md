- [Key](#key)
  - [키](#키)
    - [키의 종류](#키의-종류)
      - [후보키(Candidate Key)](#후보키candidate-key)
      - [기본키(Primary Key)](#기본키primary-key)
      - [대체키(Alternate Key)](#대체키alternate-key)
      - [슈퍼키(Super Key)](#슈퍼키super-key)
      - [외래키(Foregin Key)](#외래키foregin-key)

---

# Key

## 키

> 데이터베이스에서 조건에 맞는 튜플을 찾거나 정렬을 할때, 튜플을 구분할 수 있는 **기준**이 되는 속성

- 튜플 : 관계를 구성하는 각각의 행, 속성의 모임. 레코드와 같은 개념이며 튜플의 수는 카디널리티(Cardinality)와 같다.

### 키의 종류

#### 후보키(Candidate Key)

-  관계를 구성하는 속성들 중에서 튜플을 유일하게 식별하기 위해 사용하는 속성들의 부분 집합
  
  - 기본키로 사용할 수 있는 속성들을 의미함

- 하나의 관계내에서는 중복된 튜플들이 있을 수 없으므로, 모든 관계에서는 반드시 하나 이상의 후보키가 존재한다.

- 후보키는 관계에 있는 모든 튜플에 대해서 **유일성**과 **최소성**을 만족해야 한다.
  
  - 유일성 : 하나의 키값으로 하나의 튜플만을 식별
  
  - 최소성 : 모든 레코드들은 유일하게 식별하는데 꼭 필요한 속성만으로 구성

#### 기본키(Primary Key)

- 후보키 중에서 선택한 주 키(Main Key)이다.

- 한개의 관계에서 특정 튜플을 유일하게 구별할 수 있는 속성

- `NULL` 값을 가질 수 없으며, 기본키로 정의된 속성은 동일한 값이 중복되어 저장될 수 없다.(개체 무결성의 첫번째 조건, 두번째 조건)

#### 대체키(Alternate Key)

- 후보키가 둘 이상일 때, 기본키를 제외한 나머지 후보키
  
  - 보조키라고도 한다.

#### 슈퍼키(Super Key)

- 한개의 관계 내 속성들의 집합으로 구성된 키
  
  - 관계를 구성하는 모든 튜플들 중 슈퍼키로 구성된 속성의 집합과 동일한 값을 나타나지 않는다.

- 관계를 구성하는 모든 튜플에 대해 유일성을 만족하지만, 최소성을 만족시키지 못한다.

#### 외래키(Foregin Key)

- 서로 관련된 관계 `R1`,`R2`에서 `R1`가 참조하는 `R2`의 기본키를 `R1`의 외래키라고 한다.

- 외래키는 참조되는 관계의 기본키와 대응되어, 관계간 참조 관계를 표현하는데 중요하다.

---

- 레퍼런스

> [[DB기초] 여러가지 키(기본키,후보키,외래키등)의 종류와 개념](https://coding-factory.tistory.com/220)
> 
> [키(Key)의 개념 및 종류 : 후보키, 기본키, 외래키, 대체키, 후보키 :: 가치관제작소](https://valuefactory.tistory.com/704)
