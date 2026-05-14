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
      localStorage.setItem('access_token', response.data.access)
      localStorage.setItem('refresh_token', response.data.refresh)
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
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
  }

  async function fetchMe() {
    const token = localStorage.getItem('access_token')
    if (!token) {
      user.value = null
      return
    }
    try {
      const response = await api.get('/auth/me/')
      user.value = response.data
    } catch {
      user.value = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
  }

  return { user, loading, error, login, logout, fetchMe }
})
