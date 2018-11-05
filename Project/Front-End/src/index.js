// NodeJS components
import React from "react";
import ReactDOM from "react-dom";
import Terminal from 'terminal-in-react';

// Custom components
import Header from "./components/header.js";
import Section from "./components/section.js";

// CSS
import "./public/css/w3.css";
import "./public/css/custom.css";

// Globals
const old_puzzles = [
	"28 10 2018\n",
	"29 10 2018\n",
	"30 10 2018\n",
	"31 10 2018\n",
	"01 11 2018\n"
];
// Render
const react_root = document.getElementById("root");
function renderReactDOM(section_state) {
	ReactDOM.render(
	<React.Fragment>
		<Header />
		<Section type={section_state} />
		<Terminal
			hideTopBar = {true}
			allowTabs = {true}
			startState = {'maximised'}
			style={{ fontWeight: "bold", fontSize: "1em", height: "350px"}}
			commands={{
				"get-today": (args, print, runCommand) => {
					console.log("Getting today's puzzle!");
					console.log("Trying to connect NYTIMES...");
					setTimeout(function(){
						renderReactDOM("today");
						console.log("Today's puzzle fetched successfully!");
				  	}, 3000);
				},
				"print-old": (args, print, runCommand) => {
					print("Old puzzle list:");
					print(old_puzzles);
					print("You can run an old puzzle by typing:");
					print("get-old 28 10 2018");
				},
				"get-old": (args, print, runCommand) => {
					renderReactDOM(args);
				}
			}}
			descriptions={{
				show: "Shows the greeting message",
				clear: "Clears the screen",
				help: "Lists all the commands and shows their explanations",
				"get-today": "This command gets the today's puzzle",
				"print-old": "This command gets the list of old puzzles",
				"get-old": "This command gets a specific old puzzle"
			}}
			msg='Welcome to Project Dolphin. To get help type: help'
		/>
	</React.Fragment> ,react_root);
}
renderReactDOM("idle");