- [udemy React-hook](#udemy-react-hook)
  - [hook](#hook)
  - [hook 규칙](#hook-규칙)
  - [useState](#usestate)
    - [useState - 업데이트 함수](#usestate---업데이트-함수)
    - [컴포넌트 간에 State 데이터 전달하기](#컴포넌트-간에-state-데이터-전달하기)
  - [useEffect](#useeffect)
    - [useEffect 사용 예시](#useeffect-사용-예시)
    - [useEffect의 종속성](#useeffect의-종속성)
# udemy React-hook
## hook
- `hook`을 통해 함수형 컴포넌트 내에서 `state`에 접근이 가능하다.
- 이전에는 클래스형 컴포넌트로만 가능했지만, 이젠 아니다.

## hook 규칙
1. `hook`은 함수형 컴포넌트나 커스텀훅에서만 사용해야 한다.
2. `hook`은 컴포넌트의 루트 레벨에서 선언하도록한다.(컴포넌트 내 함수(중첩함수)에서 선언하지 않는다.)
  
## useState
- 가장 핵심적인 `hook`
- 언제나 두개의 요소를 반환한다. 
  1. 현재 `state`의 `snapshot`. 업데이트되면 포함하는 컴포넌트를 다시 렌더링한다.
  2. 두번째는 현재 상태를 업데이트할수있는 함수.
### useState - 업데이트 함수
- `state`를 업데이트할때는 업데이트하는 하나의 인자만 입력하는게 아니라, 원래 객체의 모양을 유지하면서 변경된 `state`인자를 넣어야한다.

```javascript
import { useState } from "react"

const [inputState, setInputState] = useState({ title: "", amount : ""})
```
- `useState`를 통헤 `state`를 생성한다면, 가독성을 위해 위와 같이 선언하도록 하자.
```javascript
import { useState } from "react"

const [enteredTitle, setEnteredTitle] = useState("")
const [enteredAmount, setEnteredAmount] = useState("")
```
- 더 간단히 명확하게 위와 같이 선언할 수도 있다.

### 컴포넌트 간에 State 데이터 전달하기
- 부모 컴포넌트 - 자식 컴포넌트 간에 props에 함수를 적절히 배치하여 컴포넌트간 `state` 데이터를 전달하도록 한다.
- 부모 컴포넌트에서 전달한 `state`또는 함수를 자식컴포넌트에서 적절히 사용하도록 해야한다.

## useEffect
- 모든 컴포넌트의 렌더링 이후에 실행된다.
- 즉 컴포넌트가 **렌더링될때마다** 실행된다.
- 두가지 인자를 포함한다.
  1. 렌더링이 끝나고 실행되는 함수
  2. 함수에서 사용되는 의존성(dependencies)이 저장된 배열
- **의존성 배열이 변경될때**와 처음 렌더링될때 1.의 함수가 실행된다.

### useEffect 사용 예시
```javascript
useEffect(렌더링시 실행되는 함수, 의존성을 갖는 배열)
```
- 위와같이 선언하여 사용한다.


```javascript
fetch(
  "https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients.json"
)
  .then((response) => response.json())
  .then((responseData) => {
    const loadedIngredients = []
    for (const key in responseData){
      loadedIngredients.push({
        id : key,
        title : responseData[key].title,
        amount : responseData[key].amount
      })
    }
    setUserIngredients(loadedIngredients)
  });
```
- 위의 함수를 `useEffect`없이 사용하면 다음의 과정에 의해 **무한루프**에 빠지게 된다.
  1. DB에 데이터를 요청하고 응답을 받아 `state`에 저장한다.
  2. `state`가 변경되었음을 감지하고 **렌더링**이 실행된다.
  3. **렌더링**이 실행되었으므로, 다시 `fetch`가 실행된다. 다시 1.로 돌아간다.
   
```javascript
useEffect( fetch..., [])
```
- `useEffect`를 활용하여 위같이 선언하면, 처음 렌더링될때 실행되고 의존성을 갖는 배열 `[]`에 아무런 변화가 없으므로 결국 컴포넌트의 렌더링이후 1번만 실행된다.

### useEffect의 종속성
~431
