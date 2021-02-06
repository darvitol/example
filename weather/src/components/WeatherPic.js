import React from "react";

function temperature (t) {
    if (t > 20) {
      return <img src="https://cdn.pixabay.com/photo/2016/12/11/12/02/bled-1899264_960_720.jpg" />;
    } else if (t < 0){
      return <img src="https://images.unsplash.com/photo-1460919920543-d8c45f4bd621?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80" />;
    } else if (t == undefined) {
      return
    }
    else {
      return <img src="https://images.unsplash.com/photo-1484345115483-5b738dafdd7e?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"/>
    }
}


class WeatherPic extends React.Component {
  render() {
    return (
      <div>
        {temperature(this.props.temp)}
      </div>
    )
  }
}
export default WeatherPic;
