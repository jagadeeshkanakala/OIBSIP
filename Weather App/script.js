function getElement(element){
    return document.querySelector(element) || console.log(element + ' cannot be found')

}

// defining date
let d = new Date();
const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

let year = d.getFullYear();
let month = months[d.getMonth()]
let day = d.getDate()
getElement('.date').innerHTML = day + " "+month + " "+year;
getElement(".day").innerHTML = days[d.getDay()]

let allArticle = document.querySelectorAll('.forecast article');

let apiKey = 'ec02baefd862ae0ce76df07d3a712a38'
let submitBtn = getElement('.submit__btn');
let cityName


const url = (cityName)=>{
    if(!cityName){
        return `//api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`
    }else{
        return `//api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&appid=${apiKey}`
    }
}

getWeather();

function getWeather(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition((position) => {
            lat = position.coords.latitude.toFixed(2);
            lon = position.coords.longitude.toFixed(2);
            // url()
            fetchWeather();
        }, (error)=>{
            if(error.code) {
                try {
                    if(error.PERMISSION_DENIED) throw "User denied the request for Geolocation.";
                    if(error.POSITION_UNAVAILABLE) throw "Location information is unavailable.";
                    if(error.TIMEOUT) throw "The request to get user location timed out.";
                    if(error.UNKNOWN_ERROR) throw "An unknown error occurred.";
                    
                } catch (error) {
                    getElement('.error').innerHTML = error;
                    showError()
                }
            } 
    
        })
    

    } else{
        getElement('.error').innerHTML = "Geolocation is not supported on your browser"
    }
};








// all function
async function fetchWeather(){
    await fetch(url(cityName))
    .then( response=>{
    // console.log(response.status)
        return response.json()
    })
    .then(data =>{

        return effectChanges(data)

    })
    .catch(err=>{
        getElement('.error').innerHTML = err.status;
        console.log(err)
        showError()
    });


}
let effectChanges = (data)=>{

    // for temperature
    getElement('.temp span').innerHTML = Math.round(data.main.temp);
    // for humidty
    getElement('.hum span').innerHTML = data.main.humidity + "%";
    // kilometer per hr for wind
    const mtPsc = data.wind.speed;
    let kmPhr = mtPsc * 3.6;
    getElement('.wind span').innerHTML = Math.round(kmPhr) + " km/h";
    // for locatin
    getElement('.location span').innerHTML = data.name + ", "+ data.sys.country;
    // for forecast days
    // setting weather image 
    let imageID = data.weather[0].icon;
    let imgUrl = `http://openweathermap.org/img/wn/${imageID}@4x.png`
    getElement('#report__img').src = imgUrl;
    // weather condition 'rainy or sunny etc.'
    getElement('.weather').innerHTML = data.weather[0].main

    // document.querySelectorAll('#day').forEach((wkday,ind)=>{
    //     let d = new Date()
    //     // code not correct yet
    //     wkday.innerHTML = days[d.getDay() + (days.length) + ind].slice(0,3);
    // });

    getElement('#name').value = '' ;
    getElement('#input__form').style.display = 'none'

    
}
allArticle.forEach((art, ind) => {
    art.addEventListener('click', ()=>{
        for (let i = 0; i < allArticle.length; i++) {
            const element = allArticle[i];
                element.classList.remove('active')
        }
        art.classList.add('active')
        
    })
    
});

getElement('.submit__btn').addEventListener('click', (e)=>{

    e.preventDefault()

    if(getElement('#name').value == ''){
        getElement('.error').innerHTML = 'City name cannot be empty'
        showError()
        
    }else{
        cityName = getElement('#name').value;
        // console.log(cityName, url(cityName));
        fetchWeather(cityName)
    


    

    }
});

// function to display and clear error after 7 minutes

const showError = () =>{
    getElement('.error').style.display = 'block';
    setTimeout(()=>{
        getElement('.error').style.display = 'none';
    }, 7000)


}






// making input be visible upon locaton change

getElement('.change__btn').addEventListener('click', ()=>{
    getElement('#input__form').style.display = 'inline-block'
});

// making Forecast section visible on arrow click
getElement('.more').addEventListener('click', ()=>{
    getElement('.more').style.display = 'none'
    getElement('.report__info').classList.add('show')
});




