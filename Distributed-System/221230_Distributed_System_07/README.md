- [Distributed\_System\_07](#distributed_system_07)
  - [부하 분산(Load Balancing)](#부하-분산load-balancing)
    - [부하 분산 장치(Load Balancers)](#부하-분산-장치load-balancers)
    - [부하 분산 방식 및 알고리즘](#부하-분산-방식-및-알고리즘)
      - [부하 분산 방식](#부하-분산-방식)
    - [부하 분산과 네트워크 계층](#부하-분산과-네트워크-계층)
    - [HAProxy - 부하 분산 실습](#haproxy---부하-분산-실습)
      - [High Availability Proxy(HAProxy)](#high-availability-proxyhaproxy)


# Distributed_System_07

## 부하 분산(Load Balancing)

- 많은 작업량을 분산하여 처리하는 분산시스템
  
  - 유저에서 요청을 받는 User Facing Server가 한개이면 많은 유저 트래픽을 감당하지 못하는 문제가 발생한다.
  
  - 단일 실패 지점(Single Failure Point)이기 때문이다. 이때 User Facing Server가 죽는다면 고치기 전까지 서비스는 먹통이 된다.

### 부하 분산 장치(Load Balancers)

- 응용 프로그램 서버가 모인 클러스터에서 네트워크 트래픽을 분산해 주는 장치

- 서버에 업무를 분산시켜서 특정 응용 프로그램 서버의 병목(bottleneck) 현상을 예방한다.

- 응용 프로그램 서버의 상태를 지속적으로 감시하여 사용 가능한 서버에만 트래픽을 보낸다. -> 신뢰성과 가용성 확보

- 부하 분산 장치의 종류
  
  - 하드웨어 부하 분산 장치 : 부하 분산을 위해 설계된 하드웨어 장치. 
  
  - 소프트웨어 부하 분산 장치 : 다목적 컴퓨터에서 수행되는 로직으로 하나의 프로그램

### 부하 분산 방식 및 알고리즘

#### 부하 분산 방식

1. Round Robin(라운드 로빈) : Uniform Load Distribution으로, 모든 서버에 각각 1개의 요청씩 순차적으로 보낸다.

2. Weighted Round Robin(가중 라운드 로빈) : 각 서버에 보내는 트래픽의 양을 조절하여 보낸다.
   
   - 각 서버에 가중치를 할당하고 그에 따라 트래픽을 할당한다.
   
   - 각 서버의 하드웨어의 성능이 다르거나, 버전 업데이트 등으로 서버간 차이가 발생할때 사용한다.

3. Source IP Hash Motivation(소스 IP 해시) : 트래픽 분산 중 특정 사용자의 요청을 특정 서버에만 할당하는 방법
   
   - 장바구니와 같이 한 서버와의 세션을 유지해야 하는 경우
   
   - 요청에 대한 IP를 한개의 서버에 연결하여 요청을 분산, 유지한다.
- 문제 상황
  
  - 라운드 로빈 로드 밸런서에서 서버 1에는 적은 자원의 요청, 서버 2와 서버 3에는 많은 자원의 요청이 갈 경우. 모든 트래픽을 동일하게 분산하였다 하여도 **각 요청에서 요구하는 자원**이 다를 수 있다.
  
  - 위 3개의 방식은 모두 각 서버의 상황, 요청마다 다른 요구 자원 등을 고려하지 않았으므로, 이는 곧 클러스터 전체의 과부하를 불러 일으킨다.
  
  - 각 서버의 작업량을 적극적으로 모니터링하는 아래와 같은 해결책이 필요하다.
4. Least Connection(최소 연결) : 모든 서버가 처리할 요청이 이미 많은 상태로 인지한다.
   
   - 각 서버의 연결을 측정하여 가장 적은 연결을 갖는 서버에 작업을 할당한다.
   
   - 가장 작은 연결은 적은 부하를 갖는 서버로 인지함

5. Weighted Response Time(가중 응답 시간) : 각 서버에 주기적으로 상태 확인 요청을 보내 서버의 응답 시간을 측정한다.
   
   - 서버마다 측정된 응답 시간을 기반으로 부하 분산 알고리즘은 서버마다의 **가중치를 조정**한다.

6. Agent Based Policy(요원 기반 정책) : 요원(Agent)를 활용하여 백그라운드에서 서버의 부하를 모니터링한다.
   
   - CPU 사용률, 네트워트 트래픽의 요청과 응답, 디스크 작의 개수, 메모리 사용량 등등등
   
   - 자체적인 성능값을 측정하여 이를 기반하여 각 서버(노드)에 **최적의 작업량을 할당**한다.

### 부하 분산과 네트워크 계층

- OSI Model
  
  
  
  1. Physical
  
  2. Data Link
  
  3. Network
  
  4. Transport
  
  5. Session
  
  6. Presentation
  
  7. Application

- 부하 분산 장치가 트래픽을 검사하고 응용 프로그램 서버로 라우팅할 수 있는 계층
  
  - Layer 4, Transport 
    
    - 클라이언트로부터 TCP 패킷을 받아 부하 분산 방식에 따라 백엔드 서버로 전달
    
    - TCP 패킷만 확인하기 때문에 가장 비용이 적은 방식
  
  - Layer 7, Application
    
    - HTTP 메시지 헤더를 기반으로 라우팅
    
    - TCP패킷 뿐만아니라 HTTP헤더의 내용도 확인한다.
    
    - 로드 밸런서가 다양한 클러스터에 연결할때, HTTP헤더의 내용에 따라 각기 다른 부하 분산 방식을 사용하여 트래픽을 할당할 수 있다.

### HAProxy - 부하 분산 실습

#### High Availability Proxy(HAProxy)

- TCP/HTTP 계층에서 사용할 수 있는 신뢰성높은 고성능의 부하 분산 장치 

- 오픈소스로 부하 분산 기능의 업계 표준 

- 설정(Configuration) 파일을 기반으로 작업이 수행된다.

- Configuration File Structure
  
  - global section - 전체 분산 부하 과정을 위한 변수 정의
  
  - proxy section -  백엔드 서버로 들어오는 트래픽을 라우팅하는 모든 로직과 방식을 정의
    
    - default - 선택적으로 네트워크 프록시에 적용할 기본 매개변수를 설정 가능
    
    - frontend - 클라이언트로 들어오는 요청을 수신할 소켓과 해당 요청을 처리할 로직을 설정
    
    - backend - 백엔드 클러스터에 있는 서버
    
    - listen - 선택 사항으로 frontend와 backend section을 하나의 영역으로 합칠 수 있다.

- 예시 코드
  
  ```c
  global
      maxconn 500 // 최대 연결개수 500
  defaults // 기본 매개 변수 설정 
      mode http
      timeout connect 10s
      timeout client 50s
      timeout server 50s
  
  frontend http-in 
      bind *:80
      default_backend application_nodes
  
  backend applicaton_nodes
      balence roundrobin // 로드밸런서 설정 
      option httpchk GET /status // 서버 상태 모니터링 옵션 
      server server01 localhost:9001 weight 2 // 서버 이름, 주소, 가중치 설정
      server server02 localhost:9002 weight 2
      server server03 localhost:9003 weghit 1
      server server03 localhost:9004 check // 상태 모니터링(health check)할 서버 설정
  
  listen stats_page // 모든 서버 상태와 수치를 확인할 수 있는 관리자 페이지 설정
      bind *:83     // frontend와 backend를 listen으로 묶어서 설정했다.
      stats enable
      stats url / 
  ```

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
