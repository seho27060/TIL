[TOC]

# 분산 시스템에서의 HTTP 통신

- HTTP는 컴퓨터(노드)간 통신을 가능하게 하는 가장 편리하고 대중적이며 유연한 프로토콜

- HTTP를 활용할 경우 아래 계층은 거의 설정하지 않아 편리하다.

- 해당 내용에서는 분산 시스템 내에서의 통신에 다루기 때문에 기존 용어와 차이가 있다.(ex : 컴퓨터 -> 노드)

#### HTTP Transaction

- Request

- Reponse

- 클라이언트 노드의 요청에 서버 노드에 응답으로 HTTP Transaction이 완료된다.

### HTTP - Request Structure

- method : GET, POST...etc

- path : 라우팅할 수 있는 상대 경로

- Protocol Version

- HTTP Headers : key-value로 구성되어 메시지 내용이나 연결 지점 정보를 담고 있음

- Message Body

#### method

- 각각의 의미와 정의를 갖는 표준 메서드

- GET, POST, DELETE...etc

- GET 핸들러에 포함되어야 하는 속성
  
  - Safe - 조회의 기능만 하기 때문에 side effects가 없다.
  
  - Idempotent(멱등성) - 동일한 작업에는 동일한 결과를 반환한다.
  
  - 어떤 Body도 포함하지 않는다.
  
  - 분산 시스템에서의 사용예시
    
    - 리더 노드의 워커 노드에 대한 Health check
    
    - 마이크로서비스에서 클라이언트 서비스에서 1개의 HTTP 요청으로 2개의 다른 서버에 요청을 보낼 수 있다.

- POST 핸들러에 포함되어야 하는 속성
  
  - Body - payload의 기능을 하기 위한다.
    
    - 요청에 의한 서버의 복잡한 연산 side effects가 발생할 수 있다.
    
    - 서로 다른 노드간에 메시지를 전달하는 데 용이하다.

#### Path

- 요청을 위한 경로(url)로 경로내에서는 요청에 필요한 정보가 포함 될 수 있다.

#### Protocol Version

- HTTP/1.1 - 클라이언트와 서버간의 TCP 연결이 1개일 경우, 1개의 요청에 대한 응답(HTTP Transaction)이 완료되지 않으면 다음 요청을 수행할 수 없다.
  
  - 여러개의 요청을 위해선 많은 연결이 필요하므로 비용이 증가한다.

- HTTP/2 - 1.1 버전과는 다르게 1개의 TCP연결에도 여러개의 요청과 응답이 Sequential하게 오갈 수 있다.

#### HTTP Headers

- key-value로 구성된 다양한 목적을 갖는 정보가 포함되어 있다.

- 수신 서버는 헤더의 내용을 토대로 메모리 할당과 같은 사전 작업을 진행한다.
  
  - Message Body의 길이를 뜻하는 `Content-Length`, Message의 type을 뜻하는 `Content-Type`, byte로 변환된 메세지에 적용된 압축 알고리즘인 `Content-Encoding`
  
  - `X-Debug`, `X-Experiment`, `X-Test`와 같은 헤더를 통해 커스터마이징이 가능하다.

#### Message Body

- 원하는 내용 어떤 것이든 담을 수 있다.

- 데이터 객체 또한 포함이 가능하다.

### HTTP - Response Structure

- Request Structure에 HTTP Status Code를 포함한다.

---  

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
