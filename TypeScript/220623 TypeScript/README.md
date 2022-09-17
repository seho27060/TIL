- [TypeScript](#typescript)
  - [TypeScript](#typescript-1)
    - [TypeScript와 JavaScript의 차이점](#typescript와-javascript의-차이점)
    - [설치 및 실행](#설치-및-실행)
# TypeScript
## TypeScript

### TypeScript와 JavaScript의 차이점

- JavaScript

```js
//// JavsScript에서는 문제없이 실행됨.
if ("" == 0) {
  // 참입니다! 근데 왜죠??
}
if (1 < x < 3) {
  // *어떤* x 값이던 참입니다!
}

const obj = { width: 10, height: 15 };
// 기존의 JS에서는 밑에 값에 오류가 발생함에도 Nan값을 출력한다.
const area = obj.width * obj.heigth;

console.log(4 / []);
// Nan 출력
```

- TypeScript

```js
const obj = { width: 10, height: 15 };
const area = obj.width * obj.heigth;
// TS에서는 위와 같은 변수 선언에 대해 Js와는 다르게 아래와 같은 오류 값을 출력한다.
// @errors: 2551

console.log(4 / []);
// @errors: 2363
```

- 일반적 프로그래밍 언어에서 위와 같은 상황에서 발생하는 오류에 대해 확인이 가능하지만, JS에서는 그렇지 않다.
- **TypeScript는 컴파일-타임 타입 검사자가 있는 JavaScript의 런타임이다.**
- TypeScript: 정적 타입 검사자(TypeScript: A Static Type Checker)
  - 정적 검사 : 프로그램을 실행시키지 않으면서 코드의 오류를 검출하는 것/ 어떤 것이 오류인지와 어떤 것이 연산 되는 값에 기인하지 않음을 정하는 것이 정적 타입 검사

- TypeScript는 JavaScript의 상위 집합으로 Ts에서 실행되는 코드는 Js에서도 실행이 된다.
  == 이미 잘 작동하고 있는 Js 코드는 그 자체가 Ts 코드이다.



### 설치 및 실행
```bash
$npm install -g typescript
```
- node.js, npm이 설치되있는 VScode에서 설치 진행
- example.ts 의 이름을 갖는 ts 파일을 생성하고, typescript 언어로 작성한다.

```bash
#example.ts를 js 파일로 컴파일
$tsc example.ts
#ts파일의 수정이 실시간 반영되어 js파일로 컴파일 된다.
$tsc example.ts -w 
```