- [IP and IP Packet](#ip-and-ip-packet)
  - [IP and IP Packet](#ip-and-ip-packet-1)
    - [한계](#한계)
---
# IP and IP Packet

## IP and IP Packet

> **인터넷 프로토콜**(**IP**, **I**nternet **P**rotocol)은 송신 [호스트](https://ko.wikipedia.org/wiki/%ED%98%B8%EC%8A%A4%ED%8A%B8_(%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC) "호스트 (네트워크)")와 수신 호스트가 정보를 주고받는 데 사용하는 정보 위주의 규약(프로토콜, Protocol)이며, OSI 네트워크 계층에서 호스트의 주소지정과 패킷 분할 및 조립 기능을 담당한다. 줄여서 **아이피**(IP)라고도 한다. - 위키백과

- `IP`의 정보는 패킷(Packet)이나 데이터그램(Datagram)이라는 단위로 분할되어 전송된다.

- `IP`는 지정한 IP 주소(IP Address)에 패킷으로 데이터를 전달한다.

### 한계

- **비연결성(connectionlessness)** : 패킷을 받을 대상이 없거나, 서비스 불능 상태여도 클라이언트는 서버의 상태를 파악할 방법이 없으므로 패킷을 수신 가능 여부에 상관없이 전송한다.

- **비신뢰성(unreliability)** : 서버까지의 데이터 전송 흐름에서 데이터 소실이 발생하여도 클라이언트는 이를 파악할 방법이 없다. 큰 용량의 데이터의 경우 분할되어 여러 다른 노드를 거쳐 전송되어 취합되는데, 이때 클라이언트가 의도하지 않는 순서로 패킷에 도착할 수 있다.

- 이러한 `IP`의 한계를 개선하기 위해 `TCP`와 같은 프로토콜이 제안되었다.

--- 

- 레퍼런스

> [전송 제어 프로토콜 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%A0%84%EC%86%A1_%EC%A0%9C%EC%96%B4_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C)
> 
> [[네트워크] 인터넷 프로토콜 (IP, TCP/UDP, HTTP) — 경험은 성장](https://vvs1.tistory.com/99)
