import React, { Component, Fragment } from "react";
import { Button, Form,  FormGroup, Input, Label } from 'reactstrap';
import { connect } from 'react-redux'

import apiCall from "../../api/axios";

import './login.css'
import { userAuthenticate } from "../../features/user/user";
import Header from "../header/header";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      errors: {}
    };
    this.validateLoginButton = this.validateLoginButton.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.authenticateUser  = this.authenticateUser.bind(this);

  }

  validateLoginButton = () => {
    const { username, password } = this.state;
    if (username && password) {
      return false;
    }
    return true;
  }

  handleChange = (type, value) => {
    if (type === 'username') {
      this.setState({ username: value });
    }
    else if (type === 'password') {
      this.setState({ password: value });
    }
  }

  authenticateUser = (event) => {
    event.preventDefault();
    this.props.userAuthenticate({username: this.state.username, password: this.state.password});
  }
  render() {
    const { username, password, errors } = this.state;
    const { validateLoginButton,  authenticateUser} = this;
    return (
      <>
        <Header></Header>
        <div className="login">
          <Form className="form" inline>
              <h2 className="title">Login</h2>
              <FormGroup floating>
                <Input id="username" name="username" type="text" placeholder="Username" required bsSize="sm" className="mb-3" 
                  onChange={(e)=> this.handleChange('username', e.target.value)} value={username}
                  ></Input>
                <Label for="username" className="primary-dark">Username</Label>
              </FormGroup>
              <FormGroup floating>
                <Input id="password" type="password" name="password" placeholder="Password" required bsSize="sm" className="mb-3" 
                  onChange={(e)=> this.handleChange('password', e.target.value)} value={password}
                  ></Input>
                <Label for="password" className="primary-dark">Password</Label>
              </FormGroup>
              <FormGroup>
                <Button type="submit" className="button-dark me-3" disabled={validateLoginButton()} onClick={(e)=> authenticateUser(e)}>Login</Button>
                <Button outline className="button-light button">Signup</Button>
              </FormGroup>
          </Form>
        </div>
      </>
    );
  }
}

const mapStateToProps = (state) =>{
  return {
    user: state.rootReducer.user.user,
    token: state.rootReducer.user.token
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    userAuthenticate : (data) => dispatch(userAuthenticate(data))
  }
}

export default connect(mapStateToProps, mapDispatchToProps )(Login);
