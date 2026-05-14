<template>
  <div class="min-h-screen bg-white">
    <!-- Navbar -->
    <nav class="flex items-center justify-between px-8 py-5 border-b border-gray-100">
      <div class="flex items-center gap-2">
        <span class="text-lg font-medium text-gray-900 tracking-tight">Calend</span>
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
      </div>
      <div class="hidden md:flex items-center gap-8">
        <a href="#" class="text-sm text-gray-500 hover:text-gray-800 transition-colors">Producto</a>
        <a href="#" class="text-sm text-gray-500 hover:text-gray-800 transition-colors">Precios</a>
        <a href="#" class="text-sm text-gray-500 hover:text-gray-800 transition-colors">Docs</a>
      </div>
      <button
        @click="$router.push('/login')"
        class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-5 py-2 rounded-lg transition-colors"
      >
        Empezar gratis
      </button>
    </nav>

    <!-- Hero -->
    <section class="px-8 pt-20 pb-24 max-w-5xl mx-auto">
      <div class="flex flex-col md:flex-row items-center gap-16">
        <!-- Texto -->
        <div class="flex-1">
          <div
            class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs px-3 py-1.5 rounded-full mb-6"
          >
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Agendamiento con IA para tu negocio
          </div>
          <h1 class="text-5xl font-medium text-gray-900 leading-tight tracking-tight mb-6">
            Agendá citas <span class="text-emerald-500">sin esfuerzo</span>,<br />
            con un chatbot propio
          </h1>
          <p class="text-lg text-gray-500 leading-relaxed mb-10 max-w-xl">
            Dale a tu negocio un asistente virtual que agenda, recuerda y gestiona citas por vos,
            las 24 horas del día.
          </p>
          <div class="flex items-center gap-4">
            <button
              @click="$router.push('/login')"
              class="bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium px-6 py-3 rounded-lg transition-colors"
            >
              Ver demo
            </button>
            <a href="#" class="text-sm text-gray-500 hover:text-gray-800 transition-colors">
              Saber más →
            </a>
          </div>
        </div>

        <!-- Mockup chat -->
        <div class="flex-1 w-full">
          <div
            class="bg-white border border-gray-200 rounded-2xl shadow-sm overflow-hidden max-w-sm mx-auto"
          >
            <!-- Header del chat -->
            <div class="flex items-center gap-3 px-4 py-3 border-b border-gray-100 bg-gray-50">
              <div class="w-8 h-8 rounded-full bg-emerald-400 flex items-center justify-center">
                <svg
                  class="w-4 h-4 text-white"
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
              <div>
                <p class="text-xs font-medium text-gray-900">Calend Bot</p>
                <p class="text-xs text-emerald-500">En línea</p>
              </div>
            </div>

            <!-- Mensajes -->
            <div class="px-4 py-4 flex flex-col gap-3 bg-white min-h-48">
              <div class="flex gap-2 items-end">
                <div class="w-6 h-6 rounded-full bg-emerald-400 flex-shrink-0"></div>
                <div
                  class="bg-gray-100 text-gray-700 text-xs px-3 py-2 rounded-2xl rounded-bl-sm max-w-xs"
                >
                  ¡Hola! Soy el asistente de <strong>Clínica Verde</strong>. ¿En qué te puedo
                  ayudar?
                </div>
              </div>

              <div class="flex justify-end">
                <div
                  class="bg-emerald-400 text-white text-xs px-3 py-2 rounded-2xl rounded-br-sm max-w-xs"
                >
                  Quiero agendar una cita para el martes
                </div>
              </div>

              <div class="flex gap-2 items-end">
                <div class="w-6 h-6 rounded-full bg-emerald-400 flex-shrink-0"></div>
                <div
                  class="bg-gray-100 text-gray-700 text-xs px-3 py-2 rounded-2xl rounded-bl-sm max-w-xs"
                >
                  Perfecto, tengo disponibilidad el martes a las <strong>10:00 am</strong> o
                  <strong>3:00 pm</strong>. ¿Cuál preferís?
                </div>
              </div>

              <div class="flex justify-end">
                <div
                  class="bg-emerald-400 text-white text-xs px-3 py-2 rounded-2xl rounded-br-sm max-w-xs"
                >
                  A las 10 am está bien
                </div>
              </div>

              <div class="flex gap-2 items-end">
                <div class="w-6 h-6 rounded-full bg-emerald-400 flex-shrink-0"></div>
                <div
                  class="bg-gray-100 text-gray-700 text-xs px-3 py-2 rounded-2xl rounded-bl-sm max-w-xs"
                >
                  ¡Listo! Tu cita quedó agendada para el <strong>martes a las 10:00 am</strong>. Te
                  enviamos una confirmación. 🗓️
                </div>
              </div>
            </div>

            <!-- Input simulado -->
            <div class="px-4 py-3 border-t border-gray-100 flex items-center gap-2">
              <div class="flex-1 bg-gray-50 rounded-full px-4 py-2 text-xs text-gray-400">
                Escribí tu mensaje...
              </div>
              <div
                class="w-8 h-8 rounded-full bg-emerald-400 flex items-center justify-center flex-shrink-0"
              >
                <svg
                  class="w-4 h-4 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                  />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="px-8 pb-24 max-w-5xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center mb-4">
            <svg
              class="w-5 h-5 text-emerald-600"
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
          <h3 class="text-sm font-medium text-gray-900 mb-2">Chatbot personalizado</h3>
          <p class="text-sm text-gray-500 leading-relaxed">
            Creá un bot con la identidad de tu negocio que atiende a tus clientes de forma natural.
          </p>
        </div>

        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center mb-4">
            <svg
              class="w-5 h-5 text-emerald-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
          </div>
          <h3 class="text-sm font-medium text-gray-900 mb-2">Calendario integrado</h3>
          <p class="text-sm text-gray-500 leading-relaxed">
            Las citas se sincronizan automáticamente. Vos y tu cliente reciben confirmación al
            instante.
          </p>
        </div>

        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center mb-4">
            <svg
              class="w-5 h-5 text-emerald-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
              />
            </svg>
          </div>
          <h3 class="text-sm font-medium text-gray-900 mb-2">Panel de control</h3>
          <p class="text-sm text-gray-500 leading-relaxed">
            Gestioná todas tus citas, clientes y estadísticas desde un dashboard simple y claro.
          </p>
        </div>
      </div>
    </section>

    <!-- Testimonios -->
    <section class="px-8 pb-24 max-w-5xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-medium text-gray-900 tracking-tight mb-3">
          Negocios que ya confían en Calend
        </h2>
        <p class="text-gray-500 text-base max-w-md mx-auto">
          Más de 500 empresas automatizaron sus citas con nosotros.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="flex gap-1 mb-4">
            <span class="text-emerald-400 text-sm">★★★★★</span>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            "Antes perdíamos clientes por no poder atender llamadas. Con Calend, el bot agenda solo
            y nosotros nos enfocamos en atender."
          </p>
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 rounded-full bg-emerald-200 flex items-center justify-center text-xs font-medium text-emerald-700"
            >
              MR
            </div>
            <div>
              <p class="text-xs font-medium text-gray-900">María Rodríguez</p>
              <p class="text-xs text-gray-400">Clínica Dental Sonrisa</p>
            </div>
          </div>
        </div>

        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="flex gap-1 mb-4">
            <span class="text-emerald-400 text-sm">★★★★★</span>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            "La integración fue sencillísima. En menos de una hora ya teníamos el chatbot
            funcionando en nuestra página."
          </p>
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 rounded-full bg-emerald-200 flex items-center justify-center text-xs font-medium text-emerald-700"
            >
              CA
            </div>
            <div>
              <p class="text-xs font-medium text-gray-900">Carlos Alvarado</p>
              <p class="text-xs text-gray-400">FitLife Gym</p>
            </div>
          </div>
        </div>

        <div class="bg-gray-50 rounded-2xl p-6">
          <div class="flex gap-1 mb-4">
            <span class="text-emerald-400 text-sm">★★★★★</span>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed mb-4">
            "Redujimos un 80% las llamadas al consultorio. Los pacientes prefieren agendar por el
            chat y nosotros ahorramos tiempo."
          </p>
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 rounded-full bg-emerald-200 flex items-center justify-center text-xs font-medium text-emerald-700"
            >
              LP
            </div>
            <div>
              <p class="text-xs font-medium text-gray-900">Laura Pérez</p>
              <p class="text-xs text-gray-400">Consultorio Bienestar</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Precios -->
    <section class="px-8 pb-24 max-w-5xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-medium text-gray-900 tracking-tight mb-3">
          Planes simples, sin sorpresas
        </h2>
        <p class="text-gray-500 text-base max-w-md mx-auto">
          Elegí el plan que mejor se adapta a tu negocio. Cancelá cuando quieras.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
        <!-- Plan Básico -->
        <div class="border border-gray-200 rounded-2xl p-6">
          <p class="text-sm font-medium text-gray-900 mb-1">Básico</p>
          <p class="text-gray-500 text-xs mb-4">Para negocios pequeños</p>
          <div class="flex items-baseline gap-1 mb-6">
            <span class="text-3xl font-medium text-gray-900">$19</span>
            <span class="text-gray-400 text-sm">/mes</span>
          </div>
          <ul class="flex flex-col gap-3 mb-6">
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              1 chatbot
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Hasta 100 citas/mes
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Calendario integrado
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-400">
              <span
                class="w-4 h-4 rounded-full bg-gray-100 flex items-center justify-center text-xs"
                >✗</span
              >
              Soporte prioritario
            </li>
          </ul>
          <button
            class="w-full border border-gray-200 text-gray-700 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Empezar
          </button>
        </div>

        <!-- Plan Pro (destacado) -->
        <div class="border-2 border-emerald-400 rounded-2xl p-6 relative">
          <div class="absolute -top-3 left-1/2 -translate-x-1/2">
            <span class="bg-emerald-400 text-white text-xs font-medium px-3 py-1 rounded-full">
              Más popular
            </span>
          </div>
          <p class="text-sm font-medium text-gray-900 mb-1">Pro</p>
          <p class="text-gray-500 text-xs mb-4">Para negocios en crecimiento</p>
          <div class="flex items-baseline gap-1 mb-6">
            <span class="text-3xl font-medium text-gray-900">$49</span>
            <span class="text-gray-400 text-sm">/mes</span>
          </div>
          <ul class="flex flex-col gap-3 mb-6">
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              5 chatbots
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Citas ilimitadas
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Calendario integrado
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Soporte prioritario
            </li>
          </ul>
          <button
            class="w-full bg-emerald-400 hover:bg-emerald-500 text-white text-sm font-medium py-2.5 rounded-lg transition-colors"
          >
            Empezar
          </button>
        </div>

        <!-- Plan Enterprise -->
        <div class="border border-gray-200 rounded-2xl p-6">
          <p class="text-sm font-medium text-gray-900 mb-1">Enterprise</p>
          <p class="text-gray-500 text-xs mb-4">Para grandes empresas</p>
          <div class="flex items-baseline gap-1 mb-6">
            <span class="text-3xl font-medium text-gray-900">Custom</span>
          </div>
          <ul class="flex flex-col gap-3 mb-6">
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Chatbots ilimitados
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Citas ilimitadas
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Integraciones custom
            </li>
            <li class="flex items-center gap-2 text-sm text-gray-600">
              <span
                class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center text-xs"
                >✓</span
              >
              Soporte dedicado
            </li>
          </ul>
          <button
            class="w-full border border-gray-200 text-gray-700 text-sm font-medium py-2.5 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Contactarnos
          </button>
        </div>
      </div>
    </section>

    <!-- CTA Final -->
    <section class="px-8 pb-24 max-w-5xl mx-auto">
      <div class="bg-emerald-400 rounded-3xl px-10 py-14 text-center">
        <h2 class="text-3xl font-medium text-white mb-4 tracking-tight">
          ¿Listo para automatizar tu negocio?
        </h2>
        <p class="text-emerald-50 text-base mb-8 max-w-md mx-auto">
          Empezá hoy y tené tu chatbot funcionando en minutos.
        </p>
        <button
          class="bg-white text-emerald-600 font-medium text-sm px-8 py-3 rounded-lg hover:bg-emerald-50 transition-colors"
        >
          Empezar gratis
        </button>
      </div>
    </section>
  </div>
</template>
