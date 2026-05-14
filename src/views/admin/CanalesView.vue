<template>
  <AdminLayout>
    <!-- Header -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-lg font-medium text-gray-900">Canales</h1>
        <p class="text-sm text-gray-400">Conecta y administra los canales de tus chatbots</p>
      </div>
      <button
        @click="mostrarModal = true"
        class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors"
      >
        + Conectar canal
      </button>
    </div>

    <!-- Canales conectados -->
    <div class="mb-8">
      <p class="text-xs font-medium text-gray-400 uppercase tracking-wider mb-4">Conectados</p>
      <div class="grid grid-cols-3 gap-4">
        <div
          v-for="canal in canalesConectados"
          :key="canal.id"
          class="bg-white border border-gray-100 rounded-2xl p-5"
        >
          <div class="flex items-start justify-between mb-4">
            <div class="flex items-center gap-3">
              <div
                :class="canal.color"
                class="w-10 h-10 rounded-xl flex items-center justify-center"
              >
                <svg
                  class="w-5 h-5 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="1.5"
                    :d="canal.icono"
                  />
                </svg>
              </div>
              <div>
                <p class="text-sm font-medium text-gray-900">{{ canal.nombre }}</p>
                <p class="text-xs text-gray-400">{{ canal.descripcion }}</p>
              </div>
            </div>
            <span
              class="text-xs bg-emerald-50 text-emerald-700 px-2 py-1 rounded-full font-medium flex-shrink-0"
            >
              Activo
            </span>
          </div>
          <div class="grid grid-cols-2 gap-3 mb-4">
            <div class="bg-gray-50 rounded-xl p-3">
              <p class="text-xs text-gray-400 mb-1">Conversaciones</p>
              <p class="text-sm font-medium text-gray-900">{{ canal.conversaciones }}</p>
            </div>
            <div class="bg-gray-50 rounded-xl p-3">
              <p class="text-xs text-gray-400 mb-1">Bots activos</p>
              <p class="text-sm font-medium text-gray-900">{{ canal.bots }}</p>
            </div>
          </div>
          <div class="flex gap-2">
            <button
              class="flex-1 text-xs border border-gray-200 text-gray-600 py-2 rounded-lg hover:bg-gray-50 transition-colors"
            >
              Configurar
            </button>
            <button
              class="text-xs border border-red-100 text-red-500 px-3 py-2 rounded-lg hover:bg-red-50 transition-colors"
            >
              Desconectar
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Canales disponibles -->
    <div>
      <p class="text-xs font-medium text-gray-400 uppercase tracking-wider mb-4">Disponibles</p>
      <div class="grid grid-cols-3 gap-4">
        <div
          v-for="canal in canalesDisponibles"
          :key="canal.id"
          class="bg-white border border-gray-100 rounded-2xl p-5 opacity-70"
        >
          <div class="flex items-center gap-3 mb-4">
            <div :class="canal.color" class="w-10 h-10 rounded-xl flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.5"
                  :d="canal.icono"
                />
              </svg>
            </div>
            <div>
              <p class="text-sm font-medium text-gray-900">{{ canal.nombre }}</p>
              <p class="text-xs text-gray-400">{{ canal.descripcion }}</p>
            </div>
          </div>
          <button
            @click="mostrarModal = true"
            class="w-full text-xs bg-gray-50 hover:bg-emerald-50 border border-gray-200 hover:border-emerald-200 text-gray-600 hover:text-emerald-700 py-2 rounded-lg transition-colors font-medium"
          >
            Conectar
          </button>
        </div>
      </div>
    </div>

    <!-- Modal conectar canal -->
    <div
      v-if="mostrarModal"
      class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50"
    >
      <div class="bg-white rounded-2xl p-8 w-full max-w-md shadow-lg">
        <h2 class="text-base font-medium text-gray-900 mb-1">Conectar canal</h2>
        <p class="text-sm text-gray-400 mb-6">Ingresa las credenciales del canal</p>

        <div class="mb-4">
          <label class="block text-xs font-medium text-gray-700 mb-1.5">Token de acceso</label>
          <input
            type="text"
            placeholder="Ej: EAABsbCS..."
            class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 focus:border-transparent transition"
          />
        </div>

        <div class="mb-6">
          <label class="block text-xs font-medium text-gray-700 mb-1.5">Webhook URL</label>
          <div class="flex items-center gap-2">
            <input
              type="text"
              value="https://calend.io/webhook/abc123"
              readonly
              class="flex-1 border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-400 bg-gray-50 focus:outline-none"
            />
            <button
              class="text-xs border border-gray-200 text-gray-600 px-3 py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
            >
              Copiar
            </button>
          </div>
          <p class="text-xs text-gray-400 mt-1.5">Pega esta URL en la configuracion de tu canal</p>
        </div>

        <div class="flex gap-3">
          <button
            @click="mostrarModal = false"
            class="flex-1 border border-gray-200 text-gray-600 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cancelar
          </button>
          <button
            @click="mostrarModal = false"
            class="flex-1 bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
          >
            Conectar
          </button>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue'
import AdminLayout from '@/components/AdminLayout.vue'

const mostrarModal = ref(false)

const canalesConectados = ref([
  {
    id: 1,
    nombre: 'Webchat',
    descripcion: 'Chat embebido en sitio web',
    color: 'bg-emerald-400',
    icono:
      'M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9',
    conversaciones: 842,
    bots: 4,
  },
  {
    id: 2,
    nombre: 'WhatsApp',
    descripcion: 'WhatsApp Business API',
    color: 'bg-green-500',
    icono:
      'M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z',
    conversaciones: 406,
    bots: 2,
  },
])

const canalesDisponibles = ref([
  {
    id: 3,
    nombre: 'Instagram',
    descripcion: 'Mensajes directos',
    color: 'bg-pink-500',
    icono:
      'M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z',
  },
  {
    id: 4,
    nombre: 'Facebook',
    descripcion: 'Messenger',
    color: 'bg-blue-500',
    icono:
      'M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z',
  },
  {
    id: 5,
    nombre: 'Telegram',
    descripcion: 'Bot de Telegram',
    color: 'bg-sky-500',
    icono: 'M12 19l9 2-9-18-9 18 9-2zm0 0v-8',
  },
])
</script>
