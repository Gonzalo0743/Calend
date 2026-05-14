import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'

import DashboardView from '../views/client/DashboardView.vue'
import ChatView from '../views/client/ChatView.vue'

import AdminView from '../views/admin/AdminView.vue'
import FlujosView from '../views/admin/FlujosView.vue'
import EditorView from '../views/admin/EditorView.vue'
import CanalesView from '../views/admin/CanalesView.vue'
import ContactosView from '../views/admin/ContactosView.vue'
import ConfiguracionView from '../views/admin/ConfiguracionView.vue'

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
    {
      path: '/admin/canales',
      name: 'canales',
      component: CanalesView,
    },
    {
      path: '/admin/contactos',
      name: 'contactos',
      component: ContactosView,
    },
    {
      path: '/admin/configuracion',
      name: 'configuracion',
      component: ConfiguracionView,
    },
  ],
})

export default router
