<template>
    <div class="footer">
      <p>{{ copyright }}</p>
    </div>
</template>
<script>
export default {
  data() {
    return {
      copyright: 'SmartRoom 2018'
    };
  }
};
</script>
<style scoped>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(0, 184, 15, 0.74);
    color: white;
    text-align: center;
    font-size: 13px;
    border-radius: 4px;
}
.footer p {
    margin: 10px 0;
}
</style>
