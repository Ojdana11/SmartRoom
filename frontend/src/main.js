import Vue from 'vue'
import App from './App.vue'
import store from './store'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// font awesome stuff
import {
  library
} from '@fortawesome/fontawesome-svg-core'
import {
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'
import {
  fas
} from '@fortawesome/free-solid-svg-icons'
library.add(fas)
Vue.component('font-awesome-icon', FontAwesomeIcon)

// websocket stuff
import VueNativeSock from 'vue-native-websocket'
Vue.use(VueNativeSock, 'ws://192.168.1.5:8080/ws/dashboard', {
  format: 'json'
})

var vm = new Vue({
  el: '#app',
  store,
  render: h => h(App)
})
vm.$options.sockets.onmessage = data => {
  let content = JSON.parse(data.data);
  if (content.type == 'devices') {
    vm.$store.commit('devices', {
      devices: content['devices']
    });
  }
};