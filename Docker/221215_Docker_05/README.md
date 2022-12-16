[TOC]

# Docker & Kubernetes 05

## Docker로 다중 컨테이너 애플리케이션 구축하기

- 데이터베이스, 백엔드, 프론트엔드 3개의 블록을 각각 컨테이너로 실행하고 네트워크를 활용해 상호간 통신을 구축해보자

### 호스트 머신으로 연결

1. 데이터베이스 컨테이너 실행
2. 백엔드 컨테이너 실행
3. 프론트엔드 컨테이너 실행

### 네트워크를 활용하여 연결

#### 프론트엔드 컨테이너

- React의 경우 JavaScript가 브라우저에서 실행되므로 도커의 url 식별자를 사용할 수 없다.
- 로컬호스트의 url을 사용한다. 일단

#### 데이터베이스 컨테이너

- 관련 공식 이미지의 사용 docs에 여러 정보가 명시되있으니 참고하자

- 현재 데이터베이스 컨테이너를 재시작시, 모든 데이터가 리셋된다.
  
  - 볼륨을 추가하여 데이터 지속성을 추가한다.

- 인증 기능 추가
  
  - 환경 변수(ENV)를 추가한다.
    `docker run --name mongodb -v 볼륨태그:컨테이너내볼륨저장위치 --rm -d --network goals-net -e MONGO_INITDB_ROOT_USERNAME=인증아이디 -e MONGO_INITDB_ROOT_PASSWORD=인증패스워드 mongo`
  
  - 백엔드 컨테이너에 접근 url을 `mongodb://인증아이디:u인증패스워드@mongodb:27017/course-goals?authSource=admin`로 수정한다.

#### 백엔드 컨테이너

- WIndows 파일 시스템에서 바인딩 마운트를 통한 라이브 소스코드 업데이트가 불가하다.
  - Windows와 WSL2를 같이 써서 발생하는 문제, Linux 파일 시스템을 세팅하고 그 위에서 도커를 사용하면 문제가 해결된다.
- Mongodb에 인증을 추가했을시, 동적인 상황을 고려하여 환경변수로 디폴트 인증 값을 추가한다.
  - 컨테이너를 올릴때 각 맞는 값을 따로 넣어주면 환경변수에 덮어진 값으로 접근한다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
