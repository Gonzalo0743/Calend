<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
    <div
      class="w-full max-w-sm bg-white border border-gray-200 rounded-2xl overflow-hidden flex flex-col"
      style="height: 600px"
    >
      <!-- Header -->
      <div class="flex items-center gap-3 px-4 py-4 border-b border-gray-100 bg-white">
        <button
          @click="$router.push('/dashboard')"
          class="text-gray-400 hover:text-gray-600 transition mr-1"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M15 19l-7-7 7-7"
            />
          </svg>
        </button>
        <div
          class="w-9 h-9 rounded-full bg-emerald-400 flex items-center justify-center flex-shrink-0"
        >
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
            />
          </svg>
        </div>
        <div>
          <p class="text-sm font-medium text-gray-900">Calend Bot</p>
          <div class="flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <p class="text-xs text-gray-400">En linea</p>
          </div>
        </div>
      </div>

      <!-- Mensajes -->
      <div ref="messagesContainer" class="flex-1 overflow-y-auto px-4 py-4 flex flex-col gap-3">
        <div
          v-for="mensaje in mensajes"
          :key="mensaje.id"
          :class="mensaje.tipo === 'bot' ? 'flex gap-2 items-end' : 'flex justify-end'"
        >
          <div
            v-if="mensaje.tipo === 'bot'"
            class="w-6 h-6 rounded-full bg-emerald-400 flex-shrink-0"
          ></div>

          <div
            :class="
              mensaje.tipo === 'bot'
                ? 'bg-gray-100 text-gray-700 rounded-2xl rounded-bl-sm'
                : 'bg-emerald-400 text-white rounded-2xl rounded-br-sm'
            "
            class="text-sm px-4 py-2.5 max-w-xs"
          >
            {{ mensaje.texto }}
          </div>
        </div>

        <!-- Indicador de escritura -->
        <div v-if="escribiendo" class="flex gap-2 items-end">
          <div class="w-6 h-6 rounded-full bg-emerald-400 flex-shrink-0"></div>
          <div class="bg-gray-100 rounded-2xl rounded-bl-sm px-4 py-3 flex gap-1 items-center">
            <span
              class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce"
              style="animation-delay: 0ms"
            ></span>
            <span
              class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce"
              style="animation-delay: 150ms"
            ></span>
            <span
              class="w-1.5 h-1.5 rounded-full bg-gray-400 animate-bounce"
              style="animation-delay: 300ms"
            ></span>
          </div>
        </div>
      </div>

      <!-- Opciones rápidas -->
      <div v-if="opciones.length > 0" class="px-4 pb-3 flex flex-wrap gap-2">
        <button
          v-for="opcion in opciones"
          :key="opcion"
          @click="seleccionarOpcion(opcion)"
          class="text-xs border border-emerald-300 text-emerald-600 px-3 py-1.5 rounded-full hover:bg-emerald-50 transition-colors"
        >
          {{ opcion }}
        </button>
      </div>

      <!-- Input -->
      <div class="px-4 py-3 border-t border-gray-100 flex items-center gap-2">
        <input
          v-model="inputTexto"
          @keyup.enter="enviarMensaje"
          type="text"
          placeholder="Escribi tu mensaje..."
          class="flex-1 bg-gray-50 rounded-full px-4 py-2 text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
        />
        <button
          @click="enviarMensaje"
          class="w-9 h-9 rounded-full bg-emerald-400 hover:bg-emerald-500 flex items-center justify-center flex-shrink-0 transition-colors"
        >
          <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
            />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import api from '../../services/api'
import { useAuthStore } from '../../stores/auth'

const route = useRoute()
const authStore = useAuthStore()

const botId = ref(route.query.bot || authStore.user?.bot_id || null)

const botNombre = ref('Calend Bot')
const cargando = ref(true)

const mensajes = ref([])
const opciones = ref([])
const escribiendo = ref(false)
const inputTexto = ref('')
const messagesContainer = ref(null)

const nodos = ref([])
const edges = ref([])
const nodoActual = ref(null)

let nombreCliente = ''
let horaSeleccionada = ''

async function cargarBot() {
  if (!botId.value) {
    cargando.value = false
    return
  }
  try {
    const res = await api.get(`/bots/${botId.value}/`)
    botNombre.value = res.data.nombre
    if (res.data.flujo && res.data.flujo.nodes) {
      nodos.value = res.data.flujo.nodes
      edges.value = res.data.flujo.edges || []
    }
  } catch (err) {
    console.error('Error cargando bot:', err)
  } finally {
    cargando.value = false
  }
}

