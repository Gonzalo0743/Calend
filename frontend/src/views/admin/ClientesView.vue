<template>
  <AdminLayout>
    <!-- Header -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-lg font-medium text-gray-900">Clientes</h1>
        <p class="text-sm text-gray-400">Administra los usuarios clientes y sus bots asignados</p>
      </div>
      <button
        @click="mostrarModal = true"
        class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
      >
        + Nuevo cliente
      </button>
    </div>

    <!-- Tabla -->
    <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="border-b border-gray-100">
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Cliente</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Email</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Bot asignado</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Estado</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="clientes.length === 0">
            <td colspan="5" class="text-center text-sm text-gray-400 px-6 py-8">
              No hay clientes registrados todavia
            </td>
          </tr>
          <tr
            v-for="cliente in clientes"
            :key="cliente.id"
            class="border-b border-gray-50 last:border-0 hover:bg-gray-50 transition-colors"
          >
            <td class="px-6 py-4">
              <div class="flex items-center gap-3">
                <div
                  class="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-xs font-medium text-emerald-700"
                >
                  {{ cliente.username[0].toUpperCase() }}
                </div>
                <p class="text-sm font-medium text-gray-900">{{ cliente.username }}</p>
              </div>
            </td>
            <td class="px-6 py-4 text-sm text-gray-500">{{ cliente.email }}</td>
            <td class="px-6 py-4">
              <span v-if="cliente.bot_nombre" class="text-sm text-gray-700">{{
                cliente.bot_nombre
              }}</span>
              <span v-else class="text-sm text-gray-400">Sin bot asignado</span>
            </td>
            <td class="px-6 py-4">
              <span
                :class="
                  cliente.tiene_bot ? 'bg-emerald-50 text-emerald-700' : 'bg-gray-100 text-gray-500'
                "
                class="text-xs px-2.5 py-1 rounded-full font-medium"
              >
                {{ cliente.tiene_bot ? 'Activo' : 'Pendiente' }}
              </span>
            </td>
            <td class="px-6 py-4">
              <button
                @click="abrirAsignar(cliente)"
                class="text-xs text-emerald-600 hover:text-emerald-700 font-medium transition-colors"
              >
                Asignar bot
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal nuevo cliente -->
    <div
      v-if="mostrarModal"
      class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 w-full max-w-md shadow-lg">
        <h2 class="text-base font-medium text-gray-900 mb-1">Nuevo cliente</h2>
        <p class="text-sm text-gray-400 mb-6">Crea las credenciales para el cliente</p>

        <div class="flex flex-col gap-4 mb-6">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Usuario</label>
            <input
              v-model="nuevoCliente.username"
              type="text"
              placeholder="Ej: clinicaverde"
              class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
            />
          </div>
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Email</label>
            <input
              v-model="nuevoCliente.email"
              type="email"
              placeholder="Ej: contacto@clinicaverde.com"
              class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
            />
          </div>
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Contrasena</label>
            <input
              v-model="nuevoCliente.password"
              type="password"
              placeholder="••••••••"
              class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
            />
          </div>
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Bot a asignar</label>
            <select
              v-model="nuevoCliente.bot_id"
              class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-300 transition bg-white"
            >
              <option :value="null">Sin bot por ahora</option>
              <option v-for="bot in bots" :key="bot.id" :value="bot.id">{{ bot.nombre }}</option>
            </select>
          </div>
        </div>

        <p v-if="errorModal" class="text-xs text-red-500 mb-4">{{ errorModal }}</p>

        <div class="flex gap-3">
          <button
            @click="cerrarModal"
            class="flex-1 border border-gray-200 text-gray-600 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancelar
          </button>
          <button
            @click="crearCliente"
            class="flex-1 bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
          >
            Crear cliente
          </button>
        </div>
      </div>
    </div>

    <!-- Modal asignar bot -->
    <div
      v-if="mostrarModalAsignar"
      class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 w-full max-w-md shadow-lg">
        <h2 class="text-base font-medium text-gray-900 mb-1">Asignar bot</h2>
        <p class="text-sm text-gray-400 mb-6">
          Selecciona el bot para
          <strong class="text-gray-700">{{ clienteSeleccionado?.username }}</strong>
        </p>

        <div class="mb-6">
          <label class="block text-xs font-medium text-gray-700 mb-1.5">Bot</label>
          <select
            v-model="botAsignar"
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-300 transition bg-white"
          >
            <option :value="null">Sin bot</option>
            <option v-for="bot in bots" :key="bot.id" :value="bot.id">{{ bot.nombre }}</option>
          </select>
        </div>

        <div class="flex gap-3">
          <button
            @click="mostrarModalAsignar = false"
            class="flex-1 border border-gray-200 text-gray-600 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancelar
          </button>
          <button
            @click="asignarBot"
            class="flex-1 bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
          >
            Guardar
          </button>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import AdminLayout from '@/components/AdminLayout.vue'
import api from '@/services/api'

const clientes = ref([])
const bots = ref([])
const mostrarModal = ref(false)
const mostrarModalAsignar = ref(false)
const clienteSeleccionado = ref(null)
const botAsignar = ref(null)
const errorModal = ref('')

const nuevoCliente = ref({
  username: '',
  email: '',
  password: '',
  bot_id: null,
})

async function cargarDatos() {
  try {
    const [clientesRes, botsRes] = await Promise.all([api.get('/clientes/'), api.get('/bots/')])
    clientes.value = clientesRes.data
    bots.value = botsRes.data
  } catch (err) {
    console.error('Error cargando datos:', err)
  }
}

async function crearCliente() {
  errorModal.value = ''
  if (!nuevoCliente.value.username || !nuevoCliente.value.email || !nuevoCliente.value.password) {
    errorModal.value = 'Por favor completa todos los campos obligatorios.'
    return
  }
  try {
    await api.post('/clientes/crear/', nuevoCliente.value)
    await cargarDatos()
    cerrarModal()
  } catch (err) {
    errorModal.value = err.response?.data?.error || 'Error creando cliente'
  }
}

function cerrarModal() {
  mostrarModal.value = false
  nuevoCliente.value = { username: '', email: '', password: '', bot_id: null }
  errorModal.value = ''
}

function abrirAsignar(cliente) {
  clienteSeleccionado.value = cliente
  botAsignar.value = cliente.bot_id
  mostrarModalAsignar.value = true
}

async function asignarBot() {
  if (!clienteSeleccionado.value) return
  try {
    await api.post('/clientes/asignar-bot/', {
      user_id: clienteSeleccionado.value.id,
      bot_id: botAsignar.value,
    })
    await cargarDatos()
    mostrarModalAsignar.value = false
  } catch (err) {
    console.error('Error asignando bot:', err)
  }
}

onMounted(() => {
  cargarDatos()
})
</script>
