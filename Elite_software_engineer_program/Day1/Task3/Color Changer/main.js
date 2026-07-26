function changeColor(){
     // Generate random hex color
      const color = "#" + Math.floor(Math.random() * 16777215).toString(16);
      document.body.style.backgroundColor = color;
}