import React, { Component } from 'react';
import {connect } from 'react-redux';

import './App.css';
import Login from './components/login/login';
import Header from './components/header/header';
import  { getToken }  from './features/user/user';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {

    }
  }

  componentDidMount(){
      this.props.getToken();
  }
  render(){
    const { token : {accessToken, refreshToken}} = this.props;
    return (
      <div className="App">
        {/* <Header></Header> */}
        <Login ></Login>
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    token: state.rootReducer.user.token,
  }
}
const mapDispatchToProps = (dispatch) => {
  return {
    getToken: ()=> dispatch(getToken())
  }
}
export default connect(mapStateToProps, mapDispatchToProps)(App);
