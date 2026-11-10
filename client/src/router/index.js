import { createRouter, createWebHistory } from 'vue-router'
import TournamentsView from '../views/TournamentsView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "TournamentsView",
      component: TournamentsView
    }
  ],
})

export default router
