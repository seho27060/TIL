- [Today's Keyword](#todays-keyword)
  - [Stateful vs Stateless](#stateful-vs-stateless)
    - [Stateful(상태 유지)](#stateful상태-유지)
      - [Stateful의 문제점](#stateful의-문제점)
    - [Stateless(무상태)](#stateless무상태)
      - [Stateless의 문제점](#stateless의-문제점)


# Today's Keyword

## Stateful vs Stateless

- 웹 서버에서 클라이언트와 서버간의 상태를 관리하는 방식을 의미하는 Stateful과 Stateless의 차이점을 알아보자

### Stateful(상태 유지)

- 클라이언트와 서버의 상태를 보존

- 서버는 클라이언트의 작업, 행동 등 서버에 전달하는 모든 행위를 기억(유지)한다.

- 온라인 뱅킹, 세션을 통한 로그인 유지, 쿠키 등이 이에 해당한다.

- 예시 - TCP의 3-way handshaking
  
  1. 클라이언트는 서버에 접속 요청 메세지 전달 - 요청 전송 상태
  
  2. 서버는 요청을 받고, 클라이언트에 요청을 수락하는 메세지 전달 - 요청 수령 상태
  
  3. 클라이언트는 서버에 수락 확인 메세지 전달 - ESTABLESHED 상태
  
  4. 세션의 상태가 ESTABLESHED가 됨으로, 서버와 클라이언트는 데이터를 주고 받을 수 있는 상태가 된다.

#### Stateful의 문제점

- Stateful한 상품 구매 서버 A가 감당하지 못한 트래픽으로 인해 작동 불능이 된다면 어떻게 될까.
  
  - 해당 서비스가 MSA 형태로 다른 백업 서버 B가 그 역할을 이어 받는다고 할때, 서버가 다운되는 시점에 **저장된 모든 클라이언트의 행위**(구매단계, 로그인정보 등)들은 초기화된다.
  
  - 서버 A에서 Stateful하게 클라이언트-서버 간 보존되는 상태들은 서버 B에서 보존되지 않는다.

### Stateless(무상태)

- 클라이언트와 서버 관계에서 서버가 클라이언트의 **상태를 보존하지 않음**

- 이때 서버는 단순히 요청에 적절한 응답을 보내는 역할만 수행한다.
  
  - 상태관리는 전적으로 클라이언트에게 책임이 있다.
  
  - 이로 인해 서버는 상태 유지의 부하를 줄일 수 있다.

- 통신에 필요한 모든 상태 정보들을 클라이언트가 가지고 있다가 서버와 통신에 데이터를 실어 보내는 구조

- 요청에 대한 응답은 어떤 서버든 같은 답을 내놓기 때문에 서버의 수평적 확장을 통해 대용량 트래픽 발생에도 대응할 수 있다.

- 예시 - UDP와 HTTP/ JWT
  
  - TCP의 handshaking 과정이 없다.
  
  - 요청을 보내고 요청 수신 확인, 요청 수락 전송 등의 단계가 없이 서버에서는 응답을 반환한다.

#### Stateless의 문제점

- 모든 요청에서 클라이언트의 상태를 포함한 정보를 같이 전송하기 때문에 Stateful보다 더 많은 비용(데이터)를 소모하게 된다.

---

- 레퍼런스

> [[WEB] 🌐 Stateful / Stateless 차이 💯 정리](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-Stateful-Stateless-%EC%A0%95%EB%A6%AC)
