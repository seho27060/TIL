[toc]
# udemy React
## React 02
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

### Router 
- SPA 구현을 위한 router 사용하기.
- **react-router-dom v5** 를 사용한다.
#### Router
- URL에서 변화를 감지하고 URL에 기초하여 화면 전환을 실행한다.
  ```bash
  $npm install react-router-dom
  ```
- 위와 같은 react의 router 패키지를 설치한다.

#### BrowerRouter
- react-router-dom 에서 import
- html element 로 활용가능한 하나의 컴포넌트
- 라우터는 감싼 컴포넌트의 URL 변화를 감지한다.
```react
ReactDOM.render(
  <BrowserRouter>
    <App /> // App 컴포넌트는 url 변화가 감지된다.
  </BrowserRouter>,
   document.getElementById('root')
);
```

#### Route
- react-router-dom 에서 import 
- url별로 각기 다른 경로를 지정, 경로별로 어떤 컴포넌트를 실행할지 결정하는 컴포넌트
```react
<Route path="기본url/ 다음에 나올 url"></Route>
```

#### Switch
- Route 만으로 형성시, url 변화에 따라 교차되어 출력되는게 아닌 누적적으로 출력하게 된다.
- 한번에 하나의 url만 출력되도록 Switch 컴포넌트로 감싸준다.
- 여기서 각각의 Route 컴포넌트에는 exact 옵션을 추가해준다.