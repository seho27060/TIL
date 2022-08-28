[TOC]

# springboot_05

- 엔티티에 @Setter를 지양하는 이유

- 지연로딩 -> 연관관계로 묶인 애들이 다 끌려옴.(n+1쿼리문제)

- 순환참조 -> 디티오로 해결

- onetomany관계의 테이블은 지연로딩전략이 적용된다. 

- 영속성 컨텍스트에 포함되어있는 값들은 연관관계의 테이블이 삭제될때 삭제되지 않는다.

- Http method 종류의 작동 차이/ 멱등성

## Subject Detail

### index1

#### detail-index1
