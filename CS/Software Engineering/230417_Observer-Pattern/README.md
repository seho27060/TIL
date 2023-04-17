- TOC

---

# Observer Pattern

## 옵서버 패턴

> **옵서버 패턴**(observer pattern)은 [객체](https://ko.wikipedia.org/wiki/%EA%B0%9D%EC%B2%B4_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99) "객체 (컴퓨터 과학)")의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 [메서드](https://ko.wikipedia.org/wiki/%EB%A9%94%EC%84%9C%EB%93%9C "메서드") 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 [디자인 패턴](https://ko.wikipedia.org/wiki/%EB%94%94%EC%9E%90%EC%9D%B8_%ED%8C%A8%ED%84%B4 "디자인 패턴")이다. 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다. [발행/구독 모델](https://ko.wikipedia.org/wiki/%EB%B0%9C%ED%96%89/%EA%B5%AC%EB%8F%85_%EB%AA%A8%EB%8D%B8 "발행/구독 모델")로 알려져 있기도 하다. - 위키 백과

- 옵서버 패턴의 핵심은 옵서버(Observer) 또는 리스너(Listener)라 불리는 하나 이상의 객체를 관찰 대상이 되는 객체에 등록한다.

- 각각의 옵서버들은 관찰 대상인 객체(Subject)가 발생시키는 이벤트를 감지하고 각각의 처리를 수행한다.

### 구조

- 구조는 아래와 같다.
  
  ![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Observer.svg/1708px-Observer.svg.png)
  
  각각의 `Observer`들은 `Subject`를 바라보고 있으며, `Subject`의 `Event`를 감지하여 각각의 `notify`라는 함수로 처리를 수행한다.

- 객체는 옵저버를 **등록(register)** 하고 **제거(unregister)** 하는 메서드를 갖는다.
  
  - 등록은 새로운 옵저버를 목록에 등록하고
  
  - 제거는 목록에서 특정 옵저서를 뺀다.

### 사례

- 옵저버 패턴에서는 순환 실행을 방지하는 메커니즘이 필요하다.
  
  - `Event X`가 발생하면 `Observer A`가 `Observer B`를 갱신한다고 할때,
  
  - `Observer B`는 해당 과정에서 `Observer A`를 갱신한다.
  
  - `Observer A`갱신은 `Event X`의 발생으로 이어져 순환 구조로 빠지게 된다.

- 위와 같은 사례를 방지하기 위해 `Event X` 처리 이후에 `Observer A`가 다시 `Event X`를 발생시키지 않도록 하는 장치가 필요하다.

- `MVC Pattern`의 형태와 결합되어 사용한다. `MVC`에서 모델(Model)과 뷰(View)간의 **연결을 느슨히** 하기 위해 옵저버 패턴이 사용된다.

--- 

- 레퍼런스

> [옵서버 패턴 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%98%B5%EC%84%9C%EB%B2%84_%ED%8C%A8%ED%84%B4)
