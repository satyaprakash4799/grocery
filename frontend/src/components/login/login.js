import React, { Component, Fragment } from "react";
import { Button, Form,  FormGroup, Input, Label } from 'reactstrap';
import { connect } from 'react-redux'

import apiCall from "../../api/axios";

import './login.css'
import { userAuthenticate } from "../../features/user/user";

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

  componentDidUpdate(prevProps) {
    if (prevProps.token !== this.props.token){
      console.log(this.props.token)
    }
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
    const { username, password, errors } = this.props;
    const { validateLoginButton,  authenticateUser} = this;
    return (
        <div className="login">
          <Form className="form" inline>
              <h2 className="title">Login</h2>
              <FormGroup floating>
                <Input id="username" name="username" type="text" placeholder="Username" required bsSize="sm" className="mb-3" 
                  onChange={(e)=> this.handleChange('username', e.target.value)} value={username}
                  ></Input>
                <Label for="username">Username</Label>
              </FormGroup>
              <FormGroup floating>
                <Input id="password" type="password" name="password" placeholder="Password" required bsSize="sm" className="mb-3" 
                  onChange={(e)=> this.handleChange('password', e.target.value)} value={password}
                  ></Input>
                <Label for="username">Password</Label>
              </FormGroup>
              <FormGroup>
                <Button type="submit" color="warning" className="me-3" disabled={validateLoginButton()} onClick={(e)=> authenticateUser(e)}>Login</Button>
                <Button outline color="warning">Signup</Button>
              </FormGroup>
          </Form>
        </div>
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
