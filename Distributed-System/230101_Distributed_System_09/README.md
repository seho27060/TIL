[TOC]

# Distributed_System_09

## 분산형 메시지 브로커 - 02

### 아파치 카프카 클러스터 구축 실습

#### Kafka Cluster Architecture

- 카프카 클러스터는 1개 이상의 서버로 구성되어 있으며

- 리더 선출 및 작업 배정은 주키퍼 클러스터에 연결되어 관리된다.

- 퍼블리셔(publisher)와 컨슈머(consumer)를 카프카 클러스터 연결하기 위한 카프카 서버 주소들을 부트스트랩 서버(Bootstrap Server)라고 한다.
  
  - 부트스트랩 서버에 연결이 완료되면 프로듀서(Producer)와 컨슈머는 서로 메시지를 주고 받을 수 있다.

### 카프카 다운로드 및 실행

- 공식 홈피에서 실행 ㄱㄱ
  
  - OS에 따라 적절한 파일 실행하기(linux라면 sh, windows라면 bat)
  
  - 다운로드한 kafka폴더가 root에 멀리있으면 가깝게 바꿔줘야함

#### 설정

- config 폴더의 `zookeeper.properties`에서 사용할 주키퍼의 설정을 변경할 수 있다.

- config 폴더의 `server.properties`에서 카프카 서버의 설정을 변경할 수 있다.

#### 실행

- `bin/windows/zookeeper-server-start.bat config/zookeeper.properties`으로 주키퍼 서버 실행
  
  - 기존에 사용하던 주키퍼 설정을 사용해도 되고, 카프카에 기본으로 포함된 설정을 사용해도 된다.

- `bin/windows/kafka-server.start.bat config/server.properties`로 카프카 서버 실행

- `bin/windows/kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic chat` 로 토픽을 생성한다
  
  - 부트스트랩 서버의 port를 지정하고
  
  - 복제 횟수(replication factor)를 설정하고
  
  - 토픽의 파티션(partition) 개수를 설정한다.
  
  - 마지막으로 토픽의 이름을 "chat"으로 설정했다.
  
  - `bin/windows/kafka-topics.bat --list --bootstrap-server localhost:9092`로 토픽이 카프카에 생성되었는지 확인
  
  ![](https://user-images.githubusercontent.com/81341784/210167639-246bd52e-b528-4b50-8511-062edf67645e.png)

- `bin/windows/kafka-console-producer.bat --broker-list localhost:9092 --topic 토픽이름`으로 프로듀서 콘솔 실행 후 컨슈머로 메시지 보내기
  ![](https://user-images.githubusercontent.com/81341784/210167640-570655fd-62fe-49a8-b6ae-5c20367d07a8.png)
  
  - windows 환경에서 git bash로 실행하면 안된다!! cmd로 실행할것!!

- `bin/windows/kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic chat --from-beginning` 로 컨슈머 콘솔을 실행하여 localhost:9092를 부트스트랩으로 연결하여 chat이라는 토픽의 처음 메시지부터(`--from-beginning`) 출력한다.
  ![](https://user-images.githubusercontent.com/81341784/210167651-297fadcc-a424-4135-a055-c9b074183509.png)

#### 여러개의 카프카 브로커 실행

- config 내에 있는 `server.properties`를 복제하여 새로운 서버 설정 파일을 생성한다.

- ```properties
  broker.id=1
  listeners=PLAINTEXT://:9093
  log.dirs=/tmp/kafka-logs-1
  ```
  
  위와 같이 브로커 id와 listeners의 포트번호, log 저장 위치를 새롭게하여 설정해준다.
  해당 실습에서는 2개의 설정 파일을 추가하여 총 3개의 브로커를 실행한다.

- `bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 3 --topic purchases`로 3번의 복제횟수와 3개의 파티션을 갖는 새로운 토픽 "purchases"를 생성한다.
  
  - 3개의 브로커를 실행하지만 bootstrap-server로는 1개의 서버(포트)를 지정해야한다.
  
  - `bin\windows\kafka-topics.bat --describe --bootstrap-server localhost:9092 --topic 토픽이름`로 토픽의 형태를 확인할 수 있다.
    
    ![](https://user-images.githubusercontent.com/81341784/210167657-2d482d38-b82a-4c26-b9f2-00ffd5e78f83.png)
    
    생성된 3개의 파티션은 각 다른 큐를 갖는다. 
    
    프로듀서에서 컨슈머로 메시지를 보낸다면 1개의 파티션을 갖는 토픽에서는 메시지를 순차적으로 받지만
    
    **3개의 파티션을 갖는 토픽**에서는 메시지의 id대로 정해진 파티션에 쌓이기 때문에 **메시지가 쌓이는 순서가 순차적이지 않다.**(근데 1개의 파티션 내에서는 순차적으로 쌓임!!)(실행했는데 순차적으로 쌓여서 사진은 넘어감 ㅎ..)

- 만약 3개의 브로커(broker-0, broker-1, broker-2) 중 broker-1의 연결이 끊어진다면 어떻게될까?
  
  - 연결된 분산 코디네이터 Zookeeper에 의해 자동으로 새로운 리더가 선정된다.
    
    ![](https://user-images.githubusercontent.com/81341784/210167662-c5ed9637-a6e6-4060-97ca-ae8e10553986.png)
    
    토픽 `purchases`의 `partition:0`은 broker-1을 리더로 사용중이였지만, 연결이 끊긴후 broker-0을 리더로 다시 선출(reelection by Zookeeper)하여 사용한다.
  
  - `producer-console`이나 `consumer-console`을 다시 실행해도 이전의 메시지가 누락되지 않고 출력됨을 확인할 수 있다.
  
  - 여러대의 카프카 브로커들을 통해 **내결함성(fault tolerance)** 을 갖추게 된다.

#### Java를 활용한 카프카 프로듀서

- 카프카 프로듀서 생성

- 레코드의 토픽, id, key, value 등의 값 할당
  
  - id를 할당하지 않으면 카프카의 디폴트 방식대로 메시지가 분배됨
  
  - 분배 과정에서 메시지는 직렬화를 거쳐 송신된다.

- 로컬의 개인프로젝트 참고

#### java를 활용한 카프카 컨슈머

- 카프카 컨슈머 생성
  
  - 필요 옵션 지정

- 메시지를 소비하는 메서드 생성
  
  - 카프카는 컨슈머의 갑작스런 종료에도 해당 컨슈머의 메시지 수신 권한을 다른 컨슈머로 할당한다(fault tolerance)
  
  - 같은 컨슈머 그룹내의 컨슈머들은 다른 파티션을 할당받아 RoundRobin과 같은 방식으로 메시지를 소비(consume)한다.
  
  - 발행/구독 패턴에서는 모든 컨슈머 그룹에 메시지를 송신한다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
