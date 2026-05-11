<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center px-4">
    <div
      class="w-full max-w-sm bg-white border border-gray-200 rounded-2xl overflow-hidden flex flex-col"
      style="height: 600px"
    >
      <!-- Header -->
      <div class="flex items-center gap-3 px-4 py-4 border-b border-gray-100 bg-white">
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
import { ref, nextTick } from 'vue'

const messagesContainer = ref(null)
const inputTexto = ref('')
const escribiendo = ref(false)
const opciones = ref([])
const paso = ref(0)

const mensajes = ref([
  {
    id: 1,
    tipo: 'bot',
    texto: 'Hola, bienvenido a Clinica Verde. Soy tu asistente virtual. Como te llamas?',
  },
])

let nombreCliente = ''
let diaSeleccionado = ''

const flujo = [
  {
    opciones: [],
    respuesta: (texto) => {
      nombreCliente = texto
      return `Mucho gusto, ${nombreCliente}. En que te puedo ayudar hoy?`
    },
    siguientesOpciones: ['Agendar una cita', 'Ver mis citas', 'Cancelar una cita'],
  },
  {
    opciones: ['Agendar una cita', 'Ver mis citas', 'Cancelar una cita'],
    respuesta: () => 'Perfecto. Para que dia queres agendar tu cita?',
    siguientesOpciones: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
  },
  {
    opciones: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
    respuesta: (texto) => {
      diaSeleccionado = texto
      return `Tengo estos horarios disponibles para el ${diaSeleccionado}:`
    },
    siguientesOpciones: ['9:00 am', '11:00 am', '2:00 pm', '4:00 pm'],
  },
  {
    opciones: ['9:00 am', '11:00 am', '2:00 pm', '4:00 pm'],
    respuesta: (texto) =>
      `Listo! Tu cita quedo agendada para el ${diaSeleccionado} a las ${texto}. Te esperamos, ${nombreCliente}.`,
    siguientesOpciones: [],
  },
]

async function scrollAbajo() {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

async function responderBot(texto) {
  escribiendo.value = true
  opciones.value = []
  await scrollAbajo()

  await new Promise((resolve) => setTimeout(resolve, 1000))

  const etapa = flujo[paso.value]
  const respuesta = etapa.respuesta(texto)

  mensajes.value.push({
    id: Date.now(),
    tipo: 'bot',
    texto: respuesta,
  })

  escribiendo.value = false
  paso.value++

  if (paso.value < flujo.length) {
    opciones.value = flujo[paso.value].opciones
  }

  await scrollAbajo()
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
  await responderBot(texto)
}

async function seleccionarOpcion(opcion) {
  mensajes.value.push({
    id: Date.now(),
    tipo: 'usuario',
    texto: opcion,
  })

  await scrollAbajo()
  await responderBot(opcion)
}
</script>
