[TOC]

# Docker 11

## Docker 컨테이너 배포하기 - 03

### AWS ECS로 다중 컨테이너 배포하기

- 로컬에서 docker-compose를 활용하여 동일한 머신에서 여러 서비스를 배포한 내용을 여러대의 머신이 함께 작동할 클라우드로 이동할 경우, 고려해야할 세부 사항이 많아진다.

- backend와 mongodb 서비스를 AWS에 배포해보자.

- 이미지빌딩
  
  - 사용할 이미지를 빌딩하고 dockerhub에 푸쉬한다.
  
  - 로컬에서는 docker-compose로 형성된 네트워크내에서 컨테이너의 이름으로 해당 ip로 접근이 가능하다. 하지만 **AWS에서는 불가능**하다.
    
    - AWS ECS에서 무언가를 배포한다면 동일한 머신에서 docker-compose를 실행한다는 보장이 없기 때문이다
    
    - 이를 위해 **AWS ECS의 동일한 task**에 docker-compose를 실행하면 동일한 머신에서 컨테이너를 실행할 수 있다.

- 클러스터 생성
  
  - 태스크 생성
  
  - 서비스 생성
    
    - task definition 생성 및 할당
      
      - 컨테이너 생성
        
        - 백엔드 컨테이너
        
        - 디비 컨테이너
          
          - 하란대로 했는데 몽고디비 인증 오류 뜸^^..
      
      - 로드밸런서 생성 및 할당
      
      - target group 생성 및 할당
  
  - 

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
