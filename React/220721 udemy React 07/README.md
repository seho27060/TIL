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

####