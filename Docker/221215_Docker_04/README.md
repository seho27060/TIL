- [Docker \& Kubernetes 04](#docker--kubernetes-04)
  - [네트워킹 : 컨테이너 통신](#네트워킹--컨테이너-통신)
    - [WWW 통신 컨테이너](#www-통신-컨테이너)
    - [호스트 머신과 컨테이너 간 통신](#호스트-머신과-컨테이너-간-통신)
    - [컨테이너 끼리 통신](#컨테이너-끼리-통신)
    - [Docker Network](#docker-network)


# Docker & Kubernetes 04

## 네트워킹 : 컨테이너 통신

- 총 3가지의 경우의 수가 있다.
- 해당 강의에서는 node.js  애플리케이션과 mongodb 데이터베이스를 예시로 각각의 예시를 살펴본다.

### WWW 통신 컨테이너

- 컨테이너 내 애플리케이션과 다른 웹사이트의 API와의 통신

- 인증, 인가가 필요없다면 별 다른 설정없이 작동함!

### 호스트 머신과 컨테이너 간 통신

- 호스트 머신의 데이터베이스와 도커의 컨테이너간 통신
- `mongodb://host.docker.internal:port ~`와 같은 도커를 위한 특별한 url로 내부 db에 접근 가능하다.
  - 웹서버에 올리면 `mongdb`는 `http`로 대체해야한다.

### 컨테이너 끼리 통신

- 데이터베이스 컨테이너와 애플리케이션 컨테이너간 통신

- 1개의 컨테이너는 1개의 관심사를 갖는다 라는 구조가 모범적인 컨테이너 구조임.

- 통신 흐름
  
  - mongodb 공식 이미지로 mongodb 컨테이너 생성
  
  - `docker container inspect mongodb`로 해당 컨테이너의 IP 주소 확인 후 애플리케이션 컨테이너의 api에 연결
    
    ```javascript
    mongoose.connect(
      'mongodb://몽고디비ip주:27017/swfavorites',
      { useNewUrlParser: true },
      (err) => {
        if (err) {
          console.log(err);
        } else {
          app.listen(3000);
        }
      }
    );
    ```
  
  - 이제 도커내의 DB 컨테이너와 애플리케이션 컨테이너 끼리 통신이 가능하다!
    
    - 이때 mongdb의 ip주소는 생성때마다 바뀌므로 하드코딩을 해야하는 문제 발생
    
    - **컨테이너 네트워크**로 컨테이너의 가변적인 ip 주소로 매번 수정하지 않고 연결가능하다.

### Docker Network

- 도커의 네트워크 기능을 통해 컨테이너간의 통신이 가능하다.

- `docker run --network my_network ...`로 컨테이너끼리 통신이 가능한 네트워크 생성 
  
  - `docker run -d ~~ --network 네트워크이름 이미지이름`을 통해 `--network` 옵션을 추가하여 컨테이너 생성시 네트워크를 연결한다.
    
    - 만약 컨테이너를 외부에 노출할 계획이 없다면 포트 번호를 **게시(publish)**할 필요가 없다.(옵션에 `-p` 필요 X)
  
  - 이제 연결이 필요한 애플리케이션에서 **docker network의 이름**을 url 에 할당하면 된다. 
    
    - `mongodb://연결할네트워크이름:27017/swfavorites` . 이를 통해 유동적인 IP 주소를 자동으로 연결이 가능하다.

- 하지만 db 컨테이너의 재시작 시 데이터가 초기화되는 문제가 있다.
  
  - 볼륨을 통해 해결 가능하다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
