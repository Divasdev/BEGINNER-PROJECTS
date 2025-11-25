//Selecting the DOM elements

const searchBox=document.querySelector('.search-box input').value;
const searchBtn=document.querySelector('.search-box button')
const weatherIcon=document.getElementById('weather-icon');

const temp=document.querySelector('.temp');

const weatherDesc=document.querySelector('.type')

const cityName=document.querySelector('.city');

const humidity=document.querySelector('.humidity');

const windSpeed=document.querySelector('.wind');


const apiKey="b4211a78c0cc6323e0287901ff614c4c";
const apiUrl="https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

async function checkWeather(city){

   const response =await fetch(apiUrl +city +`&appid=${apiKey}`);
   if (response.status==404){
      alert("Invalid city Name");
   }
   var data = await response.json();
   console.log(data.main);
   console.log(data.weather);
   console.log(data.wind);

}

  const events =searchBtn.addEventListener('click', ((event)=>{
      const searchBox = document.querySelector('.search-box input').value;
      
      checkWeather(searchBox);
 }));
 
