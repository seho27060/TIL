[TOC]

# Querydsl_01

## JPQL vs QueryDsl

- JPQL과 QueryDsl의 차이를 간단한 테스트 코드를 통해 살펴보자

### JPQL

```java
@Test
    public void startJPQL(){
        // find member1
        String qlString = "select m from Member m where m.username = :username";
        Member findMember = em.createQuery(qlString, Member.class)
                .setParameter("username","member1")
                .getSingleResult();

        assertThat(findMember.getUsername()).isEqualTo("member1");
    }
```

### QueryDsl

```java
@Test
    public void startQuerydsl(){

        JPAQueryFactory queryFactory = new JPAQueryFactory(em);
        QMember m = new QMember("m");

        Member findMember = queryFactory
                .select(m)
                .from(m)
                .where(m.username.eq("member1"))
                .fetchOne();
        assertThat(findMember.getUsername()).isEqualTo("member1");
    }
```

- JPQL의 경우 String으로 쿼리를 생성후 `EntityManager`에 할당한다. 이때 String으로 생성되는 쿼리에서 발생하는 실수를 컴파일러로 감지하지 못한다.

- QueryDsl의 경우 쿼리를 생성하는 과정 자체가 컴파일러에 의해 감지되므로, JPQL에 비해 실수를 미연에 방지하기 용이하다.

### 기본 Q-type 활용

#### Q클래스를 사용하는 3가지 방법

```java
        // 1. 
        QMember m = new QMember("m");
        // 2.
        QMember m = QMember.member;
        // 3. QMember의 모든 메서드를 static 메서드로 임포트
//         import static study.querydsl.entity.QMember.*;
        Member findMember = queryFactory
                .select(member)
                .from(member)
                .where(member.username.eq("member1"))
                .fetchOne();
        assertThat(findMember.getUsername()).isEqualTo("member1");
```

- 3.의 방법을 사용하면 코드 가독성이 훨씬 좋아진다.

---

- 레퍼런스

> 
