<script>
  import { link, push } from 'svelte-spa-router';
  import active from 'svelte-spa-router/active';
  import { IconDog } from '@tabler/icons-svelte';
</script>

<header class="mb-10 border-b px-12">
  <nav class="flex justify-between py-5">
    <div class="flex items-center gap-12">
    <a use:link use:active class="pr-1 text-xl-custom font-bold logo flex gap-2 items-center" href="/">
      <IconDog />
      PetConnect
    </a>
     
    </div>
    <div>  
    <button 
      on:click={() => push("/signup")} 
      class="bg-[#f48c25] text-[#1e1911] py-2 px-4 rounded-xl font-bold text-sm"
    >Sign up</button>
    <button 
      on:click={() => push("/login")} 
      class="bg-[#f5efe8] text-[#1e1911] py-2 px-4 rounded-xl font-bold text-sm"
    >Log in</button>
    </div>
  </nav>
</header>