import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true, // Necesario para Docker en Windows/algunos Linux
    },
    host: true, // Exponer a la red local de Docker
    strictPort: true,
    port: 5173,
  }
})