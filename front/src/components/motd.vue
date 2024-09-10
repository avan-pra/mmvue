<template>
    <div class="module">
        <span v-text="msg"></span>
        <input v-if="edit" type="text" v-model="msg"/>
    </div>
</template>

<script lang="ts">
import { ref } from 'vue';

export default {
    props: ['edit'],
    data() {
        return {
            msg: msg
        }
    },
}

const msg = ref('salut')

</script>

<style scoped>

span {
    font-size: xx-large;
}

</style>
