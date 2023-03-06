- [Spark-with-Python 07](#spark-with-python-07)
  - [클러스터에서 Spark 실행 - 02](#클러스터에서-spark-실행---02)
    - [One Million Ratings에서 유사한 영화 만들기 - 1부](#one-million-ratings에서-유사한-영화-만들기---1부)
    - [\[활동\] One Million Ratings에서 유사한 영화 만들기 - 2부](#활동-one-million-ratings에서-유사한-영화-만들기---2부)
      - [Specifying Memory Per Executor](#specifying-memory-per-executor)
      - [Running On A Cluster](#running-on-a-cluster)
    - [클러스터에서 Spark 문제 해결](#클러스터에서-spark-문제-해결)
    - [종속성 문제 해결 및 관리](#종속성-문제-해결-및-관리)
      - [Troubleshooting Cluster Jobs](#troubleshooting-cluster-jobs)
      - [Managing Dependencies](#managing-dependencies)

---

# Spark-with-Python 07

## 클러스터에서 Spark 실행 - 02

### One Million Ratings에서 유사한 영화 만들기 - 1부

- 100만개의 영화 데이터를 유사한 영화끼리 묶어보자.

- 10만개의 데이터에 비해 규모가 증가함에 따라 여러 노드로 구성된 클러스터로 작업을 진행한다.
  
  - 이때 우린 AWS의 EMR을 사용하자.

- 로컬에서 마스터 노드 1개를 실행시킬때와 다르게 AWS의 EMR에서는 **조금 다른점**이 있다.
  
  ```python
  conf = SparkConf()
  sc = SparkContext(conf = conf)
  ```
  
  위와 같이 `SparkConf`를 통해 직접 설정을 하지 않는다. 설정을 비어 놓으면 EMR이 사전에 설정해둔 옵션으로 작업을 진행하다.(매우 편리함!)

### [활동] One Million Ratings에서 유사한 영화 만들기 - 2부

- AWS의 EMR에 클러스터 운영하기 위해 사용할 기본 전략

#### Specifying Memory Per Executor

- 드라이버 스크립트의 `SparkConf`는 비어둔다.
  
  - 이를 통해 default EMR set을 사용할 수 있다.
  
  - 기본 설정은 EMR 하둡 YARN 클러스터 관리자 위에 실행하도록 해준다.

- 해당 예제에서는 기본 excutor memory budget인 512MB는 100만개의 데이터를 처리하는데 적절하지 않다.
  
  - 따라서 `spark-submit --executor-memory 1g MovieSimilarities1M.py 260`을 통해  executor에 할당되는 메모리를 1GB로 설정한다.
  
  - 이런 하드웨어 설정은 어떻게 알까? -> 빵모자아저씨는 512MB에서 계속 실패해서 경험적으로 알게 됐다고 하신다 ^^..

#### Running On A Cluster

- 전반적인 실행 과정은 아래와 같다.
1. 실행할 스크립트와 데이터를 EMR이 쉽게 접근 가능한 곳이 위치시킨다.
   
   - AWS S3를 분산 저장 시스템으로 사용하는건 좋은 선택이다. 같은 서비스내에서 접근성이 좋으므로 쉽게 접근이 가능하다.

2. AWS console에서 스파크를 구동하기 위한 EMR 클러스터를 실행한다.

3. 해당 클러스터의 외부 DNS로 PuTTY를 통해 마스터 노드에 접근한다.

4. 1.에서 위치한 스크립트와 데이터를 복제한다.

5. `spark-submit`을 통해 스크립트를 실행 후 결과를 확인하다.

6. 작업이 끝나면 클러스터를 중지시키기!! 요금은 계속 청구된다.
- 클러스터 생성하고 `Connection Timed out`이 나와서 뭐지 했는데;; 보안그룹에 SSH 연결로 내 IP를 추가해줬다!

- free tier의 경우 사용할 수 있는 ec2의 용량에 제한이 있다..
  
  - 강의에서는 `m3.xlarge`를 10개는 써야 제대로 작동한다는데, 강의 촬영연도가 15년도다
  
  - 지금은 23년도이고 CPU와 메모리기술은 1년마다 급성장중인걸 감안하자
  
  - `m5.xlarge`를 3개만 할당했다.

### 클러스터에서 Spark 문제 해결

- 스파크는 기본적으로 포트 4040에서 웹 UI를 제공한다.
  
  - 작업 기록을 보거나 오류상황을 확인할 수 있다.

### 종속성 문제 해결 및 관리

#### Troubleshooting Cluster Jobs

- 로그 확인하기
  
  - web UI로 로그정보 확인
  
  - `yarn lㅐgs -applicationID <app ID>` 로 `YARN` 을 통해 분산된 작업을 모아서 확인해야 한다.

- 빵모자 아재는 위 예제를 실행하면서 executor가 heartbeats를 발생시키지 못한다는 오류를 확인했다.
  
  - 관리자(Executor)를 실행시켰는데 그대로 사라지고 반응이 없다는 의미다.
  
  - 이는 관리자에 너무 많은 신호를 주기 때문에 발생한다.
    
    - 더 많은 노드, 더 많은 메모리가 필요하다는 뜻..
  
  - 관리자가 shut down 되면 새로운 관리자를 생성한다. 이게 여러번 반복되면 `Spark`가 shut down된다.

- 파티션을 더 분할하여 작업량을 축소함으로 각 관리자의 작업량을 줄일 수 도 있다.

- 아무리 `Hadoop`, `Spark`, `YARN`이 fault-tolerance하다지만, 관리자 하나에게 너무 많은 걸 요구하면 못하는게 당연하다.

- 각 관리자가 적당한 작업을 하도록 설정을 마쳤다면
  
  - 내결함성을 기대할 수 있다. 다만
  
  - 구조가 엉망인 코드, 부적절한 파티션 수, 부족한 메모리 또는 관리자와 관련해서는 하둡은 할 수 있는게 없다.

#### Managing Dependencies

- 데스크톱에서 문제없이 돌아간다고 클러스터(클라우드)에서도 문제없다는 보장은 없다!

- 절대적인 경로로 분산 파일 시스템에 접근하거나, 브로드캐스트를 통해 RDD 외부로 값을 공유하자.

- 애매모호한(obscure) 파이썬 패키지에 의존하면 EMR을 사용할 경우, `pip`를 통해 설치를 하는 스크립트를 작성해줘야 한다.

- 

--- 

- 레퍼런스

> [Apache Spark 와 Python으로 빅 데이터 다루기 | Udemy](https://www.udemy.com/course/best-apache-spark-python/)
