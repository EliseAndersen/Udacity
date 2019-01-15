//create grid
function makeGrid() {

	//define grid height/width and pixelcanvas table
	var canvas = document.querySelector("#pixelCanvas");
	var height = document.querySelector("#inputHeight").value;
	var width = document.querySelector("#inputWidth").value;

	//remove all children from canvas so if makeGrid 
	//gets called again it cleans the canvas
	while (canvas.firstChild) {
    	canvas.removeChild(canvas.firstChild);
  	}
	
	//Loop for height and add tr to canvas
	for (let x = 0; x < height; x++) {
		var row = document.createElement("<tr></tr>");
    	canvas.appendChild(row);

    	for (let z = 0; z < width; z++) {
    		let cell = document.createElement('td')
      		row.appendChild(cell)
    	}
  	}

}


//Assign the form submit to a variable and put an eventlistener on click that runs makeGrid
// var submit = document.querySelector("#inputSubmit");
document.getElementById('sizePicker').addEventListener('submit', function(e){
	e.preventDefault();
	makeGrid();
})


//Change the color of the cells when clicked
function newColor() {
	this.style.background = colorPicker.value;
}