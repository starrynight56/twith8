/*
FILE NAME: twitter.js
WRITTEN BY: Rosanne Hu, Nick Alvarez, Sam Yang, and Sarah Jee
DATE: January 2015
PURPOSE: Javascript for HackRice Project
*/

//FUNCTION1
//function to toggle background screen colors

var colors = [
    "#00ACED",
    '#F04DDA',
    '#77DD77',
    '#FE4A49',
    '#0084b4'];

var currentColor = 0;

function colorTog(){
    var color = colors[ currentColor ];
    $('body').css("background-color", color)
    $('body').fadeto();
    //$('body').animate( { backgroundColor: hue }, 1000);
}
// function whiteBlue(){
//     if (currentColor == 2){
//         $('img').attr("src", 'blue.png');
//     }else{
//         $('img').attr("src", 'twit.png');
//     }
// }
function nextColor(){
    currentColor++;
    if( currentColor >=colors.length){
        currentColor = 0;
    }
    // whiteBlue();
    colorTog();
}

setInterval(nextColor, 1500);

colorTog;

//FUNCTION 2
//TAKES DATA OF RECENT TWEETS FROM TWITTER

$('button').click($.ajax({
   url: "/cats",
   success: function(response){
     //here you do whatever you want with the response variable
     var output = response;
     $('#t1').attr(output);
   }
}));
//FUNCTION 3

//INPUT FUNCTION, TAKES DATA FROM TWITTER AND PROVIDES DATA??

function inputWhat(){
    var stuff = $('#tb10').val();

    document.querySelector('#time').innerHTML = meal + dat;
}

function showDiv() {
    document.getElementById('t1').style.display = "block";
    document.getElementById('t2').style.display = "block";
    document.getElementById('t3').style.display = "block";
}
