<template>
  <AdminLayout>
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-lg font-medium text-gray-900">Configuracion</h1>
      <p class="text-sm text-gray-400">Ajustes generales de tu cuenta y plataforma</p>
    </div>

    <div class="grid grid-cols-3 gap-8">
      <!-- Menu lateral -->
      <div class="col-span-1">
        <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
          <button
            v-for="seccion in secciones"
            :key="seccion.id"
            @click="seccionActiva = seccion.id"
            :class="
              seccionActiva === seccion.id
                ? 'bg-emerald-50 text-emerald-700 border-l-2 border-emerald-400'
                : 'text-gray-500 hover:bg-gray-50'
            "
            class="w-full flex items-center gap-3 px-5 py-3.5 text-sm transition-colors text-left"
          >
            <svg
              class="w-4 h-4 flex-shrink-0"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                :d="seccion.icono"
              />
            </svg>
            {{ seccion.label }}
          </button>
        </div>
      </div>

      <!-- Contenido -->
      <div class="col-span-2">
        <!-- Perfil -->
        <div
          v-if="seccionActiva === 'perfil'"
          class="bg-white border border-gray-100 rounded-2xl p-6"
        >
          <h2 class="text-sm font-medium text-gray-900 mb-6">Informacion del perfil</h2>

          <div class="flex items-center gap-5 mb-6 pb-6 border-b border-gray-100">
            <div
              class="w-16 h-16 rounded-full bg-emerald-100 flex items-center justify-center text-xl font-medium text-emerald-700"
            >
              GA
            </div>
            <div>
              <p class="text-sm font-medium text-gray-900 mb-1">Gonzalo Acuna</p>
              <button
                class="text-xs text-emerald-600 hover:text-emerald-700 transition font-medium"
              >
                Cambiar foto
              </button>
            </div>
          </div>

          <div class="flex flex-col gap-4">
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-medium text-gray-700 mb-1.5">Nombre</label>
                <input
                  v-model="perfil.nombre"
                  type="text"
                  class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
                />
              </div>
              <div>
                <label class="block text-xs font-medium text-gray-700 mb-1.5">Apellido</label>
                <input
                  v-model="perfil.apellido"
                  type="text"
                  class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
                />
              </div>
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5"
                >Correo electronico</label
              >
              <input
                v-model="perfil.correo"
                type="email"
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              />
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5">Rol</label>
              <input
                value="Desarrollador"
                type="text"
                readonly
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-400 bg-gray-50 focus:outline-none"
              />
            </div>
            <div class="flex justify-end pt-2">
              <button
                class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-5 py-2.5 rounded-lg transition-colors"
              >
                Guardar cambios
              </button>
            </div>
          </div>
        </div>

        <!-- Seguridad -->
        <div
          v-if="seccionActiva === 'seguridad'"
          class="bg-white border border-gray-100 rounded-2xl p-6"
        >
          <h2 class="text-sm font-medium text-gray-900 mb-6">Seguridad</h2>

          <div class="flex flex-col gap-4">
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5"
                >Contrasena actual</label
              >
              <input
                type="password"
                placeholder="••••••••"
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              />
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5">Nueva contrasena</label>
              <input
                type="password"
                placeholder="••••••••"
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              />
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5"
                >Confirmar contrasena</label
              >
              <input
                type="password"
                placeholder="••••••••"
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              />
            </div>
            <div class="flex justify-end pt-2">
              <button
                class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-5 py-2.5 rounded-lg transition-colors"
              >
                Actualizar contrasena
              </button>
            </div>
          </div>
        </div>

        <!-- Notificaciones -->
        <div
          v-if="seccionActiva === 'notificaciones'"
          class="bg-white border border-gray-100 rounded-2xl p-6"
        >
          <h2 class="text-sm font-medium text-gray-900 mb-6">Notificaciones</h2>

          <div class="flex flex-col gap-5">
            <div
              v-for="notif in notificaciones"
              :key="notif.id"
              class="flex items-center justify-between py-4 border-b border-gray-50 last:border-0"
            >
              <div>
                <p class="text-sm font-medium text-gray-900">{{ notif.titulo }}</p>
                <p class="text-xs text-gray-400 mt-0.5">{{ notif.descripcion }}</p>
              </div>
              <button
                @click="notif.activo = !notif.activo"
                :class="notif.activo ? 'bg-emerald-400' : 'bg-gray-200'"
                class="relative w-10 h-5 rounded-full transition-colors flex-shrink-0"
              >
                <span
                  :class="notif.activo ? 'translate-x-5' : 'translate-x-1'"
                  class="absolute top-0.5 w-4 h-4 bg-white rounded-full shadow transition-transform"
                >
                </span>
              </button>
            </div>
          </div>
        </div>

        <!-- Plataforma -->
        <div
          v-if="seccionActiva === 'plataforma'"
          class="bg-white border border-gray-100 rounded-2xl p-6"
        >
          <h2 class="text-sm font-medium text-gray-900 mb-6">Ajustes de plataforma</h2>

          <div class="flex flex-col gap-4">
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5"
                >Nombre de la plataforma</label
              >
              <input
                value="Calend"
                type="text"
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition"
              />
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5"
                >URL base de webhooks</label
              >
              <div class="flex items-center gap-2">
                <input
                  value="https://calend.io/webhook"
                  type="text"
                  readonly
                  class="flex-1 border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-400 bg-gray-50 focus:outline-none"
                />
                <button
                  class="text-xs border border-gray-200 text-gray-600 px-3 py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
                >
                  Copiar
                </button>
              </div>
            </div>
            <div>
              <label class="block text-xs font-medium text-gray-700 mb-1.5">Zona horaria</label>
              <select
                class="w-full border border-gray-200 rounded-lg px-4 py-2.5 text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-emerald-300 transition bg-white"
              >
                <option>America/Costa_Rica (UTC-6)</option>
                <option>America/New_York (UTC-5)</option>
                <option>America/Los_Angeles (UTC-8)</option>
                <option>Europe/Madrid (UTC+1)</option>
              </select>
            </div>
            <div class="flex justify-end pt-2">
              <button
                class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-5 py-2.5 rounded-lg transition-colors"
              >
                Guardar cambios
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup>
import { ref } from 'vue'
import AdminLayout from '@/components/AdminLayout.vue'

const seccionActiva = ref('perfil')

const secciones = [
  {
    id: 'perfil',
    label: 'Perfil',
    icono: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z',
  },
  {
    id: 'seguridad',
    label: 'Seguridad',
    icono:
      'M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z',
  },
  {
    id: 'notificaciones',
    label: 'Notificaciones',
    icono:
      'M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9',
  },
  {
    id: 'plataforma',
    label: 'Plataforma',
    icono:
      'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z',
  },
]

const perfil = ref({
  nombre: 'Gonzalo',
  apellido: 'Acuna',
  correo: 'gonzaloa0743@gmail.com',
})

const notificaciones = ref([
  {
    id: 1,
    titulo: 'Nueva cita agendada',
    descripcion: 'Recibir alerta cuando un bot agende una cita',
    activo: true,
  },
  {
    id: 2,
    titulo: 'Bot desconectado',
    descripcion: 'Recibir alerta cuando un canal se desconecte',
    activo: true,
  },
  {
    id: 3,
    titulo: 'Nuevo cliente',
    descripcion: 'Recibir alerta cuando se registre un nuevo cliente',
    activo: false,
  },
  {
    id: 4,
    titulo: 'Reporte semanal',
    descripcion: 'Recibir resumen de actividad cada lunes',
    activo: true,
  },
])
</script>
