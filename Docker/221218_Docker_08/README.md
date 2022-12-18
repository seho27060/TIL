[TOC]

# Docker & Kubernetes 08

## Docker의 복잡한 세부 설정

- 로컬 환경에 복잡한 설정이 필요한 Laravel과 PHP를 도커를 활용하여 간편하게 구축해보자

- 과정 중 새로운 도커 기능도 사용한다!

##### \*Laravel & PHP

- Laravel : 가장 인기있는 PHP 프레임워크

- 패키지 관리자 Composer, 데이터 관리 Laravel Artison, npm 등.. 여러 애플리케이션이 Laravel 웹 서비스를 구축하는데 필요하다.
  
  - 총 6개의 컨테이너를 활용한다!

### docker container 구축하기

#### Docker compose 파일 설정

- 애플리케이션 별 서비스 설정
  
     1. `nginx.conf`로 nginx 서버 설정, `docker-compose.yaml`내에서 해당 서버의 서비스 설정 진행
  
  2. `docker-compose.yaml`내에서 php 애플리케이션 설정
  
  3. MySQL 서버 설정 진행
  
  4. docker-compose로 composer 서비스를 따로 실행하여 laravel 기본 폴더 생성
  
  5. artisan, npm 컨테이너 추가

#### docker-compose 의 참고 사항

- `docker-compose.yaml`내에 추가가능한 사항
  
  - `entrypoint` : `dockerfile`내에서 설정하지 않은 entrypoint를 docker-compose 파일 내에서 설정가능
  
  - `build: context: dockerfile:` : 빌드에 필요한 dockerfile을 직접 지정해 줄 수 있다.

- 만약 배포를 앞둔 프로젝트라면, 바인드 마운트는 선택사항이 아니다.
  
  - 개발을 위한 기능이지, 배포를 위한 기능이 아님.
  
  - 항상 컨테이너에 노출되기 때문에 안정성이 떨어짐.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
