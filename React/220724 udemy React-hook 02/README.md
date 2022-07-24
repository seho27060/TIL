[toc]

# udemy React-hook

## What is useCallback?

- `useEffect` hook 과 같은 경우는 1.렌더링이 될때와 2. 의존성 배열의 변화를 감지할때 실행된다.
- 즉 컴포넌트 내의 `state`나 기타 등의 이유로 컴포넌트가 렌더링이 다시 될때(리렌더링) `useEffect` 함수는 실행된다.
- `useCallback` hook은 **1.가장 처음 렌더링될때와 2.의존성 배열의 변화가 감지**될때, 실행된다.
- 가장 처음 렌더링될때 할당된 함수를 캐싱(cache)하여 localstorage에 저장된다.
- 컴포넌트가 리렌더링될시 이전에 `useCallback`에서 할당된 함수는 다시 실행(생성)되는것이 아니라, 캐싱된 함수를 가져와 사용하게 된다.

## useRef

- 참조객체

```javascript
import { useRef } from "react"

const refValue = useRef()

return (
  <form>
  <input ref = {refValue}>
  </form>
)
```

- 위와 같이 설정하면 `<input>`태그의 값이 참조객체 `refValue`에 연결되어 할당된다.

## useEffect로 정리하기

- `useEffect`함수 내에서 반환할때는 해당 반환값은 **함수**여야한다.

```javascript
useEffect(() =>{
  //blah blah do something
  cosnt timer = setTimeout(() => {
    // blah blah
  }, 500);
  return () => {
    clearTimeout(timer)
  } // 반환값을 함수로 줌.
}, [의존성배열])
```

- 해당 반환값에서 clear up 함수가 할당되었다.
- 해당 `useEffect`에서는 의존성 배열의 변화에 따른 실행마다, `timer` 상수가 생성된다. 이는 불필요한 생성이다.
- `useEffect`가 다시 실행되기전 `return`에 해당하는 구문이 실행되고, 위의 예시에서는 생성된 `timer`를 clear up 시켜 삭제한다.
- 이를 통해 `useEffect`의 반복마다 여러개의 타이머가 생성되고 남게되는 비효율적 문제가 개선된다.

## Delete 기능 구현

```javascript
const removeIngredientHandler = (ingredientId) => {
  fetch(
    `https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients/${ingredientId}.json`,
    {
      method: "DELETE",
    }
  ).then((response) => {
    setUserIngredients((prevIngredients) =>
      prevIngredients.filter((ingredient) => ingredient.id !== ingredientId)
    );
  });
};
```

- list의 item을 삭제하기 위한 삭제 handler 구현
- 삭제 기능 api url을 요청한다.
  - 문자열 보간 : 백틱(``)으로 문자열을 감싸면 문자열내에서 ${}을 통해 문자열 변수를 동적으로 할당할 수 있다. 위 예시에서는 삭제하려는 item의 id를 동적으로 할당하였다.
- 삭제 요청을 통해 DB에서는 해당 id를 갖는 데이터가 삭제되고
- 응답이 오면 현재 로컬에서의 `ingredient` 데이터에서 해당 id 데이터를 제외한 배열로 갱신한다.

## State의 일괄처리(batching)

- 리액트에서는 state에 대한 set을 일괄로 처리한다.
- 한 블록내에서 state를 set 요청을 보내고 변경 state를 사용할 수 없다.
- 블록내에서 set State가 실행됐다면, 해당 블록이 끝나고 난후 state의 변경사항이 갱신된다.
- '동일한 시점(synchronous)'에, 동일한 이벤트 핸들러에서 요청한 모든 상태 업데이트(State Batching)는 일괄로 처리된다.

```javascript
const clearError = () => {
  setError(null);
  setIsLoading(false);
};
```

- 위와 같은 구문에서 두개의 state set 요청은 해당 함수가 끝나고 일괄로 처리된다.

## useReducer

- Reducer Function: 여러개의 입력을 받아 하나의 결과를 반환하는 함수.
  - useReducer = 리듀서 객체, Reducer Function = 기능을 정의한 함수
- Reducer Function은 보통 컴포넌트의 외부에 선언한다. 컴포넌트 내부에 선언시 렌더링마다 다시 생성 됨으로 문제가 된다. `Reducer`객체는 `useReducer`를 통해 컴포넌트 내부에서 선언한다.

### useReducer Function 선언

```javascript
const ingredientReducer = (currentIngredients, action) => {
  switch (action.type) {
    case "SET":
      return action.ingredients;
    case "ADD":
      return [...currentIngredients, action.ingredient];
    case "DELETE":
      return currentIngredients.filter((ing) => ing.id !== action.id);
    default:
      throw new Error("Should not get there");
  }
};
```

