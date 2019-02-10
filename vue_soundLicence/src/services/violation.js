import api from '@/services/api'


const APP_NAME = 'violation';

export default {
	getViolations() {
	    return api.getAll(`${APP_NAME}`).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	getViolation(__id) {
	    return api.get(`${APP_NAME}`).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	createViolation(__data){
	    return api.create(`${APP_NAME}`, __data).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	updateViolation(__data){
	    return api.update(`${APP_NAME}`, __data).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	deleteLicence(__data){
		__data['is_deleted'] = true;
	    return api.update(`${APP_NAME}`, __data).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });
	}
}