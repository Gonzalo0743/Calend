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
          :key="item.id"
          href="#"
          @click.prevent="$router.push(item.ruta)"
          :class="
            esActivo(item.ruta)
              ? 'bg-emerald-50 text-emerald-700'
              : 'text-gray-500 hover:bg-gray-50'
          "
          class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors"
        >
          <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              :d="item.icono"
            />
          </svg>
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
      <slot />
    </main>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const navItems = [
  {
    id: 'inicio',
    label: 'Inicio',
    ruta: '/admin',
    icono:
      'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6',
  },
  {
    id: 'flujos',
    label: 'Flujos de trabajo',
    ruta: '/admin/flujos',
    icono: 'M4 6h16M4 10h16M4 14h16M4 18h16',
  },
  {
    id: 'canales',
    label: 'Canales',
    ruta: '/admin/canales',
    icono:
      'M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0',
  },
  {
    id: 'contactos',
    label: 'Contactos',
    ruta: '/admin/contactos',
    icono:
      'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z',
  },
  {
    id: 'configuracion',
    label: 'Configuracion',
    ruta: '/admin/configuracion',
    icono:
      'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z',
  },
]

function esActivo(ruta) {
  return route.path === ruta
}
</script>
