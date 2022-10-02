import { Routes, Route } from 'react-router-dom';


import App from '../App';
import { Login } from '../components';

const routes = () => {
    return (
        <Routes>
            <Route path="/" element={<App />}></Route>
            <Route path="/login" element={<Login />}></Route>
        </Routes>
    )
}

export default routes;