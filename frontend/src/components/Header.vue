<template>
    <div class="header">
      <a href="#default" class="logo">{{ title }}</a>
      <div class="header-right">
        <a class="active" href="#">{{ dashboard }}</a>
        <a href="#">{{ settings }}</a>
        <a href="#">{{ logout }}</a>
      </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      title: 'SmartRoom',
      dashboard: 'Dashboard',
      logout: 'Log Out',
      settings: 'Settings'
    };
  }
};
</script>
<style scoped>
.header {
  position: fixed;
  z-index: 10;
  width: 100%;
  overflow: hidden;
  background-color: #f1f1f1;
  padding: 20px 10px;
}

.header a {
  float: left;
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px; 
  line-height: 25px;
  border-radius: 4px;
}

.header a.logo {
  font-size: 25px;
  font-weight: bold;
}

.header a:hover {
  background-color: #ddd;
  color: black;
}

.header a.active {
  background-color: rgba(0, 184, 15, 0.74);
  color: white;
}

.header-right {
  float: right;
}

@media screen and (max-width: 500px) {
  .header a {
    float: none;
    display: block;
    text-align: left;
  }
  .header-right {
    float: none;
  }
}
</style>
