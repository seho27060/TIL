import NewTodo from "./components/NewTodo";
import Todos from "./components/Todo";
import TodoContextProvider from "./store/todos.content";

function App() {

  return (
    <TodoContextProvider>
      <NewTodo />
      <Todos />
    </TodoContextProvider>
  );
}

export default App;
