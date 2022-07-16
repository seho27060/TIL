import { Route, Routes } from "react-router-dom"

import AllMeetupsPage from "./pages/AllMeetups";
import NewMeetupPage from "./pages/NewMeetup";
import FavoritePage from "./pages/Favorites";
import MainNavigation from "./components/layout/MainNavigation";

function App() {
  return <div>
    <MainNavigation></MainNavigation>
    <Routes>
      <Route path="/" element = {<AllMeetupsPage/>}>
      </Route>
      <Route path="/new-meetup" exact element = {<NewMeetupPage/>}>
      </Route>
      <Route path="/favorites" element = {<FavoritePage/>}>
      </Route>
    </Routes>
  </div>;
}

export default App;
