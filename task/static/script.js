document.getElementById("user").onclick = function(){
    var user = prompt("Type An Affirmation for the Day");
    document.getElementById("outputUser").innerText = user;
}