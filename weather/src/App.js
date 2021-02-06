import React from "react";
import Info from "./components/info"
import Form from "./components/form"
import Weather from "./components/weather"
import WeatherPic from "./components/WeatherPic"

const API_KEY = "2ab4720225cbadcc3af5dd2dd692cefd";

class App extends React.Component {

  state = {
    temp: undefined,
    city:undefined,
    county:undefined,
    pressure: undefined,
    sunset: undefined,
    error: undefined
  }

  gettingWeather = async (e) => {
    e.preventDefault();
    const city = e.target.elements.city.value;
    const api_url = await fetch(`http://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`);
    const data = await api_url.json();
    console.log(data);
    if(city) {
      try {
        var celcium_temp = data.main.temp ;
        var sunset = data.sys.sunset;
        var date = new Date();
        date.setTime(sunset);
        var sunset_date = date.getHours()+":"+date.getMinutes()+":"+date.getSeconds();
        this.setState({
          temp: celcium_temp,
          city:data.name,
          county:data.sys.country,
          pressure: data.main.pressure,
          sunset: sunset_date,
          error: undefined
        });
      } catch (error) {
        this.setState({
          temp: undefined,
          city:undefined,
          county:undefined,
          sunrise: undefined,
          sunset: undefined,
          error: "Не могу показать погоду для этого города"
        });
      }
    } else {
      this.setState({
        temp: undefined,
        city:undefined,
        county:undefined,
        sunrise: undefined,
        sunset: undefined,
        error: "Введите название города"
      });
    }
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-12 col-lg-4">
            <Info />
          </div>
          <div className="col-4 col-lg-4">
            <Form weatherMethod={this.gettingWeather} />
          </div>
          <div className="col-4 col-lg-4">
            <Weather

            temp={this.state.temp}
            city={this.state.city}
            country={this.state.county}
            pressure={this.state.pressure}
            sunset={this.state.sunset}
            error={this.state.error}
            />
          </div>
          <div className="col-4 col-lg-4 text-center">
            <WeatherPic temp={this.state.temp}/>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
