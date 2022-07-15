import { Routes, Switch } from "react-router-dom"

import AllMeetupsPage from "./pages/AllMeetups";
import NewMeetupPage from "./pages/NewMeetup";
import FavoritePage from "./pages/Favorites";

function App() {
  return <div>
    <Switch>
      <Routes path="/" exact>
        <AllMeetupsPage/>
      </Routes>
      <Routes path="/new-meetup">
        <NewMeetupPage/>
      </Routes>
      <Routes path="/favorites">
        <FavoritePage/>
      </Routes>
    </Switch>
  </div>;
}

export default App;
