# Callback

## Callback

> [프로그래밍](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D "프로그래밍")에서 **콜백**(callback) 또는 **콜백 함수**(callback function)는 다른 코드의 인수로서 넘겨주는 [실행 가능한 코드](https://ko.wikipedia.org/wiki/%EC%8B%A4%ED%96%89_%ED%8C%8C%EC%9D%BC "실행 파일")를 말한다. 콜백을 넘겨받는 코드는 이 콜백을 필요에 따라 즉시 실행할 수도 있고, 아니면 나중에 실행할 수도 있다. - 위키 백과

- `JavaScript`에서 함수(`function`)은 **"일급 객체"** 이다.
  
  - 함수는 `Object` 타입이며 다른 일급객체와 똑같이 사용할 수 있다.

- `function` 자체가 "객체" 이므로 변수안에 담길 수도, 인수로서 다른 함수에 전달될 수 도, 함수 내에서 생성되거나 반환될 수 있다.

- `Callback function`은 특정 함수에 **매개변수로서 전달된 함수**를 지칭한다.

## Why we use Calback?

- 기존의 `Blocking Code`에서는 함수의 실행 흐름이 순차적으로 진행된다.
  
  - 이전에 실행된 함수가 끝나야 프로그램의 종료가 이어짐.

- `Callback` 함수를 사용할 경우 프로그램을 `Non-Blocking Code`로 작성할 수 있다.
  
  - 이전에 실행된 함수가 끝날때까지 대기하지 않고, 바로 그 다음의 함수를 실행한다.

- `Callback`을 사용한 `Non-Blocking Code`의 프로그램의 경우
  
  - 프로그램의 "흐름"을 끊지 않고
  
  - 해당 프로그램을 통한 서버는 더 많은 양의 요청을 빠르게 처리할 수 있다.

# Event Loop

## Event Loop

- `Node.js`는 `Event`가 매우 많이 사용되며, 이로 인해 비슷한 기술보다 훨씬 빠른 속도를 자랑한다.

- `Node.js` 기반의 서버가 가동되면, 변수들을 초기화하고 함수를 선언하여 **"이벤트"** 가 발생할때까지 기다린다.

- 이벤트 위주 어플리케이션(Event-Driven Application)에서는 이벤트를 대기하는 메인루프가 있다.
  
  - 이벤트가 감지되었을 시 `Callback`함수를 호출한다.

- `Event`와 `Callback`이 비슷해 보이지만, 
  
  - 차이점은 `Callback Function`은 비동기식 함수에서 결과를 반환할 때 호출되지만,
  
  - `Event Handling`은 `Observer Pattern`에 의해 작동한다.

### Event Handling

- 이벤트를 대기(Event Listeners)하는 함수들은 옵저버(Observer) 역할을 한다.

- 이벤트 대기 함수는 이벤트를 기다리다가, 이벤트가 실행되면 이벤트를 처리하는 함수를 실행한다.
  
  - 옵저버(이벤트 대기 함수)가 객체(Subject)를 바라보다가 객체의 이벤트 발생(Event)시 각각의 함수를 실행하는 것과 같다.

- `Node.js`에서는 `events` 모듈과 `EventEmiiter` 클래스가 내장되어 있다.
  
  - 이를 사용하여 `Event`와 `Event Handler`를 연동(bind)할 수 있다.
  
  ```javascript
  var events = require('events')
  
  var eventEmitter = new events.EventEmitter()
  ```
  
  아래와 같이 `Event Handler`와 `Event`를 연동한다.
  
  ```javascript
  // 연동
  eventEmitter.on('eventName', eventHandler)
  
  // eventName이라는 이벤트 발생할려면 다음 코드 실행
  eventEmitter.emit('eventName')
  ```
  
  - 이때 **Emit**은 **"방출하다"** 라는 뜻을 갖음을 떠올리자.

---

- 레퍼런스

> [[Node.JS] 강좌 06편: Callback Function 개념 | VELOPERT.LOG](https://velopert.com/255)
> 
> [[Node.JS] 강좌 07편: Event Loop | VELOPERT.LOG](https://velopert.com/267)
> 
> [Events | Node.js v19.9.0 Documentation](https://nodejs.org/api/events.html#events_class_eventemitter)
