[toc]
# Learning React
## Ch.4 리액트의 작동원리
- JSX 라는 HTML과 아주 비슷해 보이는 태그를 기반으로 하는 JS 구문을 사용하여 React 구축할 것이다.
- React에서는 React Element가 핵심 단위이다.

### 1. 페이지 설정

- 리액트를 브라우저에서 다루기 위해선 React, ReactDOM 라이브러리가 필요하다.
  1. React : 뷰를 만들기 위한 라이브러리/
  2. ReactDOM : UI를 실제로 브라우저에 렌더링할 때 사용하는 라이브러리.

### 2. 리액트 엘리먼트

- HTML을 이루는 엘리먼트 -> 브라우저가 HTML문서 읽음 -> DOM 엘리먼트 변환 -> DOM은 사용자 인터페이스를 화면에 표시한다.
- AJAX(Asynchronous JavaScript and XML)의 등장으로 단일 페이지 애플리케이션(SPA, Single Page Application)이 가능해짐.
- 리액트는 브라우저 DOM을 갱신해주기 위해 만들어진 라이브러리/ 리액트가 모든 처리를 대신 해주므로 SPA를 효율적으로 만들기 위해 복잡하게 구현할 필요가 없다.
- 브라우저의 DOM = DOM 엘리먼트로 구성/ React DOM = 리액트 엘리먼트로 구성. 비슷해 보이지만, 리액트 엘리먼트는 해당 엘리먼트에 대응하는 실제 DOM 엘리먼트가 어떻게 생겨야 하는지 기술한다.(리액트 엘리먼트는 브라우저 DOM을 만드는 방법을 알려주는 명령)

```react
React.createElement("h1", { id : "recipe-0"}, "구운 연어")
///  와 같은 명령은
<h1 id = "recipe-0">구운 연어</h1> 와 같은 DOM 엘리먼트로 렌더링 한다.
```

### 3. ReactDOM

- ReactDOM의 **render 메서드**를 통해 브라우저에 렌더링

```react
var dish = React.createElement("h1", null, "구운 연어")
ReactDOM.render(dish, document.getElementById('root'))
```

 위와 같은 ReactDOM.render 을 통해 아래와 같은 HTML로 렌더링 된다.

```html
<body>
    <div id = "root">
        <h1>
            구운 연어
        </h1>
    </div>
</body>
```

#### 3.1 자식들

- **props.children**을 사용해 자식 엘리먼트를 렌더링한다.
- 리액트 엘리먼투에 다른 리액트 엘리먼트를 자식으로 렌더링하여 **엘리먼트 트리(element tree)**를 구현 가능하다.

##### 데이터를 가지고 엘리먼트 만들기

```react
const list = React.createElement(
      "ul",
      {className : "ingredients"},
      recipe.map((ingridient, i) => React.createElement('li',{key:i},ingridient)))
    const result = React.createElement(
      "section",
      {id : "baked-salmon"},
      dish,
      list,
    )const recipe = ["salmon 900g", "fresh rosemary", "olive oil","small remon slice","salt 1 tea spoon","mashed garlic"]
    // const list = React.createElement(
    //   "ul",
    //   null,
    //   React.createElement("li",null,"salmon 900g"),
    //   React.createElement("li",null,recipe[1]),
    //   React.createElement("li",null,recipe[2]),
    //   React.createElement("li",null,recipe[3]),
    //   React.createElement("li",null,recipe[4]),
    //   React.createElement("li",null,recipe[5]),
    // ) 
    
    const list = React.createElement(
      "ul",
      {className : "ingredients"},
      recipe.map((ingridient, i) => React.createElement('li',{key:i},ingridient)))
    const result = React.createElement(
      "section",
      {id : "baked-salmon"},
      dish,
      list,
    )
```

- 위 주석처리된 하드코딩을 아래와 같이 반복문으로 구현가능하다.

- 배열을 이터레이션해서 자식 엘리먼트의 리스트를 만드는 경우, 리액트에서는 각 자식 엘리먼트에 **key 프로퍼티를 넣는 것을 권장한다.**

### 4. 리액트 컴포넌트

- **컴포넌트(Componet)**: 다른 내용이 들어갈 수 있는 같은 형태의 DOM 구조.
- 1개의 객체를 만들고(해당 객체에 여러개의 자식객체를 만들 수도있다.) 다른 내용의 10,000개의 인스턴스가 간단하게 생성가능하다.

#### 4.1 리액트 컴포넌트의 역사

- 시간에 따른 리액트 API 변화를 살펴보자.

##### 첫 번째 정류장: createClass

- render() 메서드 정의가 포함되어 있었다.

##### 두 번째 정류장: 클래스 컴포넌트

- React.componet API 를 활용하여 class 구문을 사용해 새로운 컴포넌트 인스턴스 만들기

```react
class IngredientList extends React.Component {
    render(){
        return React.createElement(
        "ul",
        { className: "ingredients"},
        this.props.items.map((ingredient, i) =>
                            React.createElement("li", { key : i}, ingredient)
                            )
        )
    }
}
```



