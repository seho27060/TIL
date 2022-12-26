[TOC]

# Distributed_System_03

## 분산 코디네이터와 분산 알고리즘 - 02

#### 리더 선출 알고리즘 구현

```java
      public static void main(String[] arg) throws IOException, InterruptedException, KeeperException {
          LeaderElection leaderElection = new LeaderElection();

          leaderElection.connectToZookeeper(); 
          leaderElection.volunteerForLeadership();
          leaderElection.electLeader();
          leaderElection.run();
          leaderElection.close();
          System.out.println("Disconnected from Zookeeper, exiting application");
      }
```

- `leaderElection.connectToZookeeper();` - `zookeeper`에 연결 후

- `leaderElection.volunteerForLeadership();` - 리더에 자원하며

- `leaderElection.electLeader();` - 리더를 선출한다.

- `Maven`을 clean 후 package로 하여 `pom.xml`의 설정대로 파일을 빌드한다.

- 이후 4개의 터미널에 각각의 인스턴스를 실행하면, 4개의 인스턴스 중 가장 작은 Sequential number를 갖는 Znode가 리더로 선출됨을 확인할 수 있다.

#### 워처(Watcher)와 트리거(Trigger)

- 워처(Watcher) : 변경사항 발생 시 알림 이벤트를 받기 위해 주키퍼에게 등록하는 객체

- 주키퍼는 `getChidren()`, `getData`, `exists()`와 같은 메서드를 호출할때 워처의 객체 참조를 전달한다.

- 위 3개의 메서드로 등록된 워처들은 일회성 **트리거**(trigger)를 발생시킨다.
  
  - 변화가 발생할시 워처는 알림이벤트인 트리거를 발생
  
  - 비슷한 변화의 알림을 받기 위해선 워처를 다시 한번 등록해야함.

- 워처를 활용한 실패 감지
  
  - Cluster Node 1 - Ephemeral zNode 1
  
  - Cluster Node 2 - Ephemeral zNode 2
  
  - 위와 같은 노드가 있으면, Cluster Node 1은 Ephemeral zNode2의 exists()를 호출하며 워처가 등록되며, Cluster Node 2는 Ephemeral zNode1의 exists()를 호출하며 워처가 등록된다.
  
  - Cluster Node 1이 중단되면 주키퍼는 Ephemeral zNode 1 를 삭제한다.
    
    - 이때 주키퍼는 워처를 사용해 Ephemeral zNode 1의 변화에 대한 알림(Cluster Node 1의 중단)을 Cluster Node 2에게 보낸다.
  
  - 위와 같은 과정을 통해 zNode와 워처를 활용해 노드 간 실패를 감지한다.

### 리더 재선출 알고리즘 구현

- 분산 시스템의 경우 1개의 작업을 마스터 - 워커 노드 관계에서 병렬적으로 분산되어 작업 후 작업 결과를 수집하여 반환한다.

- 이때 마스터 노드의 부재는 해당 시스템 전체의 불능으로 이어지므로 **내결함성(Fault Tolerace)** 과 **가용성(Available)** 이 필수이다.

#### 리더 재선출 시도 1

- 워처와 트리거, 실패 감지를 통해 **리더 노드의 중단**을 다른 노드들이 알 수 있다.
  
  - 리더 노드를 제외한 나머지 노드들은 리더 노드의 zNode의 메서드를 호출하여 변화를 감지할 수 있다.
  
  - 하지만 이런 리더 노드에 중앙집중된 방식은 **The Herd Effect(군집 효과)** 를 불러일으킨다.

- **The Herd Effect(군집 효과)**
  
  - 많은 노드가 이벤트 발생을 기다리고 있을때 발생
  - 이벤트 발생시 연결된 모든 노드에 영향이 감
  - **완전히 부정적으로 작동하며 잘못된 클러스터 설계**의 예시이다.

#### 리더 재선출 시도 2

- 군집 효과를 예방하기 위해 리더 재선출 시도 1의 알고리즘을 수정한다.

- 모든 노드들이 리더 노드의 zNode에 워처를 등록하는게 아닌, 각 노드들은 후보 zNode를 **순서대로 세웠을때 바로 자기 앞에 오는 zNode에 워처를 등록**한다.

- 위와 같이 구성되면 리더 노드가 중단될 시 해당 알림을 받는 유일한 다음 순서 노드가 후계자 노드가 된다.

> 전체적인 오류 ^^..
> 
> `Exception in thread "main" org.apache.zookeeper.KeeperException$NoNodeException: KeeperErrorCode = NoNode for /election/c_` 의 오류로 왜 node가 생성이 안되는거지 ^^..했는데 내가 따로 /election zNode를 생성해줬어야 했다 ^^... 하

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
