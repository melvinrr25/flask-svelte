<script>
  import { link, push } from "svelte-spa-router";
  import active from "svelte-spa-router/active";
  import { IconDog } from "@tabler/icons-svelte";
</script>

<header class="mb-10 border-b px-12">
  <nav class="flex justify-between py-5">
    <div class="flex items-center gap-12">
      <a
        use:link
        use:active
        class="text-xl-custom logo flex items-center gap-2 pr-1 font-bold"
        href="/"
      >
        <IconDog />
        PetConnect
      </a>
    </div>
    <div>
      <button
        on:click={() => push("/signup")}
        class="rounded-xl bg-[#f48c25] px-4 py-2 text-sm font-bold text-[#1e1911]"
        >Sign up</button
      >
      <button
        on:click={() => push("/login")}
        class="rounded-xl bg-[#f5efe8] px-4 py-2 text-sm font-bold text-[#1e1911]"
        >Log in</button
      >
    </div>
  </nav>
</header>
