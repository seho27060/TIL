[TOC]

# restful API with mongoDB on express

## mongodb와 express를 활용한 api 만들기

- `express` 상에서 `mongodb`를 `DB`로 두어 `CRUD`를 수행하는 `API`를 만들어보자.

- `API`는 흔히 그렇듯 `REST-ful`하게 만들도록 한다.

- 기본적인 형태를 취하므로 `module`은 최소로 사용한다.
  
  - `express` : 서버 작동을 위한 `Node.js` 프레임워크
  
  - `body-parser` : 요청을 parsing하는 `Node.js` 미들웨어
  
  - `mongoose`: `express`와 `mongoDB`를 연결하는 모듈
  
  - `cors` : CORS 설정에 사용되는 `express` 미들웨어

- 실행하는 기기에 `mongoDB`가 설치되어 있음을 가정한다.  

### 서버 구현

#### mongodb-server

- 서버를 실행하는 중축

- `express`, `bodyParser`, `db` 등과 같이 `API` 구현에 필요한 모듈을 객체에 할당하고

- 접근 `url`, `port` 등 접속 페이로드와

- `db` 설정을 마친 후
  
  - `mongoDB`를 사용하므로 `mongoose`를 활용한다.

- `.listen`으로 서버가 요청을 받을 수 있도록 실행(running)한다.

#### MongDB

- 

---

- 레퍼런스

> 
