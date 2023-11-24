import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte'
 
export default defineConfig({
  plugins: [svelte()],
  server: {
    watch: {
      usePolling: true,
    },
    host: true, // needed for the Docker Container port mapping to work
    strictPort: true,
    port: 5173, // you can replace this port with any port
  },
});
