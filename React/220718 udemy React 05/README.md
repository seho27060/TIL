- [udemy React](#udemy-react)
  - [React 05](#react-05)
    - [리액트 컨텍스트](#리액트-컨텍스트)
    - [Context](#context)
      - [context 객체 생성](#context-객체-생성)
      - [context Provider 함수](#context-provider-함수)
        - [addFavoriteHandler](#addfavoritehandler)
        - [removeFavoriteHandler](#removefavoritehandler)
        - [itemIsFavoriteHandler](#itemisfavoritehandler)
    - [컴포넌트에서의 컨텍스트 사용](#컴포넌트에서의-컨텍스트-사용)
      - [useContext](#usecontext)
    - [더 많은 컨텍스트 사용하기](#더-많은-컨텍스트-사용하기)
# udemy React
## React 05
### 리액트 컨텍스트
- 이제까지의 state들은 포함된 하나의 컴포넌트에 영향을 끼친다.
- 부모 - 자식 컴포넌트 간의 prop 관계가 연쇄적으로 이어질 경우, 그 길이가 엄청나게 길어질 수 있다. 이는 비효율적인 컴포넌트 구현이다.
- 이를 위해 `Vue.js`의 `Vuex`와 비슷한 기능을 하는 `Redux`를 사용한다.
- 물론 react에 내장된 store 관리 솔루션이 존재한다.

### Context
```react
import { createContext } from "react"
```
- createContext import
- scr 하위에 `store` 폴더를 생성한다.
- `store` 폴더 하위에 `favorites-context.js` 을 생성.

#### context 객체 생성
```react
const FavoritesContext = createContext({
  favotires: [],
  totlaFavorites: 0,
});
```
- `context` 객체는 컴포넌트와 같은 취급함으로 대문자로 시작하여 생성한다.
#### context Provider 함수
```react
function FavoritesContextProvider(props) {
  const [userFavorites, setUserFavorites] = useState([]) /// State hook 활용

  ...

  const context = {
    favorites : userFavorites,
    totlaFavorites: userFavorites.length
  }

  return (
    <FavoritesContext.Provider value={context}>
      {props.children}
    </FavoritesContext.Provider>
  );
}
```
- `.Provider` 컴포넌트는 context의 state를 사용하는 모든 컴포넌트를 wrapping 해줘야 한다.
- 해당 프로젝트에서는 `index.js`에서 모든 컴포넌트를 wrapping하여 프로젝트의 모든 컴포넌트는 `context`사용이 가능하다.

```react
function FavoritesContextProvider(props) {
  const [userFavorites, setUserFavorites] = useState([]) /// State hook 활용

  function addFavoriteHandler(favoriteMeetup) {
    setUserFavorites((prevUserFavorites) => {
      return prevUserFavorites.concat(favoriteMeetup)
    })
  }

  function removeFavoriteHandler(meetupId) {
    setUserFavorites(prevUserFavorites => {
      return prevUserFavorites.filter(meetup => meetup.id !== meetupId)
    })
  }

  function itemIsFavoriteHandler(meetupId) {
    return userFavorites.some(meetup => meetup.id === meetupId)
  }
  ...
```
##### addFavoriteHandler
- 새로운 favoriteMeetup을 이전 리스트에 추가하여 반환
- **.concat** : 해당 배열에 인수 값을 더한 새로운 배열을 반환
##### removeFavoriteHandler
- 입력받은 meetup의 id를 찾아 삭제한 리스트를 반환
- **.filter** : 조건문이 true인 배열의 인자들을 갖는 새로운 배열 반환
##### itemIsFavoriteHandler
- 해당 meetup이 favorite에 해당되는지 확인하는 helper 함수
- **.some** : 모든 인자에 대한 조건문이 true라면 true 반환
- `FavoritesContext` 컴포넌트에서 `context`는 하나의 `state`로 관리된다.
`state`의 변화를 감지하여 재실행/재평가되며 `context`를 prop 했으므로 하위 컴포넌트들은 갱신된 `context` 값을 사용가능하다.

```react
  const context = {
    favorites : userFavorites,
    totlaFavorites: userFavorites.length,
    addFavorite : addFavoriteHandler,
    removeFavorite : removeFavoriteHandler,
    itemIsFavorite : itemIsFavoriteHandler,
  }
```
- `context`의 모든 인자를 `FavoritesContext` 컴포넌트가 감싸는 모든 컴포넌트에 노출시킨다.
```react
/// index.js
import { FavoritesContextProvider } from "./store/favorites-context";

ReactDOM.render(
  <FavoritesContextProvider>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </FavoritesContextProvider>,
  document.getElementById("root")
);
```
- `index.js`파일에서 모든 컴포넌트를 `FavoritesContextProvider`로 감싼다.

### 컴포넌트에서의 컨텍스트 사용
- 전역으로 state 관리하기
#### useContext
```react 
/// MeetupItem
import { useContext } from "react"
...
import FavoritesContext from "../../store/favorites-context";

function MeetupItem(props) {
  const favoriteCtx = useContext(FavoritesContext);

  const itemIsFavorite = favoriteCtx.itemIsFavorite(props.id);

  function toggleFavoriteStatusHandler() {
    if (itemIsFavorite) {
      favoriteCtx.removeFavorite(props.id);
    } else {
      favoriteCtx.addFavorite({
        id: props.id,
        title: props.title,
        description: props.description,
        image: props.image,
        address: props.address,
      });
    }
  }
```
- `FavoritesContext` 컴포넌트를 import 
- `FavoritesContext` 컴포넌트를 `useContext`를 활용하여 Context 객체로 선언한다. 이제 해당 컴포넌트에서 `FavoritesContextProvider`의 컴포넌트에 액세스 할 수 있다.
- `itemIsFavorite`의 bool 값에 따라 `toggleFavoriteStatusHandler` 함수 실행시 분기가 달라진다.

### 더 많은 컨텍스트 사용하기
```React
/// Favorites
import { useContext } from "react"

...

function FavoritePage() {
  const favoriteCtx = useContext(FavoritesContext)

  let content

  if (favoriteCtx.totlaFavorites === 0){
    content =  <MeetupList meetups = {favoriteCtx.favotires}/>

  }
  return (
    <section>
      <h1>My Favorite</h1>
      {content}
    </section>
  )
}
```
- `useContext`로 Context 객체를 선언하고, Favorites에 해당하는 meetup을 리스트로 반환받는 `favorites`함수를 통해 `content`에 저장한다.
- 이제 `Favorite`컴포넌트에서는 Favorites에 해당하는 meetup을 리스트로 반환한다.
  - 해당 컴포넌트에서는 `MeetupList` 컴포넌트에 prop을 다르게 주어 **재활용**하였다.