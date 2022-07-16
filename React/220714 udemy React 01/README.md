- [udemy React](#udemy-react)
  - [React 01](#react-01)
    - [create-react-app](#create-react-app)
      - [1. 프로젝트 생성하기](#1-프로젝트-생성하기)
      - [2. 서버 실행하기](#2-서버-실행하기)
    - [2. react 구문 알아보기](#2-react-구문-알아보기)
      - [1. JSX 코드](#1-jsx-코드)
      - [2. 컴포넌트](#2-컴포넌트)
      - [2.1 컴포넌트에 값(속성) 넘겨주기(props)](#21-컴포넌트에-값속성-넘겨주기props)
      - [2.2 컴포넌트에 이벤트 추가하기](#22-컴포넌트에-이벤트-추가하기)
      - [2.3 더 많은 컴포넌트 만들기](#23-더-많은-컴포넌트-만들기)
    - [3. State](#3-state)
      - [조건부 연산자(JavaScript)](#조건부-연산자javascript)
    - [Event props](#event-props)
      - [Event](#event)

# udemy React

- React에서는 **명령형 코드**가 아닌 **선언형 코드**를 통해 구현하도록 한다.

## React 01

### create-react-app

#### 1. 프로젝트 생성하기

- `bash`에서 `npx create-react-app appName`을 실행하여 react 프로젝트를 생성한다.
- Todos 만들기를 진행해보자.

#### 2. 서버 실행하기

```react
/// react 18 이하에서 렌더링할 때
ReactDOM.render(<App/>, document.getElementById('root'));

/// react 18 이상에서 렌더링할때 사용 구문
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);
```

- 서버실행에 있어서 위 사항을 주의하도록 한다.

### 2. react 구문 알아보기

#### 1. JSX 코드

- 위 예시의 `<App/>`와 같은 js파일내의 html 구문을 사용

- 브라우저는 그대로 이해를 못하므로 변환이 필요함.

- 태그의 클래스는 `class`가 아닌 `className`으로 준다.

  ```react
  <div class="html"></div> // 기존 html상에서 class 부여
  <div className="react"></div> //JSX 상에서 calss 부여
  ```

  - Html에서는 class가 맞나, react는 바닐라 js기반으로 js에서는 className을 html상의 element class로 읽어들인다.

#### 2. 컴포넌트

- react에서 컴포넌트는 반환값을 가지는 함수이다.

- 기능을 분할하고 재조립을 통해 페이지 구성(reusable)

- 부모 컴포넌트에서 자식 컴포넌트 import

- 보통 **src**에 **component**폴더를 만들어 컴포넌트들을 관리한다.

  ```react
  import Todo from "컴포넌트 경로"

  function App() {
    return <div>
      <h1>My Todos</h1>
      <Todo/>
    </div>;
  }

  export default App;
  ```

#### 2.1 컴포넌트에 값(속성) 넘겨주기(props)

- props는 기본적으로 key-value 형태로 넘어간다.

```react
function Todo(props) {
  return(
    <div className="card">
    <h2>{props.text}</h2>
    <div className="actions">
      <button className="btn">Delete</button>
    </div>
  </div>
  )
}

export default Todo
```

- `Todo(props)`를 통해 props 라는 객체에 key-value 형식으로 데이터가 전송되고
- html상의 {}안은 자바스크립트가 적용된다.

#### 2.2 컴포넌트에 이벤트 추가하기

- `onClick`와 같은 이벤트 핸들러를 통해 html에서 받은 신호를 자바스크립트 실행으로 연결되게 한다.

  ```react
  function deleteHandler(){
      //함수 내용 실행
  }

  <button className="btn" onClick={deleteHandler}>Delete</button>

  ```

#### 2.3 더 많은 컴포넌트 만들기

- 기능을 세분화하여 코드를 쪼갠다. 그리고 조립하여 다시 재사용

####

### 3. State

- useState 를 import한다.

- `useState`: 해당 컴포넌트에서 사용하는 state를 정의할 수 있다./ 리액트 훅

- 항상 두개의 element를 반환한다.(state값, state 변경함수)

  ```react
    const [firstElement, secondElement] = useState(default)
  ```

  - 초기값 default가 firstElement에 할당된다.
  - secondeElement는 함수로, 호출하여 firstElement에 변경값을 줄 수 있다.

  ```react
    function deleteHandler() {
      setModalIstOpen(true) // firstElement의 값을 true로 변경
    }
  ```

```react
function Todo(props) {
  const [modalIsOpen, setModalIstOpen] = useState(false)

  function deleteHandler() {
    setModalIstOpen(true)
  }
  return(
    <div className="card">
    <h2>{props.text}</h2>
    <div className="actions">
      <button className="btn" onClick={deleteHandler}>Delete</button>
    </div>
    { modalIsOpen  ? <Modal/> : null}
    { modalIsOpen  ? <Backdrop/> : null}
  </div>
  )
}
```

- onClick으로 `deleteHandler`가 호출 -> `setModalIsOpen(false)`로 `modalIsOpen`의 값이 false로 변경된다.
- `modalIsOpen`의 값에 따라 `Modal`컴포넌트와 `Backdrop`컴포넌트의 출력여부가 결정된다.

#### 조건부 연산자(JavaScript)

- 삼항 연산자

```react
{function ? execute1 : execute2} // function이 true시 execute1 실행, false 라면 execute2 실행
```

- &&, || 연산자(단축평가)
  1. || 연산자 : `A || B`라고 할때 true 인 값(함수, 변수 등 모두 포함)을 반환 
  2. && 연산자 : `A && B`라고 할때 둘다 ture 라면 오른쪽(B)값을 반환한다. 둘 중 하나라도 false 라면 false를 반환한다.

### Event props
- 모든 커스텀 컴포넌트에서 Event 를 사용할 경우 props를 필수로 사용해야 한다.
#### Event
- html 상의 `<div>`태그와 같은 컴포넌트는 기본적으로 `onClick`과 같은 Event가 내장되어 있다.
- `React`에서는 커스텀 컴포넌트를 사용할 경우 기본 컴포넌트의 Evnet와 연결하여 사용한다.
```react
    <div className="actions">
      <button className="btn" onClick={deleteHandler}>Delete</button>
    </div>
    { modalIsOpen  && <Modal onCancel = {closeModalHandler} onConfirm = {closeModalHandler}/>} // Modal 커스텀 컴포넌트에 onCancel 이라는 props에 함수를 대입해준다.
    { modalIsOpen  && <Backdrop onClick = {closeModalHandler}/>}
  </div>

  /// Modal.js
  function Modal(props){
  function cancelHandler() {
    props.onCancel()
  }

  function confirmHandler(){
    props.onConfirm()
  }
  return(
    <div className="modal">
      <p>Are you Sure?</p>
      <button className="btn btn--alt" onClick={cancelHandler}>Cancel</button> // 기본 컴포넌트인 button에서는 내장된 onClick 이벤트를 props.onCancel을 실행하는 함수 cancelHandler를 연결하여 실행시킨다.
      <button className="btn" onClick={confirmHandler}>Confirm</button>
    </div>
  )
}

export default Modal
```
- 커스텀 컴포넌트에 이벤트를 연결하기 위해 어떤 Event 와 props가 연결되는지 확인하자.