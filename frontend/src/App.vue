<template>
    <div>
        <app-header></app-header>
        <app-dashboard></app-dashboard>
        <app-footer></app-footer>
    </div>
</template>

<script>
// Imports
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Dashboard from './components/Dashboard.vue';

export default {
  components: {
    'app-header': Header,
    'app-footer': Footer,
    'app-dashboard': Dashboard
  },
  data() {
    return {};
  }
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Nunito SemiBold';
}
</style>
