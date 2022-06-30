[toc]
# React_00
## React 시작하기
### 개요
#### React 란 무엇인가요?
- React 는 사용자 인터페이스를 구축하기 위한 선언적이고 효율적이며 유연한 JavaScript 라이브러리 이다.
- "컴포넌트" 라는 작고 고립된 코드의 파편을 이용하여 복잡한 UI를 구성한다.
- 아래의 코드를 통해 "컴포넌트"를 살펴보자

```react
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}
```

- ShoppingList 는 **React 컴포넌트 클래스, React 컴포넌트 타입** 이라고 한다.
- render 함수를 통해 화면에서 보고자 하는 내용을 경량화한 React 엘리먼트로 반환한다.



### 틱태토 게임 만들기

#### Create React App

- 새로운 프로젝트 만들기

```npm
npx create-react-app [AppName] // App 생성
cd my-app
npm start // 서버 실행
```

![image-20220630224044091](README.assets/image-20220630224044091.png)

- npx ~~ 은 실수가 아니며, npm 5.2+ 버전의 패키지 실행 도구 라고 한다.
- Create React App 은 백엔드 로직과 DB를 제어할 수 없다./ **오직 프론트엔드 빌드 파이프라인 만 생성**
- Babel, webpack 과 같은 build 도구를 사용하나, 설정없이도 동작
- 프로젝트가 배포 준비되고, npm run build 를 실행하면 build 폴더 안에 제작한 앱의 최적화된 build를 생성한다.

#### 틱태토 스켈레톤 코드 작성
- my-app 프로젝트를 생성하고, scr 를 비우고 해당 scr 폴더에 index.js, index.css 를 생성하고 제시된 코드들을 입력해준다.

![image-20220630224845698](README.assets/image-20220630224845698.png)

- index.js 파일을 살펴보면, Square, Board, Game 의 3가지 컴포넌트를 확인할 수 있다.
- Game 은 Board를, Board는 Square를 렌더링함을 알 수 있다.

#### Props를 통해 데이터 전달하기

```react
class Board extends React.Component {
  renderSquare(i) {
    return <Square value={i} />;
  }
}
class Square extends React.Component {
  render() {
    return (
      <button className="square">
        {this.props.value}
      </button>
    );
  }
}
```

- Board 컴포넌트의 renderSquare 함수와 Square 컴포넌트의 render 함수를 위와 같이 수정해주면
  틱택토가 아래와 같이 숫자가 기입된다.

![image-20220630231240529](README.assets/image-20220630231240529-16565983613051.png)

- 부모 컴포넌트 Board 에서 자식 컴포넌트 Square 로 "prop을 전달"했다.

#### 사용자와 상호작용하는 컴포넌트 만들기
- Square 컴포넌트를 "클릭"하면 "X"가 체크되도록 만들어보자
  아래의 코드 추가

```react
class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={function() { console.log('click'); }}>
        {this.props.value}
      </button>
        // 아래와 같이 화살표 함수를 사용하면 this 의 혼란스런 동작을 피하고 타이핑 횟수가 감소한다!
       <button className="square" onClick={() =>console.log('click');}>
        {this.props.value}
      </button>
    );
  }
}
```

- button  태크에 "onClick" 이 추가되고 click 이벤트 발생시 할당된 function이 작동한다.
- 해당 funtion은 브라우저 개발자 도구에 "click"을 출력한다.



- 다음단계, Square 컴포넌트의 "click"을 "기억"하기 위해 **state**를 사용한다.
- onClick 핸들러에 할당된 함수를 아래와 같이 수정해준다.
- 변경된 함수에 의해, 클릭을 발생하면 Square 컴포넌트의 state의 value가 "X"가 되어 렌더링된다.

```react
class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }

  render() {
    return (
      <button
        className="square"
        onClick={() => this.setState({value: 'X'})}
      >
        {this.state.value}
      </button>
    );
  }
}
```

- JavaScript 에서는 하위 클래스의 생성자를 정의할때, 항상 **super()**를 호출해야 한다.
- == **모든 React 컴포넌트 클래스는 생성자를 가질때, super(props) 호출 구문부터 작성해야 한다.**



#### State 끌어올리기

- 현재는 클릭 유무를 나타내는 value가 개별적인 Square 컴포넌트에 유지되고 있다.
- 틱택토에서는 X와 O를 표시해야 하는데, 이를 위해 부모 컴포넌트인 Board에서 자식 컴포넌트인 Square로 state를 요청한다고 생각할 수 있는데, 이러한 접근은 가능하지만 코드를 복잡하게 하고, 버그에 취약하고 리팩토링이 어렵다(추천하지 않는다.)
- 따라서 부모 컴포넌트에 상태를 저장하는 state를 만들어준다.

> **여러개의 자식으로부터 데이터를 모으거나 두 개의 자식 컴포넌트들이 서로 통신하게 하려면 부모 컴포넌트에 공유 state를 정의해야 합니다. 부모 컴포넌트는 props를 사용하여 자식 컴포넌트에 state를 다시 전달할 수 있습니다. 이것은 자식 컴포넌트들이 서로 또는 부모 컴포넌트와 동기화 하도록 만듭니다.**

- state를 부모 컴포넌트로 끌어올리는건 React 컴포넌트를 리팩토링할 때 흔히 사용한다.

```react
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
    };
  }

  handleClick(i) {
    const squares = this.state.squares.slice();
    squares[i] = 'X';
    this.setState({squares: squares});
  }

  renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
  }

  render() {
    const status = 'Next player: X';

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}
```

- 위와 같이 index.js의 Board 컴포넌트를 수정했을때,
  1. 내장된 DOM <button> 컴포넌트에 있는 onClick prop 은 React 에게 클릭 이벤트 리스너를 설정하라고 한다.
  2. 버튼이 클릭되면, React는 render() 함수에 정의된 onClick 이벤드 핸들러를 호출한다.
  3. 이벤트 핸들러는 this.props.onClick()을 호출한다. Square의 `onClick` prop은 Board에서 정의되었습니다.
  4. Board에서 Square로 `onClick={() => this.handleClick(i)}`를 전달했기 때문에 Square를 클릭하면 Board의 `handleClick(i)`를 호출합니다.

- Dom <button> 엘리멘트의 **onClick 어트리뷰트**는 **내장된 컴포넌트**임으로 React에게 특별한 의미가 있다.
