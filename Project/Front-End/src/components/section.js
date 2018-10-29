import React from "react";

class Section extends React.Component {
	constructor(props) {
		super(props);
	}
	getDate = (props) => {
		if(props.type == "idle" || props.type == "today") {
			let options = { year: 'numeric', month: 'long', day: 'numeric' };
			return new Date().toLocaleDateString([],options);
		}
		// else is props.type == "old"
		else {
			// Fetch old date
		}
	}
	drawTable = (props) => {
		let table = [];
		let children = [];

		// empty table
		if(props.type == "idle") {
			for(let i = 0; i < 5; i++) {
				children.length = 0;
				for(let j = 0; j < 5; j++) {
					children.push(<td></td>);
				}
				table.push(<tr>{children}</tr>);
			}
			return table
		}
		// fetch today's puzzle
		else if(props.type == "today") {

		}
		// get old puzzles
		else {
			
		}
	}
	render() {
		return(
			<section id="main-section">

				<div id="main-section-table">
					<h2>{this.getDate(this.props)}</h2>
					<h4><strong>1A</strong> No clue</h4>
					<table>{this.drawTable(this.props)}</table>
				</div>

				<div id="main-section-clues">
					<div id="clues-across">
						<h5><strong>ACROSS</strong></h5>
						<ul>
							<li>1. No clue</li>
						</ul>
					</div>

					<div id="clues-down">
						<h5><strong>DOWN</strong></h5>
						<ul>
							<li>1. No clue</li>
						</ul>
					</div>

				</div>
				<div className="clear"></div>
			</section>
		);
	}
}
export default Section;