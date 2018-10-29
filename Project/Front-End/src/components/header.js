import React from "react";
import logo from "../public/img/logo.png";

class Header extends React.Component {
	render() {
		return(
			<header id="main-header" className="w3-display-container">
				<a href="/">
					<img id="main-header-logo" className="w3-display-middle" src={logo}></img>
				</a>
			</header>
		);
	}
}
export default Header;