function obtenerNodoInicial() {
  const nodosConEntrada = new Set(edges.value.map((e) => e.target))
  return nodos.value.find((n) => !nodosConEntrada.has(n.id)) || nodos.value[0]
}

function obtenerSiguienteNodo(nodoId, handleId = null) {
  let edge
  if (handleId) {
    edge = edges.value.find((e) => e.source === nodoId && e.sourceHandle === handleId)
  } else {
    edge = edges.value.find((e) => e.source === nodoId)
  }
  if (!edge) return null
  return nodos.value.find((n) => n.id === edge.target) || null
}

async function scrollAbajo() {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

async function procesarNodo(nodo) {
  if (!nodo) return
  nodoActual.value = nodo
  escribiendo.value = true
  opciones.value = []
  await scrollAbajo()

  await new Promise((resolve) => setTimeout(resolve, 800))
  escribiendo.value = false

  if (nodo.type === 'mensaje') {
    mensajes.value.push({
      id: Date.now(),
      tipo: 'bot',
      texto: nodo.data.texto,
    })
    await scrollAbajo()
    const siguiente = obtenerSiguienteNodo(nodo.id)
    if (siguiente) await procesarNodo(siguiente)
  } else if (nodo.type === 'opciones') {
    opciones.value = nodo.data.opciones
    await scrollAbajo()
  } else if (nodo.type === 'esperar') {
    await new Promise((resolve) => setTimeout(resolve, 1500))
    const siguiente = obtenerSiguienteNodo(nodo.id)
    if (siguiente) await procesarNodo(siguiente)
  } else if (nodo.type === 'condicion') {
    const siguiente = obtenerSiguienteNodo(nodo.id)
    if (siguiente) await procesarNodo(siguiente)
  }
}

async function manejarRespuestaUsuario(texto) {
  if (!nodoActual.value) return

  // Guardar datos relevantes
  if (nodoActual.value.type === 'mensaje' && mensajes.value.length === 1) {
    nombreCliente = texto
  }

  const nodo = nodoActual.value

  if (nodo.type === 'opciones') {
    // Buscar si hay condicion conectada que coincida con la opcion elegida
    const siguiente = obtenerSiguienteNodo(nodo.id)
    if (!siguiente) return

    if (siguiente.type === 'condicion') {
      // Evaluar condiciones — buscar la que coincide con el texto
      const edgesDesdeOpciones = edges.value.filter((e) => e.source === nodo.id)
      let nodoDestino = null

      for (const edge of edgesDesdeOpciones) {
        const posibleCondicion = nodos.value.find((n) => n.id === edge.target)
        if (posibleCondicion && posibleCondicion.type === 'condicion') {
          const condicion = posibleCondicion.data.condicion || ''
          const partes = condicion.split('==').map((p) => p.trim())
          if (partes[1] && texto.toLowerCase().includes(partes[1].toLowerCase())) {
            nodoDestino = obtenerSiguienteNodo(posibleCondicion.id)
            break
          }
        }
      }

      if (nodoDestino) {
        await procesarNodo(nodoDestino)
      } else {
        await procesarNodo(siguiente)
      }
    } else {
      await procesarNodo(siguiente)
    }
  } else {
    // Para nodos mensaje, avanzar al siguiente
    const siguiente = obtenerSiguienteNodo(nodo.id)

    // Si el nodo actual es el último mensaje antes de terminar, guardar cita
    if (!siguiente) {
      try {
        await api.post('/citas/', {
          nombre: nombreCliente || texto,
          servicio: 'Consulta general',
          hora: horaSeleccionada || texto,
          estado: 'Confirmada',
        })
      } catch (err) {
        console.error('Error guardando cita:', err)
      }
      return
    }

    await procesarNodo(siguiente)
  }
}

async function enviarMensaje() {
  const texto = inputTexto.value.trim()
  if (!texto) return

  mensajes.value.push({
    id: Date.now(),
    tipo: 'usuario',
    texto,
  })

  inputTexto.value = ''
  await scrollAbajo()
  await manejarRespuestaUsuario(texto)
}

async function seleccionarOpcion(opcion) {
  mensajes.value.push({
    id: Date.now(),
    tipo: 'usuario',
    texto: opcion,
  })

  opciones.value = []
  await scrollAbajo()
  await manejarRespuestaUsuario(opcion)
}

onMounted(async () => {
  await cargarBot()
  if (nodos.value.length > 0) {
    const nodoInicial = obtenerNodoInicial()
    if (nodoInicial) await procesarNodo(nodoInicial)
  }
})
</script>
