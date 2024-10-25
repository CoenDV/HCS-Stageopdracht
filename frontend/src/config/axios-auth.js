import axios from 'axios'
const instance = axios.create({
    baseURL: 'https://backend-v1-coen-de-vries-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/'
});
export default instance;