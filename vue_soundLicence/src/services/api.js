import axios from 'axios'

// const API_URL = 'https://license-management-01.herokuapp.com/api/v1';
const API_URL = 'http://localhost:8000/api/v1';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

export default {
	getAll(__app) {
	    const url = `${API_URL}/${__app}/`;
	    return axios.get(url).then(response => response.data);
	},

	get(__app, __id) {
	    const url = `${API_URL}/${__app}/${__id}`;
	    return axios.get(url).then(response => response.data);
	},

	create(__app, __data){
	    const url = `${API_URL}/${__app}/`;
	    return axios.post(url, __data);
	},

	update(__app, __data){
	    const url = `${API_URL}/${__app}/${__data.id}/`;
	    return axios.put(url, __data);
	},

	delete(__app, __data){
	    const url = `${API_URL}/${__app}/${__data.id}/`;
	    return axios.delete(url);
	}
}

