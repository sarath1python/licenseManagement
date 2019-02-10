import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard/Dashboard.vue'
import Login from './views/Login/Login.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/licence',
      name: 'licence',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Licence/Licence.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})
