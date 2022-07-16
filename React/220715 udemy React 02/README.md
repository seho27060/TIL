[toc]
# udemy React
## React 02
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

#### Link
- 기존의 `<a>`태그는 서버에 요청을 보내 새로고침을 유도한다.
- 리액트에서는 그럴 필요가 없다.
- `react-router-dom`에서 `Link`컴포넌트를 import 하여 대체한다.
  - Event에 의한 서버 요청을 방지하고, url에 변화에 매치되는 컴포넌트를 출력하게 된다.

##### to props
- `Link`컴포넌트에 `to` props를 추가하여, 추가된 url로 이동이 가능하다.
- 변화된 url에 따라 `Routes`에 할당된 url중 매칭이 되면 적절한 컴포넌트가 출력된다.
```react
function MainNavigation() {
  return (
    <header>
      <div>React Meetuos</div>
      <nav>
        <ul>
          <li>
            <Link to="/new-meetup">Add new meetups</Link>
            /// 하이퍼링크가 출력되지만, url변화를 주는 라우터 형식으로 기능한다.
          </li>
          ...
        </ul>
      </nav>
    </header>
  )
}
```
### css module
- 컴포넌트마다 스타일을 모듈로 관리하기 위한 방법
- 컴포넌트 스타일 옵션을 갖는 css 파일을 `componentName.module.css`와 같은 방식으로 생성해준다.
```react
import classes from './MainNavigation.module.css' // 생성된 css 파일을 classes라는 객체로 import

...
<header className = {classes.header}> // 이와 같이 classes로 import 된 css 파일에서 필요한 옵션을 태그의 클래스에 추가하여 스타일 props에 추가 할 수 있다.
```

### 데이터 목록 출력하기
```react
const DUMMY_DATA = [
  {
    id: '1',
    title : "title1",
    ...
  },
  {
    ...
  }
] // 와 같은 데이터가 있다고 할때,

...
// 컴포넌트 내에서
{[<li>item1</li>, <li>item2</li>]}

{DUMMY_DATA.map((item) => {
  return <li key = {item.id}> {item.title} </li>
})}
```
- {} 안의 자바스크립트(JSX) 구문 내에서 html 태그를 포함할 수도 있고
- {} 안의 JSX를 통해 데이터를 `map`하여 리스트의 인자중 원하는 값의 key를 통해 출력가능하다
- `map`사용시 `key` prop으로 unique한 값을 줘야 한다.
---

### 더 많은 리액트 컴포넌트 추가하기
- 컴포넌트를 생성하고, props를 통적으로 할당하여 공통된 템플릿에 다른 데이터를 대입하여 여러 데이터를 같은 컴포넌트 형식으로 출력가능하다.
```react
/// MeetupItem 컴포넌트
import classes from './MeetupItem.module.css'

function MeetupItem(props) {
  return (
  <li className={classes.item}>
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
  </li>
  )
}

/// MeetupList 컴포넌트
import MeetupItem from "./MeetupItem";
import classes from "./MeetupList.module.css";

function MeetupList(props) {
  return (
    <ul className={classes.list}>
      {props.meetups.map((meetup) => (
        <MeetupItem
          key={meetup.id}
          id={meetup.id}
          image={meetup.image}
          title={meetup.title}
          address={meetup.address}
          description={meetup.description}
          /// prop 된 props에 meetups 데이터에 대해 mapping 하여 출력을 원하는 데이터를 MeetupItem 컴포넌트에 prop 한다.
        />
      ))}
    </ul>
  );
}
```
- ComponentList 는 Component로 구성되어 있는 컴포넌트이다.
- 모듈화를 위해 기능을 세분화하는 철학과 부합하다.

 
### react-router-dom ver.6에서 달라진 라우팅
#### Route
- `Route` 컴포넌트내부에 다른 컴포넌트를 포함하여, url 변경시 출력하도록 했지만
- ver.6부터는 `Route`컴포넌트의 `props`로 컴포넌트를 주어 라우팅을 한다.
```react
<Route path="">
  <Component/>
<Route/>
////
<Route path="" element={Component}/> // self-closing 으로 깔끔히 끝낼수도 있다.
```

#### Switch -> Routes
- ver.6에서 부터는 Switch의 기능이 Routes로 대체되었다. 
- 그냥 이름만 바꿔주면 된다.
- `Route`가 하나여도 무조건 `Routes`로 랩핑해줘야 한다.

#### exact
- ver.5에서는 url에서 path와 매칭되는 모든 컴포넌트를 출력하여, url으로만 매칭되는 path를 출력하기 위해 exact를 `Route`의 옵션에 추가해주었다.
- ver.6에서는 자동으로 정의한 path로만 매칭되어 이동되므로 exact를 옵션으로 안넣어 줘도 된다.

#### 내부적 변화
- ver.5에서는 `Route`의 순서가 중요했으나(동적 세그먼트를 뒤에 배치), 이젠 그렇지 않다.