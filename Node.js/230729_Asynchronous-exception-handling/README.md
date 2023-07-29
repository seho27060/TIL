[TOC]

# Node.js

## Asynchronous exception handling

- 비동기 예외 처리

- 비동기가 간단하게 "요청에 대한 응답을 기다리지 않는" 방식이라 할때,
  객체 지향으로 메서드를 작성할때 드문 의문에 대한 해답 찾기
  
  - 메서드를 작성하면서 동기/비동기로 흐르는 작동 흐름은 알겠으나.. 예외 처리에서 의도한 방향대로 작동하지 않는 문제 발생 😂

- 비동기 부터..`Promise`, `try-catch,finally` 까지 정리

### 비동기 함수

- 비동기 처리를 다루기 위한 방법으로 `Promise`와 `async-await`가 있다.

- 아래는 이에 대한 간단한 설명

#### Promise

> `Promise`는 프로미스가 생성된 시점에는 알려지지 않았을 수도 있는 값을 위한 대리자로, 비동기 연산이 종료된 이후에 결과 값과 실패 사유를 처리하기 위한 처리기를 연결할 수 있습니다. 프로미스를 사용하면 비동기 메서드에서 마치 동기 메서드처럼 값을 반환할 수 있습니다. 다만 최종 결과를 반환하는 것이 아니고, 미래의 어떤 시점에 결과를 제공하겠다는 '약속'(프로미스)을 반환합니다. - [Mozilla]([Promise - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#%EC%84%A4%EB%AA%85))

```javascript
const func = (params) => {
    // 변수값 단순 할당과 같은 간단한 작업
...

return new Promise((resolove, reject) => {
    // 비동기 처리가 필요한 작업
    ...
    if( result == 성공) {
    resolve(성공의 반환값)
} else if (result == 실패){
    reject(실패의 반환값)
}
})
```

- `Promise` 객체를 반환 함으로, `Promise`에 할당된 작업을 수행한다.

- 성공했을 시는 `resolve`의 값을, 실패했을때는 `reject`의 값 반환

- `Promise` 내부에서 발생하는 예외에 대해서도 `reject`를 반환한다.
  
  - `Promise` executor와 `.then`, `.catch`와 같은 `Promise` 핸들러에서 발생하는 예외는 가장 **가까운 에러 핸들러**로 처리하게 된다.
  - 이 주위에는 '보이지 않는(암시적) `try-catch`' 가 존재하는 것과 같다.

- `Promise`의 작동 흐름은 아래와 같다.
  ![](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)
  
  - `Promise` 생성시 "pending" 상태가 되며, 성공 여부에 따라 "fulfill"되거나 "reject" 한다.
  
  - 변수에 `Promise` 객체를 호출 이후에 `resolve` 또는 `reject`로 결과 반환 전에 변수를 사용할 경우, pending 상태의 `Promise` 객체가 호출된다.
    
    - 이는 사용자가 비동기 흐름을 이해하지 못하여, **의도하지 않는(예상하지 못한)** 작동 흐름으로 이어지므로 주의해야 한다.(이 글 쓰는 이유)

#### async-await

- 이름과 같이 비동기(async)와 동기(await)를 구분하여 작동하게 한다.

```javascript
const func2 = async (req, res) => {
    // 간단 작업...
    ...
    // 비동기 함수인 asyncFunc의 결과를 기다린다(동기적 작동).
    await asyncFunc()
    .then(data => doSometing(data))
    .catch(error => console.error(error))

   const value = asyncFunc2(); // 비동기 함수이지만 await가 없으므로 다음 동작을 수행한다

   const result = makeResult();
   return res(json);
}
```

- 위와 같이 함수 선언에서 async를 달아줌으로 비동기 함수임을 명시한다.
- 해당 구문 내에서 `await`가 붙은 비동기 함수는 동기적으로 작동한다.
  - 해당 비동기 함수 내부에서도 비동기로 작동할 수 도 있지만, 우선 해당 구문에서는 비동기 함수의 **결과를 기다린다**.
- `async-await`로 작성된 함수는 `Promise` 객체를 반환하므로, `.then-.catch`와 같은 `Promise` 핸들러 사용이 가능하다.

### 비동기 함수에서의 예외 처리

- 비동기식으로 작동하는 콜백(callback)의 **내부에서 발생하는 에러**는, 콜백 바깥에 있는 `try-catch` 블록으로 잡아낼 수 없다.
  
  - `JavaScript` 엔진은 에러가 발생하는 순간, 호출 스택을 되감는 과정을 거친다.
  
  - 위 과정에서 `try-catch` 블록을 만나야 코드의 실행 흐름을 원상 복구시킬 수 있다.
  
  - 하지만 단순 `try-catch` 내부에서 비동기를 수행하는 코드의 경우, 비동기적 작동 흐름에 의해 원복이 되지 않는다.

- 비동기식으로 작동하는 콜백 내부의 에러(예외) 처리를 위해서는, 콜백 내부에서 `try-catch`를 수행하거나 `Promise` 객체를 사용한다.

#### try-catch-finally

- 이제까지 배우고, 사용해왔던 동기적 프로그래밍에서는.. 순서를 생각할 필요가 없었다. 적어도 `try-catch-finally`에서는.

- 하지만 `node.js`에서는 그 흐름이 차이가 난다.

- 기존의 `try-catch-finally`는 
  
  1. `try` 블록 실행
  
  2. 예외 발생시 `catch` 블록에서 잡아내어 처리
  
  3. 뭐가 되든간에 `finally` 블록 수행

#### finally와 Promise 핸들링

- `try-catch-finally`의 수행 흐름은 비동기에서도 똑같이 적용되나.. 
  **"비동기" 적으로 수행**함을 고려해야 한다.
  
  ```javascript
  const func3 = async (input) => {
      const beforeAct = doSomething();
  
      doSomething2();
  
      let result;
      promiseMethod()
      .then(data => result = data)
      .catch(err => result = err)
      .finally(
          promiseMethod2(result);
          return result;
      );
   })
  }
  ```
  
  이와 같은 함수 `func3`이 생성되었다.

- ```javascript
  const resultValue = func3(inputData);
  doSomething4(resultValue);
  ```
  
  위와 같은 코드에서 실행 결과인 `resultValue`는 pending 상태의 `Promise` 객체가 반환된다.
  
  - `async` 가 선언된 메서드는 `Promise` 객체가 반환됨을 잊지말자.

- ```javascript
  func3(inputData)
  .then(res => doSomething4(res))
  .catch(err => console.error(err);
  ```
  
  만약 `.then`, `.catch`를 통해 핸들링을 했을때, `func3`의 **`finally` 블록에서 `promiseMethod2` 메서드 수행 중 에러가 발생했을 경우**
  `func3.catch()`를 통해 에러를 잡아내지 못한다.
  
  - 이는  `finally`의 콜백의 흐름에 의한 것인데, `try-catch` 블록내에서 발생하는 에러를 `catch`가 잡아주지 못하는 것처럼, 콜백의 에러는 콜백 내부에서 처리해야 한다.

- 콜백 내부에서 적절히 `try-catch`를 사용했음에도 문제가 발생한다면, 해당 콜백의 에러 발생을 JavaScript(node.js)에서 **stack을 추적할 수 없게** 되는 것이다.
  - `Promise` 는 암시적인 `try-catch`로 wrapping되어 있다는 걸 떠올리면 해결 방법은 간단하다.
  
  ```javascript
  const func3 = async (input) => {
      const beforeAct = doSomething();
  
      doSomething2();
  
      return new Promise((resolove) => {
      promiseMethod()
      .then(data => result = data)
      .catch(err => result = err)
      .finally(
          promiseMethod2(result);
          resolove(result);
      );
      })
  }
  ```
  
  - 예외가 발생 가능한 부분을 `Promise`로 감싸게 되면, 암시적 `try-catch`로 예외처리가 가능하다.
  
  - **하지만!!,** `undefinedException`과 같이 **개발자가 의도하지 않는 예외, 에러**가 발생할 수 있으므로 맹목적인 사용은 자제하자.
  
  - 비동기적인 흐름에서 의도하는 사항이 어떤 것인지 명확하게 하고, 실제 과정을 정확히 이해하는 사전 작업(설계)가 필요하다.

---

- 레퍼런스

> [[JavaScript]async, await 예외 처리](https://developer-talk.tistory.com/370)
> 
> https://ko.javascript.info/promise-error-handling
> 
> [Promise - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise#%EC%84%A4%EB%AA%85)
> 
> https://helloworldjavascript.net/pages/290-exception.html#%EB%B9%84%EB%8F%99%EA%B8%B0%EC%8B%9D-%EC%BD%94%EB%93%9C%EC%97%90%EC%84%9C%EC%9D%98-%EC%98%88%EC%99%B8-%EC%B2%98%EB%A6%AC
