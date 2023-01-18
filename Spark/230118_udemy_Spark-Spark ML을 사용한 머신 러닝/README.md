[TOC]

# Spark-with-Python 08

## Spark ML을 사용한 머신 러닝

### MLLib 소개

#### ML Capabilities

- Feature extraction
  
  - 단어 빈도 검색, 역 문서 빈도 검색

- 기본 통계
  
  - 카이스퀘어 검정, 피어슨, 스피어만 상관계수

- 선형 회귀, 로지스틱 회귀

- SVM

- 나이브베이스 분류

- 분류 나무

- k-mean 클러스터링

- 주 성분 분석, 특이값 분해

- 교차 최소 제곱을 통한 추천

- 등등등 여러 분석 모델이 `Spark ML`에 포함되어 있다.
  
  - 물론 분산 시스템을 활용하여 모델이 작동된다.

#### ML uses DataFrames

- `MLLib`이라고 불렸고 `RDD`과 특별한 데이터 구조를 사용했으나.. `Spark 3`로 넘어오면서 `ML`이라는 새로운 라이브러리로 편성되었고 `DataFrame`을 기본적으로 사용한다.

#### Lets make some movie recommendations

- 강의에서 말하는 거처럼.. "사용 만"하는건 매우 쉽다. 데이터를 구하고 모델이 원하는 형태로만 입력해주면 되니까. 

### [활동] Spark ML을 사용하여 영화 추천 제작

- ALS 모델로 추천했으나..분석 데이터가 초라해서 결과가 좋지 않다.

### [활동] Spark ML을 사용한 선형 회귀

- 아주 오랜만만인 선형회귀. `ML` 라이브러리에 포함된 선형 회귀로 영화르 추천해봅시다다다

### [연습] Spark ML에서 의사 결정 트리를 사용하여 부동산 가격 예측

- 

---

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
