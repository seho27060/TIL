import React, { useState } from "react";
import Todo from "../models/todo";

type TodosContextObj = {
  items: Todo[];
  addTodo: (text:string) => void;
  removeTodo: (id: string) => void;
}

export const TodoContext = React.createContext<TodosContextObj>({
  items: [],
  addTodo: () => {},
  removeTodo: (id: string) => {},
});

// 강의 나온대로 하면 안되고 밑에처럼 하니깐 되네?..오ㅓㅐ??..
function TodoContextProvider(props:any) {
  const [todos, setTodos] = useState<Todo[]>([]); // <>로 지정해주지 않으면 해당 state는 빈 배열만을 가져야한다는 의미를 가짐.

  const addTodoHandler = (todoText: string) => {
    const newTodos = new Todo(todoText);

    setTodos((prevTodos) => {
      return prevTodos.concat(newTodos);
    });
  };

  const deleteTodoHandler = (todoId: string) => {
    const deletId = todoId;

    setTodos((prevTodos) => {
      return prevTodos.filter((todo: Todo) => todo.id !== deletId);
    });
  };

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