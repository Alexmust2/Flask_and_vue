import { createRouter, createWebHistory } from 'vue-router'
import Users from '../components/Users.vue'
import Posts from '../components/Posts.vue'

const routes = [
  {
    path: '/users',
    name: 'users',
    component: Users
  },
  {
    path: '/user/:id',
    name: "user_id",
    component: Posts
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
