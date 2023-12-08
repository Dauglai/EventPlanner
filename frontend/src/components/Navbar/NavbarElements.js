import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
 
const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/create-event" activeStyle>
                        New Event
                    </NavLink>
                    <NavLink to="/event" activeStyle>
                        My event
                    </NavLink>
                    <NavLink to="/profile" activeStyle>
                        Profile
                    </NavLink>
                    <NavLink to="/maim_1" activeStyle>
                        Home
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};
 
export default Navbar;