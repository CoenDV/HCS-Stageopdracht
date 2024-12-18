import axios from 'axios'
const instance = axios.create({
    baseURL: 'https://hcs-backend-coen-de-vries-dev.apps.lab-01.hcs-lab.nl/',
});
export default instance;