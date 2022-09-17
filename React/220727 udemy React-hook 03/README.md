- [udemy React-hook](#udemy-react-hook)
  - [What is useMemo?](#what-is-usememo)
    - [How to use useMemo?](#how-to-use-usememo)
  - [Custom Hook](#custom-hook)
    - [Http Hook](#http-hook)
    - [사용자 정의 훅을 사용한 컴포넌트간 데이터 공유](#사용자-정의-훅을-사용한-컴포넌트간-데이터-공유)
# udemy React-hook

## What is useMemo?

- 프로젝트 구현에 있어서 불필요한 렌더링이 여러번 일어나는 경우가 있다.
- `state` 변화에 따른 리렌더링.. 함수 호출에 따른 리렌더링..등등
- `useCallback`이 "함수"를 저장하여 불필요한 재생성-호출을 방지했다면, `useMemo`는 "값"을 저장하여 불필요한 재생성-호출을 방지한다.
- 컴포넌트를 기억(Memorizing)하는 하나의 방법
- 컴포넌트를 생성할때 보통 `React.Memo`를 사용한다.
  - `useMemo`를 사용하면 렌더링할때마다 데이터를 재생성하지 않아 효울적 렌더링이 가능하다.

### How to use useMemo?

```javascript
  const ingredientList = useMemo(() => {
    return (
      <IngredientList
        ingredients={userIngredients}
        onRemoveItem={removeIngredientHandler}
      />
    );
  }, [userIngredients, removeIngredientHandler]);

  ...

  <section>
    {ingredientList}
  </section>
```

- 위와 같이 `useMemo(() => {함수실행내용}.[의존성배열])`로 구성하여 사용한다.

- 의존성 배열의 값의 변경이 감지되면 함수실행내용의 컴포넌트를 렌더링한다.

- 컴포넌트에 포함된 데이터의 규모가 크다면 리렌더링이 실행될때마다 많은 시간이 걸리므로, 위의 기능을 활용하도록 하자.

- #### detail-index1

## Custom Hook

### Http Hook

- Http 요청을 많이 보낸다는 가정하에 custom hook을 구성해보자.

- 같은 사항을 갖는 함수를 `hook`으로 생성하는게 아닌, 같은 "논리"를 갖는 함수를 `hook`함수로 생성한다.

- 해당 부분에서는 CRUD에 있어서 서버에 요청을 보내는 공통된 논리를 가지므로, 해당 기능을 `custom hook`으로 생성한다.

```javascript
import { useReducer, useCallback } from "react";

const httpReducer = (curHttpState, action) => {
  switch (action.type) {
    case "SEND":
      return { loading: true, error: null };
    case "RESPONSE":
      return { ...curHttpState, loading: false, data:action.responseData }; // 분해 구조에서, 같은 이름의 인자는 덮어씌여짐
    case "ERROR":
      return { loading: false, error: action.errorMessage };
    case "CLEAR":
      return { ...curHttpState, error: null };
    default:
      throw new Error("Should not be reached");
  }
};
```

- 사용할 `Reducer`를 컴포넌트 외부에서 선언한다. 렌더링마다 재 선언할 필요가 없기때문이다.

```javascript
const useHttp = () => {
  const [httpState, dispatchHttp] = useReducer(httpReducer, {
    loading: false,
    error: null,
    data : null
  });
  const sendRequest = useCallback((url, method, body) => {
    dispatchHttp({ type: "SEND" });
    fetch(url, {
      method: method,
      body: body,
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then(response => {
      return response.json()
    })
      .then((responseData) => {
        dispatchHttp({ type: "RESPONSE", responseData:responseData });
      })
      .catch((error) => {
        dispatchHttp({ type: "ERROR", errorMessage: error.message });
      });
  },[])
  return {
    isLoading:httpState.loading,
    data : httpState.data,
    error: httpState.error,
    sendRequest:sendRequest
  }
}

export default useHttp;
```

- `httpState`를 `useReducer`로 `httpReducer`와 연결한다. 이제 `action`에 따라 `state`를 반영한다.

- CRUD에 있어서 공통된 서버 url에 각기 다른 `method`와 `body`를 담아 보낸다. 이때 "서버에 보낸다."라는 논리는 공용으로 사용되므로, 해당 부분을 `custom hook`으로 선언한다.

- 이제 `useHttp` custom hook은 3개의 state, 1개의 함수를 리턴한다.

### 사용자 정의 훅을 사용한 컴포넌트간 데이터 공유
