[TOC]

# What Is Java?

## What is Java?

> **자바**([영어](https://ko.wikipedia.org/wiki/%EC%98%81%EC%96%B4 "영어"): Java)는 [썬 마이크로시스템즈](https://ko.wikipedia.org/wiki/%EC%8D%AC_%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%A6%88 "썬 마이크로시스템즈")의 [제임스 고슬링](https://ko.wikipedia.org/wiki/%EC%A0%9C%EC%9E%84%EC%8A%A4_%EA%B3%A0%EC%8A%AC%EB%A7%81 "제임스 고슬링")(James Gosling)과 다른 연구원들이 개발한 [객체 지향적](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D "객체 지향 프로그래밍") [프로그래밍 언어](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4 "프로그래밍 언어")이다. 처음에는 가전제품 내에 탑재해 동작하는 프로그램을 위해 개발되었지만 현재 [웹 애플리케이션](https://ko.wikipedia.org/wiki/%EC%9B%B9_%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98 "웹 애플리케이션") 분야에 가장 많이 사용하는 언어 중 하나이고, [안드로이드](https://ko.wikipedia.org/wiki/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C "안드로이드")를 비롯한 모바일 기기용 소프트웨어 개발에도 널리 사용되고 있다. 현재 버전 18까지 출시했다. - 위키백과

- 운영체제(`Operation System`, 플랫폼)에 독립적
  
  - `JVM`을 통해 운영체제와 관계없이 실행 가능

- `C++`의 장점과 "객체 지향"이라는 개념을 채택하여 비교적 배우기 쉽고 이해하기 쉬운 간결한 언어

- `Java`를 잡아 ㅋㅋ

### Java의 특징

1. 운영체제에 독립적 - `JVM`

2. 객체지향언어 - `OOP`

3. 낮은 러닝커브

4. 자동 메모리 관리(Garbage Collection) - `garbage collector`

5. 네트워크와 분선처리 지원 - `Java API`를 통한 지원

6. 멀티쓰레드(`multi-thread`) 지원 - 시스템관 무관하게 구현 가능, `Java API`로 지원

7. 동적 로딩(Dynamic Loading) 지원 

#### JVM(Java Virtual Machine)

- `JVM`(Java Virtual Machine, 자바 가상 머신) : 자바를 실행하기 위한 가상 기계

- 실제 하드웨어(컴퓨터)가 아닌 소프트웨어로 구현된 컴퓨터와 같다.

- `Java`로 작성된 애프리케이션은 모두 `JVM` 에서만 실행된다.

| Java          | 일반적       |
| ------------- | --------- |
| `Java` 애플리케이션 | 일반 애플리케이션 |
| `JVM`         | OS        |
| OS            | 컴퓨터(하드웨어) |
| 컴퓨터(하드웨어)     |           |

- 위와 같이 일반적인 애플리케이션의 실행과 다르게 `Java`에서는 `JVM`을 통해 실행된다.
  
  - `JVM`을 한 번 거치면서 애플리케이션은 `OS`에 맞게 **해석(interpret)** 된다.
  
  - `OS` 종속적인 일반 프로그래밍언어와 다르게 `JVM`으로만 애플리케이션을 실행하는 `JAVA`는 다른 여러 `OS`에서 동일한 실행이 가능하다.
  
  - 근데 `JVM`은 `OS` 종속적이라 `OS`마다 맞는 `JVM`이 필요하다.

#### JDK(Java Development Kit)

- `Java`로 프로그래밍을 하기 위한 Kit
  
  - 설치시 `JVM`과 자바 클래스 라이브러리(`Java API`)외에 개발하기 위한 프로그램이 설치된다.



---

- 레퍼런스

> 
