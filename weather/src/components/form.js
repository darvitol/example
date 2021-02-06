import React from "react";
import $ from "jquery";

class Form extends React.Component {
  render() {

    return (
      <form onSubmit={this.props.weatherMethod}>
        <input type="text" name="city" placeholder="Город"/><br/><br/>
        <button class="btn btn-outline-success">Унать погоду</button>
      </form>
    )
  }
}

export default Form;
