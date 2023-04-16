# REPL, NPM

## Read Eval Print Loop(REPL)

- **REPL**은 윈도우 커맨드, Linux Shell 처럼 사용자가 커맨드를 입력하면 시스템이 값을 반환하는 환경을 가르킨다.

- `Node.js`는 REPL 환경과 함께 제공되며 아래 기능을 수행한다.
  
  - Read : 유저의 값을 입력 받아 JavaScript 데이터 구조로 메모리에 저장.
  
  - Eval : 데이터를 처리(Evaluate)
  
  - Print : 결과값을 출력
  
  - Loop : Read, Eval, Print를 유저가 종료할때까지 반복

- `Node.js`의 `REPL` 환경은 자바스크립트 코드를 테스팅, 디버깅할때 유용하게 사용된다.

## Node Package Manager(NPM)

- 아래 두 주요기능을 갖는다.
  
  - NPMSearch에서 탐색 가능한 `Node.js` 패키지/ 모듈 저장소
  
  - `Node.j` 패키지 설치 및 버전/ 호환성 관리를 하는 커맨드라인 유틸리티

- 기본적으로 `npm`은 모듈을 로컬모드로 설치한다.
  
  - 해당 디렉토리 내에서 `node_modules`라는 폴더에 저장한다.
  
  - 글로벌 모드로 설치시 시스템 디렉토리에 할당되어 설치가 진행된다.

- `package.json` 이라는 파일에 사용 패키지/모듈을 관리할 수 있다.

### 특징

> 왜 `JavaScript`로 서버를?..

- 정확히는 `Node.js`를 통한 `express`와 같은 프레임워크로 서버를 구성하는 것.

- 아래와 같은 이점을 취할 수 있다.
  
  - `Non-blocking I/O`
  
  - 짧고 쉬운 코드를 통한 빠른 개발
    
    - `V8` 자바스크립트 엔진을 사용한 빠른 코드 실행
  
  - 웹서비스 제작에 적합

- 실시간 채팅 서비스와 같이 실시간성(Realtime)이 필요한 서비스에서 많은 요청을 비동기적으로 수행하여 대기시간을 감축할 수 있다.
  
  - 입출력이 잦은
  
  - 데이터 스트리밍
  
  - 실시간 데이터를 다루는
  
  - `JSON` `API` 기반
  
  - `SPA`
  
  - 와 같은 분야에서 `Node.js`로 뛰어난 효율성을 달성할 수 있다.

---

- 레퍼런스

> [[Node.JS] 강좌 04편: REPL 터미널 | VELOPERT.LOG](https://velopert.com/235)
> 
> [[Node.JS] 강좌 05편: NPM | VELOPERT.LOG](https://velopert.com/241)
