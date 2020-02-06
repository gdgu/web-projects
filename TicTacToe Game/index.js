// function clk(r){
//     r.textContent = "X";
//   };
// function dbclk(r){
//     r.textContent = "O";
//   };
// // Method 1
// var r1 = document.querySelector("#ra");
// r1.addEventListener("click",function(){
//   r1.textContent = "X";
// });
// r1.addEventListener("dblclick",function(){
//   r1.textContent = "O";
// });
// // Method 2
// var r2 = document.querySelector("#rb")
// r2.addEventListener("click",clk.bind(null,r2))
// r2.addEventListener("dblclick",dbclk.bind(null,r2))
//
// var r3 = document.querySelector("#rc")
// r3.addEventListener("click",clk.bind(null,r3))
// r3.addEventListener("dblclick",dbclk.bind(null,r3))
//
// var r4 = document.querySelector("#rd")
// r4.addEventListener("click",clk.bind(null,r4))
// r4.addEventListener("dblclick",dbclk.bind(null,r4))
//
// var r5 = document.querySelector("#re")
// r5.addEventListener("click",clk.bind(null,r5))
// r5.addEventListener("dblclick",dbclk.bind(null,r5))
//
// var r6 = document.querySelector("#rf")
// r6.addEventListener("click",clk.bind(null,r6))
// r6.addEventListener("dblclick",dbclk.bind(null,r6))
//
// var r7 = document.querySelector("#rg")
// r7.addEventListener("click",clk.bind(null,r7))
// r7.addEventListener("dblclick",dbclk.bind(null,r7))
//
// var r8 = document.querySelector("#rh")
// r8.addEventListener("click",clk.bind(null,r8))
// r8.addEventListener("dblclick",dbclk.bind(null,r8))
//
// var r9 = document.querySelector("#ri")
// r9.addEventListener("click",clk.bind(null,r9))
// r9.addEventListener("dblclick",dbclk.bind(null,r9))
var squares = document.querySelectorAll("td")
for(var i=0;i<squares.length;i++)
{
  squares[i].textContent = "";
}
// Restart
function clear() {
  for(var i=0;i<squares.length;i++)
  {
    squares[i].textContent ="";
  }
}
var bt = document.querySelector("#btn")
bt.addEventListener("click",clear.bind(null))

// METHOD 3
// check marker using this(object-element)
function marker() {
  if(this.textContent==="" || this.textContent===" "){
    this.textContent="X"}
  else if (this.textContent==="X"){
    this.textContent="O"}
  else{
    this.textContent=" "}
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click",marker)
  }
// Random Color Generator
var hd = document.querySelector("#hd");
function randomColor(tag) {
  var hex = "0123456789ABCDEF";
  var st = "#";
  for(var x=0;x<6;x++)
  {
    st+=hex[Math.floor(Math.random(hex)*16)];
  }
  tag.style.color=st;
}
setInterval("randomColor(hd)",500);
