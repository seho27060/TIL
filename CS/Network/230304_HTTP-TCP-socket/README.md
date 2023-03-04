# HTTP TCP socket

## HTTP TCP socket

- `Network`의 큰 축을 이루는 `HTTP`통신 , `TCP`통신 그리고 `socket`에 대해 알아보자.

### HTTP 통신

> `HTTP` 란 HyperText Transfer Protocol의 약자로 `HTML` 파일을 전송하는 프로토콜이라는 의미를 갖는다.
> 
> `HTTP` 통신은 웹 브라우저에서 일어나며, `HTML`뿐만 아니라 `JSON`, 이미지 파일등을 전송한다.

- 요청(Question)에 대해 반드시 응답(Answer)이 존재하는 **비연결지향 단방향 통신**
  
  - `HTTP` 통신을 사용하는 프로그래밍을 `HTTP` 프로그래밍이라고 한다.

- `OSI 7 Layer`나 `TCP/IP 4 Layer`의 응용 계층(Application Layer)에 해당하는 프로토콜이다.

-  `HTTP/1.1`, `HTTP/2`는 `TCP` 통신에 기반하여 작동하며, `HTTP/3`는 `UDP` 기반 프로토콜이다.
  
  - `TCP/IP`에 기반하기 때문에 `Socket`을 통신에 사용하지만, `TCP` 통신과 구분되는 소켓을 사용하므로 `TCP`통신과는 다르게 단방향으로 작동한다.

- 요청-응답의 클라이언트-서버 구조에서 `HTTP`는 서버가 클라이언트의 상태를 보존하지 않는 **무상태(Stateless) 프로토콜**이다.

- `URL`을 요청하여 그에 대한 반환값을 받는 웹 서비스나, `REST API` 가 `HTTP` 통신의 예시이다.

### TCP 통신(socket 통신)

> `TCP/IP Layer`에서 `Handshake`라는 과정으로 클라이언트-서버가 서로 통신 가능한 상태로 인증 후 통신을 유지하는 **연결지향적 양방향 통신**

- `Client -> Server`, `Server -> Client`와 같은 양방향성을 갖으며, 클라이언트 입장에서 봤을때, 요청이 없음에도 응답을 받을 수 있다.

- 연결지향적인 특성에 의해 실시간 통신에 용이하다.
  
  - 그에 따라 `HTTP` 통신에 비해 많은 비용이 발생한다.

- 연결에서는 `Socket`을 활용하며 `TCP` 프로토콜 기반의 연결을 **소켓 통신**이라고도 한다.
  
  - 소켓 통신을 사용하는 프로그래밍을 소켓 프로그래밍이라고 한다.

#### Socket

> 프로그램이 네트워크에서 데이터를 주고 받을 수 있도록 네트워크 환경에 연결할 수 있게 만들어진 연결부(인터페이스)

- 일반적으로 `TCP/IP` 프로토콜을 사용한다.

- `TCP/IP 4 Layer`의 전송 계층에 속한다.

- `IP`와 서비스 `Port`를 통해 소프트웨어와 소프트웨어를 연결하여 데이터 통신을 수행한다.

- `Socket`을 사용한 `Socket`프로그래밍은 클라이언트와 서버간의 흐름으로 작동한다.

##### Socket API 실행 흐름

-  클라이언트와 서버의 실행흐름으로 구분한다.
  
  | 클라이언트                      | 서버                                                     |
  | -------------------------- | ------------------------------------------------------ |
  | 1. 클라이언트 소켓 생성             | 1. 서버 소켓 생성                                            |
  |                            | 2. 바인딩(Bind) - 여러 프로세스들에 고유한 포트번호를 할당하여 분리한다.          |
  |                            | 3. 클라이언트 연결 요청 대기                                      |
  | 2. 연결 요청(Connection)       | 4. 클라이언트 연결 수립 - 동시에 새로운 소켓을 생성하여 클라이언트 소켓과 매핑하여 반환한다. |
  | 3. 데이터의 송수신(Send, Recieve) | 5. 데이터 송수신                                             |
  | 4. 소켓 닫기                   | 6. 소켓 닫기                                               |

---  

- 레퍼런스

> https://velog.io/@rhdmstj17/%EC%86%8C%EC%BC%93%EA%B3%BC-%EC%9B%B9%EC%86%8C%EC%BC%93-%ED%95%9C-%EB%B2%88%EC%97%90-%EC%A0%95%EB%A6%AC-1
> 
> [[소켓과 웹소켓] 한 번에 정리 (2) | 소켓과 웹소켓의 차이점, 웹소켓의 모든것, http-tcp-소켓의 상관관계](https://intrepidgeeks.com/tutorial/clean-the-socket-and-web-socket-at-one-time-2-the-difference-between-socket-and-web-socket-everything-about-web-socket-and-the-relationship-between-http-tcp-socket)
> 
> [HTTP 통신과 TCP 통신 그리고 웹 소켓에 대한 기본 개념 정리 | 기획하는 개발자](https://sooolog.dev/HTTP-%ED%86%B5%EC%8B%A0%EA%B3%BC-TCP-%ED%86%B5%EC%8B%A0-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%9B%B9-%EC%86%8C%EC%BC%93%EC%97%90-%EB%8C%80%ED%95%9C-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC/)
> 
> [HTTP 통신과 TCP 통신의 차이와 이해](https://moondongjun.tistory.com/34)
> 
> [HTTP 통신과 Socket 통신의 차이점 — Dev World](https://kotlinworld.com/75)
