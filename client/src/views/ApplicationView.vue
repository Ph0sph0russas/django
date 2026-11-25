<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';




const tournaments = ref([])
const applications = ref([])
const applicationToAdd = ref({})
const applicationToEdit = ref({})

async function fetchApplications() {
    const r = await axios.get("/api/applications/")
    console.log(r.data)
    applications.value = r.data
}
async function fetchTournaments() {
    const r = await axios.get("/api/tournaments/");
    tournaments.value = r.data
}



async function onApplicationAdd() {
    await axios.post("/api/application/", {
        ...applicationToAdd.value,
    });
    await fetchApplications()
}

async function onRemoveClick(application) {
    await axios.delete(`/api/applications/${application.id}/`)
    await fetchApplications()
}
async function onApplicationEditClick(application) {
    applicationToEdit.value = { ...application }
}

async function onApplicationUpdate() {
    await axios.put(`/api/applications/${applicationToEdit.value.id}/`, {
        ...applicationToEdit.value,
    });
    await fetchApplications()
}
onBeforeMount(async () => {
    fetchTournaments();
    fetchApplications();
})

</script>

<template>




    <div class="p-2">
        <form @submit.prevent.stop="onApplicationAdd">
            <div class="row">
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="applicationToAdd.name" required>
                        <label for="floatingInput">Имя</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="applicationToAdd.team_name" required>
                        <label for="floatingInput">Название команды</label>
                    </div>
                </div>

                <!--SELECT-->
                <div class="col-auto">
                    <div class="form-floating">
                        <select name="" id="" class="form-select" v-model="applicationToAdd.tournament" required>
                            <option :value="t.id" v-for="t in tournaments">{{ t.name }}</option>
                        </select>
                        <label for="floatingInput">Турнир</label>
                    </div>
                </div>

                <div class="col-auto">
                    <div class="form-floating">
                        <input type="checkbox" class="form-control" v-model="applicationToAdd.approval">
                        <label for="floatingInput">Одобрение</label>
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
            <b> Стадия{{ item.stage }} {{ item.status }} {{ item.place }} </b><b>{{ item.tournament_instance?.name }}</b>
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
                                <select name="" id="" class="form-select" v-model="gameToEdit.tournament" required>
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