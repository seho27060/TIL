- [Docker \& Kubernetes 12](#docker--kubernetes-12)
  - [Docker 컨테이너 배포하기 - 04](#docker-컨테이너-배포하기---04)
      - [EFS 볼륨 사용하기](#efs-볼륨-사용하기)
    - [구성 아키텍쳐](#구성-아키텍쳐)
      - [데이터베이스 \& 컨테이너](#데이터베이스--컨테이너)
    - [MongoDB Atlas로 이동하기](#mongodb-atlas로-이동하기)
      - [MongoDB Atlas 생성과정](#mongodb-atlas-생성과정)
    - [Production 환경과 Development 환경](#production-환경과-development-환경)
      - [멀티 스테이지 빌드](#멀티-스테이지-빌드)
      - [스탠드얼론 프론트엔드 앱 배포하기](#스탠드얼론-프론트엔드-앱-배포하기)

# Docker & Kubernetes 12

## Docker 컨테이너 배포하기 - 04

#### EFS 볼륨 사용하기

- EFS(Elastic File System): 로컬 머신의 Docker volume과 같이 컨테이너가 재시작되어도 데이터를 보존하게 하는 클라우드 기능

### 구성 아키텍쳐

- AWS ECS
  
  - ECS Task
    
    - Nodejs REST API
    
    - MongoDB
      
      - AWS EFS Storage(Volume)

#### 데이터베이스 & 컨테이너

- 위 구조에서 mongodb 컨테이너는 내부적으로 데이터베이스를 생성하여 데이터를 저장한다.

- 다만 아래 3개의 문제에 대한 고려가 필요하다.
  
  - 읽기/쓰기 작업이 다중으로 발생할 시, 동기화가 되지 않는 문제가 야기된다.
  
  - 트래픽 급증시 성능 문제 발생
  
  - 백업과 보안 미비로 인한 데이터 안정성 문제 발생

- 데이터베이스 설정, 관리가 완벽히 수행된다면 위와 같은 문제는 예방된다.
  
  - 우리 모두가 전문가가 아니라는게 맹점, 오히려 문제를 더 만들 수 있다.
  
  - 다양한 솔루션이 있으며 해당 과정에서는 **MongoDB Atlas**를 데이터베이스 관리 서비스로 사용한다.

### MongoDB Atlas로 이동하기

- MongoDB에서 제공하는 데이터베이스 관리 서비스

- 기존의 mongodb 컨테이너를 MongoDB Atlas로 대체한다.

#### MongoDB Atlas 생성과정

- 클러스터 생성

- 접근 유저 생성

- Network Access 생성

- 클러스터의 접근 유저 id, password, url을 애플리케이션에 할당한다.
  
  - 환경 변수를 활용하여 url에 접근 값을 동적으로 활용하자.

- ECS에 연결된 로드밸런서의 DNS name으로 접근하면 배포된 서버에 접근 가능하다!
  
  - (실제로 각 컨테이너의 모든 설정 만지는것보다 기존의 서비스 활용이 더 효율적이네..)
  
  - *이전에 컨테이너를 개별 설정할때는 AthenticatedError가 발생했다.
    
    - 보안그룹..접근 id, password, 작업 그룹..여러 요인이 있지만 정확한 이유를 파악하지 못했다.

### Production 환경과 Development 환경

- 클라우드 접근 url, 머신에 따른 네트워크 접근 및 보안 설정 등 여러 설정이 실제 배포되는 Production 환경과 개발이 진행되는 Development 환경에서 차이점이 발생할 수 있다. 

- 해당 강의의 예시로 React의 경우 로컬에서는 `npm start`로 실행할 수 있지만, 실제 배포 환경에서는 `npm run build`를 통해 최적화된 형태로 실행한다.

- 이와 같이 배포환경과 개발환경에서 설정 및 실행의 차이점으로 인해 "빌드 전용 컨테이너"로 배포환경에서 애플리케이션을 실행한다.

#### 멀티 스테이지 빌드

- 배포 전용 컨테이너를 위해 `Dockerfile.prod`라는 도커파일을 생성한다.
  
  ```dockerfile
  FROM node:14-alpine as build
  
  WORKDIR /app
  
  COPY package.json .
  
  RUN npm install
  
  COPY . .
  
  EXPOSE 3000
  
  RUN npm run build
  # 첫번째 빌드(스테이지) 실행
  
  # FROM을 통해 기존의 baseimage를 변경할 수 있다.
  FROM nginx:stable-alpine
  
  COPY --from=build /app/build /usr/share/nginx/html
  
  EXPOSE 80
  # nginx를 통해 배포 웹 서버 실
  CMD ["nginx", "-g", "daemon off;"]
  ```
  
  - 1개의 도커 파일 내에서 baseimage 교체를 통해 2번의 빌드(멀티 스테이지 빌드)가 가능하다.
  - React 애플리케이션을 먼저 빌드한 후, 이를 위한 nginx 서버를 빌드한다.

- 멀티 스테이지 이미지 구축
  
  - 기존의 이미지 구축과 같이 진행한다
  
  - `docker build -f frontend/Dockerfile.prod -t 도커허브레포위치 ./frontend`
    
    - `-f`옵션을 통해 빌드 파일을 지정할 수 있다.

#### 스탠드얼론 프론트엔드 앱 배포하기

- AWS ECS의 같은 클러스터에 새로운 Task를 생성하여 frontend 서버를 스탠드얼론 모드로 배포해보자.

- frontend 애플리케이션내에서 backend 서버 연결을 위한 url에 환경(개발 or 배포)에 따라 다른 url을 `App.js`상에서 환경변수 상으로 사용한다.
  
  - 개발환경에서는 localhost
  
  - 배포 환경에서는 backend의 로드밸런서의 DNS name으로 접근한다.

- Task 정의
  
  - frontend 컨테이너 생성

- Service 생성
  
  - 새로 정의한 Task를 기반으로 Service를 생성한다
  
  - frontend용 로드밸런서 생성 후 Target group과 보안 그룹을 생성하여 할당한다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
