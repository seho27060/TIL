[TOC]

![](https://user-images.githubusercontent.com/81341784/210832483-787c0f84-2d32-4b8a-9bb9-e7ee9a043cbc.png)

# Spark-with-Python 00

## Spark 시작하기

- 시작하기에 앞서...`Java 11`은 사용하지 말자
  
  - `Apache Spark`는 `Java 8`이나 `Java 11`로 호환성이 맞다.

- 자바, 파이썬, 스파크를 설치하자

- 윈도우라면 환경변수로 `java`와 `hadoop`, `python`의 경로를 설정해주자
  
  - 스파크 3부터는 파이썬의 경로 필수(2는 아님)

- `anaconda prompt`에서 `pyspark`실행
  
  - `내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다.` 어쩌고 하는 오류가 났는데^^^^^ 환경변수 설정할때 `PYSPARK_PYTHON`을 `python.exe`로 설정해줘야 한다 ^^^^^ python39 같은 폴더가 아니라 ^^^^^^^^^^^^^^^^^^^^^^^^
  
  ![](https://user-images.githubusercontent.com/81341784/210832500-00dcf6ea-3992-4a2a-817a-0a20ea460e99.png)

---

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
