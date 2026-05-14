<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
    <div class="w-full max-w-sm">
      <!-- Logo -->
      <div class="flex items-center justify-center gap-2 mb-8">
        <span class="text-xl font-medium text-gray-900 tracking-tight">Calend</span>
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
      </div>

      <!-- Card -->
      <div class="bg-white border border-gray-200 rounded-2xl px-8 py-10">
        <h1 class="text-lg font-medium text-gray-900 mb-1">Bienvenido de vuelta</h1>
        <p class="text-sm text-gray-400 mb-8">Ingresá a tu cuenta para continuar</p>

        <!-- Email -->
        <div class="mb-4">
          <label class="block text-xs font-medium text-gray-700 mb-1.5"> Correo electrónico </label>
          <input
            v-model="email"
            type="email"
            placeholder="tu@correo.com"
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 focus:border-transparent transition"
          />
        </div>

        <!-- Contraseña -->
        <div class="mb-6">
          <div class="flex items-center justify-between mb-1.5">
            <label class="block text-xs font-medium text-gray-700"> Contraseña </label>
            <a href="#" class="text-xs text-emerald-500 hover:text-emerald-600 transition">
              ¿Olvidaste tu contraseña?
            </a>
          </div>
          <input
            v-model="password"
            type="password"
            placeholder="••••••••"
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 focus:border-transparent transition"
          />
        </div>

        <!-- Error -->
        <p v-if="error" class="text-xs text-red-500 mb-4">
          {{ error }}
        </p>

        <!-- Botón -->
        <button
          @click="handleLogin"
          class="w-full bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
        >
          Ingresar
        </button>
      </div>

      <!-- Footer -->
      <p class="text-center text-xs text-gray-400 mt-6">
        <a
          @click.prevent="$router.push('/')"
          href="#"
          class="text-emerald-500 hover:text-emerald-600 transition"
        >
          ← Volver al inicio
        </a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const error = ref('')

async function handleLogin() {
  if (!email.value || !password.value) {
    error.value = 'Por favor completa todos los campos.'
    return
  }

  const user = await authStore.login(email.value, password.value)

  if (!user) {
    error.value = authStore.error
    return
  }

  if (user.role === 'admin') {
    router.push('/admin')
  } else {
    router.push('/dashboard')
  }
}
</script>
