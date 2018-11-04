import React from "react";

const NODE_PORT = 5000;

class Section extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			section_header: undefined,
			data: undefined,
			clues: undefined
		}
	}
	systemIDLE = () => {
		let idle =
		<div>
			<div className="section_box w3-card-4 margin_right_for_box">
				<h1>Front-End</h1>
				<h4>Ready!</h4>
			</div>
			<div className="section_box w3-card-4 margin_right_for_box">
				<h1>Back-End</h1>
				<h4>Ready!</h4>
			</div>
			<div className="section_box w3-card-4 margin_right_for_box">
				<h1>Puzzles</h1>
				<h4>There are 5 old puzzles available!</h4>
			</div>
			<div className="section_box w3-card-4">
				<h1>Team</h1>
				<h4>We have 5 contributors!</h4>
			</div>
		</div>;
		this.setState({section_header: undefined});
		this.setState({data: idle});
		this.setState({clues: undefined});
	}
	drawTable = (response) => {
		// Render date
		const [, day, month, year] = this.props.type;
		let section_header = [];
		section_header.push(
			<div id="main-day">
				<strong>{response.day}</strong>
				<span> {response.date}</span>
				<br></br>
				<a id="answers" href='#' onClick={()=> window.open(`http://localhost:${NODE_PORT}/answers/${day}_${month}_${year}.jpeg`, "_blank")}>
					Show the solution
				</a>
			</div>
		);
		this.setState({section_header: section_header});
		// Render table
		let table = [];
		let children = [];
		let cells = 0;
		for(let k = 0; k < 5; k++) {
			for(let i = 0; i < 5; i++) {
				if(response.cells[cells] === "-1") {
					children.push(
						<td className="black">&nbsp;</td>
					);
				}
				else if(response.cells[cells] === "0") {
					children.push(
						<td>&nbsp;</td>
					);
				}
				else {
					children.push(
						<td className="w3-display-container"><a className="w3-display-topleft">{response.cells[cells]}</a></td>
					);
				}
				cells++;
			}
			table.push(<tr>{children}</tr>);
			children = [];
		}
		this.setState({data: <table id="main-table">{table}</table>});
		// Render Clues
		let clues = [];
		let across = [];
		let down = [];
		let i = 0;
		while(i < response.across.length) {
			across.push(<p><strong>{response.across[i].no}.</strong> {response.across[i].text}</p>);
			i++;
		}
		i = 0;
		while(i < response.down.length) {
			down.push(<p><strong>{response.down[i].no}.</strong> {response.down[i].text}</p>);
			i++;
		}
		clues.push(<div id="across"><h1>ACROSS</h1>{across}</div>);
		clues.push(<div id="down"><h1>DOWN</h1>{down}</div>);
		this.setState({clues: clues});
	}

	fetchData = (day,month,year) => {
		const url = `http://localhost:${NODE_PORT}/old/${day}/${month}/${year}`;
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

	componentDidUpdate = (prevProps) => {
		// Get today's data
		if(this.props.type === "today" && prevProps.type !== "today") {
			this.fetchData("05","11","2018");
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
				this.fetchData(day,month,year);
			}
		}
	}

	componentDidMount = () => {
		this.systemIDLE();
	}

	render() {
		return(
			<section id="main-section">
				{this.state.section_header}
				{this.state.data}
				{this.state.clues}
				<div className="clear"></div>
			</section>
		);
	}
}
export default Section;