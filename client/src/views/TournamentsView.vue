<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';
//import _ from 'lodash'


const tournaments = ref([])
// const groupsById=computed ((=> {return _keyBy(groups.value, x => x.id)}))
//groupsById[item.group]?# ? - не выводит, если нет #.name
const tournamentToAdd = ref({})

const tournamentToEdit = ref({})
const tournamentEditImageUrl = ref()
const tournamentEditPictureRef=ref()

const tournamentImageUrlCheck=ref()

const tournamentAddPictureRef = ref()
const tournamentAddImageUrl = ref()



async function fetchTournaments() {
    const r = await axios.get("/api/tournaments/");
    tournaments.value = r.data
}

async function checkTournamentPictureClick(picture)
{
    tournamentImageUrlCheck.value=picture ? picture : null;
}


async function tournamentsAddPictureChange() {
    tournamentAddImageUrl.value = URL.createObjectURL(tournamentAddPictureRef.value.files[0])
}

async function tournamentsEditPictureChange()
{
    tournamentEditImageUrl.value=URL.createObjectURL(tournamentEditPictureRef.value.files[0])
}


async function onTournamentAdd() {
    const formData = new FormData();
    formData.append('preview', tournamentAddPictureRef.value.files[0])
    
    

    formData.set('name', tournamentToAdd.value.name)
    formData.set('start_date', tournamentToAdd.value.start_date)
    formData.set('end_date', tournamentToAdd.value.end_date)
    formData.set('stages_count', tournamentToAdd.value.stages_count)
    formData.set('prize', tournamentToAdd.value.prize)
    formData.set('g_power_limit', tournamentToAdd.value.g_power_limit)
    formData.set('rules', tournamentToAdd.value.rules)


    await axios.post("/api/tournaments/", formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
    await fetchTournaments()
}

async function onRemoveClick(tournament) {
    await axios.delete(`/api/tournaments/${tournament.id}/`)
    await fetchTournaments()
}
async function onTournamentEditClick(tournament) {
    tournamentToEdit.value = { ...tournament }

    tournamentEditImageUrl.value=tournament.preview ? tournament.preview : null
}

async function onTournamentUpdate() {


    const formData = new FormData();
    if (tournamentEditPictureRef.value && tournamentEditPictureRef.value.files[0]) {
        formData.append('preview', tournamentEditPictureRef.value.files[0]);
    }

    formData.set('name', tournamentToEdit.value.name)
    formData.set('start_date', tournamentToEdit.value.start_date)
    formData.set('end_date', tournamentToEdit.value.end_date)
    formData.set('stages_count', tournamentToEdit.value.stages_count)
    formData.set('prize', tournamentToEdit.value.prize)
    formData.set('g_power_limit', tournamentToEdit.value.g_power_limit)
    formData.set('rules', tournamentToEdit.value.rules)

    await axios.patch(`/api/tournaments/${tournamentToEdit.value.id}/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
    await fetchTournaments()
}
onBeforeMount(async () => {
    fetchTournaments();
})

</script>

<template>

    <div class="p-2">
        <form @submit.prevent.stop="onTournamentAdd">
            <div class="row">
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="tournamentToAdd.name" required>
                        <label for="floatingInput">Название</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="date" class="form-control" v-model="tournamentToAdd.start_date" required>
                        <label for="floatingInput">Дата начала</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="date" class="form-control" v-model="tournamentToAdd.end_date" required>
                        <label for="floatingInput">Дата окончания</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="number" min="1" class="form-control" v-model="tournamentToAdd.stages_count"
                            required>
                        <label for="floatingInput">Количество стадий</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="tournamentToAdd.prize" required>
                        <label for="floatingInput">Приз</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="number" min="250" class="form-control" v-model="tournamentToAdd.g_power_limit"
                            required>
                        <label for="floatingInput">Ограничение силы</label>
                    </div>
                </div>
                <div class="col-auto">
                    <div class="form-floating">
                        <input type="text" class="form-control" v-model="tournamentToAdd.rules" required>
                        <label for="floatingInput">Правила</label>
                    </div>
                </div>
                <div class="col-auto">
                    <input class="form-control" type="file" ref="tournamentAddPictureRef" required
                        @change="tournamentsAddPictureChange">
                </div>
                <div class="col-auto">
                    <img :src="tournamentAddImageUrl" style="max-height: 60px;" alt="">
                </div>
            </div>
            <div class="col-auto" style="margin-top: 10px;">
                <button class="btn btn-primary">Добавить</button>
            </div>
        </form>
    </div>
    <div>
        <div v-for="item in tournaments" class="tournament-item">
            <b>{{ item.name }}</b>

            <div v-show="item.preview" @click="checkTournamentPictureClick(item.preview)" data-bs-toggle="modal" 
            data-bs-target="#checkTournamentPicture"> 
                <img :src="item.preview" style="max-height:60px;">
            </div>

            <button class="btn btn-success" @click="onTournamentEditClick(item)" data-bs-toggle="modal"
                data-bs-target="#editTournamentModal">
                <i class="bi bi-pencil"></i>
            </button>
            <button class="btn btn-danger" @click="onRemoveClick(item)">
                <i class="bi bi-x"></i>
            </button>
        </div>
    </div>


<!-- Modal for picture -->
    <div class="modal fade" id="checkTournamentPicture" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    <div class="row">
                        <img :src="tournamentImageUrlCheck" style="max-height: 400px;" alt="">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                </div>
            </div>
        </div>
    </div>



    <!-- Modal for Edit -->
    <div class="modal fade" id="editTournamentModal" tabindex="-1">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLongTitle">Редактировать</h5>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="tournamentToEdit.name" required>
                                <label for="floatingInput">Название</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="date" class="form-control" v-model="tournamentToEdit.start_date" required>
                                <label for="floatingInput">Дата начала</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="date" class="form-control" v-model="tournamentToEdit.end_date" required>
                                <label for="floatingInput">Дата окончания</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="number" min="1" class="form-control"
                                    v-model="tournamentToEdit.stages_count" required>
                                <label for="floatingInput">Количество стадий</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="tournamentToEdit.prize" required>
                                <label for="floatingInput">Приз</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="number" min="250" class="form-control"
                                    v-model="tournamentToEdit.g_power_limit" required>
                                <label for="floatingInput">Ограничение силы</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="tournamentToEdit.rules" required>
                                <label for="floatingInput">Правила</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <input class="form-control" type="file" ref="tournamentEditPictureRef" 
                                @change="tournamentsEditPictureChange">
                        </div>
                        <div class="col-auto">
                            <img :src="tournamentEditImageUrl" style="max-height: 60px;" alt="">
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
                    <button type="button" data-bs-dismiss="modal" class="btn btn-primary"
                        @click="onTournamentUpdate">Сохранить</button>
                </div>
            </div>

        </div>
    </div>


</template>
<style scoped>
.tournament-item {
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