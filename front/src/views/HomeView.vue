<template>
  <main>
    <button style="opacity: 0; left: 0; top: 0; position: fixed;" @click="edit = !edit" >{{ edit }}</button>
    <div class="region fullscreen below"><div class="container"></div></div>
    <div class="region top bar">
      <div class="container"></div>
      <div class="region top left"><div class="container">
        <Date />
        <Calendar :edit="edit"/>
      </div></div>
      <div class="region top center"><div class="container"></div></div>
      <div class="region top right"><div class="container"></div></div>
    </div>
    <div class="region upper third"><div class="container"></div></div>
    <div class="region middle center"><div class="container">
      <Motd :edit="edit"/>
    </div></div>
    <div class="region lower third">
      <div class="container"><br /></div>
    </div>
    <div class="region bottom bar">
      <div class="container"></div>
      <div class="region bottom left"><div class="container"></div></div>
      <div class="region bottom center"><div class="container"></div></div>
      <div class="region bottom right"><div class="container"></div></div>
    </div>
    <div class="region fullscreen above"><div class="container"></div></div>
  </main>
</template>

<script setup lang="ts">
import Calendar from '@/components/calendar.vue';
import Date from '@/components/date.vue';
import Motd from '@/components/motd.vue';
import { ref } from 'vue';

const edit = ref(false)

</script>
