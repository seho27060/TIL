import React, { useEffect, useState } from "react";

import Card from "../UI/Card";
import "./Search.css";

const Search = React.memo((props) => {
  const { onLoadIngredients } = props;
  const [inputWord, setInputWord] = useState("");

  useEffect(() => {
    const query =
      inputWord.length === 0 ? "" : `?orderBy="title"&equalTo"="${inputWord}"`;
    fetch(
      "https://react-hooks-update-d7cdc-default-rtdb.firebaseio.com/ingredients.json" +
        query
    )
      .then((response) => response.json())
      .then((responseData) => {
        const loadedIngredients = [];
        for (const key in responseData) {
          loadedIngredients.push({
            id: key,
            title: responseData[key].title,
            amount: responseData[key].amount,
          });
        }
        // onLoadIngredients(loadedIngredients);
      });
  }, [inputWord, onLoadIngredients]);

  return (
    <section className="search">
      <Card>
        <div className="search-input">
          <label>Filter by Title</label>
          <input type="text" value={inputWord} onChange={setInputWord} />
        </div>
      </Card>
    </section>
  );
});

export default Search;
