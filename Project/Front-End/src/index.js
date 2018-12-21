// NodeJS components
import React from "react";
import ReactDOM from "react-dom";
import Terminal from 'terminal-in-react';

// Custom components
import Header from "./components/header.js";
import Section from "./components/section.js";

// CSS
import "./public/css/custom.css";

// Globals
const PYTHON_IP = "139.179.55.24";
const PYTHON_PORT = 5000;
const old_puzzles = [
	"08 11 2018\n",
	"05 11 2018\n",
	"01 11 2018\n",
	"31 10 2018\n",
	"30 10 2018\n",
	"29 10 2018\n",
	"28 10 2018\n",
	"01 06 2016\n",
	"02 10 2015\n",
	"23 10 2014\n"
];
function render_answers(args) {
	const [, day, month, year] = args;

	let url_cells = `http://${PYTHON_IP}:${PYTHON_PORT}/static/data/${day}_${month}_${year}.json`;
	let url_answers = `http://${PYTHON_IP}:${PYTHON_PORT}/static/${day}_${month}_${year}answer.json`;

	fetch(url_cells)
	.then(response => response.json())
	.then(response_cells => {
		fetch(url_answers)
		.then(response => response.json())
		.then(response_answers => {
			for(let i = 0; i < 25; i += 5) {
				let cell = i/5;
				cell = "A_"+String(cell);
				let single_answer = response_answers[cell];
	
				console.log(single_answer);
				for(let j = 0; j < 5; j++) {
					if(single_answer.length !== 0) {
						if(response_cells.cells[i+j] !== "-1") {
							const table = document.getElementById("main-table").getElementsByTagName("td")[i+j];
							table.innerHTML = "<span>"+single_answer[j]+"</span>";
						}
					}
				}
			}
		})
	})
}
function connect_server(args) {
	let connect_back_end = `http://${PYTHON_IP}:${PYTHON_PORT}/static/state.json`
	fetch(connect_back_end)
	.then(response => response.json())
	.then(responseJSON => {
		if(responseJSON.state[0] === "DONE!") {
			console.log("Puzzle solved! Trying to render answers...");
			clearInterval(window.timer);
			//let answers = get_answers(args);
			render_answers(args);
		}
		else {
			console.log(responseJSON.state[0]);
		}
	})
	.catch(error => {
		console.log("Trying to connect back-end server....");
	});
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
			allowTabs = {true}
			startState = {'maximised'}
			style={{ fontWeight: "bold", fontSize: "1em", height: "375px"}}
			commands={{
				"print-old": (args, print, runCommand) => {
					print("Old puzzle list:");
					print(old_puzzles);
				},
				"get-today": (args, print, runCommand) => {
					print("Trying to connect NYTimes...");
					print("Getting clues...");
					setTimeout(function(){ renderReactDOM("today");; }, 6000);
				},
				"get-old": (args, print, runCommand) => {
					print("Getting old puzzle....");
					print("Loading....");
					renderReactDOM(args);
				},
				"solve": (args, print, runCommand) => {
					const [, day, month, year] = args;
					// Send request to solve
					var http = new XMLHttpRequest();
					var url = `http://${PYTHON_IP}:${PYTHON_PORT}/solve/${day}/${month}/${year}`;
					http.open("GET", url, true);
					http.setRequestHeader("Content-Type", "application/json");
					http.send();

					window.timer = setInterval(function(){
						connect_server(args);
					}, 195);
				},
				"clear": (args, print, runCommand) => {
					window.location.reload(true);
				}
			}}
			descriptions={{
				show: "Shows the greeting message",
				clear: "Clears the screen",
				help: "Lists all the commands and shows their explanations",
				"get-today": "This command gets the today's puzzle",
				"print-old": "This command gets the list of old puzzles",
				"get-old": "This command gets a specific old puzzle",
				"solve-it": "Solves the displayed puzzle"
			}}
			msg='Welcome to Project Dolphin. To get help type: help'
		/>
	</React.Fragment> ,react_root);
}
renderReactDOM("idle");