<script setup>
import { onBeforeMount } from 'vue';

import NavBar from '../components/NavBar.vue';


</script>

<template>
  <nav-bar />
  <div class="container">
    <router-view />
  </div>
</template>

<style scoped></style>
