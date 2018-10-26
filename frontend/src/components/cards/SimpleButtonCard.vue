<template>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <button class="button" :disabled="!values.value">
        <font-awesome-icon icon="lightbulb"/>
        <!-- endpoint.icons.icon -->
      </button>
      <h5 class="card-title">{{ endpoint.title }}</h5>
    </div>
    <div class="device-color" v-bind:style="{ 'background-color': deviceColor}"></div>
  </div>
</template>

<script>
import BaseCard from './BaseCard.vue';
export default {
  extends: BaseCard
};
</script>

<style scoped>
.button {
  width: 100px;
  height: 100px;
  padding: 15px 25px;
  font-size: 24px;
  text-align: center;
  cursor: pointer;
  outline: none;
  color: #fff;
  background-color: #4ecdc4;
  border: none;
  border-radius: 50%;
  box-shadow: 1px 3px #999;
}

.button:hover {
  background-color: #4fcfcf;
}

.button:active {
  background-color: #5eddd4;
  box-shadow: 1px 3px #666;
  transform: translateY(4px);
}

.card {
  text-align: center;
  height: 100px;
  color: #646464;
}

.card-title {
  margin-bottom: 20px;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
}

.device-color {
  background-color: rgba(0, 184, 15, 0.74);
  width: 100%;
  height: 10px;
}
</style>
