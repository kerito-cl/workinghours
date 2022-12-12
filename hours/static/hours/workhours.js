var minutesLabel = document.getElementById("minutes");
var secondsLabel = document.getElementById("seconds");
var hoursLabel = document.getElementById("hour");
var totalSeconds = 0;
let myInterval;
let mySecondInterval
var functionIsRunning = false
document.getElementById("call").addEventListener("click",startTime)

document.getElementById("halt").addEventListener("click",stopTime)
document.getElementById("pau").addEventListener("click",pauseTime)



function startTime(){

   
    myInterval = setInterval(setTime, 1000)
    
  
}

function stopTime(){
  
  secondsLabel.innerHTML = "00"
  minutesLabel.innerHTML = "00"
  totalSeconds.innerHTML = 0
  clearInterval(myInterval)

  totalSeconds = 0

}

function pauseTime(){
  
  clearInterval(myInterval)


}






function setTime() {
  
  ++totalSeconds;
  secondsLabel.innerHTML = pad(totalSeconds % 60);
  minutesLabel.innerHTML = pad(parseInt(totalSeconds / 60));
  hoursLabel.innerHTML = pad(parseInt(totalSeconds / 3600)); 
}

function pad(val) {

  var valString = val + "";
  if (valString.length < 2) {

    return "0" + valString;

  }
  else {

    return valString;
  }
}


