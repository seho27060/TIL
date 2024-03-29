- [HDFS 02](#hdfs-02)
  - [MapReduce](#mapreduce)
    - [Mapping](#mapping)
      - [Shuffle and Sort](#shuffle-and-sort)
    - [Reduce](#reduce)
    - [MapReduce의 분산처리](#mapreduce의-분산처리)
    - [작업 흐름](#작업-흐름)
      - [작업은 데이터에 최대한 가깝게 이뤄진다.](#작업은-데이터에-최대한-가깝게-이뤄진다)
    - [Handling Failure](#handling-failure)

# HDFS 02

- PuTTY 로 리눅스 서버 접속후 커맨드라인 명령으로 조작해보자.

```
hadoop fs - 실행내용
```

- 리눅스 환경의 로컬에 파일을 가져오고, `hadoop fs` 명령어를 통해 하둡에 파일을 올리는 등의 작동

## MapReduce

- 매핑 : 데이터를 변형한다. 

- 리듀싱 : 매퍼에서 변형된 데이터를 집계한다.

### Mapping

- 입력 정보를 사용하려는 형식에 맞게 변환하여 출력한다.#\

#### Shuffle and Sort

### Reduce

- 매퍼가 출력한 데이터를 집계한다.

### MapReduce의 분산처리

- 대량의 데이터를 여러개로 쪼개 여러개의 머신(Mapper)에 나누어 입력한다.

- Mppaer는 입력데이터를 기준에 맞게 key-value로 분류

- 분류된 데이터는 key값에 따라 shuffle and sort 된다.

- Shuffle and sort 된 데이터는 Reducer로 보내지고, 작동 내용에 따라(값 카운팅, 점수분베 등) key에 맞춰 출력한다.

### 작업 흐름

1. 클라이언트 노드가 작업 지시

2. 클라이언트는 yarn과 노드메니져와 대화.
   
   - 입력값에 대한 작업 노드메니져에게 지시
   
   - HDFS에서 데이터 가져오기;

3. 노드메니져 노드에서 명령받고 각 머신은 분산된 데이터에 대해 작업 처리(mapreduc

#### 작업은 데이터에 최대한 가깝게 이뤄진다.

- 데이터가 HDFS에 입력되면 복제되어 2~3개 이상의 블록에 저장된다.

- 작업이 이뤄질때, 각 노드에 할당된 작업은 최대한 노드가 갖는 블록에 가진데이터에 대해 처리하도록 할당된다.

### Handling Failure

- 애플리케이션 마스터가 노드 모니터링중 다운 -> 리소스관리자 YARN이 재시작

- 전체 노드 다운, 클러스터의 모든 피시, 애플리케이션 다운 -> 리소스관리자가 다시 재시작

- 리소스 관리자가 다운 -> High availability(고 가용성)을 zookeeper가 실행. 다른 백업 리소스 관리자를 작동한다.
