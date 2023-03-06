- [TCP Handshake And UDP](#tcp-handshake-and-udp)
  - [TCP Handshake](#tcp-handshake)
    - [Handshake](#handshake)
        - [3-way Handshake](#3-way-handshake)
        - [4-way Handshake](#4-way-handshake)
  - [UDP](#udp)
    - [TCP vs UDP](#tcp-vs-udp)
---
# TCP Handshake And UDP

## TCP Handshake

### Handshake

- `TCP`가 장치들 사이에서 논리적인 접속을 성립(establish)하거나 종료(terminate)하기 위한 작업

- 연결을 위한 `3-way Handshake`와 종료를 위한 `4-way Handshake`가 있다.

- 해당 과정에서는 

##### 3-way Handshake

- `TCP/IP` 를 이용한여 통신을 하는 프로그램이 데이터 전송 전 연결을 위한 작업 과정이다.

- 3가지 단계로 구성되어 있으며 아래와 같다.
  
  ![](https://upload.wikimedia.org/wikipedia/commons/8/8a/Tcp-handshake.png?20051221162333)
  
  *`SYN` : synchronize sequence numbers, *`ACK`: acknowledgment
  
  1. `Client -> Server : TCP SYN` - 클라이언트가 서버에 접속을 요청하는 `SYN` 패킷을 보낸다. 클라이언트는 패킷 전송 후 `SYN/ACK` 응답을 기다리는 `SYN_SENT` 상태가 된다.
  
  2. 서버는 `SYN` 요청을 받고 클라이언트에 요청을 수락한다는 `ACK`, `SYN flag`가 설정된 패킷을 발송한다. 서버는 클라이언트의 `ACK` 응답을 기다리는 `SYN_RECEIVED` 상태가 된다.
  
  3. 클라이언트가 서버에 `ACK` 을 전송후 연결이 완료된다. 해당 시점부터 데이터의 수-송신이 가능하다. 서버의 상태는 `ESTABLISHED`가 된다.

##### 4-way Handshake

- `TCP/IP` 의 연결에서 세션을 종료하기 위해 수행되는 절차이다.

- 4단계로 구성되어 있으며 아래와 같다.
  
  ![](https://wiki.wireshark.org/uploads/__moin_import__/attachments/TCP-4-times-close/TCP-close-diagram.png)
  
  1. `Client -> Server : FIN flag` - 클라이언트가 연결을 종료하겠다는 `FIN flag`를 서버에 전송한다.
  
  2. `Server -> Client : ACK` - 서버는 요청 "확인" 후 확인 메세지를 클라이언트에 전송한다. 클라이언트-서버 간 통신이 끝날때까지 기다리는데 이를 `TIME_WAIT` 상태라고 한다.
  
  3. `Server -> Client : FIN flag` - 서버가 통신이 끝나면 연결 종료를 알리는 `FIN flag`를 클라이언트에 전송한다.
  
  4. 클라이언트는 `FIN flag`를 확인하고, 서버에 확인 메세지를 전송한다.

## UDP

> IP 프로토콜에 Port, 체크섬 필드 정보만 추가된 단순한 프로토콜

### TCP vs UDP

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
  
  | TCP           | UDP               |
  |:-------------:|:-----------------:|
  | 연결지향형 프로토콜    | 비 연결지향형 프로토콜      |
  | 전송 순서 보장      | 전송 순서 보장 X        |
  | 데이터 수신 여부 확인함 | 데이터 수신 여부 확인하지 않음 |
  | 신뢰성 높지만 속도 느림 | 신뢰성 낮지만 속도 빠름     |

--- 

- 레퍼런스

> https://velog.io/@nnnyeong/Network-TCP-3-way-4-way-Handshake
