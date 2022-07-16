import { Route, Routes } from "react-router-dom";

import AllMeetupsPage from "./pages/AllMeetups";
import NewMeetupPage from "./pages/NewMeetup";
import FavoritePage from "./pages/Favorites";
import Layout from "./components/layout/Layout";

function App() {
  return (
    <div>
      <Layout>
        <Routes>
          <Route path="/" element={<AllMeetupsPage />}></Route>
          <Route path="/new-meetup" exact element={<NewMeetupPage />}></Route>
          <Route path="/favorites" element={<FavoritePage />}></Route>
        </Routes>
      </Layout>
    </div>
  );
}

export default App;
