[TOC]

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

- 모든 인스턴스를 수동으로 반복적으로 실행하는건 

---

- 레퍼런스

> [Java 를 활용한 분산 시스템 및 클라우드 컴퓨팅](https://www.udemy.com/course/java-distributed-system/)
