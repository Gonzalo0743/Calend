<template>
  <div class="h-screen flex flex-col bg-gray-50">
    <!-- Topbar -->
    <div
      class="bg-white border-b border-gray-100 px-6 py-3 flex items-center justify-between flex-shrink-0"
    >
      <div class="flex items-center gap-4">
        <button
          @click="$router.push('/admin/flujos')"
          class="text-gray-400 hover:text-gray-600 transition"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>
        <div>
          <h1 class="text-sm font-medium text-gray-900">Bot Clinica Verde</h1>
          <p class="text-xs text-gray-400">Editor de flujo</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <button
          class="text-xs border border-gray-200 text-gray-600 px-4 py-2 rounded-lg hover:bg-gray-50 transition-colors"
        >
          Vista previa
        </button>
        <button
          class="text-xs bg-emerald-400 hover:bg-emerald-500 text-white px-4 py-2 rounded-lg transition-colors font-medium"
        >
          Guardar
        </button>
      </div>
    </div>

    <div class="flex flex-1 overflow-hidden">
      <!-- Panel izquierdo — bloques disponibles -->
      <aside
        class="w-56 bg-white border-r border-gray-100 flex flex-col px-4 py-5 flex-shrink-0 overflow-y-auto"
      >
        <p class="text-xs font-medium text-gray-400 uppercase tracking-wider mb-4">Bloques</p>
        <div class="flex flex-col gap-2">
          <div
            v-for="bloque in bloquesDisponibles"
            :key="bloque.tipo"
            draggable="true"
            @dragstart="onDragStart($event, bloque.tipo)"
            class="flex items-center gap-3 px-3 py-2.5 bg-gray-50 hover:bg-emerald-50 border border-gray-100 hover:border-emerald-200 rounded-xl cursor-grab transition-colors"
          >
            <div
              :class="bloque.color"
              class="w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0"
            >
              <svg
                class="w-3.5 h-3.5 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  :d="bloque.icono"
                />
              </svg>
            </div>
            <div>
              <p class="text-xs font-medium text-gray-900">{{ bloque.label }}</p>
              <p class="text-xs text-gray-400">{{ bloque.descripcion }}</p>
            </div>
          </div>
        </div>
      </aside>

      <!-- Canvas Vue Flow -->
      <div class="flex-1 relative" @drop="onDrop" @dragover.prevent>
        <VueFlow
          v-model:nodes="nodes"
          v-model:edges="edges"
          :default-viewport="{ zoom: 1 }"
          class="bg-gray-50"
          @node-click="onNodeClick"
        >
          <Background pattern-color="#e5e7eb" :gap="20" />
          <Controls />
          <MiniMap />

          <template #node-mensaje="{ data }">
            <div
              class="bg-white border-2 border-emerald-300 rounded-2xl px-4 py-3 min-w-48 shadow-sm"
            >
              <div class="flex items-center gap-2 mb-2">
                <div class="w-5 h-5 rounded-md bg-emerald-400 flex items-center justify-center">
                  <svg
                    class="w-3 h-3 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
                    />
                  </svg>
                </div>
                <span class="text-xs font-medium text-gray-700">Mensaje</span>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">{{ data.texto }}</p>
              <Handle type="target" :position="Position.Top" />
              <Handle type="source" :position="Position.Bottom" />
            </div>
          </template>

          <template #node-opciones="{ data }">
            <div class="bg-white border-2 border-blue-300 rounded-2xl px-4 py-3 min-w-48 shadow-sm">
              <div class="flex items-center gap-2 mb-2">
                <div class="w-5 h-5 rounded-md bg-blue-400 flex items-center justify-center">
                  <svg
                    class="w-3 h-3 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M4 6h16M4 10h16M4 14h16M4 18h16"
                    />
                  </svg>
                </div>
                <span class="text-xs font-medium text-gray-700">Opciones</span>
              </div>
              <div class="flex flex-col gap-1">
                <div
                  v-for="op in data.opciones"
                  :key="op"
                  class="text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-md"
                >
                  {{ op }}
                </div>
              </div>
              <Handle type="target" :position="Position.Top" />
              <Handle type="source" :position="Position.Bottom" />
            </div>
          </template>

          <template #node-condicion="{ data }">
            <div
              class="bg-white border-2 border-amber-300 rounded-2xl px-4 py-3 min-w-48 shadow-sm"
            >
              <div class="flex items-center gap-2 mb-2">
                <div class="w-5 h-5 rounded-md bg-amber-400 flex items-center justify-center">
                  <svg
                    class="w-3 h-3 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                </div>
                <span class="text-xs font-medium text-gray-700">Condicion</span>
              </div>
              <p class="text-xs text-gray-500">{{ data.condicion }}</p>
              <Handle type="target" :position="Position.Top" />
              <Handle type="source" :position="Position.Bottom" id="si" />
              <Handle type="source" :position="Position.Right" id="no" />
            </div>
          </template>

          <template #node-esperar="{ data }">
            <div
              class="bg-white border-2 border-purple-300 rounded-2xl px-4 py-3 min-w-48 shadow-sm"
            >
              <div class="flex items-center gap-2 mb-2">
                <div class="w-5 h-5 rounded-md bg-purple-400 flex items-center justify-center">
                  <svg
                    class="w-3 h-3 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                </div>
                <span class="text-xs font-medium text-gray-700">Esperar</span>
              </div>
              <p class="text-xs text-gray-500">{{ data.tiempo }}</p>
              <Handle type="target" :position="Position.Top" />
              <Handle type="source" :position="Position.Bottom" />
            </div>
          </template>
        </VueFlow>
      </div>

      <!-- Panel derecho — propiedades -->
      <aside
        v-if="nodoSeleccionado"
        class="w-64 bg-white border-l border-gray-100 flex flex-col px-5 py-5 flex-shrink-0"
      >
        <div class="flex items-center justify-between mb-5">
          <p class="text-xs font-medium text-gray-900 uppercase tracking-wider">Propiedades</p>
          <button
            @click="nodoSeleccionado = null"
            class="text-gray-400 hover:text-gray-600 transition"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <div v-if="nodoSeleccionado.type === 'mensaje'" class="flex flex-col gap-4">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Texto del mensaje</label>
            <textarea
              v-model="nodoSeleccionado.data.texto"
              rows="4"
              class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition resize-none"
              placeholder="Escribe el mensaje..."
            />
          </div>
          <button
            @click="eliminarNodo"
            class="text-xs text-red-500 hover:text-red-600 transition text-left"
          >
            Eliminar bloque
          </button>
        </div>

        <div v-if="nodoSeleccionado.type === 'opciones'" class="flex flex-col gap-4">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-2">Opciones</label>
            <div class="flex flex-col gap-2 mb-3">
              <div
                v-for="(op, i) in nodoSeleccionado.data.opciones"
                :key="i"
                class="flex items-center gap-2"
              >
                <input
                  v-model="nodoSeleccionado.data.opciones[i]"
                  type="text"
                  class="flex-1 border border-gray-200 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
                />
                <button
                  @click="nodoSeleccionado.data.opciones.splice(i, 1)"
                  class="text-gray-400 hover:text-red-500 transition"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
            </div>
            <button
              @click="nodoSeleccionado.data.opciones.push('Nueva opcion')"
              class="text-xs text-emerald-600 hover:text-emerald-700 transition font-medium"
            >
              + Agregar opcion
            </button>
          </div>
          <button
            @click="eliminarNodo"
            class="text-xs text-red-500 hover:text-red-600 transition text-left"
          >
            Eliminar bloque
          </button>
        </div>

        <div v-if="nodoSeleccionado.type === 'condicion'" class="flex flex-col gap-4">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Condicion</label>
            <input
              v-model="nodoSeleccionado.data.condicion"
              type="text"
              class="w-full border border-gray-200 rounded-lg px-3 py-2 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              placeholder="Ej: respuesta == si"
            />
          </div>
          <button
            @click="eliminarNodo"
            class="text-xs text-red-500 hover:text-red-600 transition text-left"
          >
            Eliminar bloque
          </button>
        </div>

        <div v-if="nodoSeleccionado.type === 'esperar'" class="flex flex-col gap-4">
          <div>
            <label class="block text-xs font-medium text-gray-700 mb-1.5">Tiempo de espera</label>
            <input
              v-model="nodoSeleccionado.data.tiempo"
              type="text"
              class="w-full border border-gray-200 rounded-lg px-3 py-2 text-xs focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              placeholder="Ej: 2 segundos"
            />
          </div>
          <button
            @click="eliminarNodo"
            class="text-xs text-red-500 hover:text-red-600 transition text-left"
          >
            Eliminar bloque
          </button>
        </div>
      </aside>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { VueFlow, useVueFlow } from '@vue-flow/core'
