<template>
  <AdminLayout>
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
  </AdminLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import AdminLayout from '@/components/AdminLayout.vue'

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
