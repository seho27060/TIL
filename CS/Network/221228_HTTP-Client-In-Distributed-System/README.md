- [분산 시스템에서의 HTTP 클라이언트](#분산-시스템에서의-http-클라이언트)
  - [HTTP Client](#http-client)
    - [통신 성능의 주요 기능](#통신-성능의-주요-기능)
      - [Synchronous Communication(동기식 통신)](#synchronous-communication동기식-통신)
      - [Asynchromous Communication(비동기식 통신)](#asynchromous-communication비동기식-통신)
      - [Connection Pooling](#connection-pooling)
      - [44](#44)


# 분산 시스템에서의 HTTP 클라이언트

## HTTP Client

### 통신 성능의 주요 기능

#### Synchronous Communication(동기식 통신)

- 1개의 요청에 대한 응답을 받을때까지 해당 쓰레드는 사용할 수 없다.

- 다음 요청을 위해서는 이전의 Transaction이 완료되어야함.

- 여러 노드에 동시 작업을 할 수없다!

#### Asynchromous Communication(비동기식 통신)

- 요청을 보낸 후 응답때까지 쓰레드를 중단하는게 아닌, 다음 요청을 보낼 수 있다.

- 요청을 모두 보낸 후 모든 응답을 대기후 취합할 수 있다.

#### Connection Pooling

- 특정 서버에 지속적으로 요청-응답이 이뤄질 경우, 1개의 요청-응답으로 연결을 끊고 필요할때 다시 연결하는건 비용적으로 큰 낭비다.
  
  - HTTP/2의 경우 자동으로 커넥션풀이 지원된다.

- 클라이언트, 서버 중 1개라도 HTTP/2 가 아니라면 직접 커넥션풀링을 설정해줘야한다.



#### 44

---  

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
