import axios from 'axios'
import store from '@/store/store'
import * as types from '@/store/types'
import router from '@/router/index'

axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://localhost:5000'



axios.interceptors.request.use(
	config => {
		if (store.state.token){
			config.headers.Authorization = `token ${store.state.token}`;
		}
		return config
	},
	err => {
		return Promise.reject(err)
	}
);

axios.interceptors.response.use(
	response => {
		return response
	},
	error => {
		if(error.response){
			switch(error.response.status){
				case 401:
					store.commit(types.OUT);
					router.replace({
						path: '/'
					})
			}
		}
		return Promise.reject(error)
	}
);

export default axios
