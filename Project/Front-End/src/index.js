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
	"12.10.2018",
	"13.10.2018"
]
const _12_10_18 = {
	cells: [
		-1,1,2,3,4,
		 5,0,0,0,0,
		 6,0,0,0,0,
		 7,0,0,0,0,
		 8,0,0,0,-1
	]
}

// Render
const react_root = document.getElementById("root");
function renderReactDOM(section_state) {
	ReactDOM.render(
	<React.Fragment>
		<Header />
		<Section type={section_state} />
		<Terminal
			hideTopBar = {true}
			allowTabs = {false}
			startState = {'maximised'}
			style={{ fontWeight: "bold", fontSize: "1em", height: "250px" }}
			commands={{
				"get-today": (args, print, runCommand) => {
					print("Getting today's puzzle...");
					renderReactDOM("today");
					print("Today's puzzle fetched successfully!");
				},
				"get-old": (args, print, runCommand) => {
					print("Old puzzle list:");
					print(`${old_puzzles}`);
				},
			}}
			descriptions={{
				show: "Shows the greeting message",
				clear: "Clears the screen",
				help: "Lists all the commands and shows their explanations",
				"get-today": "This command gets the today's puzzle",
				"get-old": "This command gets the old puzzles"
			}}
			msg='Welcome to Project Dolphin. To get help type: help'
		/>
	</React.Fragment> ,react_root);
}
renderReactDOM("idle");