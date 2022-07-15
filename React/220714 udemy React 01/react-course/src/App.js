import Todo from "./components/Todo";
import Modal from "./components/Modal";
import Backdrop from "./components/Backdrop";
function App() {
  return <div>
    <h1>My Todos</h1>
    <Todo text="learning React"/>
    <Todo text="Review React"/>
    <Todo text="make Todo"/>
  </div>;
}

export default App;
