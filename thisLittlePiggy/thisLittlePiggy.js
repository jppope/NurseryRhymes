
/* 
 This little piggy went to market.
 This little piggy stayed home.
 This little piggy had roast beef.
 This little piggy had none.
 This little piggy cried, "Wee, wee, wee, wee."
 All the way home.
 */

// Math.random version
var whatPiggyDid = ["went to market", "stayed home", "had roast beer", "had none", "cried 'wee wee wee wee'... All the way home"];
function thisLittlePiggy(){
 var whichPiggy = Math.floor(Math.random() * 5);
 console.log(whatPiggyDid[whichPiggy])
}
thisLittlePiggy();



// for loop version
function this_little_piggy(){
 for(var i = 0; i < whatPiggyDid.length; i++){
  console.log("This little piggy " + whatPiggyDid[i]);
 }
}
this_little_piggy();

