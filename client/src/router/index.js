import { createRouter, createWebHistory } from 'vue-router'
import TournamentsView from '../views/TournamentsView.vue'
import GamesView from '../views/GamesView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "TournamentsView",
      component: TournamentsView
    },
    {
      path: "/games",
      name: "GamesView",
      component: GamesView
    }
  ],
})

export default router
