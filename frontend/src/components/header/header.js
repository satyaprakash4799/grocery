import React, { Component } from 'react';
import { connect } from 'react-redux';

import './header.css';

class Header extends Component {
    constructor(props){
        super(props);
        this.state = {};
    }

    render() {
        return (
            <div className="header">
                <h3>Grocery</h3>
            </div>
        )
    }
}


const mapStateToProps = (state) => {
    return {

    }
}


const mapDispatchToProps = (dispatch) => {
    return {

    }
}

export default connect(null, null)(Header);


