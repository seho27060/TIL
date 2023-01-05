- [Distributed\_System\_05](#distributed_system_05)
  - [분산 시스템 내 통신](#분산-시스템-내-통신)
    - [분산 시스템에서 메시지를 전송하는 방법](#분산-시스템에서-메시지를-전송하는-방법)
      - [서버 실행 시나리오](#서버-실행-시나리오)
      - [메시지 전달 방식](#메시지-전달-방식)
    - [복잡한 형태의 데이터 전송 - 직렬화와 역직렬화](#복잡한-형태의-데이터-전송---직렬화와-역직렬화)


# Distributed_System_05

## 분산 시스템 내 통신

### 분산 시스템에서 메시지를 전송하는 방법

#### 서버 실행 시나리오

- 서버 성공 시나리오
  
  - 클라이언트의 요청
  
  - 서버 수신, 실행, 클라이언트에 응답

- 서버 실패 시나리오
  
  - 서버의 응답 과정 중 네트워크 실패(Network Failure)
  
  - 서버에서 실행 작업 전후로 실패(Server  Crash)
  
  - 서버에서 요청 수신 실패(Server Crash Before Receiving the Request)

#### 메시지 전달 방식

- 서버 실패 시나리오를 예방하기 위한 다양한 전달 방식

- At Most Once Semantics(딱 한번 전달) : 클라이언트는 서버에 요청을 단 한번 보낸다.
  
  - 서버가 수신하지 못하든, 서버가 작업하지 못하든(Server Crash) 단 한번만 보낸다.

- At Least Once Semantics(최소 한번 전달) : 클라이언트는 서버에 요청 수신 응답을 받을때까지 요청을 보낸다.
  
  - 이와 같은 방식은 멱등(Idempotent) 작업에 적합하다.

- Idempotent Operations(멱등 작업) : 여러번 수행해도 같은 작업, 같은 결과를 응답하는 작업
  
  - GET..etc
  
  - 여러번 수행해도 결과가 같기 때문에 At Least Once Semantics에 적합하다.

- non Idempotent Operations에 멱등성을 인공적으로 주입하는건 매우 복잡하고 까다로운 작업이다.
  
  - 느슨한 결합과 확장 가능한 형태의 분산시스템에서 이러한 복잡함은 그에 대한 대가로 받아들여야한다.

### [복잡한 형태의 데이터 전송 - 직렬화와 역직렬화](https://github.com/seho27060/TIL/tree/master/CS/Network/221228_Serialization-And-Deserialization)

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
