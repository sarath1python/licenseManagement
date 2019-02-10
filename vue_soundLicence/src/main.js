import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store/index'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
  beforeMount(){
    if(this.$store.state.userDetails.is_loggedIn == true)
    {
      Promise.all([
        store.dispatch('switchUser', this.$store.state.sampleUserData.name),
      ]).then(() => {
      });
    }
    else
    {
      Promise.all([
        store.dispatch('switchUser', this.$store.state.userDetails.defaultUser),
      ]).then(() => {
      });
    }  
  }
}).$mount('#app')
