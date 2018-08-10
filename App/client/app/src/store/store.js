import Vuex from 'vuex'
import Vue from 'vue'
import * as types from '@/store/types'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		token: null,
		statu: false
	},
	mutations: {
		[types.TESTING]: (state, data) => {
			localStorage.token = data
			state.token = data
			state.statu = true
		},
		[types.OUT]: (state) => {
			localStorage.removeItem('token')
			state.token = null
			state.statu = false
		}
	}
})