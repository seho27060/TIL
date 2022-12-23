[TOC]

# Docker & Kubernetes 01

## Docker?

- 컨테이너를 생성하고 관리하는 도구

- 컨테이너( Container) : 표준화된 소프트웨어 유닛
  
  - 각 컨테이너에 작동중인 애플리케이션을 위한 환경, 도구를 할당하여 독립적으로 실행할 수 있다.
  
  - 애플리케이션간 연결성이 엹어지는 장점.
  
  - 하 죄다 쓴거 도커설치하다 다날라갔네

### Virtual Machines VS Virtual Operation Systems

- VM의 경우
  
  - Host OS
    
    - VM(Guest OS) - [Libraries, Dependencies, Tools, ] - Application1
    
    - VM(Guest OS) - [Libraries, Dependencies, Tools, ] - Application2
    
    - VM(Guest OS) - [Libraries, Dependencies, Tools, ] - Application3
  
  Host OS에서 각 Application에 맞는 Guest OS를 설치하고 그에 따른 라이브러리, 종속성, 도구들을 설정해야 한다.
  
  설치의 과정에서는 중복적인 작업이 일어나 **오버헤드**가 발생한다.
  
  - 장점 : 각 App마다 분리된 환경으로 각 설정 커스터마이징이 가능하다
  
  - 단점 : 중복복제로 인해 비용의 소모가 크다. 이는 성능 저하로 직결된다. 로컬 환경과 생산 환경을 동일한 상태로 설정하는건 매우 까다로운 일이다.

- Container의 경우
  
  - Host OS
    
    - Built-in Container Support(OS 내장 기능)
      
      - Docker Engine
        
        - Container - [Libraries, Dependencies, Tools, ] - Application1
        
        - Container - [Libraries, Dependencies, Tools, ] - Application2
        
        - Container - [Libraries, Dependencies, Tools, ] - Application3
  
  Host OS 위에 각 Application에 필요한 자원을 Docker Engine에서 선택적으로 사용 가능하다. 이는 중복적인 설치로 인한 자원 낭비를 방지 할 수 있다.
  
  이미지 파일로 생산이 가능하며 이를 통해 재생산이 용이하다.
  
  - 장점 : 적은 비용으로 구축 가능하며 공유 재구축에 용이하다.
  
  - 단점 : Host OS에 문제가 생길시 모든 컨테이너에 영향을 끼친다.

#### Docker 설치

- 공식문서를 보고 잘 설치해보자.

#### 강의 개요

1. 기초 
   
   1. Images & Containers
   
   2. Data & Volumes
   
   3. Containers & Networking

2. 활용
   
   1. Multi-Container Projects
   
   2. Using Docker-Compose
   
   3. "Unity Containers"
   
   4. Deploying Docker Containers

3. Kubernetes
   
   1. 소개 & 기본
   
   2. Kubernetes : Data & Volume
   
   3. Kubernetes : Networking
   
   4. Deploying Kubernetes Cluster

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
