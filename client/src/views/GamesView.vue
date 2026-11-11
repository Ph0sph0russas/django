<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';





const tournaments = ref([])
const games = ref([])
const gameToAdd = ref({})
const gameToEdit = ref({})

async function fetchGames() {
    const r = await axios.get("/api/games/")
    console.log(r.data)
    games.value = r.data
}
async function fetchTournaments() {
    const r = await axios.get("/api/tournaments/");
    tournaments.value = r.data
}



async function onGameAdd() {
    await axios.post("/api/games/", {
        ...gameToAdd.value,
    });
    await fetchGames()
}

async function onRemoveClick(game) {
    await axios.delete(`/api/games/${game.id}/`)
    await fetchGames()
}
async function onGameEditClick(game) {
    gameToEdit.value = { ...game }
}

async function onGameUpdate() {
    await axios.put(`/api/games/${gameToEdit.value.id}/`, {
        ...gameToEdit.value,
    });
    await fetchGames()
}
onBeforeMount(async () => {
    fetchTournaments();
    fetchGames();
})

</script>

<template>




    <div class="p-2">
        <form @submit.prevent.stop="onGameAdd">
            <div class="row">
                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="gameToAdd.tournament" required>
                            <option :value="t.id" v-for="t in tournaments">{{ t.name }}</option>
                        </select>
                        <label for="floatingInput">Турнир</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="gameToAdd.place" required>
                        <label for="floatingInput">Место проведения</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="date" class="form-control" v-model="gameToAdd.start_date" required>
                        <label for="floatingInput">Дата начала</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="date" class="form-control" v-model="gameToAdd.end_date" required>
                        <label for="floatingInput">Дата окончания</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="number" min="1" class="form-control" v-model="gameToAdd.stage" required>
                        <label for="floatingInput">Стадия</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="gameToAdd.status" required>
                        <label for="floatingInput">Статус</label>
                    </div>
                </div>

            </div>
            <div class="col-auto" style="margin-top: 10px;">
                <button class="btn btn-primary">Добавить</button>
            </div>
        </form>
    </div>
    <div>
        <div v-for="item in games" class="game-item">
            <b> Стадия{{ item.stage }} {{ item.status }} {{ item.place }} </b><b>{{ item.tournament_instance?.name}}</b>
            <button class="btn btn-success" @click="onGameEditClick(item)" data-bs-toggle="modal"
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
                        <div class="col-auto">
                            <div class="form-floating">
                                <select name="" id="" class="form-select" v-model="gameToAdd.tournament" required>
                                    <option :value="t.id" v-for="t in tournaments">{{ t.name }}</option>
                                </select>
                                <label for="floatingInput">Турнир</label>
                            </div>
                        </div>

                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="gameToEdit.place" required>
                                <label for="floatingInput">Место проведения</label>
                            </div>
                        </div>

                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="date" class="form-control" v-model="gameToEdit.start_date" required>
                                <label for="floatingInput">Дата начала</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="date" class="form-control" v-model="gameToEdit.end_date" required>
                                <label for="floatingInput">Дата окончания</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="number" min="1" class="form-control" v-model="gameToEdit.stage" required>
                                <label for="floatingInput">Стадия</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="gameToEdit.status" required>
                                <label for="floatingInput">Статус</label>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                    <button type="button" data-bs-dismiss="modal" class="btn btn-primary"
                        @click="onGameUpdate">Сохранить</button>
                </div>
            </div>

        </div>
    </div>




</template>
<style scoped>
.game-item {
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