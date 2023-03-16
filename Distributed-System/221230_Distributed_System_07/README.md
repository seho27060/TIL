- [Distributed\_System\_07](#distributed_system_07)
  - [HAProxy - 부하 분산 실습](#haproxy---부하-분산-실습)
    - [High Availability Proxy(HAProxy)](#high-availability-proxyhaproxy)

# Distributed_System_07

### [Load Balancing](https://github.com/seho27060/TIL/tree/master/CS/Network/230316_Load-Balancing)

## HAProxy - 부하 분산 실습

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
