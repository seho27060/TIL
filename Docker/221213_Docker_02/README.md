- [Docker 02](#docker-02)
  - [Docker 이미지 \& 컨테이너 : 코어 빌딩 블록](#docker-이미지--컨테이너--코어-빌딩-블록)
      - [Images](#images)
      - [Containers](#containers)
    - [Finding/ Creating Images](#finding-creating-images)
      - [Image는 readonly](#image는-readonly)
    - [이미지 레이어](#이미지-레이어)
      - [레이어 기반 아키텍쳐](#레이어-기반-아키텍쳐)
    - [이미지 \& 컨테이너 관리](#이미지--컨테이너-관리)
      - [Detached \& Attached 컨테이너](#detached--attached-컨테이너)
      - [인터렉티브 모드 실행](#인터렉티브-모드-실행)
      - [이미지 \& 컨테이너 삭제하기](#이미지--컨테이너-삭제하기)
      - [컨테이너에/로부터 파일 복사하기](#컨테이너에로부터-파일-복사하기)
      - [컨테이너와 이미지에 태그, 이름 지정](#컨테이너와-이미지에-태그-이름-지정)


# Docker 02

## Docker 이미지 & 컨테이너 : 코어 빌딩 블록

#### Images

- 템플릿, 컨테이너의 블루프린트/ 코드와 코드실행환경이 포함된 

- 코드와, 코드 실행을 위한 도구가 포함됨

- 1개의 이미지로 여러개의 컨테이너를 실행할 수 있다.

#### Containers

- 애플리케이션, 웹사이트, 서버, 환경 등 모든 것을 포함하는 패키지

- 소프트웨어 실행 유닛

- 이미지의 인스턴스

### Finding/ Creating Images

1. Docker hub에 pre-built인 **공식 이미지**를 가져와 사용하기
   
   ```cmd
   docker run node
   ```
   
   Docker hub에서 자동으로 node image를 불러옴
   
   ![](C:\Users\seho2\AppData\Roaming\marktext\images\2022-12-13-17-09-03-image.png)
   
   동일한 Image `node`로 다른 2개의 컨테이너(`quirky_burnell`,`wizardly_torvalds`)생성

2. 사용자가 필요한 조건의 custom image 생성하기
   
   1. 애플리케이션 생성
   
   2. Dockerfile 생성
      
      ```dockerfile
      FROM node # 베이스 이미지 파일 설정 
      
      WORKDIR /app # working directory 설정 
      
      COPY . /app # workdir의 모든 파일을 /app 로 복사한다.
      
      RUN npm install # 이미지 생성시 실행
      
      EXPOSE 80 # 컨테이너 내부에서 수신 대기중인 포트를 외부로 알린다.
      
      CMD ["node", "server.js"] # 이미지를 기반으로 컨테이너 시작시 실행
      ```
   
   3. `docker -p 3000:80 dockerId` 와 같은 명령어로 컨테이너 실행
      
      - `EXPOSE`에서 포트 번호를 80으로 "명시"했는데, 이는 문서화에만 그친다. 결국 노출되는 포트는 명령어에서 지정된 포트로 노출된다.

#### Image는 readonly

- 수정사항이 생겨 애플리케이션에 반영하면 이전에 생성된 image는 어떤 상태일까?
  - 수정사항이 반영되지 않는다! 새로운 image를 생성후 다시 빌드해야한다.

### 이미지 레이어

#### 레이어 기반 아키텍쳐

- Dockerfile의 1줄의 명령어는 1개의 레이어로 치환된다.
  
  - 모든 각각의 레이어는 캐시로 저장된다.

- 애플리케이션 또는 환경의 변경사항이 없다면, 새로운 빌드에 이전에 캐싱된 레이어를 사용한다.
  
  - 레이어 A에서 변경사항이 발견된다면, **그 이후의 모든 레이어는 새롭게 실행**된다.(이전 캐싱 레이어 사용X)

- 도커는 새로운 빌드가 필요한 이미지만 부분적으로 생산한다.
  
  - 이미지 생성 시간의 효율적 관리

- 이미지 기반 레이어를 이해했다면 이전의 Dockerfile 예시를 최적화할 수 있다.
  
  ```dockerfile
  FROM node
  
  WORKDIR /app
  # 우선 npm install을 위한 package.json을 미리 COPY
  COPY package.json /app
  # 필요 환경 실행
  RUN npm install
  
  COPY . /app
  
  EXPOSE 80
  
  CMD ["node", "server.js"] 
  ```
  
  - 이전에는 환경 변동이 없어도 코드 변동이 감지되면 무조건 재실행되기 때문에 불필요한 작업이었다. 
  - 하지만 미리 환경 변동을 확인함으로 최적화가 가능하다.

### 이미지 & 컨테이너 관리

- 이미지 태그, 리스트, 분석, 삭제

- 컨테이너 명명, 확인, 리스트, 삭제

- `docker --help`로 명령어 확인 가능

#### Detached & Attached 컨테이너

- Attached : 터미널과 실행중인 컨테이너를 연결. 컨테이너의 로그를 실시간 확인 가능. 실행 default
  
  > `docker attach container_name`으로 분리된 컨테이너와 연결할 수 있다.

- Dettached : 터미널을 실행 후 터미널과 분리한다. 
  
  > `docker run -d ~~` 로 컨테이너를 실행후 터미널과 분리 가능하다.

- `docker logs container_name`으로 각 컨테이너의 log를 확인 가능하다!

#### 인터렉티브 모드 실행

- `docker run -it container_id` 로 인터렉티브 모드가 실행 가능하다.
  
  - help를 통해 옵션값을 찾아보자.

- `docker start -a -i container_name`로 이전에 생성한 컨테이너를 attached로 interactive로 실행 가능하다.

#### 이미지 & 컨테이너 삭제하기

- 실행중이지 않은 이전에 생성된 컨테이너를 삭제해보자.
  
  - `docker rm container_name` : 컨테이너를 삭제한다. 실행중인건 끄고 삭제해야함 
  
  - 중지된 컨테이너 자동 제거하기
    
    - `docker run -p port1:port2 -d --rm image_id` : image_id를 detached로 실행하며, 실행 컨테이너가 중지하면 자동으로 제거한다.

- 실행중인 컨테이너가 없는 이미지를 삭제해보자
  
  - `docker images` : 이미지 목록 확인
  
  - `docker rmi image_id` : 이미지 삭제하기
    
    - 만약 해당 이미지로 만들어진 컨테이너가 있다면 연관 컨테이너 삭제 or 강제 삭제해야한다.
  
  - `docker image prune` : 컨테이너로 사용되지 않는 이미지를 삭제(prune : 가지치기) 한다.

#### 컨테이너에/로부터 파일 복사하기

- 컨테이너에  붙여넣기 
  
  - `docker cp from/. container_name:/to`

- 컨테이너로부터 붙여넣기
  
  - `docker cp from/. container_name:/to`

- 근데 컨테이너 크기가 엄청 큰거아니면 자그마한 수정사항에도 다시 빌드해서 해야할듯;

#### 컨테이너와 이미지에 태그, 이름 지정

- 컨테이너에 이름 지정
  
  - `docker run -p port:port --name STRING image_id` : STRING을 이름으로 하는 컨테이너 생성

- 이미지에 태그 지정
  
  - 베이스이미지에 태그를 추가하여 특정 버전, 구성을 선택하여 사용할 수 있다.
  
  - `FROM imageName:imageTag`
  
  - 또는 내가 원하는 태그를 추가하여 새로운 이미지를 생성할 수 있다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
