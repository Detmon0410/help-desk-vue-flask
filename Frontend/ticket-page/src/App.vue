<template>
  <div id="app" class="container">
    <!-- Home Component inside a Bootstrap container -->
    <Home />
  </div>
</template>

<script>
import Home from './views/TicketHome.vue';

export default {
  name: 'App',
  components: {
    Home
  }
};
</script>

<style scoped>
/* Global styles */
#app {
  padding-top: 20px;
}


</style>
