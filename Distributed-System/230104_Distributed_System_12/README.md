- [Distributed System 12](#distributed-system-12)
  - [클라우드 컴퓨팅 및 전역 확장 배포](#클라우드-컴퓨팅-및-전역-확장-배포)
    - [클라우드 컴퓨팅](#클라우드-컴퓨팅)
      - [Cloud Infrastructure Building Blocks](#cloud-infrastructure-building-blocks)
    - [클라우드 배치](#클라우드-배치)
        - [Instance Templates](#instance-templates)
    - [인스턴스 그룹, 자동 확장 및 자동 복구](#인스턴스-그룹-자동-확장-및-자동-복구)
      - [Instance Groups](#instance-groups)
    - [멀티 리전 배치 및 전역 부하 분산](#멀티-리전-배치-및-전역-부하-분산)
      - [Multi Region Deployment](#multi-region-deployment)
    - [Cloud Load Balancing](#cloud-load-balancing)


# Distributed System 12

## 클라우드 컴퓨팅 및 전역 확장 배포

### 클라우드 컴퓨팅

- 기존에는 서버 운영을 위해 서버실을 대여하거나 구매하여 기반 시설(Infrastructure)을 마련해야 했다.
- 현재에 와서는 AWS, GCP, Azure와 같은 클라우드 서비스를 통해 적절한 비용을 지불하여 기반 시설을 서비스로서 사용할 수 있다.(Insfrastructure as a Service)
- 또한 다양한 기능을 제공하는 플랫폼 역시 서비스로 사용할 수 있다.(Platform as a Service)

#### Cloud Infrastructure Building Blocks

- 클라우드 서비스는 아래와 같은 기능으로 구성되어 있다.

- Computer Nodes(VMs)
  
  - AWS - EC2, GCP - Compute Engine, MS - Virtual Machine

- Autoscailing
  
  - 서버 운영에 트래픽에 따라 최저비용으로 안정적인 성능을 낼 수 있는 용량과 메모리를 조절한다.

- Load Balancers
  
  - 통합 IP 주소, 모니터링, 장애감지 등의 기능을 제공한다.

- - SQL 데이터베이스, NoSQL 데이터베이스, 두개의 조합 데이터베이스, 여러 다양한 데이터를 저장가능

- 분석, 머신러닝, 작업관리, 부하 장치등 여러 특별한 기능을 서비스로서 제공한다.

### 클라우드 배치

- GCP(Google Cloud Platform)을 활용하여 프로젝트 애플리케이션을 클라우드 서버에 배포해보자.
1. 애플리케이션의 `jar`파일을 생성한다.

2. GCP에 프로젝트를 생성후

3. Cloud Storage에서 새로운 Bucket을 생성한다.
   
   - 1.에서 생성한 `jar`파일을 업로드한다.

4. Compute Engine에서 새로운 VM인스턴스를 생성한다.
   
   - 실행창을 열어 java를 설치한다.
   
   - 버킷에 있는 `jar` 파일을 가져온다
   
   - `java -jar`를 통해 `jar`파일을 실행하며 포트 번호를 명시해준다.

##### Instance Templates

- 모든 인스턴스를 수동으로 반복적으로 실행하는건 시간도 오래 걸리고 오류가 발생하기 쉽다.

- 따라서 한번 성공하게되면 해당 형태로 템플릿을 만들어 원하는 만큼 반복하게 한다.
1. GCP에서 인스턴스 템플릿 생성 진입

2. 설정을 완료하고 고급옵션 - 관리 - 자동화 에 필요한 명령을 단일 스크립트로 작성한다.
   
   ```bash
   #! /bin/bash
   apt-get update
   apt-get -y --force-yes install openjdk-11-jdk 
   
   gsutil cp gs://first-bucket-seho/*.jar .
   
   java -jar cloud-web-application-1.0-SNAPSHOT-jar-with-dependencies.jar 80
   ```

3. 이제 해당 템플릿을 사용하여 동일한 여러 인스턴스를 실행할 수 있다.

### 인스턴스 그룹, 자동 확장 및 자동 복구

#### Instance Groups

- 독립적인 여러 인스턴스를 생성하고 관리(모니터링)하는 기능
  
  - 큰 규모의 컴퓨터 인스턴스 클러스터를 관리할 수 있다.
  
  - 모든 인스턴스의 상태를 체크할 수 있다.(Health check)
  
  - 트래픽이 최대로 발생하는 동안 더 많은 인스턴스를 추가한다
  
  - 장애 발생 클러스터를 복구할 수 있다.
1. 생성된 인스턴스 템플릿에서 인스턴스 그룹 생성

2. 리전, 대기시간, 자동화(Autoscailing) 정책을 설정한다.

3. 생성된 인스턴스중 1개에 접속하여 `stress` 부하 테스트 어플리케이션으로 테스트 해보면 실행되는 인스턴스가 자동으로 조절되는걸 확인할 수 있다.

4. 자동 확장 - 상태 확인 옵션을 추가하면 옵션에 따라 인스턴스의 상태(health)를 체크하여 복구를 진행한다.

### 멀티 리전 배치 및 전역 부하 분산

#### Multi Region Deployment

- 이전에는 단일 리전을 선택하여 해당 리전 내 여러 존에 인스턴스를 생성하여 내결함성을 유지했다.

- 지리적 이점에서 오는 짧은 대기시간과 리소스 격리를 위해 여러 리전에 배포환경을 구성해보자.
1. 그냥 새로운 인스턴스 그룹을 생성하고 원하는 리전을 설정해주면 된다.

### Cloud Load Balancing

- 여러개의 인스턴스로 실행중인 전체 서비스를 대포하는 IP 주소 형식의 단일 진입점을 생성한다.

- 소프트웨어 나 하드웨어의 부하 분산 장치와는 다르게 클라우드 부하 분산 장치는 실제로 분산된 시스템이다.
  
  - 단일 부하 분산 장치처럼 보이는 아주 정교한 분산 시스템

- 따라서 일반적으로 전용 VM에서  자체 소프트웨어 부하 분산 장치를 실행하는 것보다 더 많은 비용이 든다.
1. 고정 IP 예약으로 대표할 IP를 생성한다.

2. 부하 분산에서 새로운 부하 분산 장치(Load balancer)를 생성한다.

3. 백엔드 구성에서 기존의 다른 리전이 할당된 인스턴스 그룹을 추가한다.
   
   - 부하 장치의 정책(CPU 사용률, 초당 요청 건수)를 선택

4. 상태 확인(Health check)를 추가한다.
   
   - 인스턴스의 상태확인과 다르게 부하 장치의 상태 확인은 인스턴스의 작동 유무를 확인한 후 사용할 수 없다고 판단되면 요청의 순번에서 제외하는 비교적 단순한 작업을 실행한다.

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
