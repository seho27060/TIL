[TOC]

# QueryDSL 03

## QueryDSL 기본설정과 기본문법

### 기본설정

- `QueryDSL`을 통해서 `JPA`에서의 `repository`에서의 `ORM` 사용을 좀 더 동적으로, 좀 더 `Java` 혹은 `Spring`에 가깝게 사용할 수 있음을 알았다.

- `Q-type`을 활용하여 `QueryDSL`만의 문법으로 명확하고 쉬운 사용이 가능하다.

- 기본 사항들은 이러하고.. `Springboot` 애플리케이션 내에서 기존에 사용하던 `JPA`를 대체하기 위해 필요한 설정을 진행한다.

#### `JPAQueryFactory` 전역 설정

- `config`에 `QueryDsl` 관련 설정을 추가한다. 아래와 같다.
  
  ```java
  @Configuration
  public class QueryDslConfig {
  
      @PersistenceContext
      private EntityManager entityManager;
  
      @Bean
      public JPAQueryFactory jpaQueryFactory(){
          return new JPAQueryFactory(entityManager);
      }
  }
  ```
  
  `QueryDsl`을 사용하기 위해서는 `EntityManager`를 `JPAQueryFactory`에 등록해줘야 하는데, 이를 `config`에 설정함으로 `Spring` 전역에서 사용 가능하도록 한다.

#### `CustomRepository` 설정

- `QueryDsl`을 사용하기 위해서는 기존의 `JPARepository`가 아닌 사용자에 의한 `CustomRepository`를 설정해야 한다.
1. `Spring Data JPA Custom Repository` 사용법
   
   - 항상 2개의 `Repository`를 의존성으로 받아야 한다.
   
   - `QueryDsl`의 `Custom Repository`와 `JpaRepository`를 상속한 `Repository`가 기능을 나눠가졌기 때문이다.
   
   - `CustomeRepository` `interface`를 구현하여 그에 따른  `implement`를 생성한다.
   
   - 기존의 `JpaRepository`를 상속하는 `Repository`에 `CustomRepository`를 같이 상속해준다.

2. 상속/ 구현 없는 `CustomRepository`
   
   - `interface`에 따른 `implement`없이 `Bean`에 `CustomeRepository`를 등록함으로 사용할 수 있다.
   
   - 훨씬 간단해..지긴 하나 관리의 관점에서는 어떨지 모르겠다.
   
   - 코드량이 줄어드니 해당 방법을 사용하자.

### 기본문법

- `QueryDSL`의 기본 사용법과 문법에 대해 알아보자.

#### 사용법

```java
import static com.ED.backend.domain.entity.QDiary.diary;

@RequiredArgsConstructor
@Repository
public class DiaryQueryRepository {
    private final JPAQueryFactory jpaQueryFactory;

    public List<Diary> findByTitle(String title){
        return jpaQueryFactory.selectFrom(diary)
                .where(diary.title.eq(title))
                .fetch();
    }
}
```

- `QueryDsl` 설정을 다 끝내고 기존 `Entity`에 따른 `Q-type`이 생성되었다는 가정하에, `import static com.ED.backend.domain.entity.QDiary.diary;`와 같이 해당 `Repository`에서 사용할 `Q-type`을 미리 `import static`으로 불러온다.

- `private final JPAQueryFactory jpaQueryFactory;`으로 `config`에서 `QueryDsl`사용을 위해 전역에 등록한 `JpaQueryFactory`를 불러온다. 해당 `Factory`를 통해 `QueryDsl`과 데이터베이스를 연결하여 데이터를 조회한다.

- `jpaQueryFactory`에는 `QueryDsl` 문법으로 원하는 데이터 작업을 진행한다.

#### 문법

- `WHERE` 절 관련
  
  | SQL                              | QueryDsl                          |
  | -------------------------------- | --------------------------------- |
  | A = col                          | `eq(col)`                         |
  | A != col                         | `ne(col)`,`eq(col).not()`         |
  | A IS NOT NULL                    | `isNotNull()`                     |
  | A IN (col)/NOT IN (col)          | `in(col)`, `notIn(col)`           |
  | A BETWEEN col1 AND col2          | `between()`                       |
  | A >= col/ A > col                | `goe(col)`, `gt(col)`             |
  | A <= col/ A < col                | `loe(col)`, `lt(col)`             |
  | A LIKE "%col%"/ A LIKE "COL%COL" | `contains(col)`, `startWith(col)` |

- 결과 조회
  
  | QueryDsl         | 기능                                                               |
  | ---------------- | ---------------------------------------------------------------- |
  | `fetch()`        | 리스트 조회, 값이 없다면 빈 리스트 반환                                          |
  | `fetchOne()`     | 단 1건만 조회. 값이 없다면 `null` 반환, 둘 이상이라면 `NoUniqueResultException` 반환 |
  | `fetchFirst()`   | `limit(1).fetchOne()`과 동일                                        |
  | `fetchResults()` | 페이징 정보를 포함하여 total count 쿼리 추가 실행                                |
  | `fetchCount()`   | count 쿼리로 변형하여 count 수 조회                                        |

- 페이징

- 정렬

- 집합

- `JOIN`

- 서브쿼리

- `CASE`

- 등 여러가지가 있으나 필요에 의해 찾아보자.

---

- 레퍼런스

> https://tecoble.techcourse.co.kr/post/2021-08-08-basic-querydsl/
> 
> http://querydsl.com/static/querydsl/3.6.3/reference/ko-KR/html_single/#d0e119
