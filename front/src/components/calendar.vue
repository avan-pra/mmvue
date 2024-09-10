<template>
    <div class="module">
        <header>Anniversaires</header>
        <table class="small calendar">
            <tr v-for="item in cal">
                <td v-if="edit"><button @click="deleteBirthday(item.id)">del</button></td>
                <td :style="{opacity: item.opacity}"><img width="20px" src="@/assets/birthday-cake.svg"></td>
                <td :style="{opacity: item.opacity}" class="title bright">{{ item.name }}</td>
                <td :style="{opacity: item.opacity}" class="time light" >{{ item.dateString }}</td>
            </tr>
        </table>
        <div v-if="edit">
            <input v-model="name" name="name" placeholder="nom"></input>
            <input v-model="date" name="date" type="date"></input>
            <button @click="postBirthday">submit</button>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios';
import { ref, toRef, watch } from 'vue';

const cal = ref()
const name = ref('')
const date = ref(new Date())

export default {
    props: ['edit'],
    data() {
        return {
            cal: cal,
            name: name,
            date: date,
        }
    },
    mounted() {
        this.getBirthday()
        setInterval(this.getBirthday, 1000 * 3600)
    },
    methods: {
        async postBirthday() {
            await axios.post('/api/birthdays', { name: this.name, date: this.date })
            this.getBirthday()
        },

        async deleteBirthday(id: Number) {
            await axios.delete(`/api/birthdays/${id}`)
            this.getBirthday()
        },

        async getBirthday() {
        let today = new Date()
            let birthdays = []
            let res = await axios.get('/api/birthdays')
            for (let i in res.data['data']) {
                let person = res.data['data'][i]
                birthdays.push(
                    {
                        'id': person['id'],
                        'name': person['name'],
                        'date': new Date(today.getFullYear(), Number(person['date'].split('-')[1]) - 1, Number(person['date'].split('-')[2])),
                        'dateString': {},
                        'opacity': 0
                    }
                )
            }
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
        }
    }
}

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
