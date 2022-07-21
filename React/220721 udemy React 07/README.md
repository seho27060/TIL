- [**udemy React**](#udemy-react)
  - [**React 07**](#react-07)
    - [**리액트 컴포넌트에서 리덕스 스토어 데이터(State) 사용하기**](#리액트-컴포넌트에서-리덕스-스토어-데이터state-사용하기)
      - [**내부 컴포넌트에서 Action을 Dispatch하기**](#내부-컴포넌트에서-action을-dispatch하기)
    - [**클래스 기반 컴포넌트가 있는 리덕스**](#클래스-기반-컴포넌트가-있는-리덕스)
      - [**작업에 페이로드 연결하기](#작업에-페이로드-연결하기)
      - [**여러 state 속성 작업하기**](#여러-state-속성-작업하기)
    - [**리덕스 state를 올바르게 사용하는 방법**](#리덕스-state를-올바르게-사용하는-방법)
    - [**리덕스 도전과제 및 리덕스 툴킷 소개**](#리덕스-도전과제-및-리덕스-툴킷-소개)
      - [**리덕스에서 발생 가능한 잠재적 문제**](#리덕스에서-발생-가능한-잠재적-문제)
    - [**redux toolkit**](#redux-toolkit)
      - [createSlice](#createslice)
      - [configureStore](#configurestore)
      - [slice의 action에 접근하기](#slice의-action에-접근하기)
    - [**다중 슬라이드 관리하기**](#다중-슬라이드-관리하기)
      - [새 슬라이드에서 데이터 가져오기 및 dispatch하기](#새-슬라이드에서-데이터-가져오기-및-dispatch하기)
    - [코드 분할하기](#코드-분할하기)
# **udemy React**

## **React 07**

### **리액트 컴포넌트에서 리덕스 스토어 데이터(State) 사용하기**

#### **내부 컴포넌트에서 Action을 Dispatch하기**

```react
import {  useDispatch } from 'react-redux'
```

- `react-redux`에서 import 한다.
- `useDispatch` : `store`의 `dispatcc`를 사용하게 할 수 있는 객체

```react
dispatch({type : "actionName"})
```

- 위와 같이 호출하면 `store`의 'actionName'의 `action`이 dispatch 되어 실행된다.

```react
import classes from './Counter.module.css';

const Counter = () => {
  const dispatch = useDispatch()
  const counter = useSelector(state => state.counter)

  const InclementHandler = () => {
    dispatch({type : "increment"})
  }
  const declementHandler = () => {
    dispatch({type : "decrement"})
  }
  const toggleCounterHandler = () => {};

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      <div className={classes.value}>{counter}</div>
     <div>
     <button onClick={InclementHandler}>Inclement</button>
     <button onClick={declementHandler}>Declement</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
```

- **함수 기반 컴포넌트에서는 useSelectro, useDispatch 와 같은 함수를 사용 가능하다.**
- 클래스 기반 컴포넌트에서는 사용할 수 없다.

### **클래스 기반 컴포넌트가 있는 리덕스**

- 클래스 기반 컴포넌트에서는 훅을 사용할 수 없으므로 `connect`를 활용한다.
- 대부분 함수 기반 컴포넌트를 사용하지만 클래스 기반 컴포넌트가 존재하긴하니 참고하자.

```react
import { Component } from 'react';
import { connect } from 'react-redux'
```

```react
class Counter extends Component{
  InclementHandler() {
    this.props.inclement()
  }

  declementHandler() {
    this.props.declement()
  }

  toggleCounterHandler() {}

  render() {
    return (
      <main className={classes.counter}>
        <h1>Redux Counter</h1>
        <div className={classes.value}>{this.props.counter}</div>
       <div>
       <button onClick={this.InclementHandler.bind(this)}>Inclement</button>
       <button onClick={this.declementHandler.bind(this)}>Declement</button>
        </div>
        <button onClick={this.toggleCounterHandler}>Toggle Counter</button>
      </main>
    );
  }
}
```

- 렌더링에 필요한 html요소 및 내부 함수 선언

```react
const mapStateToProps = state => {
  return {
    counter : state.counter,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    inclement : () => dispatch({type:'inclement'}),
    declement : () => dispatch({type:'declement'}),
  }
}
export default connect(mapStateToProps,mapDispatchToProps)(Counter);
```

- `connect`를 활용하여 `store`에 연결한다. 이때 2개의 함수를 인자로 넘겨준다
- 2개의 함수는 `state`를 `prop`하는 함수, `dispatch`를 `prop`하는 함수이다.

#### **작업에 페이로드 연결하기
**
- **페이로드** : 사용에 의해 전송되는 데이터(ex : 사용자 입력값)
- 정적으로 이뤄지는 하드코딩에 의한 dispatch - action이 아닌, 사용자 입력값에 따라 결과가 달라지는 동적인 함수실행 방식이 실제 웹사이트에서 사용된다.
- 구독한 컴포넌트에서 `dispatch` 요청을 보낼때, 인자값에 동적인 변수 값을 주어 그대로 `store`에 넘겨주어 동적인 처리가 가능하다.

```react
  const IncreaseHandler = () => {
    dispatch({type : "increase" , value : 5})
  }
```

- 위 value 값은 컴포넌트 내부 state를 연결하여 사용자 입력값을 대입할 수 있다.

#### **여러 state 속성 작업하기**

- `store`에 여러개의 `state`를 생성하고, `useSelector` 훅을 통해 필요한 `state`만 컴포넌트에 가져와서 사용할 수 있다.

```react
const intialState = {counter : 0, showCounter : true,}

const counterReducer = (state = intialState, action) => {
    ...

  if (action.type === "toggle"){
    return {
      counter : state.counter,
      showCounter : !state.showCounter
    }
  }
  return state
}
```
- 명시적인 가독성을 위해 `intialState`에 state 인자들을 대입하여 선언한다.
- Reducer 함수에 state를 할당하여 함수내에서 사용, 변경 가능하다.
- 구독한 컴포넌트에서 dispatch를 보내고 그에 따른 action을 실행하여 state를 수정한다.

### **리덕스 state를 올바르게 사용하는 방법**
- ## **절대로, 절대로, 절대로절대로절대로 리덕스에서는 state를 직접 변환해서는 안된다.**
- 데이터 변환을 위해서는 새로운 state 객체를 반환하여 재정의해야한다.

### **리덕스 도전과제 및 리덕스 툴킷 소개**
#### **리덕스에서 발생 가능한 잠재적 문제**
1. dispatch 식별자의 오타
    - 애플리케이션 규모의 증가에 따른 식별자의 오타/ 출동 발생 가능성
2. 규모의 증가에 따른 유지불가능할 정도의 방대한 리덕스 store 

- `redux toolkit`으로 이 모든 문제를 해결 가능!

### **redux toolkit**
- `redux toolkit`은 이미 `redux`를 포함하고 있으므로, `package.json`에 `redux`가 있다면 삭제하도록 한다.
```bash
$npm install @reduxjs/toolkit
```
#### createSlice
- `redux toolkit`의 `createReducer`을 사용해도 되지만, Slice가 Reducer보다 강력(?)하므로 Slice를 사용하도록 한다.

```react
import { creatSlice } from '@reduxjs/toolkit'
...

createSlice({
    name: "식별자",
    initialState : "state의 초기값 할당",
    reducers : {
        "실행할 reducer 함수"(){
            "실행내용"
        },
        ...
    }
})
```
- 주의해야할 점은, 기존의 `redux`에서는 state를 직접 변경할 수 없었다.
- `redux toolkit`에서는 state를 직접 변경시, 자동으로 state 객체를 생성하고 변화된 인자를 반영하여 반환해준다.(state를 직접 변경하는것 처럼 보이지만, `redux toolkit`이 객체를 새롭게 생성하여 반영해줌.)

- 하지만 **slice가 여러개** 라면?

#### configureStore
- 앱의 규모가 커짐의 따라 slice의 종류도 증가되는게 당연하다. 이때 여러개의 slice를 한개의 store에 연결하기 위해 `configureStore` 를 사용한다.

```react
import { createSlice, configureStore } from '@reduxjs/toolkit'
```
- `reduxjs/toolkit`에서 `configureStore` import

```react
const counterSlice = createSlice({
  name : 'counter',
  initialState : initialState,
  reducers : {
    increment(state) {
      state.counter ++
    },
    decrement(state) {
      state.counter --
    },
    increase(state, action) {
      state.counter = state.counter + action.value
    },
    toggleCounter(state) {
      state.showCounter = !state.showCounter
    },
  }
})
```
- 위와 같이 slice를 생성하고

```react
const store = configureStore({
  reducer: counterSlice.reducer
  // reducer: { counter : counterSlice.reducer }
})
```
- store에 slice를 1개 연결하거나, 객체를 두어 key값의 구분을 주어 여러개의 slice를 연결할 수 있다.

#### slice의 action에 접근하기
- slice의 reducer 들을 actions 로 접근하여 export 한다.
```react 
/// store/index.js
export const counterActions = counterSlice.actions
```
- counterActions를 사용하려는 컴포넌트에서 import 
```react
import { counterActions } from '../store';
```

  아래와 같이 접근하면 slice에 포함된 reducer 함수를 사용 가능 하다.
```react
  }
  const IncreaseHandler = () => {
    dispatch(counterActions.increase(10))
  }
  const declementHandler = () => {
    dispatch(counterActions.decrement())
  }
  const toggleCounterHandler = () => {
    dispatch(counterActions.toggleCounter())
  };
```
- `redux toolkit`은 자동으로 reducer에 생성자를 설정한다. action에 할당된 값은 `payload`로 접근한다.


### **다중 슬라이드 관리하기**
- 기존의 slice외에 새로운 slice를 추가하였을때,
```react
const initialAuthState = {
  isAuthenticated : false,
}

const authSlice = createSlice({
  name:"authentication",
  initialState: initialAuthState,
  reducer :{
    login(state) {
      state.isAuthenticated = true
    },
    logout(state) {
      state.isAuthenticated = false
    },
  }
})
```
- 슬라이스 추가

```react
const store = configureStore({
  // reducer: counterSlice.reducer
  reducer: { counter : counterSlice.reducer, auth : authSlice.reducer }
})
```
- 각 slice에 접근할 unique한 key값을 지정하고 해당 slice의 reducer 함수를 등록해준다.

-`state.counter`에서 `state.counter.counter`으로 접근해야한다. 전자는 slice를 1개만 연결했을때여서 key값이 없어서 바로 접근이 가능하다.

#### 새 슬라이드에서 데이터 가져오기 및 dispatch하기
- Store에서 state 가져오기
  - `useSelector(state => state.sliceName.valueName)`를 변수에 할당
- dispatch 하기
  - `store`에서 사용할려는 action을 import
  - `const dispatch = useDispatch`와 같이 dispatch 객체 생성
  - `dispatch(storeActions.actionName(payload))`로 dispatch 전송.
  - 여러개의 payload 할때는.. 어떻게하지? -> 여러개의 값을 갖는 배열, 객체를 payload로 주면된다.

### 코드 분할하기
- 하나의 store.index.js 파일로 관리하기엔 무리가 있으므로, 코드를 나눠 관리하자.
- `store`폴더 내에서 여러개의 js 파일로 분리하여 기능별로 store들을 관리하도록 하자.
- 이후에 `index.js`파일과 같은 공통 store 파일에서 모든 store를 통합하여 하나의 리듀서 함수 모음을 갖추도록 한다.

```react
import { configureStore } from '@reduxjs/toolkit'

import counterReducer from './counter' // counter store import
import authReducer from './auth' // auth store import

const store = configureStore({
  // reducer: counterSlice.reducer
  reducer: { counter : counterReducer, auth : authReducer }
}) // configureStore로 여러개의 store를 1개의 store로 통합


export default store // 통합된 store를 export

```