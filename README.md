# Calend

Plataforma SaaS para automatizar el agendamiento de citas mediante chatbots personalizados.

## ¿Qué es Calend?

Calend permite a empresas crear su propio chatbot de agendamiento sin necesidad de una secretaria o agente humano. El bot interactúa con los clientes de forma natural, gestiona disponibilidad y confirma citas automáticamente.

## Estado del proyecto

En desarrollo activo.

## Tech Stack

- **Frontend:** Vue 3, Tailwind CSS, Vue Router, Pinia, Chart.js, Vue Flow
- **Backend:** Django REST Framework, SQLite, JWT
- **Herramientas:** Vite, ESLint, Prettier

## Funcionalidades actuales

- [x] Landing page completa con hero, features, testimonios y precios
- [x] Autenticacion real con Django — login por email, deteccion de rol, JWT
- [x] Proteccion de rutas con guards de Vue Router
- [x] Dashboard del cliente con métricas y lista de citas reales
- [x] Vista del chatbot con flujo dinamico — lee los nodos del editor en tiempo real
- [x] Panel de administracion con métricas y lista de bots reales
- [x] Editor de flujos con Vue Flow — nodos arrastrables, conectables y guardado en base de datos
- [x] Vista previa del flujo directamente desde el editor
- [x] Crear, editar y eliminar bots desde la interfaz
- [x] Gestion de clientes — crear usuarios y asignarles bots
- [x] Canales — conexion y gestion de canales de comunicacion
- [x] Contactos — lista de contactos con busqueda y filtros
- [x] Configuracion — perfil, seguridad, notificaciones y ajustes de plataforma
- [ ] Citas guardadas en base de datos desde el chat
- [ ] Contactos guardados automaticamente al interactuar con el bot

## Instalación local

### Backend
```bash
cd backend
py manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Abrí `http://localhost:5173` en tu navegador.

## Autor

Gonzalo Acuña Madrigal — [github.com/Gonzalo0743](https://github.com/Gonzalo0743)