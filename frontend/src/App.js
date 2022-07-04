
import React, { Component } from "react";
import axios from 'axios';
import "./App.css";

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      jobs: []
    };
  }

  componentDidMount() {
    this.getJobs();
  }

  getJobs = () => {
    axios 
      .get("http://localhost:8000/api/jobs/")
      .then(res => this.setState({ jobs: res.data }))
      .catch(err => console.log(err));
  };

  render() {
    return (
      <div>
        <h2> Personal Job Board </h2>
      </div>
    )
  }

};

export default App;
