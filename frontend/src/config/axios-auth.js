import axios from 'axios'
const instance = axios.create({
    baseURL: 'http://backend-v1/'
});
export default instance;