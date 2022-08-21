import axios from 'axios';

const instance = axios.create({
    baseURL:"http://127.0.0.1:8000/",
    timeout: 5000,
    headers:{
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ localStorage.getItem("accessToken")
    }
})



const apiCall = (url="", method="GET", data ={})  => {
    return instance({
        url: url,
        method: method,
        data: data
    }).then((response) => {
        return response;
    })
    .catch(function(err) {
        return err.response;
    })
}
const updateApiToken = (type='access', token) => {
    if (type === 'access') {
        instance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        localStorage.setItem('accessToken', token);
    }
    else if (type === 'refresh'){
        localStorage.setItem('refreshToken', token);
    }
}

export default apiCall;
export {updateApiToken};