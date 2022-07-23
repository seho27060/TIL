- [**udemy React + TypeScript**](#udemy-react--typescript)
  - [**React + Typescript 프로젝트**](#react--typescript-프로젝트)
    - [**Props 및 Typescript 작업하기**](#props-및-typescript-작업하기)
      - [함수 정의하기](#함수-정의하기)
      - [React.FC](#reactfc)
    - [데이터 모델 추가하기](#데이터-모델-추가하기)
    - [Typescript를 활용한 Form 구현](#typescript를-활용한-form-구현)
      - [form의 input 내용을 연결](#form의-input-내용을-연결)
      - ["Function Props" 로 작업하기](#function-props-로-작업하기)
      - [State 및 TypeScript 관리하기](#state-및-typescript-관리하기)
    - [컨텍스트 API 및 TypeScript](#컨텍스트-api-및-typescript)
      - [Type Alias 정의](#type-alias-정의)
      - [createContext](#createcontext)
      - [ContextProvider](#contextprovider)
# **udemy React + TypeScript**
## **React + Typescript 프로젝트**
- TypeScript기반 react 프로젝트 생성하기
```bash
$npx create-react-app appName --template typescript
```
- typescript를 javascript 로 변환하는 컴파일 과정이 추가되지만, 자동으로 진행되니 알고만 있자.

### **Props 및 Typescript 작업하기**
```react
import React from "react";

const Todos: React.FC<{ items: string[] }> = (props) => {
  return (
    <ul>
      {props.items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
};
export default Todos;
```

#### 함수 정의하기
- Typescript에서의 그것과 같게, react에서 typescript를 활용할때도 함수의 인자 타입을 정의할 수 있다.
- 인자의 타입은 다양하므로 **Generics(제네릭)** 타입으로 정의하도록 한다.
- `React.FC`와 같이 react에서 제공하는 기본 제네릭 타입이 있다. (FC : FunctionComponent)

#### React.FC
- `@types/react`에서 기본 제공하는 구문
- 해당 컴포넌트가 함수형 컴포넌트임을 명시한다.
```react
const FunctionName: React.FC<{items: string[],}> = {props} =>{
  return (
    ...
  )
}
```
- `React.FC<{}>`의 중괄호({})에 props의 타입을 정의하도록 한다.
- 위 예시에서 `props`의 chilren으로 `items`가 있음을 명시하고, `items`의 타입은 string을 갖는 array임을 명시하였다.
- react와 typescript로 함수를 만들면 react의 FC를 통해 함수형 컴포넌트임을 명시하자

```react
import React from "react"

const TodoItem: React.FC<{text:string}> = (prop) => {
  return (
    <li>{prop.text}</li>
  )
}

export default TodoItem
```
- `React.FC`는 함수형 컴포넌트임을 명시해주는 것 뿐만 아니라, 해당 컴포넌트에 `children` 인자와 `id`인자를 대입된 `props`들과 합쳐주는 기능을 한다.
- 위와 같이 item 컴포넌트로 분리했을때, 해당 컴포넌트를 FC로 명시해주었다.

```react
const Todos: React.FC<{ items: Todo[] }> = (props) => {
  return (
    <ul>
      {props.items.map((item) => (
        <TodoItem text={item.text} key={item.id}/>
      ))}
    </ul>
  );
};

export default Todos;
```
- 부모 컴포넌트에서 FC로 선언된 자식 컴포넌트를 호출할때, `id`를 자식컴포넌트의 인자로 선언하지 않아도 자동으로 포함되어 부모 컴포넌트에서 prop할수 있을음 확인 할 수 있다.

### 데이터 모델 추가하기
- 사용자가 정의한 객체를 만들어보자.

```typescript
class Todo {
  id: string
  text: string

  constructor(todoText: string) {
    this.text = todoText
    this.id = new Date().toISOString()
  }
}

export default Todo
```
- tpyescript에서는 클래스 선언에서 인자의 타입과 생성자를 명시해줘야 한다.(JavsScript에서는 생성자만 해도됐음.)
- Typescript-react에 따라 위와 같이 정의하고,
- class는 type으로도 사용될 수 있다.


```React
const Todos: React.FC<{ items: Todo[] }> = (props) => {
  return (
    <ul>
      {props.items.map((item) => (
        <li key={item.id}>{item.text}</li>
      ))}
    </ul>
  );
};
```
- `Todo`라는 새로운 사용자 정의 객체가 생성되었으므로, 인자의 type을 대신할 있다.

```react
function App() {
  const todos = [
    new Todo('Learn React'),
    new Todo('learn TypeScript')
  ]
  return (
    <div>
      <Todos items = {todos}/>
    </div>
  );
}
```
- 이와 같이 `Todo`의 input 인자 조건을 맞게하여 `Todo`타입의 객체를 생성하여 배열을 구성할 수 있다.

### Typescript를 활용한 Form 구현
- 기존의 방법과 매우 유사하며, 주의할 점은 `typescript`에서 했던것과 같이 input인자의 type을 잘 지정해주도록 한다.
- 
```react
// NewTodo
import React from "react"

const NewTodo= () => {
  const submitHandler =(event:React.FormEvent) => {
    event.preventDefault()
  }

  return (
    <form onSubmit={submitHandler}>
      <label htmlFor="text">Todo text</label>
      <input type = 'text' id='text'></input>
      <button>Add Todo</button>
    </form>
  )
}

export default NewTodo
```
- `const submitHandler =(event:React.FormEvent) =>`에서 input인 event에 대한 type을 지정해주고 있다.
- `React.FormEvent`는 react에서 제공하는 기본 이벤트 타입이다. 이외에 여러가지 event 타입이 제공된다.

#### form의 input 내용을 연결
- `useState`나 `useRef`를 사용하여 input된 데이터를 호출한다.
- typescript의 특성상 선언하거나, 입력할때 자료의 형태(type)을 명시해줘야함을 잊지말자.
```react
/// NewTodo
const NewTodo= () => {
  const todoTextInputRef = useRef<HTMLInputElement>(null)

  const submitHandler =(event:React.FormEvent) => {
    event.preventDefault()

    const enteredText = todoTextInputRef.current!.value 
    if (enteredText.trim().length ===0){
      return
    }
  }
```
- `const todoTextInputRef = useRef<HTMLInputElement>(null)`와 같이 ref객체를 선언할때 Generics 타입을 지정한다.
  - `HTMLInputElement는 react에서 기본 제공하는 type이다.
- ts에서의 연산자 : current? 은 current의 value가 null일수있으니 일단 접근해보고 null이 아니라면 값에 접근하고, current!는 value는 절대 null이 아님을 확신하니 current의 value값에 접근하여 값을 가져오라는 연산자이다.
  - 이때 ! 연산자는 해당 값이 null이 아님을 확신할때 사용하도록 한다.
    
#### "Function Props" 로 작업하기
- 부모 컴포넌트의 함수를 자식 컴포넌트로 prop하여 사용하는 방법을 알아보자.

```react
const NewTodo: React.FC<{onAddTodo: (text:string) => void }> = (props) => {
  const todoTextInputRef = useRef<HTMLInputElement>(null)

  const submitHandler =(event:React.FormEvent) => {
    event.preventDefault()

    const enteredText = todoTextInputRef.current!.value
    
    if (enteredText.trim().length ===0){
      return
    }
    props.onAddTodo(enteredText)
  }

  
  return (
    ...
    )
```
- `NewTodo: React.FC<{onAddTodo: (text:string) => void }> = (props) => {`와 같이 NewTodo 함수에서 `onAddTodo`함수를 prop받고, 그에 대한 type을 지정해준다.
  - 함수의 타입 지정은, 해당 함수의 input 타입, output 타입을 지정해준다.
  - 위에서 `onAddTodo`함수는 string을 입력받아 void를 출력하는 타입의 함수임을 지정한다. 
  - 이를 통해 props에는 `onAddTodo`의 타입에 포함된다.
- `props.onAddTodo(enteredText)`와 같이 컴포넌트내에서 prop된 함수를 사용하고 있다.

#### State 및 TypeScript 관리하기
- 입력받는 폼을 구성하고, Ref 를 통해 입력받은 데이터로 변수를 구성하였다. 이제 state를 이용하여 데이터를 저장해보자.

```react
///App.tsx
import { useState } from 'react';
function App() {

  const [todos, setTodos] = useState<Todo[]>([]) // <>로 지정해주지 않으면 해당 state는 빈 배열만을 가져야한다는 의미를 가짐.
  
  const addTodoHandler = (todoText: string) => {
    const newTodos = new Todo(todoText)

    setTodos((prevTodos) => {
      return prevTodos.concat(newTodos)
    })
  }
  return (
    <div>
      <NewTodo onAddTodo={addTodoHandler}/>
      <Todos items = {todos}/>
    </div>
  );
}
```
- `const [todos, setTodos] = useState<Todo[]>([])`와 같이 useState를 통해 state 객체로 선언해주고, state의 타입을 `Todo`로 지정해준다.
```react
setTodos((prevTodos) => {
      return prevTodos.concat(newTodos)
    })
```
- 위와 같이 state를 업데이트하는 dispatch에 대한 함수도 지정해준다.

### 컨텍스트 API 및 TypeScript
- Context를 활용하여 store를 구축해보자.

#### Type Alias 정의
```react
type TodosContextObj = {
  items: Todo[];
  addTodo: (text:string) => void;
  removeTodo: (id: string) => void;
}
```
- store내에서 공통으로 사용될 custom type을 지정해주자.
- `items`, `addTodo`, `removeTodo`의 객체에 어떤 타입이 input되고, output이 반환되는지 지정한다.
#### createContext
```react
import React from "react";

export const TodoContext = React.createContext<TodosContextObj>({
  items: [],
  addTodo: () => {},
  removeTodo: (id: string) => {},
});
```
- Context를 생성한다.
- 인자 값들의 초기값을 지정한다.
- 값들의 type 또한 지정해줘야 하고, 앞에서 생성한 Type Alias를 활용하여 지정한다.

#### ContextProvider
```react
// 강의 나온대로 하면 안되고 밑에처럼 하니깐 되네?..오ㅓㅐ??..
function TodoContextProvider(props: any) {
  const [todos, setTodos] = useState<Todo[]>([]); // <>로 지정해주지 않으면 해당 state는 빈 배열만을 가져야한다는 의미를 가짐.

  ...
  {대충 함수 정의 구간}
  ...
  const contextValue: TodosContextObj = {
    items: todos,
    addTodo: addTodoHandler,
    removeTodo: deleteTodoHandler
  };
  
  return (
    <TodoContext.Provider value={contextValue}>
      {props.children}
    </TodoContext.Provider>
  );
} 

export default TodoContextProvider
```
- `todos`를 state로 선언해줄때, 빈 배열로 선언시 `todos`에는 빈 배열만 들어가야한다.
  - `Todo`타입을 지정하는걸 잊지말자.
- `contextValue`를 선언하고
- `TodoContext.Provider`에 `contextValue`를 할당하여 반환하는걸로 마무리하자.
