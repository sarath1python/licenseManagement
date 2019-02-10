import api from '@/services/api'


const APP_NAME = 'license';

export default {
	getLicences() {
	    return api.getAll(`${APP_NAME}`).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	getLicence(__id) {
	    return api.get(`${APP_NAME}`).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	createLicence(__data){
		if (__data.violations) {
			delete __data.violations;
		}
	    return api.create(`${APP_NAME}`, __data).catch(error => {
	    	if (error.response) {
	    		console.log(error.response);
	    	} else {
	    		console.log('some error');
	    		console.log(error);
	    	}
	    });;
	},

	updateLicence(__data){
		if (__data.violations) {
			delete __data.violations;
		}
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
		if (__data.violations) {
			delete __data.violations;
		}
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