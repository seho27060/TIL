- [Docker \& Kubernetes 06](#docker--kubernetes-06)
  - [Docker Compose : 우아한 다중 컨테이너 오케스트레이션](#docker-compose--우아한-다중-컨테이너-오케스트레이션)
    - [Docker Compose?](#docker-compose)
      - [Docker Compose Files](#docker-compose-files)
    - [Compose 파일 만들기](#compose-파일-만들기)


# Docker & Kubernetes 06

## Docker Compose : 우아한 다중 컨테이너 오케스트레이션

- 여러 컨테이너를 같은 네트워크내에 각각의 볼륨을 갖도록 하여 환경을 구성하는건 도커의 기능을 활용하기 아주 좋지만, 너무 많은 설정과 코드가 필요하다.
- 이때 다중 컨테이너 설정을 편리하게 해주는 **Docker Compose** 등장

### Docker Compose?

- `docker build ..`와 `docker run ..`을 대체할 수 있는 도구

- 한개의 **설정 파일**과 **오케스트레이션 커맨드**를 통해 편리하게 컨테이너를 관리할 수 있다.

- Dockerfile, 이미지, 컨테이너를 대체하는게 아닌 단일 호스트에서 여러 컨테이너를 관리하는 **도구** 이다. 새로운 개념 요소가 추가되는게 아님!! 여러 기존 요소를 재조합하는것

#### Docker Compose Files

- 도커 컴포즈 파일에는 아래와 같은 사항이 들어간다
  
  - Services(Containers) 
    
    - Published Ports
    
    - 환경 변수
    
    - 볼륨
    
    - 네트워크

### Compose 파일 만들기

- `docker-compose.yaml`과 같이 yml 파일로 생성한다.

- ```yaml
  version: "0.0"
  services: 
    container1:
      image: 'imagename'
      volumes:
        - data:/data/db
      env_file:
        - ~~ 
    container2:
      ~~
  volumes:
    사용하는볼륨이름:
  ```
  
  - `docker_compose`파일에서는 따로 네트워크 설정을 안해줘도 된다.
    - 컴포즈 파일이 실행되면서 모든 서비스를 자동생성된 디폴트 네트워크에 추가한다.
  - 서비스에서 볼륨을 사용할 시, `services`와 같은 들어쓰기 레벨에 `volumes`로 사용한 볼륨을 명시해줘야한다. 이를 통해 `docker compose`가 사용 볼륨을 인지한다.

### Docker compose의 Up과 Down

- `docker-compose up` : `docker-compose.yaml`파일의 설정내용대로 서비스들을 실행

- `docker-compose down` : 컴포즈 실행을 중지한다.
  
  - `--rm`이 디폴트로 관련 컨테이너는 삭제된다.
  
  - 중지한다고 관련 볼륨들이 삭제되는건 아니다.

### 다중 컨테이너로 작업하기

- backend 컨테이너를 추가해보자
  
  ```yaml
    backend:
      build: ./backend #해당 경로에 dockerfile을 찾고 이미지를 빌드함
      ports:
        - "80:80"
      volumes:
        - logs:/app/logs # 명명 볼륨- 최상위 볼륨에 추가해야됨
        - ./backend:/app # 바인드 마운트       
        - /app/node_modules
      env_file:
        - ./env/backend.env
      depends_on:
        - mongodb # 종속성 관리
  ```
  
  - `build` 를 통해 image를 지명할 필요없이, 빌드 이미지가 바로 사용된다.
  
  - `ports`로 외부 포트와 내부 포트를 지정한다.
  
  - `depends_on`로 컨테니어간 종속성을 관리할 수 있다. 위 backend 컨테이너는 mongodb 컨테이너가 준비되면 실행이 된다. 
  
  - `docker ps`로 compose에 의해 실행된 컨테이너를 확인하면
    ![](C:\Users\seho2\AppData\Roaming\marktext\images\2022-12-16-23-13-18-image.png)
    이와 같다.
    
    - docker-compose에 의해 생성된 이름일 뿐이다.
    
    - 위의 `docker-compose.yaml`에서 지명한 서비스(컨테이너)이름은 소스코드내에서 사용 가능하다.

- frontend 컨테이너를 추가해보자.
  
  ```yaml
    frontend:
      build: ./frontend
      ports:
        - "3000:3000"
      volumes:
        - ./frontend/src:/app/src
      stdin_open: true
      tty: true
      depends_on:
        - backend
  ```
  
  - `-it`와 같은 인터렉티브 모드를 위해 `stdin_open`, `tty` 옵션을 추가한다.
    - 해당 예제에서는 프론트엔드에서 React를 활용하여 해당 라이브러리의 특성에 의해 인터렉티브 모드를 활성화한다. 

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
