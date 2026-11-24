<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';





const profiles = ref([])
const games = ref([])
const participants=ref([])
const participantToAdd = ref({})
const participantToEdit = ref({})


async function fetchParticipant() {
    const r = await axios.get("/api/participants/");
    participants.value = r.data
}
async function fetchGames() {
    const r = await axios.get("/api/games/")
    games.value = r.data
}
async function fetchProfiles()
{
    const r = await axios.get("/api/profile/")
    profiles.value=r.data
}



async function onParticipantAdd() {
    await axios.post("/api/participants/", {
        ...participantToAdd.value,
    });
    await fetchGames()
}

async function onRemoveClick(participant) {
    await axios.delete(`/api/participants/${participant.id}/`)
    await fetchParticipant()
}
async function onParticipantEditClick(participant) {
    participantToEdit.value = { ...participant }
}

async function onParticipantUpdate() {
    await axios.put(`/api/participants/${participantToEdit.value.id}/`, {
        ...participantToEdit.value,
    });
    await fetchParticipant()
}
onBeforeMount(async () => {
    fetchProfiles();
    fetchGames();
    fetchParticipant();
})

</script>

<template>




    <div class="p-2">
        <form @submit.prevent.stop="onParticipantAdd">
            <div class="row">
                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="participantToAdd.game" required>
                            <option :value="t.id" v-for="t in games">{{ t.tournament_instance?.name }} Стадия:{{ t.stage }}</option>
                        </select>
                        <label for="floatingInput">Игра</label>
                    </div>
                </div>

                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="participantToAdd.user" required>
                            <option :value="t.id" v-for="t in profiles">{{ t.user?.username }}</option>
                        </select>
                        <label for="floatingInput">Пользователь</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="participantToAdd.team_name" required>
                        <label for="floatingInput">Название команды</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="participantToAdd.win_or_lose" required>
                        <label for="floatingInput">Победа/поражение</label>
                    </div>
                </div>
            </div>
            <div class="col-auto" style="margin-top: 10px;">
                <button class="btn btn-primary">Добавить</button>
            </div>
        </form>
    </div>
    <div>
        <div v-for="item in participants" class="participant-item">
            <b> {{ item.game_instance?.tournament_instance?.name }}, Стадия: {{ item.game_instance?.stage }}, Пользователь: {{ item.user?.username }}, Команда: {{ item.team_name }}  </b><b>{{ item.win_or_lose ? "Win" : "Lose" }}</b>
            <button class="btn btn-success" @click="onParticipantEditClick(item)" data-bs-toggle="modal"
                data-bs-target="#editGameModal">
                <i class="bi bi-pencil"></i>
            </button>
            <button class="btn btn-danger" @click="onRemoveClick(item)">
                <i class="bi bi-x"></i>
            </button>
        </div>
    </div>



    <!-- Modal -->
    <div class="modal fade" id="editGameModal" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Редактировать</h5>
                </div>
                <div class="modal-body">
                    <div class="row">
                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="participantToEdit.game" required>
                            <option :value="t.id" v-for="t in games">{{ t.name }}</option>
                        </select>
                        <label for="floatingInput">Игра</label>
                    </div>
                </div>

                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="participantToEdit.user" required>
                            <option :value="t.id" v-for="t in profiles">{{ t.name }}</option>
                        </select>
                        <label for="floatingInput">Пользователь</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="participantToEdit.team_name" required>
                        <label for="floatingInput">Название команды</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-check-label" v-model="participantToEdit.win_or_lose" required>
                        <label for="floatingInput">Победа/поражение</label>
                    </div>
                </div>
            </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                    <button type="button" data-bs-dismiss="modal" class="btn btn-primary"
                        @click="onParticipantUpdate">Сохранить</button>
                </div>
            </div>

        </div>
    </div>




</template>
<style scoped>
.participant-item {
    padding: 0.5rem;
    margin: 0.5rem 0;
    border: 1px solid silver;
    border-radius: 8px;
    display: grid;
    grid-template-columns: 1fr auto auto auto;
    align-items: center;
    gap: 16px;
}
</style>