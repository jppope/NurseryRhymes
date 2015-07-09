
/* Which came first => example of recursion */

function chicken() {
 return egg();
}
function egg() {
 return chicken();
}
console.log(chicken() + " came first.");
// just a joke don't run this
