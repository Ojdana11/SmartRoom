<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h3>Uninplemented</h3>
      <h5 class="card-title">Dev: {{ device_name }}</h5>
      <h5 class="card-text">End: {{ endpoint_name }}</h5>
      <h5 class="card-text">Type: {{ this.$store.state.devices[this.device_name].endPoints[this.endpoint_name]['card-type'] }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    device: function() {
      return this.$store.state.devices[this.device_name];
    },
    endpoint: function() {
      return this.device.endPoints[this.endpoint_name];
    },
    deviceColor: function() {
      return this.device.color;
    },
    values: function() {
      return this.endpoint.values;
    }
  },
  props: ['device_name', 'endpoint_name']
};
</script>

<style scoped>
.card {
  height: 100px;
}
</style>
