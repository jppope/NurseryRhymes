/* St. Ives Rhyme 
 "As I was going to St. Ives
 I met a man with seven wives,
 Each wife had seven sacks,
 each sack had seven cats,
 Each cat had seven kits:
 kits, cats, sacks and wives,
 How many were going to St. Ives?"
 */

function Ives(people){
 var man = 1;
 var wives = 7;
 var sacks = 7;
 var cats = 7;
 var kittens = 7;
 var personsMet = man * wives * sacks * cats * kittens;
 console.log(personsMet + " total people in that guy's posse");
 if ( personsMet + people > 1){
  console.log("I was the only one going to St. Ives");
 }
 else{
  console.log("you watched 'Die Hard with a Vengance' didn't you?");
 }
}

Ives(1);