<script setup>
import useProfileStore from '@/stores/profileStore';
import { storeToRefs } from 'pinia';



const profileStore = useProfileStore()
const {
    isAuth,
    userName
} = storeToRefs(profileStore)

async function onLogoutButtonClick(){
    profileStore.logout()
}

</script>

<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-between" id="navbarNavDropdown">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/tournaments">Турниры</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/games">Игры</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/participants">Участники</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/login">Вход</router-link>
                    </li>
                    
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            Пользователь
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/admin/">Админка</a></li>
                        </ul>
                    </li>
                    <div>
                    Авторизован: {{ userName }}
                    <button v-if="isAuth" class="btn btn-outline-success" @click="onLogoutButtonClick">
                        Выход
                    </button>
                    </div>
                </ul>
                
            </div>
        </nav>
    </div>
</template>