import { Background } from '@vue-flow/background'
import { Controls } from '@vue-flow/controls'
import { MiniMap } from '@vue-flow/minimap'
import { Position, Handle } from '@vue-flow/core'
import '@vue-flow/core/dist/style.css'
import '@vue-flow/core/dist/theme-default.css'

const { addNodes } = useVueFlow()

const nodoSeleccionado = ref(null)

const nodes = ref([
  {
    id: '1',
    type: 'mensaje',
    position: { x: 250, y: 80 },
    data: { texto: 'Hola, bienvenido. Como te llamas?' },
  },
  {
    id: '2',
    type: 'opciones',
    position: { x: 200, y: 260 },
    data: { opciones: ['Agendar cita', 'Ver mis citas', 'Cancelar cita'] },
  },
  {
    id: '3',
    type: 'condicion',
    position: { x: 220, y: 460 },
    data: { condicion: 'opcion == Agendar cita' },
  },
])

const edges = ref([
  { id: 'e1-2', source: '1', target: '2', animated: true, style: { stroke: '#34d399' } },
  { id: 'e2-3', source: '2', target: '3', animated: true, style: { stroke: '#34d399' } },
])

const bloquesDisponibles = [
  {
    tipo: 'mensaje',
    label: 'Mensaje',
    descripcion: 'Envia un texto',
    color: 'bg-emerald-400',
    icono:
      'M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z',
  },
  {
    tipo: 'opciones',
    label: 'Opciones',
    descripcion: 'Muestra opciones',
    color: 'bg-blue-400',
    icono: 'M4 6h16M4 10h16M4 14h16M4 18h16',
  },
  {
    tipo: 'condicion',
    label: 'Condicion',
    descripcion: 'Bifurca el flujo',
    color: 'bg-amber-400',
    icono:
      'M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
  },
  {
    tipo: 'esperar',
    label: 'Esperar',
    descripcion: 'Pausa el flujo',
    color: 'bg-purple-400',
    icono: 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
  },
]

let idContador = 4

function onDragStart(event, tipo) {
  event.dataTransfer.setData('tipo', tipo)
}

function onDrop(event) {
  const tipo = event.dataTransfer.getData('tipo')
  const bounds = event.currentTarget.getBoundingClientRect()

  const position = {
    x: event.clientX - bounds.left - 96,
    y: event.clientY - bounds.top - 40,
  }

  const defaults = {
    mensaje: { texto: 'Escribe tu mensaje aqui...' },
    opciones: { opciones: ['Opcion 1', 'Opcion 2'] },
    condicion: { condicion: 'respuesta == si' },
    esperar: { tiempo: '2 segundos' },
  }

  addNodes([
    {
      id: String(idContador++),
      type: tipo,
      position,
      data: defaults[tipo],
    },
  ])
}

function onNodeClick({ node }) {
  nodoSeleccionado.value = node
}

function eliminarNodo() {
  nodes.value = nodes.value.filter((n) => n.id !== nodoSeleccionado.value.id)
  edges.value = edges.value.filter(
    (e) => e.source !== nodoSeleccionado.value.id && e.target !== nodoSeleccionado.value.id,
  )
  nodoSeleccionado.value = null
}
</script>
