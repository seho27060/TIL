[toc]
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

#### context Provider 함수
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
- context와 관련된 모든 컴포넌트를 wrapping 해줘야 한다.


##### addFavoriteHandler
- 새로운 favoriteMeetup을 이전 리스트에 추가하여 반환

##### removeFavoriteHandler
- 입력받은 meetup의 id를 찾아 삭제한 리스트를 반환

##### itemIsFavoriteHandler
- 해당 meetup이 favorite에 해당되는지 확인하는 helper 함수


### 컴포넌트에서의 컨텍스트 사용
- 전역으로 state 관리하기
#### useContext
```react 
import { useContext } from "react"
```

- 위와같은 방법은 일시적인것.