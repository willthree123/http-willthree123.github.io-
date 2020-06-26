///////////IndexVideoHegihtArrage////////
function displayWindowSize(){
        // Get width and height of the window excluding scrollbars
        var w = document.documentElement.clientWidth;
        var h = document.documentElement.clientHeight;
        
        // Display result inside a div element
  document.getElementById("IndexVideoid").height = window.innerHeight-(window.innerHeight*0.2);
    document.getElementById("IndexVideoid1").height = window.innerHeight-(window.innerHeight*0.2);
    document.getElementById("IndexPlaceHolder").height = window.innerHeight*0.1;
    }
     
    // Attaching the event listener function to window's resize event
    window.addEventListener("resize", displayWindowSize);
    
    // Calling the function for the first time
    displayWindowSize();


///////////////////GetScrollVal////////////////