import React from "react"
import IngredientsList from "./IngredientsList"
import Instrucntions from "./Instructions"

function Recipe({name, ingredients, steps}) {
  return (
    <section id = {name.toLowerCase().replace(/ /g, "-")}>
      <h1>{name}</h1>
      <IngredientsList list={ingredients}/>
      <Instrucntions title ="조리절차" steps={steps}/>
    </section>
  )
}

export default Recipe