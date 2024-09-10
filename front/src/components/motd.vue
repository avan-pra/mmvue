<template>
    <div class="module">
        <span v-text="msg"></span>
        <form v-if="edit" @submit.prevent="postMotd">
            <textarea @focus="$event.target.select()" type="text" v-model="msg"/>
            <button type="submit">submit</button>
        </form>
    </div>
</template>

<script lang="ts">
import axios from 'axios';
import { ref } from 'vue';

export default {
    props: ['edit'],
    data() {
        return {
            msg: msg
        }
    },
    mounted() {
        this.getMotd()
        setInterval(this.getMotd, 1000 * 60 * 5)
    },
    methods: {
        async getMotd() {
            let res = await axios.get('/api/motd')
            msg.value = res.data['data']
        },
        async postMotd() {
            let res = await axios.post('/api/motd', { 'motd': this.msg })
            this.getMotd()
        }
    }
}

const msg = ref('salut')

</script>

<style scoped>

span {
    color: whitesmoke;
    font-size: xx-large;
    white-space: pre-wrap;
}

</style>
