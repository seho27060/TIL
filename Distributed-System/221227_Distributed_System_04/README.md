[TOC]

# Distributed_System_04

## 클러스터 관리, 레지스트리 및 디스커버리

#### 서비스 레지스트리 및 서비스 디스커버리 개요

- 서비스 레지스트리
  
  - 클러스터 내에 존재하는 노드들을 등록한다.
  
  - `service_registry` 노드는 전체 노드의 `znode`를 추가한다. 이때 각 `znode`에는 부모 노드의 주소(adress)가 포함되어 있다.

- 서비스 디스커버리
  
  - 클러스터 내의 모든 노드들은 자기 자신 외 다른 노드를 인식할 수 없다.
    - 이때 설정 파일을 통한 노드간 연결로 노드들은 서로를 인식한다.
    - 정적 설정의 경우 노드의 변경(삭제, 수정 등)이 발생시 변경된 설정을 적용하기 위해 설정 파일을 재생성하고 모든 노드에 재배포해야한다.
    - 동적 설정으로 정적 설정에서의 불필요한 반복 과정을 개선한다. 이를 통해 손이 많이 가는 작업을 자동화할 수 있다.
  - 모든 노드는 `service_registry`노드에 `getChildren`과 같은 워처를 등록한다.
  - 노드의 변경시 워처를 통해 알림을 받고, `service_registry`는 변경 노드의 znode를 참고하여 주소값을 확인한다.
  - 이를 통해 노드간 서로가 연결된 Peer to Peer Communication이 아닌 Leader/Worker Architecture로 구성이 가능하다.
    - Leader/Worker Architecture로 1개의 노드의 변경으로 전체 노드에 영향이 끼치는게 아닌, 부분적으로 수정 작업이 가능하다. 

#### 서비스 레지스트리 및 서비스 디스커버리 구현

> 강의의 `service-registry` 리소스 참고

- `ServiceRegistry` class
  
  - 서비스 레지스트리 관련 작업 클래스
  
  - `createServiceRegistryZnode` :  서비스 레지스트리 znode의 존재 유무를 확인 후, 없다면 새로 생성한다. 이때 생성되는 노드는 영구 노드이다.
    
    - 두 노드에 요청을 받을 시 경쟁 상태(Race condition)이 발생 할 수 있으므로, 예외 처리를 해준다.
  
  - `registerToCluster(String metadata)` : 레지스트리 클러스터에 metaData에 할당된 주소의 노드를 등록한다.
    
    - 서비스 레지스트리에 등록되며, 임시 노드로 Sequetial하게 생성된다.
  
  - `updateAddresses` : 노드의 삭제, 변경에 따른 주소값을 업데이트한다. 이때 메서드는 synchronized 로 동작한다.
    
    - 현재 모든 znode의 길이만큼 빈 리스트 addresses를 생성 후
    
    - 모든 znode를 순회하면서 znode가 exist하다면 adresses에 할당한다.
    
    - 채워진 adresses를 allServiceAddresses같은 주소 저장값에 `unmodifiableList`로 저장한다.
  
  - `registerForUpdates` : `updateAddresses` 핸들러
  
  - `getAllServiceAddresses` : 모든 주소가 저장된 allServiceAddresses가 빈 값이라면 `updateAddresses`를 호출한다. allServiceAddresses를 반환한다.
  
  - `unregisterFromCluster` : 워커노드가 사라지거나 불가피하게 자신이 리더 노드가 되어 자기 자신과 통신하는걸 방지하기 위해 클러스터에서 unregist한다.
    
    - 현재 Znode가 exist하면 주키퍼에서 delete 한다.

- 리더 워커 아키텍쳐에 병합
  
  - `OnElectionCallback` : 노드의 리더 갱신과 워커 갱신을 위한 인터페이스를 생성한다.
    
    - `onElectedToBeLeader`는 노드 자신이 리더로 선출되었고 그에 따라 모든 노드의 주소값을 update한다.
    
    - `onWorker`는 노드 자신은 워커이며 `registerToCluster`를 통해 자기 자신을 클러스터에 등록한다.
  
  ![](C:\Users\seho2\AppData\Roaming\marktext\images\2022-12-27-20-38-20-image.png)
  
  위와 같이 리더로 선출된 리더 노드에서는 클러스터에 등록된 노드의 address를 확인하고 있다.(서비스 레지스트리로 등록, 서비스 디스커버리로 노드 관리)

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
