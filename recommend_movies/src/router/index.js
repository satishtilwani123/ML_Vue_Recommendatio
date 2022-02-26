import { createRouter, createWebHistory } from 'vue-router'
import Movies from '../views/Movies.vue'
import Recommendation from '../views/Recommendation.vue'

const routes = [
  {
    path: '/',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/Recommendation/:id/:name',
    name: 'Recommendation',
    component: Recommendation,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
