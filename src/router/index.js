import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'
import ChatView from '../views/ChatView.vue'
import AdminView from '../views/admin/AdminView.vue'
import FlujosView from '../views/admin/FlujosView.vue'
import EditorView from '../views/admin/EditorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView,
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
    },
    {
      path: '/admin/flujos',
      name: 'flujos',
      component: FlujosView,
    },
    {
      path: '/admin/flujos/editor',
      name: 'editor',
      component: EditorView,
    },
  ],
})

export default router
