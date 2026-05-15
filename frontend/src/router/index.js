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
import ClientesView from '../views/admin/ClientesView.vue'
import { useAuthStore } from '../stores/auth'

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
      meta: { requiresAuth: true, role: 'client' },
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView,
      meta: { requiresAuth: true, role: 'client' },
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/flujos',
      name: 'flujos',
      component: FlujosView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/flujos/editor',
      name: 'editor',
      component: EditorView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/canales',
      name: 'canales',
      component: CanalesView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/contactos',
      name: 'contactos',
      component: ContactosView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/configuracion',
      name: 'configuracion',
      component: ConfiguracionView,
      meta: { requiresAuth: true, role: 'admin' },
    },
    {
      path: '/admin/clientes',
      name: 'clientes',
      component: ClientesView,
      meta: { requiresAuth: true, role: 'admin' },
    },
  ],
})

router.beforeEach(async (to) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth) {
    await authStore.fetchMe()

    if (!authStore.user) {
      return { name: 'login' }
    }

    if (to.meta.role === 'admin' && authStore.user.role !== 'admin') {
      return { name: 'dashboard' }
    }

    if (to.meta.role === 'client' && authStore.user.role !== 'client') {
      return { name: 'admin' }
    }
  }
})

export default router
