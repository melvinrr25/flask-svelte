<script>
  import {
    IconUsersGroup,
    IconCar,
    IconUser,
    IconSquareRoundedPlus,
    IconDashboard,
    IconDeviceTv,
    IconUsers,
  } from "@tabler/icons-svelte";

  import Authorize from "./Authorize.svelte";

  import { link, push } from "svelte-spa-router";
  import active from "svelte-spa-router/active";
</script>

<Authorize>
  <div class="my-10 flex flex-col gap-10 md:flex-row">
    <aside
      class="fixed bottom-0 left-0 right-0 z-10 w-full bg-gray-800 text-white md:relative md:w-[200px] min-w-[200px] md:bg-white md:text-gray-700"
    >
      <ul class="flex p-2 md:flex-col">
        <li class="flex flex-1 justify-center md:block">
          <a
            use:link
            use:active
            class="flex flex-col items-center justify-center gap-2 px-2 py-2 text-gray-500 hover:text-gray-800 md:flex-row md:justify-start"
            href="/feed"
          >
            <span
              class="rounded-full bg-gradient-to-r from-cyan-500 to-blue-700 p-2 text-white"
            >
              <IconDeviceTv />
            </span> News Feed
          </a>
        </li>

        <li class="flex flex-1 justify-center md:block">
          <a
            use:link
            use:active
            class="flex flex-col items-center justify-center gap-2 px-2 py-2 text-gray-500 hover:text-gray-800 md:flex-row md:justify-start"
            href="/people"
          >
            <span
              class="rounded-full bg-gradient-to-r from-orange-500 to-orange-700 p-2 text-white"
            >
              <IconUsers />
            </span> Find People
          </a>
        </li>
        
      </ul>
    </aside>
    <main class="grow pb-[50px] bg-white p-10">
      <slot />
    </main>
  </div>
</Authorize>
