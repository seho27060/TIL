import React, { useEffect, useCallback, useReducer, useMemo } from "react";

import IngredientForm from "./IngredientForm";
import IngredientList from "./IngredientList";
import ErrorModal from "../UI/ErrorModal";
import Search from "./Search";

import useHttp from "../../hooks/http";

const ingredientReducer = (currentIngredients, action) => {
  switch (action.type) {
    case "SET":
      return action.ingredients;
    case "ADD":
      return [...currentIngredients, action.ingredient];
    case "DELETE":
      return currentIngredients.filter((ing) => ing.id !== action.id);
    default:
      throw new Error("Should not get there");
  }
};

const Ingredients = () => {
  const [userIngredients, dispatch] = useReducer(ingredientReducer, []);

  const { isLoading, error, data, sendRequest, reqExtra, reqIdentifier } =
    useHttp();

  useEffect(() => {
    if (!isLoading && reqIdentifier === "REMOVE_INGREDIENT") {
      dispatch({ type: "DELETE", id: reqExtra });
    } else if (!isLoading && !error && reqIdentifier === "ADD_INGREDIENT") {
      dispatch({
        type: "ADD",
        body: { id: data.name, ...reqExtra },
      });
    }
  }, [data, reqExtra, reqIdentifier, isLoading, error]);

  const filteredIngredientsHandler = useCallback((filteredIngredients) => {
    // setUserIngredients(filteredIngredients);
    dispatch({ type: "SET", ingredients: filteredIngredients });
  }, []);

  const addIngredientHandler = useCallback((ingredient) => {
    sendRequest(
      "https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients.json",
      "POST",
      JSON.stringify(ingredient),
      ingredient,
      "ADD_INGREDIENT"
    );
    // setIsLoading(true);
    //   dispatchHttp({ type: "SEND" });
    //   fetch(
    //     "https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients.json",
    //     {
    //       method: "POST",
    //       body: JSON.stringify(ingredient),
    //       headers: { "Content-Type": "application/json" },
    //     }
    //   )
    //     .then((response) => {
    //       // setIsLoading(false);
    //       dispatchHttp({ type: "RESPONSE" });
    //       return response.json();
    //     })
    //     .then((responseData) => {
    //       // setUserIngredients((prevIngredients) => [
    //       //   ...prevIngredients,
    //       //   { id: responseData.name, ...ingredient },
    //       // ]);
    //       dispatch({
    //         type: "ADD",
    //         ingredient: { id: responseData.name, ...ingredient },
    //       });
    //     })
    //     .catch((error) => {
    //       dispatchHttp({ type: "ERROR", errorMessage: error.message });
    //     });
  }, []);

  const removeIngredientHandler = useCallback(
    (ingredientId) => {
      // setIsLoading(false);
      sendRequest(
        `https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients.json/${ingredientId}.json`,
        "DELETE",
        null,
        ingredientId,
        "REMOVE_INGREDIENT"
      );
    },
    [sendRequest] 
  );

  const clearError = useCallback(() => {
    // setError(null);
    // dispatchHttp({ type: "CLEAR" });
  }, []);

  const ingredientList = useMemo(() => {
    return (
      <IngredientList
        ingredients={userIngredients}
        onRemoveItem={removeIngredientHandler}
      />
    );
  }, [userIngredients, removeIngredientHandler]);

  return (
    <div className="App">
      {error && <ErrorModal onClose={clearError}>{error}</ErrorModal>}
      <IngredientForm
        onAddIngredient={addIngredientHandler}
        loading={isLoading}
      />

      <section>
        <Search onLoadIngredients={filteredIngredientsHandler} />
        {ingredientList}
      </section>
    </div>
  );
};

export default Ingredients;
