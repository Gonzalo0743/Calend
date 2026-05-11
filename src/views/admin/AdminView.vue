<template>
  <div class="min-h-screen bg-gray-50 flex">
    <!-- Sidebar -->
    <aside class="w-60 bg-white border-r border-gray-100 flex flex-col px-4 py-6 fixed h-full">
      <div class="flex items-center gap-2 mb-10 px-2">
        <span class="text-base font-medium text-gray-900 tracking-tight">Calend</span>
        <span class="text-xs bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full font-medium"
          >Admin</span
        >
      </div>

      <nav class="flex flex-col gap-1 flex-1">
        <a
          v-for="item in navItems"
          :key="item.label"
          href="#"
          @click.prevent="$router.push('/admin/flujos')"
          :class="
            seccionActiva === item.id
              ? 'bg-emerald-50 text-emerald-700'
              : 'text-gray-500 hover:bg-gray-50'
          "
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors"
        >
          <component :is="item.icon" class="w-4 h-4" />
          {{ item.label }}
        </a>
      </nav>

      <div class="pt-4 border-t border-gray-100 px-2">
        <div class="flex items-center gap-3">
          <div
            class="w-7 h-7 rounded-full bg-emerald-100 flex items-center justify-center text-xs font-medium text-emerald-700"
          >
            GA
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-xs font-medium text-gray-900 truncate">Gonzalo Acuna</p>
            <p class="text-xs text-gray-400">Desarrollador</p>
          </div>
          <button
            @click="$router.push('/login')"
            class="text-gray-400 hover:text-gray-600 transition"
          >
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
      </div>
    </aside>

    <!-- Contenido -->
    <main class="ml-60 flex-1 px-8 py-8">
      <!-- Header -->
      <div class="flex items-center justify-between mb-8">
        <div>
          <h1 class="text-lg font-medium text-gray-900">Panel de desarrollo</h1>
          <p class="text-sm text-gray-400">Resumen general de Calend</p>
        </div>
        <div
          class="flex items-center gap-2 text-xs text-gray-400 bg-white border border-gray-100 rounded-lg px-3 py-2"
        >
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          Ultimos 7 dias
        </div>
      </div>

      <!-- Metricas -->
      <div class="grid grid-cols-4 gap-4 mb-8">
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Bots activos</p>
          <p class="text-2xl font-medium text-gray-900">12</p>
          <p class="text-xs text-emerald-500 mt-1">+2 este mes</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Conversaciones</p>
          <p class="text-2xl font-medium text-gray-900">1,248</p>
          <p class="text-xs text-emerald-500 mt-1">+18% vs semana anterior</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Clientes activos</p>
          <p class="text-2xl font-medium text-gray-900">8</p>
          <p class="text-xs text-emerald-500 mt-1">+1 nuevo</p>
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-5">
          <p class="text-xs text-gray-400 mb-1">Citas agendadas</p>
          <p class="text-2xl font-medium text-gray-900">340</p>
          <p class="text-xs text-emerald-500 mt-1">+22% vs semana anterior</p>
        </div>
      </div>

      <!-- Graficas -->
      <div class="grid grid-cols-2 gap-6 mb-8">
        <div class="bg-white border border-gray-100 rounded-2xl p-6">
          <h2 class="text-sm font-medium text-gray-900 mb-4">Conversaciones por dia</h2>
          <Line :data="conversacionesData" :options="chartOptions" />
        </div>
        <div class="bg-white border border-gray-100 rounded-2xl p-6">
          <h2 class="text-sm font-medium text-gray-900 mb-4">Citas agendadas por dia</h2>
          <Line :data="citasData" :options="chartOptions" />
        </div>
      </div>

      <!-- Bots recientes -->
      <div class="bg-white border border-gray-100 rounded-2xl p-6">
        <div class="flex items-center justify-between mb-5">
          <h2 class="text-sm font-medium text-gray-900">Bots activos</h2>
          <button
            class="text-xs bg-emerald-400 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg transition-colors"
          >
            + Nuevo bot
          </button>
        </div>
        <div class="flex flex-col gap-3">
          <div
            v-for="bot in bots"
            :key="bot.id"
            class="flex items-center justify-between py-3 border-b border-gray-50 last:border-0"
          >
            <div class="flex items-center gap-3">
              <div class="w-8 h-8 rounded-xl bg-emerald-100 flex items-center justify-center">
                <svg
                  class="w-4 h-4 text-emerald-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1.5"
                    d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
                  />
                </svg>
              </div>
              <div>
                <p class="text-sm font-medium text-gray-900">{{ bot.nombre }}</p>
                <p class="text-xs text-gray-400">{{ bot.cliente }}</p>
              </div>
            </div>
            <div class="flex items-center gap-6">
              <div class="text-right">
                <p class="text-xs text-gray-400">Conversaciones</p>
                <p class="text-sm font-medium text-gray-900">{{ bot.conversaciones }}</p>
              </div>
              <div class="text-right">
                <p class="text-xs text-gray-400">Citas</p>
                <p class="text-sm font-medium text-gray-900">{{ bot.citas }}</p>
              </div>
              <span
                class="text-xs bg-emerald-50 text-emerald-700 px-2.5 py-1 rounded-full font-medium"
              >
                Activo
              </span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Filler,
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Filler)

const seccionActiva = ref('inicio')

const navItems = [
  { id: 'inicio', label: 'Inicio', icon: 'svg' },
  { id: 'flujos', label: 'Flujos de trabajo', icon: 'svg' },
  { id: 'canales', label: 'Canales', icon: 'svg' },
  { id: 'contactos', label: 'Contactos', icon: 'svg' },
  { id: 'configuracion', label: 'Configuracion', icon: 'svg' },
]

const dias = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

const conversacionesData = {
  labels: dias,
  datasets: [
    {
      label: 'Conversaciones',
      data: [142, 189, 156, 210, 198, 167, 186],
      borderColor: '#34d399',
      backgroundColor: 'rgba(52, 211, 153, 0.08)',
      borderWidth: 2,
      pointRadius: 3,
      pointBackgroundColor: '#34d399',
      tension: 0.4,
      fill: true,
    },
  ],
}

const citasData = {
  labels: dias,
  datasets: [
    {
      label: 'Citas',
      data: [38, 52, 41, 67, 59, 48, 55],
      borderColor: '#34d399',
      backgroundColor: 'rgba(52, 211, 153, 0.08)',
      borderWidth: 2,
      pointRadius: 3,
      pointBackgroundColor: '#34d399',
      tension: 0.4,
      fill: true,
    },
  ],
}

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { display: false },
  },
  scales: {
    x: {
      grid: { display: false },
      ticks: { font: { size: 11 }, color: '#9ca3af' },
    },
    y: {
      grid: { color: '#f3f4f6' },
      ticks: { font: { size: 11 }, color: '#9ca3af' },
    },
  },
}

const bots = [
  {
    id: 1,
    nombre: 'Bot Clinica Verde',
    cliente: 'Clinica Verde S.A.',
    conversaciones: 423,
    citas: 118,
  },
  { id: 2, nombre: 'Bot FitLife', cliente: 'FitLife Gym', conversaciones: 312, citas: 89 },
  {
    id: 3,
    nombre: 'Bot Consultorio Bienestar',
    cliente: 'Consultorio Bienestar',
    conversaciones: 289,
    citas: 76,
  },
  {
    id: 4,
    nombre: 'Bot Dental Sonrisa',
    cliente: 'Clinica Dental Sonrisa',
    conversaciones: 224,
    citas: 57,
  },
]
</script>
