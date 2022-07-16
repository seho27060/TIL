import { Link } from "react-router-dom"

import classes from './MainNavigation.module.css'

function MainNavigation() {
  return (
    <header className = {classes.header}>
      <div className= {classes.logo}>React Meetups</div>
      <nav>
        <ul>
          <li>
            <Link to="/">All meet up</Link>
          </li>
          <li>
            <Link to="/new-meetup">Add new meetups</Link>
          </li>
          <li>
            <Link to="/favorites">my favorites</Link>
          </li>
        </ul>
      </nav>
    </header>
  )
}

export default MainNavigation