- 컴포넌트 밖에서 선언한다.
- 입력값으로 `state`와 `dispatch`를 위한 `action` 두개의 인자를 갖도록 선언한다.
- `action.type`에 따라 다른 기능을 실행하기 위해 `switch`로 분기를 나눈다.

```javascript
const Ingredients = () => {
  const [userIngredients, dispatch] = useReducer(ingredientReducer, []);
  // const [userIngredients, setUserIngredients] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  ...
}
```

- `useReducer`는 두개의 인자를 반환한다. 1.`state` 배열과 2.`dispatch`기능을 하는 함수
- `useReducer(A,B)`를 통해 A에는 이전에 선언한 `Reducer Function`, B에는 `state`의 초기값을 할당한다.

```javascript
dispatch({ type: "SET", ingredients: filteredIngredients });
```

- 이와 같이 `Reducer` 함수인 `ingredientReducer`에서 `type`에 따라 정의한 내용에 적절하게 입력값을 대입하여 `state`에 대한 CRUD를 진행한다.

### Http State에 대해 useReducer 사용하기

- 해당 프로젝트에서 `isLoading` 과 `error` state 두개는 한개의 `Reducer`로 합칠 수 있다.

```javascript
const httpReducer = (curHttpState, action) => {
  switch (action.type) {
    case "SEND":
      return { loading: true, error: null };
    case "RESPONSE":
      return { ...curHttpState, loading: false }; // 분해 구조에서, 같은 이름의 인자는 덮어씌여짐
    case "ERROR":
      return { loading: false, error: action.errorMessage };
    case "CLEAR":
      return { ...curHttpState, error: null };
    default:
      throw new Error("Should not be reached");
  }
};
```

- 위와 같이 `action.type`을 지정하고 그에 따른 `state` mutaion을 지정한다.
  - javascript에서 분해구조로 배열을 선언하고, 배열의 인자의 key 값의 value에 대해 다시 값을 할당하면 해당 key값의 value는 덮어씌워진다.

```javascript
const [httpState, dispatchHttp] = useReducer(httpReducer, {
  loading: false,
  error: false,
});

dispatchHttp({ type: "SEND" });
```

- 위와 같이 `useReducer` 객체를 선언하고 `dispatchHttp` action 함수를 통해 필요한 `type`의 함수를 실행한다.

## CONTEXT API, useContext
- 부모 - 자식 컴포넌트 간의 props 관계에 따른 prop drilling, prop chaining 과 같은 현상의 복잡한 구성을 간단히 해줄 수 있는 hook.

### Context 생성하기
1. src 하위 폴더로 `context` 생성
2. `auth-context.js`의 context js 파일 생성
3. ```javascript
   export const AuthContext = React.createContext({
    isAuth: false,
    login :() => {}
    }) 
   ```
   `createContext`를 통해 context 객체 생성
4. ```javascript
   const AuthContextProvider = props => {
    const [isAuthenticated , setIsAuthenticated] = useState(false)

    const loginHandler = () => {
      setIsAuthenticated(true)
    }
    return (
      <AuthContext.Provider value = {{login:loginHandler, isAuth:isAuthenticated}}>
        {props.children}
      </AuthContext.Provider>
    )
    }

    export default AuthContextProvider
   ```
   `AuthContext` 객체로 `state`과 `action`을 선언하고 감싸는 `AuthContextProvider`를 생성한다.
   이제 `AuthContextProvider`가 포함하는 자식 컴포넌트에서는 `AuthContext`를 사용가능하다. 

```javascript
///index.js
ReactDOM.render(
  <AuthContextProvider>
    <App />
  </AuthContextProvider>,
  document.getElementById("root")
);
```
- root 레벨의 컴포넌트에서 wrapping 하여 하위 컴포넌트들은 `AuthContext`를 사용가능하게 되었다.

```javascript
/// index 하위 App.js
const App = props => {
  const authContext = useContext(AuthContext)

  let content = <Auth/>

  if (authContext.isAuth) {
    content = <Ingredients/>
  }

  return content;
};

export default App;
```
- 자식 컴포넌트인 `App.js`에서 `AuthContext`에 대한 객체 `authContext`를 생성하고, context의 state를 활용했다.

```javascript
// Auth.js
const Auth = props => {
  const authContext = useContext(AuthContext)
  const loginHandler = () => {
    authContext.login()
  };

  return (
    <div className="auth">
      <Card>
        <h2>You are not authenticated!</h2>
        <p>Please log in to continue.</p>
        <button onClick={loginHandler}>Log In</button>
      </Card>
    </div>
  );
};
```
- 역시 `AuthContext`에 대한 객체를 선언하고, context의 action을 활용했다.
- 