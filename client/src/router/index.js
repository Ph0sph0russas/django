import { createRouter, createWebHistory } from 'vue-router'
import TournamentsView from '../views/TournamentsView.vue'
import MainPage from '../views/MainPage.vue'
import LoginPage from '../views/LogicPage.vue'
import GamesView from '../views/GamesView.vue'
import ParticipantsView from '../views/ParticipantsView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active",
  routes: [
    {
      path: "/",
      component: MainPage
    },
    {
      path: "/login",
      component: LoginPage
    },
    {
      path: "/tournaments",
      name: "TournamentView",
      component: TournamentsView
    },
    {
      path: "/games",
      name: "GamesView",
      component: GamesView
    },
    {
      path: "/participants",
      name: "ParticipantsView",
      component: ParticipantsView
    }
  ],
})

export default router
