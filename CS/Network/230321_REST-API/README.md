- [MVC Pattern](#mvc-pattern)
  - [MVC](#mvc)
    - [MVC 1](#mvc-1)
    - [MVC 2](#mvc-2)

---

# Restful API

## REST

> **REST**(Representational State Transfer)는 [월드 와이드 웹](https://ko.wikipedia.org/wiki/%EC%9B%94%EB%93%9C_%EC%99%80%EC%9D%B4%EB%93%9C_%EC%9B%B9 "월드 와이드 웹")과 같은 분산 [하이퍼미디어](https://ko.wikipedia.org/wiki/%ED%95%98%EC%9D%B4%ED%8D%BC%EB%AF%B8%EB%94%94%EC%96%B4 "하이퍼미디어") 시스템을 위한 [소프트웨어 아키텍처](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98 "소프트웨어 아키텍처")의 한 형식이다. - 위키 백과

- 엄격한 의미로 **REST**는 "네트워크 아키텍쳐 원리"의 모음이다.
  
  - 네트워크 아키텍쳐 원리 : 자원을 정의하고 자원에 대한 주소를 지정하는 방법 전반

- 로이 필딩(Roy Fielding)이 제창했으며, **REST**원리를 따르는 시스템을 **RESTful**하다고 한다.

### REST의 개념

- Representational State Transfer(표현적 상태 전송)이라는 의미와 같이 **자원**을 이름(자원의 표현)으로 구분하여 자원의 **상태**(State, 정보)를 주고 받는 모든 것을 의미한다.

- `HTTP` `URI`(Uniform Resource Identifier, 정형 자원 식별자)로 자원(Resource)를 명시하고 `HTTP method`를 통해 해당 자원에 대한 행위(CRUD Operation)을 적용하는 것을 의미한다.

### REST의 장단점

#### 장점

- `HTTP` 프로토콜의 인프라를 그대로 사용하므로 `REST API`를 위한 별도 인프라가 불필요하며 `HTTP` 프로토콜을 따르는 모든 플랫폼에서 사용할 수 있다.

- 잘 준수된 `REST API`는 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.

- 서버와 클라이언트 역할을 명확하게 분리한다.

#### 단점

- 표준이 존재하지 않는다.

- 사용 가능한 `HTTP method`가 4개 뿐이다.

- 구형 브라우저가 지원해주지 못하는 부분이 존재한다.

### REST 구성 요소

#### 자원(Resource)

- 모든 자원은 고유 ID를 갖으며, Server에 존재한다.

- 자원을 구별하는 ID는 `HTTP URI`이다.

- 클라이언트는 `URI`를 이용하여 자원을 지정하고, 상태를 조작하는 행위를 서버에 요청한다.

#### 행위(Verb)

- `HTTP` 프로토콜의 `method`를 사용한다.

#### 표현(Representation of Resource)

- 클라이언트가 자원에 대한 상태 조작을 요창하면 서버는 이에 적절한 응답(Representation)을 반환한다.

- 적절한 응답은 보통 `JSON`, `XML`, `TEXT` 등과 같은 형태를 갖는다.

## REST API

- `RESTful API`는 아래와 같은 흐름으로 작동한다.
  
  1. 클라이언트가 서버에 요청 전송
  
  2. 서버는 클라이언트 인증, 클라이언트의 인가 권한을 확인
  
  3. 서버는 요청을 수신하고 내부적으로 처리
  
  4. 서버는 클라이언트에 성공 또는 실패 응답 반환.

### 적용을 위한 6가지 제한 조건(원칙)

아래의 제한 조건을 준수한다면 개별 컴포넌트는 자유롭게 구현할 수 있다.

#### 인터페이스 일관성

- 모든 `RESTful` 웹 서비스 디자인의 기본으로 일관적인 인터페이스로 분리한다.
  - 서버가 **표준 형식**으로 정보를 전송함을 의미한다.

#### 무상태(Stateless)

- 서버가 이전의 모든 요청과 독립적으로 모든 클라이언트 요청을 완료하는 통신 방법을 의미한다.
- 요청 간 클라이언트의 컨텍스트는 서버에 저장되어선 안 된다.
- 클라이언트는 임의의 순서로 리소스를 요청하며, 요청간 직접적 연관 관계가 없어 서버는 하나의 요청을 완전히 이해하고 이행할 수 있다.

#### 캐시 처리 가능(Cacheable)

- 클라이언트는 응답을 캐싱할 수 있어야 한다.
- 잘 관리되는 캐싱은 클라이언트-서버 간 상호작용을 제거하여 scailability와 성능을 향상한다.

#### 계층화(Layed System)

- 클라이언트는 보통 대상 서버에 직접 연결되는지, 중간 서버(로드 밸런싱, 공유 캐시)에 연결되는지 알 수 없다.

#### 온디맨드 코드(Code on Demand)

- `Java` 애플릿, `JavaScript`의 제공으로 서버가 클라이언트가 실행 가능한 로직을 전송하여 기능 확장이 가능하다(선택적 조건)

#### 클라이언트/서버 구조

- 아키텍쳐를 단순화하고 작은 단위로 분리(decouple)함으로 클라이언트-서버 간 파트가 독립적으로 개선할 수 있도록 한다.

### REST 인터페이스 원칙 가이드

- 자원의 식별
  
  - 요청 내에 기술된 개별 자원은 식별 가능해야 한다.
  
  - 웹 기반 REST 시스템의 URI와 같다.
  
  - 자원 그 자체는 클라이언트가 받는 문서와 개념적으로 분리된다.
    
    - 데이터베이스 내부 자료를 직접 전송하는게 아닌 `HTML`, `XML`. `JSON`등의 형식으로 전송한다.

- 메시지를 통한 리소스 조작
  
  - 클라이언트가 어떤 자원을 지칭하는 메시지(`URI`)와 특정 메타데이터(`HTTP method`)를 갖는 다면 서버 상의 해당 자원을 조작(manipulation)할 충분한 정보를 갖음을 의미한다.

- 자기서술적 메시지
  
  - 각 메시지는 자신을 어떻게 처리해야 하는지에 대한 충분한 정보를 포함한다.

- 애플리케이션의 상태에 대한 엔진으로서 하이퍼미디어
  
  - 클라이언트가 관련 리소스에 접근하기 원한다면 반환되는 지시자에서 구별 가능해야 한다.
    
    - 충분한 컨텍스트 속에서 `URI`를 제공하는 하이퍼텍스트 링크가 그 예이다.

### REST의 주요한 목표

#### 확장성

- 구성 요소 상호작용의 규모 확장성(Scailability of componet interactions)

- `RESPful`한 시스템은 `REST` 준수로 클라이언트와 서버 간 상호 작용이 최소화되어 효율적으로 규모를 조정할 수 있다.

- Stateless와 Cachable이 도움이 많이 된다.

#### 유연성

- 인터페이스의 범용성(Generality of interfaces)

- 일관된 인터페이스를 준수하여 각 부분은 독립적으로 발전하여도 상호 작용에 영향을 받지 않는다.

- Layed System으로 애플리케이션 로직을 재작성하지 않고 데이터베이스 계층을 변경 가능하기도 하다.

#### 독립성

- 구성 요소의 독립적 배포(Independent Deployment of Components)

- 중간적 구성 요소를 이용한 응답 지연 감소, 보안 강화, 레거시 시스템의 캡슐화(Intermediary Components to Reduce Latency, Enforce Security and Encapsulate Legacy Systems)

- 다른 의미긴 한데, `REST API`는 사용 기술과 연관이 없으므로, `API` 설계에 영향을 주지 않고 다양한 프로그래밍 언어로 클라이언트, 서버 애플리케이션을 작성할 수 있다.

---

- 레퍼런스

> [REST - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/REST)
> 
> [RESTful API란 무엇인가요? - RESTful API 설명 - AWS](https://aws.amazon.com/ko/what-is/restful-api/)
> 
> [[Network] REST란? REST API란? RESTful이란? - Heee's Development Blog](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)
