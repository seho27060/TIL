[toc]
# udemy React 
## react 06
### Redux
#### What is "Redux"?
- 크로스 컴포넌트 또는 앱 와이드 상태를 관리하기 위한 state 관리 시스템

##### State의 3가지 종류
1. Local State : 데이터가 변경되어 컴포넌트 ui에 영향을 끼침. (ex: 세부정보를 끄는 토글..etc)
2. Cross-Component State : 한개의 컴포넌트에서 다른 다수의 컴포넌트에 영향을 주고 받을때의 State (ex : prop chaining,prop drilling)
3. App-Wide State : 전체 어플리케이션에 전역적으로 사용되는 State (ex : 유저 인증 상태, prop chaining,prop drilling )
- `Context`를 통해 위 3개의 컴포넌트를 관리할 수 있다.

- `Redux`는 `Context`의 복잡한 설정/ 관리, 비교적 낮은 성능과 같은 **잠재적**문제를 예방할 수 있다.

#### Redux 작동 방식
- Redux는 하나의 유일한 **데이터(State,상태) 저장소**(Central Data(State) Store)
  - 공통된 데이터 저장소를 가지므로, prop drilling, prop chaining과 같은 방식이 아닌 바로 컴포넌트간을 prop 할 수 있다.
  - 물론 컴포넌트는 Store를 Subscription 해야한다.
- 데이터는 무조건 **스토어 -> 컴포넌트**로 흐른다. 컴포넌트에서는 절대로 데이터를 수정할 수 없다.

![img1](./img/img1.jpg)

##### Reducer Function
- `Redux`에서 데이터의 업데이트를 담당함.
- 데이터의 입력을 변환하여 반환
- Mutate Store Data

##### Action
- Component에서 Dispatch를 수신받아, Reducer로 전달하면 새로운 상태로 갱신한다.
- State이 변경에 따라 Subscription한 컴포넌트에서는 UI를 업데이트한다.