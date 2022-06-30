# 220615
[toc]

## PJT 05. 비동기 프로그래밍
- 일반적으로 프로그램 함수는 순차적으로 실행된다.(동기식 실행) 많은 시간이 걸리는 작업의 경우, 해당 작업이 완료 될때까지 다음 함수 실행이 대기된다. 이러한 비효율적 문제를 위해 비동기 프로그래밍이 적용된다.


### 비동기 함수
#### Promise vs async await

- 비동기 처리를 다루기 위한 방법(객체)들

- Promise : 비동기 처리에 사용되는 객체. **내용은 실행되었지만, 결과를 바로 반환하지 않는 객체**

  처리 결과에 따른 3가지 상태

  1. Pending(대기) - 비동기 처리가 완료되지 않음
  2. Fullfiled(이행) - 비동기 처리 완료
  3. Rejected(실패) - 비동기 처리 실패

  ```js
  const condition = true;
  const promise = new Promise((resolve, reject) => {
    if (condition) {
      resolve('resolved');
    } else {
      reject('rejected');
    }
  });
  
  promise
    .then((res) => {
      console.log(res);
    })
    .catch((error) => {
      console.error(error);
    });
  ```

  - then, catch 문의 Chaining 을 통해 비동기 로직의 성공 여부에 따른 분기 처리가 가능하다.


- async/ await : chaining에 의한 코드의 비효율적 작성을 개선한 처리 문법. async 함수 내에서 await를 통해 비동기 처리의 결과를 받아 분기 처리한다.

  ```js
  (async () => {
    const condition = true;
    const promise = new Promise((resolve, reject) => {
      if (condition) {
        resolve('resolved');
      } else {
        reject('rejected');
      }
    });
  
    try {
      const result = await promise;
      console.log(result);
    } catch (err) {
      console.error(err);
    }
  })();
  ```

  - Promise와 달리 try-catch 문을 통해 에러를 핸들링해줘야 한다. 

    

#### Chaining 처리 
- 보통 하나 또는 두개 이상의 비동기 작업을 순차적으로 처리. 이전 비동기 작업을 완료 후 다음 작업을 순차적으로 진행
- Hard Code : 해당 작업의 모든 사항을 작성
```js
delay_word('SAMSUNG', 500).then((resolve) => {
	console.log(resolve)
	delay_word('SW', 490).then((resolve) => { 
		console.log(resolve)
		delay_word('ACADEMY', 480).then((resolve) => {
			console.log(resolve)
			delay_word('FOR', 470).then((resolve) => {
				console.log(resolve)
				delay_word('YOUTH', 460).then((resolve) => {
					console.log(resolve)
				})
			})
		})
	})
})
```
- Soft Code : 해당 작업이 가변적일때, 적용 가능하도록 하여 작성.

```js
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

array.reduce((prev, item) => {

	return prev.then(() =>
		delay_word(item.word, item.delay).then((promise) => {console.log(promise)}))

}, Promise.resolve())
```

- 출력 결과

  ```js
  SAMSUNG
  SW
  ACADEMY
  FOR
  YOUTH
  ```

  실행 순서에 따라 출력이 진행됨.

  

#### All 처리, 비 순차 결과

- 이전 비 동기 작업이 다음 비 동기 작업에 영향을 주지 않을 경우, 이전 비 동기 함수 작업이 끝나기 전에 현재 작업을 실행해도 무방하다.
- 함수 호출 순서와 상관없이 먼저 작업이 끝나는 순으로 결과를 받는다.
```js
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]

## promise
array.forEach(async (item) => {
	
	delay_word(item.word, item.delay).then((resolve) => {console.log(resolve)})			
})
```

```js
const array = [{word:'SAMSUNG', delay:500}, {word:'SW', delay:490}, {word:'ACADEMY', delay:480}, {word:'FOR', delay:470}, {word:'YOUTH', delay:460}]


array.forEach(async (item) => {
	
	const resolve = await delay_word(item.word, item.delay)
	
	console.log(resolve)
	
})
```

- 출력 결과

  ```js
  YOUTH
  FOR
  ACADEMY
  SW
  SAMSUNG
  ```

  작업 내용
