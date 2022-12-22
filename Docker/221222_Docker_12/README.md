[TOC]

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

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
