- [Computer Science](#computer-science)

- [네트워크 통신](#네트워크-통신)
  - [멀티쓰레딩 vs 분산 시스템](#멀티쓰레딩-vs-분산-시스템)
    - [TCP/ IP Network Model](#tcp-ip-network-model)
  - [Layer 1 - Data Link](#layer-1---data-link)
  - [Layer 2 - Internet](#layer-2---internet)
  - [Layer 3 - Transport](#layer-3---transport)
  - [Layer 4 - Application](#layer-4---application)
  - [Client Server Request Example](#client-server-request-example)

# Computer Science

## 네트워크 통신

#### 멀티쓰레딩 vs 분산 시스템

- 1개의 프로세스 내부에서 공유 메모리로 각각의 쓰레드를 실행하는 멀티쓰레드에서는 쓰레드간 통신이 아주 용이하다.

- 분산 시스템의 경우 공유 메모리가 없기때문에 노든간 통신이 쉽지않음
  
  - 따라서 통신을 위해 **네트워크**를 활용한다.

### TCP/ IP Network Model

- 4계층으로 구성된 네트워크 모델
  
  | Layer | Name        |
  | ----- | ----------- |
  | 4     | Application |
  | 3     | Transport   |
  | 2     | Internet    |
  | 1     | Data Link   |

- 각 계층은 관련 프로토콜을 사용하여 **다른 네트워크의 같은 계층**과 통신할 수 있다.

- 계층이 낮을수록 물리적 하드웨어와 가까우며, 계층이 높을수록 사용자, 개발자와 가깝다.

#### Layer 1 - Data Link

- 하드웨어에 직첩 요청하는 사항을 담당

- 단일 링크로 연결된 두 지점 사이에서 데이터를 물리적으로 전달

- 맡은 역할로는
  
  - 데이터 캡슐화, 인코딩
  
  - 데이터 흐름 제어
  
  - 오류 감지와 수정
  
  - 등등

- **Ethernet Protocol** : 데이터 패킷을 하나의 프레임으로 만들어서 장치의 MAC 주소를 사용해 다른 주소로 패킷을 전달한다. 

#### Layer 2 - Internet

- 데이터 링크로부터 정보를 받아 사용자에게 좀더 가까운 작업을 수행한다.

- 여러 네트워크를 통해 데이터를 전송, 데이터를 전송한 컴퓨터에서 받은 패킷을 라우팅하는 일을 한다.

- 해당 계층에서는 데이터가 어떤 IP를 갖는 네트워크로 이동하는게 끝이다. 전송 데이터가 어떤 역할을 하며 어떤 프로그램으로 전송되는지는 알 수 없다.

- **Internet Protocol(IP)** : 네트워크가 갖는 부호이며 패킷이 네트워크를 통해 소스 호스트에서 대상 호스트로 이동할 수 있게한다.

#### Layer 3 - Transport

- 한 시스템의 프로세스에서 다른 시스템의 프로세스로 메시지와 데이터를 전송한다.

- 소켓의 16비트 포트로 서로를 구별한다.
  
  - 수신 포트는 목적지의 응용 프로그램에 의해 미리 정해지지만
  
  - 발송 포트는 사용한 포트 중 원하는 포트를 선택하여 즉흥적으로 정해진다.

- 우편 배달에 비유하면 포트 번호는 아파트의 주소와 받는 사람의 이름.

- **User Datagram Protocol(UDP)**
  
  - 연결없는(Connectionless) 프로토콜으로 신뢰할 수 없고, 메시지가 손실되거나 중복될수있으며 순서가 바뀔 수 있다.
    - **간편함**이 신뢰성보다 더 중요한 경우 사용된다.
    - 비디오, 오디오 스트리밍, 온라인게임
  - 크기가 제한적인 데이터그램(Datagram)이 기본 단위이다.
  - 1개의 컴퓨터가 로컬 네트워크에 속한 여러개의 컴퓨터에 단방향으로 메시지를 보내는 **브로드캐스팅(Broadcasting)** 이 가능하다.
    - 수신자가 발신자 정보를 모르는 연결없는(Connectionless) 통신

- **Transmission Control Protocol(TCP)**
  
  - UDP와 반대로 데이터 손실, 복제, 중복이 발생하지 않는 **신뢰성**있는 통신이 가능하다.
  
  - 정확한 2개의 지점이 연결(Connection)된다.
    
    - 데이터가 전송되기 전에 연결이 이뤄져야 하며
    
    - 전송이 끝나면 프로토콜은 종료된다. 
  
  - UDP 프로토콜과 달리 TCP는 개별 패킷이 아니라 이진화 된 데이터 값을 연속적으로 수신한다.
  
  - 2개의 송신 컴퓨터가 같은 대상 IP와 포트에 연결하더라도 데이터 흐름은 두 개의 개별 소켓(Socket)으로 분리되어 완전히 별도로 처리된다.

#### Layer 4 - Application

- 여러 가지 목적으로 다양한 프로토콜이 사용된다.
  
  | Protocol                            | 목적                    |
  | ----------------------------------- | --------------------- |
  | FTP(File Transfer Protocol)         | 웹을 거쳐 파일 전송           |
  | SMTP(Simple Mail Transfer Protocol) | 이메일 수신 및 송신           |
  | DNS(Domain Name System)             | host name을 IP 주소로 변환  |
  | HTTP(Hypertext Transfer Protocol)   | 문서, 비디오, 사운드, 이미지를 전송 |

#### Client Server Request Example

- 클라이언트와 서버라는 두개의 노드 간의 데이터 송-수신 예시
  
  - 두 노드는 서로 다른 네트워크에서 라우터를 통해 연결되어 있다.

- 클라이언트 
  
  - Application Layer에서 HTTP를 이용하여 메시지 생성
  
  - Transport Layer에서 TCP로 클라이언트 포트(송신 포트)와 서버 포트(수신 포트)를 헤더에 추가한다.
  
  - Internet Layer에서 IP 프로토콜로 클라이언트와 서버의 IP 주소를 헤더에 추가한다. 클라이언트 포트는 이후 응답할때 사용한다.
  
  - Data Link Layer에서 이너넷 프로토콜로 클라이언트와 서버의 MAC주소를 헤더에 추가한다.
  
  - 레이어들로 구성된 하나의 프레임이 완성되며 라우터에 도착할때까지 이진화된 형태로 네트워크를 통해 송신된다.

- 라우터
  
  - 이더넷 프로토콜의 헤더를 제거후 IP 프로토콜로 수신 IP 주소를 파악하여 다음에 전송될 네트워크를 파악한다.
  
  - 라우터의 MAC 주소를 발신지로, 서버의 MAC 주소를 수신지로 하는 새로운 이더넷 프로토콜 헤더를 추가한다.

- 서버
  
  - 이더넷 프로토콜을 통해 해당 패킷이 실제로 해당 서버에 속하는 패킷이 맞는지 확인한다.
  
  - IP 헤더를 통해 응답을 보낼 IP를 확인한다.
  
  - Transport Layer에서 수신 포트를 통해 어떤 응용 프로그램과 소켓이 해당 포트를 수신 중인지 확인한다.
  
  - HTTP 프로토콜로 메시지(소스코드,요청)은 프로그램에 전달된다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
