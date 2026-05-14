<template>
  <AdminLayout>
    <!-- Header -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-lg font-medium text-gray-900">Contactos</h1>
        <p class="text-sm text-gray-400">Personas que han interactuado con tus chatbots</p>
      </div>
      <div class="flex items-center gap-3">
        <div class="flex items-center gap-2 bg-white border border-gray-200 rounded-lg px-3 py-2">
          <svg
            class="w-3.5 h-3.5 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
          <input
            v-model="busqueda"
            type="text"
            placeholder="Buscar contacto..."
            class="text-sm text-gray-700 placeholder-gray-400 focus:outline-none w-48"
          />
        </div>
        <select
          v-model="filtroCanal"
          class="text-sm border border-gray-200 rounded-lg px-3 py-2 text-gray-600 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition bg-white"
        >
          <option value="Todos">Todos los canales</option>
          <option value="Webchat">Webchat</option>
          <option value="WhatsApp">WhatsApp</option>
        </select>
      </div>
    </div>

    <!-- Metricas -->
    <div class="grid grid-cols-3 gap-4 mb-8">
      <div class="bg-white border border-gray-100 rounded-2xl p-5">
        <p class="text-xs text-gray-400 mb-1">Total contactos</p>
        <p class="text-2xl font-medium text-gray-900">248</p>
        <p class="text-xs text-emerald-500 mt-1">+12 esta semana</p>
      </div>
      <div class="bg-white border border-gray-100 rounded-2xl p-5">
        <p class="text-xs text-gray-400 mb-1">Nuevos este mes</p>
        <p class="text-2xl font-medium text-gray-900">43</p>
        <p class="text-xs text-emerald-500 mt-1">+8% vs mes anterior</p>
      </div>
      <div class="bg-white border border-gray-100 rounded-2xl p-5">
        <p class="text-xs text-gray-400 mb-1">Con cita agendada</p>
        <p class="text-2xl font-medium text-gray-900">189</p>
        <p class="text-xs text-gray-400 mt-1">76% del total</p>
      </div>
    </div>

    <!-- Tabla -->
    <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
      <table class="w-full">
        <thead>
          <tr class="border-b border-gray-100">
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Contacto</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Canal</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Bot</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">
              Ultima interaccion
            </th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Citas</th>
            <th class="text-left text-xs font-medium text-gray-400 px-6 py-4">Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="contacto in contactosFiltrados"
            :key="contacto.id"
            class="border-b border-gray-50 last:border-0 hover:bg-gray-50 transition-colors cursor-pointer"
          >
            <td class="px-6 py-4">
              <div class="flex items-center gap-3">
                <div
                  class="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-xs font-medium text-emerald-700 flex-shrink-0"
                >
                  {{ contacto.iniciales }}
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ contacto.nombre }}</p>
                  <p class="text-xs text-gray-400">{{ contacto.telefono }}</p>
                </div>
              </div>
            </td>
            <td class="px-6 py-4">
              <span
                :class="
                  contacto.canal === 'WhatsApp'
                    ? 'bg-green-50 text-green-700'
                    : 'bg-emerald-50 text-emerald-700'
                "
                class="text-xs px-2.5 py-1 rounded-full font-medium"
              >
                {{ contacto.canal }}
              </span>
            </td>
            <td class="px-6 py-4 text-sm text-gray-500">{{ contacto.bot }}</td>
            <td class="px-6 py-4 text-sm text-gray-400">{{ contacto.ultimaInteraccion }}</td>
            <td class="px-6 py-4 text-sm text-gray-900 font-medium">{{ contacto.citas }}</td>
            <td class="px-6 py-4">
              <span
                :class="
                  contacto.estado === 'Activo'
                    ? 'bg-emerald-50 text-emerald-700'
                    : 'bg-gray-100 text-gray-500'
                "
                class="text-xs px-2.5 py-1 rounded-full font-medium"
              >
                {{ contacto.estado }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Paginacion -->
      <div class="flex items-center justify-between px-6 py-4 border-t border-gray-100">
        <p class="text-xs text-gray-400">
          Mostrando {{ contactosFiltrados.length }} de 248 contactos
        </p>
        <div class="flex items-center gap-2">
          <button
            class="text-xs border border-gray-200 text-gray-500 px-3 py-1.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Anterior
          </button>
          <button class="text-xs bg-emerald-400 text-white px-3 py-1.5 rounded-lg">1</button>
          <button
            class="text-xs border border-gray-200 text-gray-500 px-3 py-1.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            2
          </button>
          <button
            class="text-xs border border-gray-200 text-gray-500 px-3 py-1.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            3
          </button>
          <button
            class="text-xs border border-gray-200 text-gray-500 px-3 py-1.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Siguiente
          </button>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref, computed } from 'vue'
import AdminLayout from '@/components/AdminLayout.vue'

const busqueda = ref('')
const filtroCanal = ref('Todos')

const contactos = ref([
  {
    id: 1,
    nombre: 'Maria Rodriguez',
    iniciales: 'MR',
    telefono: '+506 8812 3456',
    canal: 'Webchat',
    bot: 'Bot Clinica Verde',
    ultimaInteraccion: 'Hace 2 horas',
    citas: 3,
    estado: 'Activo',
  },
  {
    id: 2,
    nombre: 'Carlos Mora',
    iniciales: 'CM',
    telefono: '+506 7723 4567',
    canal: 'WhatsApp',
    bot: 'Bot FitLife',
    ultimaInteraccion: 'Hace 5 horas',
    citas: 1,
    estado: 'Activo',
  },
  {
    id: 3,
    nombre: 'Laura Jimenez',
    iniciales: 'LJ',
    telefono: '+506 8834 5678',
    canal: 'Webchat',
    bot: 'Bot Clinica Verde',
    ultimaInteraccion: 'Ayer',
    citas: 2,
    estado: 'Activo',
  },
  {
    id: 4,
    nombre: 'Andres Vargas',
    iniciales: 'AV',
    telefono: '+506 6645 6789',
    canal: 'WhatsApp',
    bot: 'Bot Dental Sonrisa',
    ultimaInteraccion: 'Hace 2 dias',
    citas: 1,
    estado: 'Inactivo',
  },
  {
    id: 5,
    nombre: 'Sofia Castro',
    iniciales: 'SC',
    telefono: '+506 8856 7890',
    canal: 'Webchat',
    bot: 'Bot Consultorio Bienestar',
    ultimaInteraccion: 'Hace 3 dias',
    citas: 4,
    estado: 'Activo',
  },
  {
    id: 6,
    nombre: 'Diego Herrera',
    iniciales: 'DH',
    telefono: '+506 7767 8901',
    canal: 'WhatsApp',
    bot: 'Bot FitLife',
    ultimaInteraccion: 'Hace 4 dias',
    citas: 1,
    estado: 'Inactivo',
  },
  {
    id: 7,
    nombre: 'Ana Mora',
    iniciales: 'AM',
    telefono: '+506 8878 9012',
    canal: 'Webchat',
    bot: 'Bot Clinica Verde',
    ultimaInteraccion: 'Hace 5 dias',
    citas: 2,
    estado: 'Activo',
  },
])

const contactosFiltrados = computed(() => {
  return contactos.value.filter((c) => {
    const coincideBusqueda = c.nombre.toLowerCase().includes(busqueda.value.toLowerCase())
    const coincideCanal = filtroCanal.value === 'Todos' || c.canal === filtroCanal.value
    return coincideBusqueda && coincideCanal
  })
})
</script>
