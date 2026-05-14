import { defineStore } from 'pinia'
import { ref } from 'vue'
import api from '../services/api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function login(username, password) {
    loading.value = true
    error.value = null
    try {
      const response = await api.post('/auth/login/', { username, password })
      user.value = response.data
      return response.data
    } catch (err) {
      error.value = err.response?.data?.error || 'Error al iniciar sesion'
      return null
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    try {
      await api.post('/auth/logout/')
    } finally {
      user.value = null
    }
  }

  async function fetchMe() {
    try {
      const response = await api.get('/auth/me/')
      user.value = response.data
    } catch {
      user.value = null
    }
  }

  return { user, loading, error, login, logout, fetchMe }
})
