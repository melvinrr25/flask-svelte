<script>
  import { link } from "svelte-spa-router";
</script>

<div>
  <section class="pet-home-page flex flex-col justify-end p-10">
    <div class="flex flex-col items-start bg-transparent">
      <h1 class="text-5xl font-bold text-white">Welcome to PetConnect</h1>
      <p class="pb-8 pt-2 text-white">
        The social network for pets and their owners
      </p>
      <a
        use:link
        class="rounded-xl bg-[#f48c25] px-8 py-4 font-bold text-[#1e1911]"
        href="/signup">Create a profile</a
      >
    </div>
  </section>
  <section class="pt-10">
    <h2 class="pb-5 text-2xl font-bold">Discover Pets</h2>

    <div class="container mx-auto">
      <div
        class="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
      >
        <!-- Image 1 -->
        <div class="max-w-full">
          <img
            src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 1"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 2 -->
        <div class="max-w-full">
          <img
            src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 2"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 3 -->
        <div class="max-w-full">
          <img
            src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 3"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 4 -->
        <div class="max-w-full">
          <img
            src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 4"
            class="h-auto w-full"
          />
        </div>
      </div>
    </div>
  </section>

  <section class="pb-10 pt-10">
    <h2 class="pb-5 text-2xl font-bold">Connect with pet owners</h2>

    <div class="container mx-auto">
      <div
        class="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
      >
        <!-- Image 1 -->
        <div class="max-w-full">
          <img
            src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 1"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 2 -->
        <div class="max-w-full">
          <img
            src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 2"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 3 -->
        <div class="max-w-full">
          <img
            src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 3"
            class="h-auto w-full"
          />
        </div>

        <!-- Image 4 -->
        <div class="max-w-full">
          <img
            src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Image 4"
            class="h-auto w-full"
          />
        </div>
      </div>
    </div>
  </section>
</div>
