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
          href="#"
          @click.prevent="$router.push('/admin')"
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-500 hover:bg-gray-50 text-sm transition-colors"
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
          href="#"
          @click.prevent="$router.push('/admin/flujos')"
          class="flex items-center gap-3 px-3 py-2 rounded-lg bg-emerald-50 text-emerald-700 text-sm font-medium"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M4 6h16M4 10h16M4 14h16M4 18h16"
            />
          </svg>
          Flujos de trabajo
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
              d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0"
            />
          </svg>
          Canales
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
          Contactos
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
              d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg>
          Configuracion
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
          <h1 class="text-lg font-medium text-gray-900">Flujos de trabajo</h1>
          <p class="text-sm text-gray-400">Crea y administra los flujos de tus chatbots</p>
        </div>
        <button
          @click="mostrarModal = true"
          class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
        >
          + Crear nuevo
        </button>
      </div>

      <!-- Filtros -->
      <div class="flex items-center gap-3 mb-6">
        <button
          v-for="filtro in filtros"
          :key="filtro"
          @click="filtroActivo = filtro"
          :class="
            filtroActivo === filtro
              ? 'bg-emerald-400 text-white'
              : 'bg-white border border-gray-200 text-gray-500 hover:bg-gray-50'
          "
          class="text-xs px-4 py-2 rounded-lg transition-colors font-medium"
        >
          {{ filtro }}
        </button>
      </div>

      <!-- Tabla -->
      <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
        <table class="w-full">
          <thead>
            <tr class="border-b border-gray-100">
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Nombre</th>
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Cliente</th>
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Estado</th>
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Conversaciones</th>
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Modificado</th>
              <th class="text-left text-xs font-medium text-gray-400 px-6 py-4"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="flujo in flujosFiltrados"
              :key="flujo.id"
              class="border-b border-gray-50 last:border-0 hover:bg-gray-50 transition-colors"
            >
              <td class="px-6 py-4">
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
                  <span class="text-sm font-medium text-gray-900">{{ flujo.nombre }}</span>
                </div>
              </td>
              <td class="px-6 py-4 text-sm text-gray-500">{{ flujo.cliente }}</td>
              <td class="px-6 py-4">
                <span
                  :class="
                    flujo.estado === 'Activo'
                      ? 'bg-emerald-50 text-emerald-700'
                      : 'bg-gray-100 text-gray-500'
                  "
                  class="text-xs px-2.5 py-1 rounded-full font-medium"
                >
                  {{ flujo.estado }}
                </span>
              </td>
              <td class="px-6 py-4 text-sm text-gray-500">{{ flujo.conversaciones }}</td>
              <td class="px-6 py-4 text-sm text-gray-400">{{ flujo.modificado }}</td>
              <td class="px-6 py-4">
                <button
                  @click="$router.push('/admin/flujos/editor')"
                  class="text-xs text-emerald-600 hover:text-emerald-700 font-medium transition-colors"
                >
                  Editar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>

    <!-- Modal nuevo flujo -->
    <div
      v-if="mostrarModal"
      class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 w-full max-w-md shadow-lg">
        <h2 class="text-base font-medium text-gray-900 mb-1">Nuevo flujo</h2>
        <p class="text-sm text-gray-400 mb-6">Dale un nombre a tu nuevo chatbot</p>

        <div class="mb-4">
          <label class="block text-xs font-medium text-gray-700 mb-1.5">Nombre del flujo</label>
          <input
            v-model="nuevoNombre"
            type="text"
            placeholder="Ej: Bot Clinica Norte"
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 focus:border-transparent transition"
          />
        </div>

        <div class="mb-6">
          <label class="block text-xs font-medium text-gray-700 mb-1.5">Cliente</label>
          <input
            v-model="nuevoCliente"
            type="text"
            placeholder="Ej: Clinica Norte S.A."
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 focus:border-transparent transition"
          />
        </div>

        <div class="flex gap-3">
          <button
            @click="mostrarModal = false"
            class="flex-1 border border-gray-200 text-gray-600 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancelar
          </button>
          <button
            @click="crearFlujo"
            class="flex-1 bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
          >
            Crear y editar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const mostrarModal = ref(false)
const nuevoNombre = ref('')
const nuevoCliente = ref('')
const filtroActivo = ref('Todos')

const filtros = ['Todos', 'Activos', 'Borradores']

const flujos = ref([
  {
    id: 1,
    nombre: 'Bot Clinica Verde',
    cliente: 'Clinica Verde S.A.',
    estado: 'Activo',
    conversaciones: 423,
    modificado: 'Hace 2 horas',
  },
  {
    id: 2,
    nombre: 'Bot FitLife',
    cliente: 'FitLife Gym',
    estado: 'Activo',
    conversaciones: 312,
    modificado: 'Hace 1 dia',
  },
  {
    id: 3,
    nombre: 'Bot Consultorio Bienestar',
    cliente: 'Consultorio Bienestar',
    estado: 'Activo',
    conversaciones: 289,
    modificado: 'Hace 3 dias',
  },
  {
    id: 4,
    nombre: 'Bot Dental Sonrisa',
    cliente: 'Clinica Dental Sonrisa',
    estado: 'Borrador',
    conversaciones: 0,
    modificado: 'Hace 5 dias',
  },
])

const flujosFiltrados = computed(() => {
  if (filtroActivo.value === 'Todos') return flujos.value
  if (filtroActivo.value === 'Activos') return flujos.value.filter((f) => f.estado === 'Activo')
  return flujos.value.filter((f) => f.estado === 'Borrador')
})

function crearFlujo() {
  if (!nuevoNombre.value || !nuevoCliente.value) return
  flujos.value.push({
    id: Date.now(),
    nombre: nuevoNombre.value,
    cliente: nuevoCliente.value,
    estado: 'Borrador',
    conversaciones: 0,
    modificado: 'Ahora',
  })
  mostrarModal.value = false
  nuevoNombre.value = ''
  nuevoCliente.value = ''
  router.push('/admin/flujos/editor')
}
</script>
