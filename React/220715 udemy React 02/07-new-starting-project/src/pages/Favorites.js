import { useContext } from "react"

import FavoritesContext from "../store/favorites-context"
import MeetupList from "../components/meetups/MeetupList"

function FavoritePage() {
  const favoriteCtx = useContext(FavoritesContext)

  let content

  if (favoriteCtx.totlaFavorites === 0){
    content =  <MeetupList meetups = {favoriteCtx.favotires}/>

  }
  return (
    <section>
      <h1>My Favorite</h1>
      {content}
    </section>
  )
}

export default FavoritePage