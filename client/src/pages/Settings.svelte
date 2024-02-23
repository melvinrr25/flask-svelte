<script>
  import Layout from "../components/Layout.svelte";
  import { IconHome } from "@tabler/icons-svelte";
  import { link, push } from "svelte-spa-router";
  import active from "svelte-spa-router/active";
</script>

<Layout>
  <div>
    <h1 class="mb-6 text-3xl font-bold text-[#00000]">Settings</h1>
    <h2 class="text-sm text-gray-400">General</h2>
    <ul>
      <li
        class="flex items-center justify-between border-b border-gray-200 py-3"
      >
        <a
          use:link
          use:active
          class="flex flex-col items-center justify-center gap-2 text-gray-500 hover:text-gray-800 md:flex-row md:justify-start"
          href="/account-info"
        >
          <span
            class="rounded-full bg-gradient-to-r from-blue-500 to-blue-700 p-2 text-white"
          >
            <IconHome />
          </span> Account Information
        </a>
      </li>
      <li
        class="flex items-center justify-between border-b border-gray-200 py-3"
      >
        <a
          use:link
          use:active
          class="flex flex-col items-center justify-center gap-2 text-gray-500 hover:text-gray-800 md:flex-row md:justify-start"
          href="/account-info"
        >
          <span
            class="rounded-full bg-gradient-to-r from-blue-500 to-blue-700 p-2 text-white"
          >
            <IconHome />
          </span> Account Information
        </a>
      </li>
    </ul>
  </div>
</Layout>
