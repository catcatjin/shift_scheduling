<template>
  <AppNavbar />
  <ScheduleCalendar/>
  
  
</template>

<script>
import AppNavbar from './components/AppNavbar.vue';
import ScheduleCalendar from './components/ScheduleCalendar.vue';
export default {
  name: 'App',
  components: {
    AppNavbar,
    ScheduleCalendar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
