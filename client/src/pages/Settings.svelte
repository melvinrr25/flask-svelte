<script>
  import Layout from "../components/Layout.svelte";
  import { fetchCurrentUser } from "../helpers/localStorage";
  
  console.log(fetchCurrentUser())
</script>

<Layout>
  <div class="flex flex-col items-center justify-center h-full">
    <h1 class="text-5xl font-bold text-[#f48c25]">Settings</h1>
    <p class="text-center text-[#a7825c]">This is the settings page</p>
  </div>
</Layout>
