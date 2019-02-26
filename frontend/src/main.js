import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import theme from './theme'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
VueCookies.config('7d')
Vue.use(Vuetify, { theme })
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
