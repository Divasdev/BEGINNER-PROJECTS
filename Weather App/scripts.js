//Selecting the DOM elements
const searchBox = document.querySelector('.search-box input');
const searchBtn = document.querySelector('.search-box button');
const weatherIcon = document.getElementById('weather-icon');

const temp = document.querySelector('.temp');
const weatherDesc = document.querySelector('.type');
const cityName = document.querySelector('.city');
const humidity = document.querySelector('.humidity');
const windSpeed = document.querySelector('.wind');

const pressureUnit=document.querySelector('.press');
const apiKey="b4211a78c0cc6323e0287901ff614c4c";
const apiUrl="https://api.openweathermap.org/data/2.5/weather?units=metric&q=";



async function checkWeather(city){
   const response = await fetch(apiUrl + city + `&appid=${apiKey}`);
   if (!response.ok) {
      alert("Invalid city Name");
      return;
   }

   const data = await response.json();
   cityName.innerHTML = data.name;
   temp.innerHTML = Math.round(data.main.temp) + "°C";
   humidity.innerHTML = data.main.humidity + "%";
   windSpeed.innerHTML = data.wind.speed + "km/h";
   weatherDesc.innerHTML=data.weather[0].description;
   pressureUnit.innerHTML=data.main.pressure +  "mm/hg";
   // Use the 'main' field from the weather array and compare lowercase strings
   const weatherMain = data.weather[0].main.toLowerCase();

   if (weatherMain === "clouds"){
      weatherIcon.src = "./images/cloudy.png";
   }
   else if (weatherMain === "clear"){
      weatherIcon.src = "./images/sun.png";
   }
   else if (weatherMain === "rain" || weatherMain === "drizzle"){
      weatherIcon.src = "./images/heavy-rain.png";
   }
   else if (weatherMain === "snow"){
      weatherIcon.src = "./images/snow.png";
   }
   else if (weatherMain === "mist"){
      weatherIcon.src = "./images/humidity-icon.png";
   }
   else if (weatherMain== "haze"){
      weatherIcon.src="./images/haze.png";
   }
   else {
      // fallback icon if none of the above match
      weatherIcon.src = "./images/default.png";
   }

   console.log(data);
}



searchBtn.addEventListener('click', (event) => {
   const city = searchBox.value.trim();
   if (city) checkWeather(city);
});

searchBox.addEventListener('keydown',(event)=>{
   if(event.key==='Enter'){
      checkWeather(searchBox.value);
   }
});


checkWeather("New York");