import { Link } from "react-router-dom";
import { useContext } from "react";
import classes from "./MainNavigation.module.css";
import FavoritesContext from "../../store/favorites-context";

function MainNavigation() {
  const favoritesCtx = useContext(FavoritesContext)

  return (
    <header className={classes.header}>
      <div className={classes.logo}>React Meetups</div>
      <nav>
        <ul>
          <li>
            <Link to="/">All meet up</Link>
          </li>
          <li>
            <Link to="/new-meetup">Add new meetups</Link>
          </li>
          <li>
            <Link to="/favorites">
              my favorites
              <span classes={classes.badge}>{favoritesCtx.totlaFavorites}</span>
              </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
