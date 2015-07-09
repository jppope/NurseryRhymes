
/* Baa, baa, black sheep,
 Have you any wool?
 Yes, sir, yes, sir,
 Three bags full;
 One for my master,
 And one for my dame,
 and one for the little boy
 Who lives down the lane.
 */
var woolOwners = [{
	"master": 1
}, {
	"dame": 1
}, {
	"little_boy": 1,
	"littleBoyLocation": "down the lane"
}];

var haveYouAnyWool = function() {
	for (var i = 0; i < woolOwners.length; i++) {
		//console.log(i);
		totalBags = i;
	}
	totalBags += i;
	return (i);
}
var bags = haveYouAnyWool();


function baabaaBlackSheep() {
	console.log("BaaBaa BlackSheep have you any wool?");
	if (bags > 0) {
		console.log("yes sir, yes sir " + bags + " bags full");
	} else {
		console.debug("error");
	}
}
baabaaBlackSheep();

function oneForMy() {
	for (var i = 0; i < 2; i++) {
		people = Object.keys(woolOwners[i]);
		var person = people.toString();
		console.log("one for my " + person);
	}
}
oneForMy();

var woolOwner = woolOwners[2];
var boy = Object.keys(woolOwner);
var littleBoy = boy[0];

var whereHeLives = woolOwners[2].littleBoyLocation;
console.log("one for the " + littleBoy + " that lives " + whereHeLives);