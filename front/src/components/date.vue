<template>
    <div class="module">
        <div class="clock-grid">
            <div class="digital">
                <div class="date normal medium">{{ day }}</div>
                <div class="time bright large light">{{ time }}<sup class="seconds dimmed">{{ timesec }}</sup></div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ref } from 'vue';

export default {
    data() {
        return {
            day: day,
            time: time,
            timesec: timesec
        }
    }
}

const day = ref()
const time = ref()
const timesec = ref()

setInterval(() => {
    let date = new Date()
    let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };

    day.value = date.toLocaleDateString('fr-FR', options)
    time.value = `${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}`
    timesec.value = `${('0' + date.getSeconds()).slice(-2)}`
}, 1000);

</script>