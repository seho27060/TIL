[toc]
# Learning React
## Ch.5 JSX를 사용하는 리액트
- JSX : JavsScript + XML, 자바스크립트 코드 안에서 바로 태그 기반의 구문을 써서 리액트 엘리먼트를 정의할 수 있게 해주는 자바스크립트 확장.

### 1. JSX로 리액트 엘리먼트 정의하기

- JSX에서는 태그를 사용해 엘리먼트의 타입을 지정한다. 태그의 속성은 프로퍼티를 표현한다. 여는 태그와 닫는 태그 사이에 엘리먼트의 자식을 넣는다.

![image-20220709171101555](README_default.assets/image-20220709171101555-16573542642221.png)

- 위와 같이 중괄호로 감싼 재료 배열을 JSX 프로퍼티로 넘길 수 있다.(이렇게 중괄호로 감싼 코드를 **자바스크립트 식(JavaScript expression, JSX)**이라고 부른다.)
- 자바스크립트 식에는 배열, 객체, 함수 등이 포함된다.

#### 1.1 JSX 팁

##### 내포된 컴포넌트

- JSX에서는 다른 컴포넌트의 자식으로 컴포넌트를 추가할 수 있다.

  ```react
  <ingredientsList>
  	<ingredient/>
  	<ingredient/>
  	<ingredient/>
  	<ingredient/>
  </ingredientsList>
  ```

##### className

- 자바스크립트에서 class가 예약어이므로, class 속성대신 className을 사용한다.

  ```react
  <h1 clasName = "fancy">구운 연어</h1>
  ```

##### 자바스크립트 식

- 중괄호로 자바스크립트 식을 감싸면 중괄호 안의 식을 평가해서 결괏값으로 사용해야 한다.

```react
const title = "WOW!!";
<h1>{title}</h1> // "WOW!!" 출력
```

##### 평가

- 중괄호 안에 들어간 자바스크립트 코드는 그 값을 평가받는다. === 함수 호출 및 연산이 가능하다.

```react
<h1>{"HELLO" + title}</h1>
<h1>{title.toLowerCase().replace}</h1>
```

#### 1.2 배열을 JSX로 매핑하기

```react
<ul>
	{props.ingredients.map((ingredient,i) => {
        <li key={i}>{ingredient}</li>
    })}
</ul>
```

- 위와 같이 JSX를 통해 배열을 JSX 엘리먼트로 변환할 수 있다.



### 2. 바벨

- 소스 코드를 브라우저가 해석할 수 있는 코드로 변환해주는 수단.

```html
<script type="text/babel">
	// JSX 코드를 넣거나 별도의 자바스크립트 파일에 대한 링크를 script 태그에 넣는다.
</script>
```

- 위와 같은 방법으로 바벨로 자바스크립트 코드를 변환 가능하다.
- 프로덕션에 적합하진 않지만, 접근하기 쉬운 방법

### 3. JSX로 작성한 조리법

- JSX의 단점은 브라우저가 JSX를 해석하지 못한다는 점.
- JSX를 순수 리액트로 변환해야한다.
