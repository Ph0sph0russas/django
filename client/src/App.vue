<script setup>
import axios from "axios"
import {ref} from 'vue'
const students = ref([])

async function onLoadClick(){
  const r = await axios.get("/api/students/");
  console.log(r.data);
  students.value = r.data
}

</script>


<template>
  <div>
    <div v-for="item in students">
      {{ item }}
    </div>
    <button @click="onLoadClick">Loading...</button>
  </div>
</template>

<style scoped></style>
