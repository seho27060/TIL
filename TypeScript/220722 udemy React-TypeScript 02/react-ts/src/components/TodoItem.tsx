import React from "react";

import classes from "./TodoItem.module.css";
const TodoItem: React.FC<{
  id: string;
  text: string;
  deleteTodo: (id: string) => void;
}> = (prop) => {
  const deleteHandler = () => {
    prop.deleteTodo(prop.id);
  };

  return (
    <li className={classes.item} onClick={deleteHandler}>
      {prop.text}
    </li>
  );
};

export default TodoItem;
