import React from "react";

const Weather  = props => (
  <div>
  { props.city &&
    <div>
      <p>Город: {props.city} </p>
      <p>Страна: {props.country} </p>
      <p>Температура: {props.temp} &deg;C</p>
      <p>Давление: {props.pressure} </p>
      <p>Закат солнца: {props.sunset} </p>
    </div>
  }
    <p>{props.error}</p>
  </div>
)
export default Weather;
