import React, { useContext, useState}  from "react";

import TodoItem from "./TodoItem";
import Todo from "../models/todo";

import { TodoContext } from "../store/todos.content";
import classes from "./Todo.module.css";

const Todos: React.FC = () => {
  const todosCtx = useContext(TodoContext)
  return (
    <ul className={classes.todos}>
      {todosCtx.items.map((item) => (
        <TodoItem
          text={item.text}
          key={item.id}
          id={item.id}
          deleteTodo={todosCtx.removeTodo}
        />
      ))}
    </ul>
  );
};

export default Todos;
