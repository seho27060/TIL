[TOC]

# Docker & Kubernetes 10

## Docker 컨테이너 배포하기 - 02

### AWS Elastic Container Service(AWS ECS)

#### ECS 구조

- 탄력적 컨테이너 서비스
  
  - 자체적으로 관리해야하는 EC2가 아닌 관리형 서비스

- Container 
  
  - 터미널에서 `docker run`의 실행시 옵션을 지정할 수 있다.
  
  - `--name --env...등등`

- Task
  
  - 1개의 작업을 실행하는 단위
  
  - 1개의 기능을 하는 1개의 컨테이너를 실행한다.

- Service

- Cluster
  
  - 여러 컨테이너를 포함하는 단위
  - 해당 클러스터의 네트워크 생성

#### 관리 컨테이너 업데이트

- 수정사항이 반영된 이미지를 리빌딩한다
  
  - 해당 이미지를 dockerhub에 푸시한다.

- AWS ECS에서 새로운 Task를 생성한다
  
  - 생성시 연결된 dockerhub의 이미지를 받아 사용한다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
