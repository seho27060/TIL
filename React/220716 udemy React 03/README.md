- [udemy React](#udemy-react)
  - [React 03](#react-03)
    - [props.chidren을 사용하여 wrapper 컴포넌트 만들기](#propschidren을-사용하여-wrapper-컴포넌트-만들기)
      - [Card 컴포넌트](#card-컴포넌트)
      - [Layout 컴포넌트](#layout-컴포넌트)
        - [왜 이렇게 하는걸까?](#왜-이렇게-하는걸까)
    - [양식 추가하기.](#양식-추가하기)
      - [입력 form 컴포넌트](#입력-form-컴포넌트)
      - [form submit](#form-submit)
        - [eventHandler](#eventhandler)
        - [event.preventDefault](#eventpreventdefault)
        - [useRef](#useref)
# udemy React
## React 03
### props.chidren을 사용하여 wrapper 컴포넌트 만들기
#### Card 컴포넌트
- 여러 컴포넌트에 적용가능 재사용성이 높은 `Card`컴포넌트를 만들어 보자.
```React
/// 재사용성이 높은 Card 컴포넌트
import classes from "./Card.module.css"

function Card(props) {
  return (
    <div className={classes.card}>
      {props.children} // 중요한 부분 아래 설명 참고.
    </div>
  )
}

export default Card

/// MeetupItem 컴포넌트, Card 컴포넌트로 감싸지는(wrapped) 컴포넌트이다.
function MeetupItem(props) {
  return (
    <li className={classes.item}>
      <Card > // Card 컴포넌트가 기존의 내용을 wrapping 하고 있다.
        <div className={classes.image}>
          <img src={props.image} alt={props.title}></img>
        </div>
        <div className={classes.content}>
          <h3>{props.titme}</h3>
          <address>{props.address}</address>
          <p>{props.description}</p>
        </div>
        <div className={classes.actions}>
          <button>To Favorite</button>
        </div>
      </Card>
    </li>
  );
}
```

#### Layout 컴포넌트
- 위 카드 컴포넌트를 생성하여 데이터를 카드에 대입하여 출력하였다.
- 카드가 놓인 화면을 수정한다고 할때, `Card`컴포넌트를 포함하는 새로운 컴포넌트를 생성하자.
```react
/// App 컴포넌트
function App() {
  return (
    <div>
      <Layout> /// Layour 컴포넌트로 Route를 감싸준다.
        <Routes>
          <Route path="/" element={<AllMeetupsPage />}></Route>
          <Route path="/new-meetup" exact element={<NewMeetupPage />}></Route>
          <Route path="/favorites" element={<FavoritePage />}></Route>
        </Routes>
      </Layout>
    </div>
  );
}

/// Layout 컴포넌트
function Layout(props) { // Layout 컴포넌트에 props을 설정하고
  return (
    <div>
      <MainNavigation/>
      <main className={classes.main}>
      {props.children} // props에 할당된 children 값(포함된 컴포넌트) 를 출력한다고 명시한다.
    </main>
    </div>
  )
}
```
- `Card`컴포넌트에서 했던것과 같이, 단순히 상위 컴포넌트로 하위 컴포넌트를 wrapping 한다고 출력되는게 아닌, **props**와 그에 할당된 **children**을 할당해줘야 제대로 출력된다.
##### 왜 이렇게 하는걸까?
- **한 개의 컴포넌트는 한 개의 기능을 한다.**라는 철학을 따른다.
- `Card`컴포넌트는 카드 형식으로, `Layout`컴포넌트는 레이아웃을 생성, `Route`컴포넌트는 라우터를 생성 등과 같이 기능을 세분화하고 그 에 따라 재사용이 가능한 컴포넌트로 구성해주기 위함이다.


### 양식 추가하기.
- 사용자 화면에서의 입력을 통해 서버에 데이터를 저장하고, 출력해보자.
- NewMeetupPage에 `form`을 추가한다. 이를 위해 `form`기능을 하는 NewMeetupForm 컴포넌트를 생성해준다.

- React 에서 JavaScript와 Html에서의 내장 키워드가 겹치는 `class`를 구분하기 위해 html이 class를 `className`으로 사용한 것과 같이 `for`을 `htmlfor`로 대체하여 사용한다.(이지만 `className`외 거의 유일한 예외라고 한다^^..)
  
#### 입력 form 컴포넌트
- 위에서 말한 것 처럼 입력을 위한 `form` 컴포넌트를 만들자.
```react
function NewMeetupForm() {
  return (
    <div>
      <Card>
      // vue 에서 만들었던 폼의 형식과 비슷하다.
      // for가 htmlfor 로 대체되었단점 제외
        <form className={classes.form}> 
          <div className={classes.control}>
            <label htmlFor="title">Meetup Title</label>
            <input type = "text" required id = "title"/>
          </div>
      // 이후 제출을 위한 버튼
          <div className={classes.actions}>
            <button>Add Meetup</button>
          </div>
        </form>
        
      </Card>
    </div>
  )
}

export default NewMeetupForm
```
- 제출 기능은 구현되지 않는 폼 형식이다.
#### form submit
- `button`을 통해 http Request을 보내고 리로드 되는걸 방지하고, react와 JavaScript로 처리하도록 해야한다.
- JavaScript의 로직으로 처리하면 request를 보내지만 리로드를 통해 페이지를 다시 불러오지 않는다.(브라우저의 기본동작을 막지않으면 리로딩이 진행된다.) 
```react
import { useRef } from "react" // reference, connection을 위해 useref를 import 한다.
function NewMeetupForm() {
  const titleInputRef = useRef() // 참조 객체, ref 생성

<form className={classes.form} onSubmit={submitHandler> // onSubmit prop을 통해 제출 event 감지한다. 감지시 submitHandler 함수 실행.
  <div className={classes.control}>
    <label htmlFor="title">Meetup Title</label>
    <input type = "text" required id = "title" ref={titleInputRef}/> // ref(참조) prop 추가
  </div>
</form>

function submitHandler(event) {
    event.preventDefault() // 페이지 리로딩이 기본인 event를 방지하는 Javascript 함수

    const enteredTitle = titleInputRef.current.value // ref 객체 저장된 정보가 enteredTitle에 할당됨

    // 결과가 meetupData에 저장.
    const meetipData = {
      title: enteredTitle,
    }
  }
}
```
##### eventHandler
- 기본 event는 리로딩을 유발하기 때문에 handlering을 위한 함수가 필요하다.
- `onEvent`의 event가 실행되면 eventHandler 함수가 실행되고, `<input>`에 참조된 prop에 따라 참조 객체(useRef)에 값이 할당된다.
- 할당된 참조 객체는 반환할 data에 저장된다.

##### event.preventDefault
- JavaScript 함수로 event에 기본으로 할당된 동작을 방지한다(해당 기능은 페이지 리로딩을 방지)

##### useRef
- React에서 import한 함수로 참조 객체를 생성한다.
- 생성된 참조 객체를 통해 `<form>`에서 입력된 값을 변수와 connetion하여 값을 할당한다.
  ```react
  const dataInputRef = useRef() // 참조객체 생성

  ...
  <input ref = {dataInputRef}/> // 참조 객체를 input의 값과 연결. input이 submit 될시 참조 객체에 그 값이 저장된다.
  /// submit 시 submitHandler 실행

  function submitHandler(event){
    event.preventDefault() // event의 기본 동작 방지

    const enteredData = dataInputRef.current.value // 참조 객체에 저장된 정보에 접근하여 변수에 할당한다.

    // 데이터를 저장하여 처리하든, 반환하여 DB에 전송한다.
  }
  ...
- `useRef.current.value` : 현재 참조 객체의 값
- '이름' 항목이 필수 입력값일때 이름을 입력 -> (참조객체에 `<input>`와 연결됨 ) -> `submit` 실행 = `submitHandler` 함수 실행 -> 기본 `submit`을 막고 참조객체는 연결된 `<input>`의 값을 갖는다.