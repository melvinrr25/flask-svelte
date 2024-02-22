<script>
  import { onMount } from "svelte";
  import { push } from "svelte-spa-router";
  import user from '../stores/userStore';

  onMount(async () => {
    if (!$user) {
      push("/login?p=" + window.location.hash.split("#")[1]);
    }
  });
</script>

{#if $user}
  <slot />
{/if}
