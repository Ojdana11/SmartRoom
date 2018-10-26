<template>
  <div class="dashboard">
    <div class="card-wrapper">
      <div v-for="(endpoint, index) in endpoints" :key="index">
        <component :is="endpoint['card-type']" :device_name="endpoint.device_name" :endpoint_name="endpoint.endpoint_name"></component>
      </div>
    </div>
  </div>
</template>
<script>
import UninplementedCard from './cards/UninplementedCard.vue';
import SimpleButtonCard from './cards/SimpleButtonCard.vue';

export default {
  components: {
    'crouton-simple-button': SimpleButtonCard,
    'crouton-simple-toggle': UninplementedCard,
    'crouton-simple-text': UninplementedCard
  },

  computed: {
    // a computed getter
    cards: function() {
      // `this` points to the vm instance
      return this.$store.state.cards;
    },

    endpoints: function() {
      let endpoints = [];
      let devices = this.$store.state.devices;
      for (let device_name of Object.keys(devices)) {
        let device = devices[device_name];
        for (let endpoint_name of Object.keys(device.endPoints)) {
          endpoints = [
            ...endpoints,
            {
              device_name: device_name,
              endpoint_name: endpoint_name,
              'card-type': device.endPoints[endpoint_name]['card-type']
            }
          ];
        }
      }
      return endpoints;
    }
  }
};
</script>
<style scoped>
.card {
  margin: 20px;
  /* background-clip: content-box; */
  background-color: #fafafa;
  /* margin-bottom: 20px; */
  font-size: 16px;
  word-wrap: break-word;
  /* display: inline-block; */
  height: 200px;
  /* width: 100%; */
}

.card-wrapper {
  padding-top: 5em;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  /* grid-auto-columns: 200px; */
  /* grid-auto-flow: row dense;
  justify-items: start; */
  /* grid-template-rows: minmax(50px, 1fr); */
}

.dashboard {
  background-color: #e5e5e5;
}
</style>
