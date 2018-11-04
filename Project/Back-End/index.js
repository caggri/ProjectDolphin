const express = require("express");
const app = express();

const PORT = 5000;

// Static answers
app.use('/answers', express.static('answers'));

// Write headers
app.use(function(req, res, next) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
	next();
 });

// Handle old puzzles
app.get("/old/:day/:month/:year", (req,res) => {
	let path = `${__dirname}/json/${req.params.day}_${req.params.month}_${req.params.year}.json`;
	res.sendFile(path, function(err) {
		if (err) {
			 res.status(err.status).end();
		}
  });
});
app.listen(PORT, console.log(`Listening port no: ${PORT}`));