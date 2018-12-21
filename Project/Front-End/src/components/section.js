import React from "react";

const PYTHON_IP = "139.179.55.24";
const PYTHON_PORT = 5000;

class Section extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			idle: undefined,
			table: undefined,
			clues: undefined,
			solution: undefined
		}
	}
	closeSolution = () => {
		let solution =
		<button onClick={this.showSolution} className="w3-button w3-green w3-hover-blue">
			Show Solution
		</button>;
		this.setState({solution: solution});
	}
	showSolution = () => {
		let solution = [];
		solution.push(
		<button onClick={this.closeSolution} className="w3-button w3-red w3-hover-blue">
			Close Solution
		</button>
		);
		
		const [, day, month, year] = this.props.type;
		let img_url = `http://${PYTHON_IP}:${PYTHON_PORT}/static/answers/${day}_${month}_${year}.jpeg`;
		solution.push(
			<img id="solution_img" src={img_url} alt="Solution screen shot"></img>
		);
		
		this.setState({solution: solution});
	}
	drawTable = (response) => {
		// Clear idle
		this.setState({idle: undefined});

		// Declare date
		const day = response.day;
		const date = response.date;

		// Render table begins!
		let table = [];
		let temp = []; // is a table cells
		let cells = 0;

		let i, k;
		for(k = 0; k < 5; k++) {
			for(i = 0; i < 5; i++) {
				if(response.cells[cells] === "-1") {
					temp.push(<td className="black">&nbsp;</td>);
				}
				else if(response.cells[cells] === "0") {
					temp.push(<td>&nbsp;</td>);
				}
				else {
					temp.push(<td className="w3-display-container">
									<a className="w3-display-topleft">{response.cells[cells]}</a>
								</td>);
				}
				cells++;
			}
			table.push(<tr>{temp}</tr>);
			temp = [];
		}
		// add date above table
		let table_with_date = 
		<div>
			<h1 id="show-date">{day}, {date}</h1>
			<table id="main-table">{table}</table>
		</div>;

		this.setState({table: table_with_date});

		// Render clues begins!
		let clues = [];
		let across = [];
		let down = [];
		// across
		i = 0;
		while(i < response.across.length) {
			across.push(<p><strong>{response.across[i].no}.</strong> {response.across[i].text}</p>);
			i++;
		}
		// down
		i = 0;
		while(i < response.down.length) {
			down.push(<p><strong>{response.down[i].no}.</strong> {response.down[i].text}</p>);
			i++;
		}
		clues.push(<div id="across"><h1>ACROSS</h1>{across}</div>);
		clues.push(<div id="down"><h1>DOWN</h1>{down}</div>);
		this.setState({clues: clues});

		// Render solution begins!
		let solution =
		<button onClick={this.showSolution} id="showSol" className="w3-button w3-green w3-hover-blue">
			Show Solution
		</button>;
		this.setState({solution: solution});
	}
	fetchData = (day, month, year) => {
		let url = null;
		if(this.props.type === "today") {
			url = `http://${PYTHON_IP}:${PYTHON_PORT}/static/data/today.json`;
		}
		else {
			url = `http://${PYTHON_IP}:${PYTHON_PORT}/static/data/${day}_${month}_${year}.json`;
		}
		fetch(url)
			.then(response => response.json())
			.then(responseJSON => {
				this.drawTable(responseJSON);
			})
			.catch(error => {
				console.log("We couldn't find the puzzle you typed.");
				console.log("To see available old puzzles simply tpye:");
				console.log("$ print-old");
			});
	}
	// If we have console command
	componentDidUpdate = (prevProps) => {
		// Get today's data
		if(this.props.type === "today" && prevProps.type !== "today") {
			this.fetchData("17", "12", "2018");
		}
		// Get old data
		else {
			const [, prevDay, prevMonth, prevYear] = prevProps.type;
			const [, day, month, year] = this.props.type;
			if (day === undefined || month === undefined || year === undefined) {
				console.log("Please use get-old command properly!");
				console.log("Usage:\nget-old day month year");
				console.log("Example:\nget-old 28 10 2018");
			}
			else if (prevDay !== day || prevMonth !== month || prevYear !== year) {
				this.fetchData(day, month, year);
			}
		}
	}
	// Show boxes if idle
	systemIDLE = () => {
		let idle =
		<div id="display-idle">
			<div className="section-box w3-card-4 margin-right-for-box">
				<h1>Front-End</h1>
				<h4>Ready!</h4>
			</div>
			<div className="section-box w3-card-4 margin-right-for-box">
				<h1>Back-End</h1>
				<h4>Ready!</h4>
			</div>
			<div className="section-box w3-card-4 margin-right-for-box">
				<h1>Puzzles</h1>
				<h4>There are 10 old puzzles available!</h4>
			</div>
			<div className="section-box w3-card-4">
				<h1>Team</h1>
				<h4>We have 5 contributors!</h4>
			</div>
		</div>;
		this.setState({idle: idle});
	}
	// First function to be executed
	componentDidMount = () => {
		this.systemIDLE();
	}
	render() {
		return(
			<section id="main-section">
				{this.state.idle}
				<div className="clear"></div>

				<div id="display-table">
					{this.state.table}
				</div>

				<div id="display-clues">
					{this.state.clues}
				</div>

				<div id="display-solution">
					{this.state.solution}
				</div>

				<div className="clear"></div>
			</section>
		);
	}
}
export default Section;