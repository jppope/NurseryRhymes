/* One two buckle my shoe

 One two buckle my shoe
 Three, four, knock at the door
 Five, six, pick up sticks
 Seven, eight, lay them straight
 Nine, ten, a big fat hen
 Eleven, twelve, dig and delve
 Thirteen, fourteen, maids a-courting
 Fifteen, sixteen, maids in the kitchen
 Seventeen, eighteen, maids in waiting
 Nineteen, twenty, my plate's empty
 */

var activities = ["buckle my shoe", "knock at the door", "pick up sticks","lay them straight","a big fat hen", "dig and delve","maids a-courting"," maids in the kitchen","maids in waiting","my plate's empty"];
var counter = 0;
for(var i = 1; i < 21; i++){
 if(i % 2 == 0){
  console.log(i);
  console.log(activities[counter]);
  counter += 1;
 }
 else{
  console.log(i);
 }
}
