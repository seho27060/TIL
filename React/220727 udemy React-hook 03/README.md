[toc]

# udemy React-hook

## What is useMemo?

- 프로젝트 구현에 있어서 불필요한 렌더링이 여러번 일어나는 경우가 있다.
- `state` 변화에 따른 리렌더링.. 함수 호출에 따른 리렌더링..등등
- `useCallback`이 "함수"를 저장하여 불필요한 재생성-호출을 방지했다면, `useMemo`는 "값"을 저장하여 불필요한 재생성-호출을 방지한다.
- 컴포넌트를 기억(Memorizing)하는 하나의 방법
- 컴포넌트를 생성할때 보통 `React.Memo`를 사용한다.
  - `useMemo`를 사용하면 렌더링할때마다 데이터를 재생성하지 않아 효울적 렌더링이 가능하다.

### How to use useMemo?

```javascript
  const ingredientList = useMemo(() => {
    return (
      <IngredientList
        ingredients={userIngredients}
        onRemoveItem={removeIngredientHandler}
      />
    );
  }, [userIngredients, removeIngredientHandler]);

  ...

  <section>
    {ingredientList}
  </section>
```

- 위와 같이 `useMemo(() => {함수실행내용}.[의존성배열])`로 구성하여 사용한다.
- 의존성 배열의 값의 변경이 감지되면 함수실행내용의 컴포넌트를 렌더링한다.

- 컴포넌트에 포함된 데이터의 규모가 크다면 리렌더링이 실행될때마다 많은 시간이 걸리므로, 위의 기능을 활용하도록 하자.
- 
#### detail-index1
