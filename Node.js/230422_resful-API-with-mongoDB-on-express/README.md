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

- `/model` 디렉토리에 db의 커넥터와 url, 컬렉션을 설정하는 `index.js`와 db의 스키마를 정의하는 `model.js`를 생성한다.

#### router와 Controller

- CRUD RESTful API가 작성되는 `router.js`
  
  - `HTTP` 요청과 `url`을 `controller.js`의 메서드와 매핑한다.

- `API`의 처리 로직이 작성되는 `controller.js`
  
  - `url`에 따른 처리 별 로직이 작성된다.
  
  - 실제 `db`와의 요청과 데이터에 대한 처리를 완료하여 `router.js`의 매핑된 `router`에 반환한다.
  
  - 컬렉션이 정의된 `index.js`를 통한 생성한 객체는 `Spring`에서의 `Entity`를 `Repository`에서 기본적으로 제공하는 함수(`.find`, `.findById` 등)을 사용할 수 있다.

---

- 레퍼런스

> 
