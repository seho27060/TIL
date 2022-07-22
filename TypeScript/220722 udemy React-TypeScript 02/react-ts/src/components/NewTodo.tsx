import React from "react"

import { useRef, useContext } from "react"

import { TodoContext } from "../store/todos.content"
import classes from './NewTodo.module.css'

const NewTodo: React.FC = () => {
  const todosCtx = useContext(TodoContext)
  
  const todoTextInputRef = useRef<HTMLInputElement>(null)

  const submitHandler =(event:React.FormEvent) => {
    event.preventDefault()

    const enteredText = todoTextInputRef.current!.value // ts에서의 연산자 current? 은 value가 null일수도있음을, current!는 value는 절대 null이 아님을 확신할때 사용
    
    if (enteredText.trim().length ===0){
      return
    }
    todosCtx.addTodo(enteredText)
  }

  
  return (
    <form onSubmit={submitHandler} className={classes.form}>
      <label htmlFor="text">Todo text</label>
      <input type = 'text' id='text' ref={todoTextInputRef}></input>
      <button>Add Todo</button>
    </form>
  )
}

export default NewTodo