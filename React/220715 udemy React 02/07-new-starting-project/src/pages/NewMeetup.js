import { useNavigate } from 'react-router-dom'

import NewMeetupForm from "../components/meetups/NewMeetupForm";

function NewMeetupPage() {
  const navigate = useNavigate()

  function addMeettupHandler(meetupData) {
    fetch("https://udemy-prac-default-rtdb.firebaseio.com/meeetups.json", {
      method: "POST",
      body: JSON.stringify(meetupData),
      headers: {
        "Content-Type": "application/json",
      },
    }).then(() => {
      navigate('/', {replace : true})
    })
  }
  return (
    <section>
      <h1>Add New Meetup</h1>
      <NewMeetupForm onAddMeetup={addMeettupHandler} />
    </section>
  );
}

export default NewMeetupPage;
