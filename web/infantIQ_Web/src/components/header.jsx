import { useState } from "react";

function Header(props){
    const [user, setUser] = useState("")

    function updateUser(event){
        setUser("richy")
    }


    return(
        <div>
            <h2>InfantIQ Data</h2>
            {/* {(user)?<h3>Hello {user}</h3>:null}
            <button onClick={updateUser}>Click to set user</button> */}
        </div>
    );
}

export default Header