<template>
  <div class="min-h-screen bg-gray-50 flex">
    <!-- Sidebar -->
    <aside class="w-56 bg-white border-r border-gray-100 flex flex-col px-4 py-6 fixed h-full">
      <div class="flex items-center gap-2 mb-10 px-2">
        <span class="text-base font-medium text-gray-900 tracking-tight">Calend</span>
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
      </div>

      <nav class="flex flex-col gap-1 flex-1">
        <a
          @click.prevent="$router.push('/dashboard')"
          href="#"
          class="flex items-center gap-3 px-3 py-2 rounded-lg bg-emerald-50 text-emerald-700 text-sm font-medium"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
            />
          </svg>
          Inicio
        </a>
        <a
          @click.prevent="$router.push('/dashboard')"
          href="#"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-500 hover:bg-gray-50 text-sm transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          Citas
        </a>
        <a
          @click.prevent="$router.push('/chat')"
          href="#"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-500 hover:bg-gray-50 text-sm transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
            />
          </svg>
          Chatbot
        </a>
        <a
          href="#"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-500 hover:bg-gray-50 text-sm transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg>
          Clientes
        </a>
        <a
          href="#"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-500 hover:bg-gray-50 text-sm transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
            />
          </svg>
          Estadisticas
        </a>
      </nav>

      <!-- Usuario -->
      <div class="flex items-center gap-3 px-2 pt-4 border-t border-gray-100">
        <div
          class="w-7 h-7 rounded-full bg-emerald-100 flex items-center justify-center text-xs font-medium text-emerald-700"
        >
          GA
        </div>
        <div class="flex-1 min-w-0">
          <p class="text-xs font-medium text-gray-900 truncate">Gonzalo Acuna</p>
          <p class="text-xs text-gray-400 truncate">Admin</p>
        </div>
        <button @click="logout" class="text-gray-400 hover:text-gray-600 transition">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
            />
          </svg>
        </button>
      </div>
    </aside>

    <!-- Contenido principal -->
    <main class="ml-56 flex-1 px-8 py-8">
      <!-- Header -->
      <div class="flex items-center justify-between mb-8">
        <div>
          <h1 class="text-lg font-medium text-gray-900">Buenos dias, Gonzalo</h1>
          <p class="text-sm text-gray-400">Aqui esta el resumen de hoy</p>
        </div>
        <button
          class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
        >
          + Nueva cita
        </button>
      </div>

      <!-- Metricas -->
      <div class="grid grid-cols-4 gap-4 mb-8">
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Citas hoy</p>
          <p class="text-2xl font-medium text-gray-900">{{ metricas.citas_hoy }}</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Este mes</p>
          <p class="text-2xl font-medium text-gray-900">{{ metricas.citas_mes }}</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Clientes activos</p>
          <p class="text-2xl font-medium text-gray-900">{{ metricas.contactos }}</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Tasa de confirmacion</p>
          <p class="text-2xl font-medium text-gray-900">94%</p>
          <p class="text-xs text-gray-400 mt-1">Promedio del mes</p>
        </div>
      </div>

      <!-- Citas de hoy -->
      <div class="bg-white border border-gray-100 rounded-2xl p-6 mb-6">
        <div class="flex items-center justify-between mb-5">
          <h2 class="text-sm font-medium text-gray-900">Citas de hoy</h2>
          <a href="#" class="text-xs text-emerald-500 hover:text-emerald-600 transition"
            >Ver todas →</a
          >
        </div>
        <div class="flex flex-col gap-3">
          <div
            v-for="cita in citas"
            :key="cita.id"
            class="flex items-center justify-between py-3 border-b border-gray-50 last:border-0"
          >
            <div v-if="citas.length === 0" class="text-sm text-gray-400 text-center py-6">
              No hay citas registradas todavia
            </div>
            <div
              v-for="cita in citas"
              :key="cita.id"
              class="flex items-center justify-between py-3 border-b border-gray-50 last:border-0"
            >
              <div class="flex items-center gap-3">
                <div
                  class="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-xs font-medium text-emerald-700"
                >
                  {{ cita.iniciales }}
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ cita.nombre }}</p>
                  <p class="text-xs text-gray-400">{{ cita.servicio }}</p>
                </div>
              </div>
              <div class="flex items-center gap-4">
                <p class="text-sm text-gray-600">{{ cita.hora }}</p>
                <span
                  :class="estadoClase(cita.estado)"
                  class="text-xs px-2.5 py-1 rounded-full font-medium"
                >
                  {{ cita.estado }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import api from '../../services/api'

const router = useRouter()
const authStore = useAuthStore()

const citas = ref([])
const metricas = ref({
  citas_hoy: 0,
  citas_mes: 0,
  contactos: 0,
})

async function cargarDatos() {
  try {
    const [citasRes, metricasRes] = await Promise.all([api.get('/citas/'), api.get('/metricas/')])
    citas.value = citasRes.data
    metricas.value = metricasRes.data
  } catch (err) {
    console.error('Error cargando datos:', err)
  }
}

function logout() {
  authStore.logout()
  router.push('/login')
}

function estadoClase(estado) {
  if (estado === 'Confirmada') return 'bg-emerald-50 text-emerald-700'
  if (estado === 'Pendiente') return 'bg-amber-50 text-amber-700'
  if (estado === 'Cancelada') return 'bg-red-50 text-red-600'
}

onMounted(() => {
  cargarDatos()
})
</script>
