- [MicroService Architecture(MSA)](#microservice-architecturemsa)
  
  - [등장배경](#등장배경)
    
    - [*Monolithic Architecture](#monolithic-architecture)
  
  - [MSA의 특징](#msa의-특징)
    
    - [MSA의 장/단점](#msa의-장단점)
      
      - [장점](#장점)
      - [단점](#단점)
    
    - [*SOA(Service-Oriented Architecture)](#soaservice-oriented-architecture)
      
      - [MSA와의 차이점](#msa와의-차이점)
    
    - [*ESB(Enterprise Service Bus)](#esbenterprise-service-bus)
      
# MicroService Architecture(MSA)

> 하나의 Application을 다수의 **독립적**인 Service로 구성하는 Architecture Style
> 
> **독립적**으로 배포 가능한 각각의 기능을 수행하는 Service로 구성된 프레임워크
> 
> 전체 어플리케이션을 특정 목적을 가진 어플리케이션 단위로 **나누는 것**. 나누어진 어플리케이션들은 **약한 결합도**와 **강한 응집도**를 목표로 한다.

## 등장배경

- 서비스의 규모가 커짐에 따라 기존의 전통적인 개발 방법론과 Monolithic System에서의 한계점이 나타났다.

- 이에 따라 새로운 개발 방법론 MSA의 등장.

### *Monolithic Architecture

> 소프트웨어의 모든 구성요소가 한 프로젝트에 통합되어 있는 형태.
> 
> 웹 개발의 프로그램을 개발하기 위해서 모듈별로 개발을 하고, 모듈들을 하나의 어플리케이션으로 묶어 배포되는 형태(Monolithic : 단일체의, 한 덩어리로 뭉친)

- 부분 장애가 전체 서비스의 장애로 확대 가능
  
  - 기능 간 결합도가 일반적으로 높아, 하나의 수정에도 전체 시스템이 변경된다.
  
  - 하나의 버그가 전체 시스템에 영향을 준다.

- 하나의 구조이므로, 수정에 대한 배포가 오래걸린다.

- 서비스 변경이 어렵고, 수정시 장애의 영향 파악이 어렵다(높은 결합도로 인해)

## MSA의 특징

- API를 통해서만 상호작용이 가능하다. MSA는 서비스의 접근점을 API형태로 외부에 노출, 실질적인 세부 사항은 모두 추상화한다.

- 약한 결합도와 강한 응집력을 갖는 각 서비스들은 빠른 개발, 배포가 가능하다.

- **SOA**(Service Oriented Architecture)와 유사한 특징을 갖는다.

- 비즈니스 기능을 컴포넌트화 하여 비즈니스 기능 개발을 맡은 팀은 개발 뿐만 아니라 **운영을 도맡아** 전체 라이프사이클을 책임진다.

- 중앙의 강력한 표준이나 절차의 준수를 강요하지 않고, **각각의 서비스**에 가장 효율적인 방법론과 도구, 기술을 적용할 수 있다.

- 중앙에서 분산된 서비스는 각 데이터를 서비스만의 방식으로 저장, 관리한다. 또한 서비스들을 각각 배포할 수 있으므로 인프라 자동화(개별적 CI/CD)가 가능하다.

- 서비스 분화로 각 서비스에서는 항상 장애가 발생한다. 특정 서비스의 장애는 다른 서비스로의 전파 가능성이 있기 때문에, **장애 방지 설계**가 필수적으로 이뤄진다.
  
  - Spring Cloud, Kubernetes를 통해 구현가능하다.

### MSA의 장/단점

#### 장점

- 각 서비스들은 독립적이므로, 작은 서비스 단위로 **확장**이 가능하다.

- 각 서비스들에 대해 적절한 기술을 선택해 개별적으로 적용가능하다.(login - spring, blockchain - node.js 와 같이 한 어플리케이션 안에서 **다른 서비스**가 서로 **다른 기술이 적용**가능)

- 어플리케이션 내 서비스간 영향이 최소화되므로. **실험과 혁신**에 용이하다.

#### 단점

- 컴퓨팅 자원의 사용이 Monolithic보다 비효율적이다.

- 보다 작은 사이즈로 분리된 서비스들을 각각 관리해야 함에 따라 비용을 증가한다.

- 중앙집중식이 아닌, 서비스 별 분화에 의해 각 서비스별로 관리해야 함은 물론, 서비스간 장애를 방지해야하는 구조로 복잡한 운영관리가 필요하다.

### *SOA(Service-Oriented Architecture)

> 대규모 컴퓨터 시스템을 구축할 때의 개념. 업무상의 일 처리에 해당하는 소프트웨어 기능을 서비스로 판단하여 그 서비스를 네트워크상에 연동하여 시스템 **전체**를 구축해 나가는 방법론

- 기존의 어플리케이션 기능들을 비즈니스적 의미를 갖는 기능 단위로 묶어서 표준화된 호출 인터페이스를 통해 서비스로 구현한다.

- SOA에서 각 **서비스**는 **완벽한 개별적 비즈니스 기능**을 구현한다. 서비스 인터페이스간의 **느슨한 결합**을 제공하여, 서비스 구현에 대한 지식이 거의 없이도 호출될 수 있다.
  
  - SOA의 서비스 : 플랫폼에 종속되지 않는 표준 인터페이스를 통해 비즈니스적인 의미를 갖는 기능들을 모아놓은 **소프트웨어 컴포넌트**

#### MSA와의 차이점

- SOA는 MSA와 유사한 개념을 갖는다. 근본적인 차이점은 범위로, SOA는 **전사적인 아키텍쳐 접근** 방식이며 MSA는 **어플리케이션 개발 팀 내의 구현 전략**으로 구분할 수 있다.

- 각각의 구성 요소와 통신하는 방법에서 SOA는 ESB(Enterprise Service Bus)를 사용하지만, MSA에서는 언어의 제약이 없는 API를 통해 stateless 방식으로 통신한다.

### *ESB(Enterprise Service Bus)

> 중앙집중화된 컴포넌트가 백엔드 시스템의 통합을 수행한 후. 이러한 통합을 서비스 인터페이스로 사용할 수 있도록 하는 패턴.

- 레거시 시스템, 레코드 시스템을 SOA 네트워크 프로토콜을 사용하여 작업하기 위해, 변환되고 통합되어야 하는 이전 프로토콜 및 독점 데이터 형식을 사용한다. 

- 작업을 위해 매번 변환, 통합하는 각각의 프로토콜을 사용하는 것이 아닌, ESB를 통해 **서비스 전달 및 통합을 표준화**하여 그 과정을 **단순화** 할 수 있다. 

- 레퍼런스
  
  > [[MSA] MSA란 무엇인가? 개념 이해하기](https://wooaoe.tistory.com/57)
  > 
  > https://velog.io/@sorzzzzy/MSA-MSAMicroService-Architecture%EB%9E%80
  > 
  > [마이크로서비스 아키텍처(MSA) | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/computer-science/software-engineering/MSA.html)
  > 
  > [SOA(Service-Oriented Architecture)란? - 대한민국 | IBM](https://www.ibm.com/kr-ko/cloud/learn/soa)
  > 
  > [[Architecture] SOA 패턴이란 - Azderica](https://azderica.github.io/01-architecture-soa/)
