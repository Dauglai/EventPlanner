// import React from "react";
// import Navbar from "./components/Navbar";
// import {
//     BrowserRouter as Router,
//     Routes,
//     Route,
// } from "react-router-dom";
// import CreateEvent from "./pages/create-event/create-event";
// import CreateProfile from "./pages/create-profile/create-profile";
// import Event from "./pages/event/event";
// import Kanban from "./pages/kanban/kanban";
// import Main1 from "./pages/main_1/main1";
// import Profile from "./pages/profile/profile";
// import Registration from "./pages/registration";
// import Login from "./pages/login";
// import StartPage from "./pages/start-page/start-page";

// function App() {
//     return (
//         <Router>
//             <Navbar />
//             <Routes>
//                 <Route exect path="/" element={<CreateEvent />} />
//                 <Route exect path="/pages/create-profile/create-profile" element={<CreateProfile />} />
//                 <Route path="/pages/event/event" element={<Event />} />
//                 <Route path="/pages/kanban/kanban" element={<Kanban />} />
//                 <Route path="/pages/main_1/main1" element={<Main1 />} />
//                 <Route path="/pages/profile/profile" element={<Profile />} />
//                 <Route path="/pages/start-page/start-page" element={<StartPage />} />
//             </Routes>
//         </Router>
//     );
// }
 
// export default App;
import React, { useState } from "react";
import './App.css';
import { Login } from "./pages/login/login";
import { Registration } from "./pages/registration/registration";

    function App() {
        const [currentForm, setCurrentForm] = useState('login')

        const toggleForm = (formName) => {
            setCurrentForm(formName);
        }

        return(
            <div className="App">
                {
                    currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Registration onFormSwitch={toggleForm}/>
                }
            </div>
        )
    }

export default App;