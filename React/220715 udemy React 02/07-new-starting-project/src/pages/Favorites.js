import { useContext } from "react"

import FavoritesContext from "../store/favorites-context"
import MeetupList from "../components/meetups/MeetupList"

function FavoritePage() {
  const favoriteCtx = useContext(FavoritesContext)

  let content

  if (favoriteCtx.totalFavorites === 0){
    content = <p>You got no favorites yetm Start adding Some?</p>
  } else {
    console.log(favoriteCtx.totalFavorites)
    console.log(favoriteCtx.favorites)
    content =  <MeetupList meetups = {favoriteCtx.favorites}/>
  }
  return (
    <section>
      <h1>My Favorite</h1>
      {content}
    </section>
  )
}

export default FavoritePage