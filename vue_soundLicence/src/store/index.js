import Vue from 'vue'
import Vuex from 'vuex'
import Role from './role.module.js'
import userDetails from './user.module'
import sampleUserData from './sampleUserData.module.js'

Vue.use(Vuex)

export default new Vuex.Store({
 modules:{
   Role,
   userDetails,
   sampleUserData
 } 
})
