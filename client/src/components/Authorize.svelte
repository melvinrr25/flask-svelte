<script>
  import { onMount } from "svelte";
  import { push } from "svelte-spa-router";
  import { fetchCurrentUser } from "../helpers/localStorage";

  onMount(async () => {
    if (!fetchCurrentUser()) {
      push("/login?p=" + window.location.hash.split("#")[1]);
    }
  });
</script>

{#if fetchCurrentUser()}
  <slot />
{/if}
