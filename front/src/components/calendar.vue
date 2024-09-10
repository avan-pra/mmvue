<template>
    <div class="module">
        <header>Anniversaires</header>
        <table class="small calendar">
            <tr v-for="item in cal">
                <td :style="{opacity: item.opacity}"><img width="20px" src="@/assets/birthday-cake.svg"></td>
                <td :style="{opacity: item.opacity}" class="title bright">{{ item.name }}</td>
                <td :style="{opacity: item.opacity}" class="time light" >{{ item.dateString }}</td>
            </tr>
        </table>
        <form v-if="edit">
            <input name="name" placeholder="nom"></input>
            <input name="date" type="date"></input>
            <button>submit</button>
        </form>
    </div>
</template>

<script lang="ts">
import { ref, toRef, watch } from 'vue';

const cal = ref()

export default {
    props: ['edit'],
    data() {
        return {
            cal: cal,
        }
    }
}

let today = new Date()

const birthdays = [
{'name': 'Julien', 'date': new Date(today.getFullYear(), 9 - 1, 9), 'dateString': {}, 'opacity': 0},
{'name': 'Arthur', 'date': new Date(today.getFullYear(), 1 - 1, 4), 'dateString': {}, 'opacity': 0},
{'name': 'Arthur', 'date': new Date(today.getFullYear(), 1 - 1, 4), 'dateString': {}, 'opacity': 0},
{'name': 'Tibo', 'date': new Date(today.getFullYear(), 3 - 1, 25), 'dateString': {}, 'opacity': 0},
]
birthdays.forEach((elem, i) => {
    if (elem['date'].getMonth() < today.getMonth()) {
        elem['date'].setFullYear(elem['date'].getFullYear() + 1)
    }
    else if (elem['date'].getMonth() == today.getMonth() && elem['date'].getDate() < today.getDate()) {
        elem['date'].setFullYear(elem['date'].getFullYear() + 1)
    }
    elem['dateString'] = elem.date.toLocaleString('fr-FR', { month: 'short', day: 'numeric' })
})

birthdays.sort((a, b) => a['date'] - b['date'])
birthdays.forEach((elem, i) => {
    if (i <= 1) {
        elem['opacity'] = 1
    }
    else {
        elem['opacity'] = 1 - (i / birthdays.length)
    }
})


cal.value = birthdays



</script>

<style scoped>

.calendar .symbol {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-left: 0;
  padding-right: 10px;
  font-size: var(--font-size-small);
}

.calendar .symbol span {
  padding-top: 4px;
}

.calendar .title {
  padding-left: 0;
  padding-right: 0;
  vertical-align: top;
}

.calendar .time {
  padding-left: 30px;
  text-align: right;
  vertical-align: top;
}

</style>
