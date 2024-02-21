<script>
  import { link, push } from "svelte-spa-router";
</script>

<div class="login-image-container mx-auto rounded-2xl sm:w-[400px]">
  <div
    class="flex h-full w-full flex-col items-center justify-center rounded-2xl bg-[rgba(1,1,1,0.4)] p-2"
  >
    <hi class="py-5 text-center text-5xl font-bold text-white">Welcome back!</hi
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
  <form class="flex flex-col gap-3 py-5">
    <label for="username" class="text-sm font-bold">Username</label>
    <input
      placeholder="Username"
      type="text"
      id="username"
      name="username"
      class="placeholder-[#a7825c] rounded-xl bg-[#f5efe8] p-3 outline-none border-2 border-transparent focus:border-[#f48c25]"
    />
    <label for="password" class="text-sm font-bold">Password</label>
    <input
      placeholder="Password"
      type="password"
      id="password"
      name="password"
      class="placeholder-[#a7825c] rounded-xl bg-[#f5efe8] p-3 outline-none border-2 border-transparent focus:border-[#f48c25]"
    />
    <button
      type="button"
      on:click={() => push("/feed")}
      class="rounded-xl bg-[#f48c25] px-6 py-3 text-sm font-bold text-[#1e1911]"
      >Log in</button
    >
  </form>
</div>
