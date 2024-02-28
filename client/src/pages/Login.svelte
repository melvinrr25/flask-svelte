<script>
  import { link, push } from "svelte-spa-router";
  import { POST } from "../helpers/http";
  import { localStorageCurrentUserUpdate } from "../helpers/localStorage";
  import { getParameterByName } from "../helpers/utilities";
  import { onMount } from "svelte";
  import user from '../stores/userStore';
  import toast from 'svelte-french-toast';

  let username = "";
  let password = "";

  onMount(() => {
    if ($user) {
      console.log($user);
      push("/feed");
    }
  });

  const handleLogin = async () => {
    if(!username || !password){
      return toast.error("Please enter a username and password");
    }
    try {
      const [status, data] = await POST(
        "/api/sessions",
        JSON.stringify({ username, password }),
      );

      if (status === 200) {
        localStorageCurrentUserUpdate(data);
        $user = data;
        var p = getParameterByName("p");
        push(p || "/feed");
        toast.success("Welcome back!");
      } else {
        toast.error("Invalid username or password");
      }
    } catch (err) {
      toast.error("Invalid username or password");
    }
  };
</script>

{#if !$user}
  <div class="login-image-container mx-auto rounded-2xl sm:w-[400px]">
    <div
      class="flex h-full w-full flex-col items-center justify-center rounded-2xl bg-[rgba(1,1,1,0.4)] p-2"
    >
      <hi class="py-5 text-center text-5xl font-bold text-white"
        >Welcome back!</hi
      >
      <p class="pb-10 text-center font-bold text-white">
        Log in to PetConnect to connect with the pet community
      </p>
      <button
        on:click={() => push("/signup")}
        class="rounded-xl bg-[#f48c25] px-6 py-3 text-sm font-bold text-[#1e1911]"
        >Sign up</button
      >
    </div>
  </div>

  <div class="mx-auto sm:w-[400px]">
    <form
      on:submit|preventDefault={handleLogin}
      class="flex flex-col gap-3 py-5"
    >
      <label for="username" class="text-sm font-bold">Username</label>
      <input
        bind:value={username}
        placeholder="Username"
        type="text"
        id="username"
        name="username"
        class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
      />
      <label for="password" class="text-sm font-bold">Password</label>
      <input
        bind:value={password}
        placeholder="Password"
        type="password"
        id="password"
        name="password"
        class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
      />
      <button
        type="submit"
        class="rounded-xl bg-[#f48c25] px-6 py-3 text-sm font-bold text-[#1e1911]"
        >Log in</button
      >
    </form>
  </div>
{/if}
