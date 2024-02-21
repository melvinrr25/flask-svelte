<script>
  import { link } from 'svelte-spa-router';
</script>

<div>
  <section class="pet-home-page flex flex-col justify-end p-10">
    <div class="bg-transparent flex flex-col items-start">
      <h1 class="text-white text-5xl font-bold">Welcome to PetConnect</h1>
      <p class="text-white pb-8 pt-2">The social network for pets and their owners</p>
      <a use:link class="bg-[#f48c25] text-[#1e1911] py-4 px-8 rounded-xl font-bold" href="/signup">Create a profile</a>
    </div>
  </section>
  <section class="pt-10">
    <h2 class="text-2xl font-bold pb-5">Discover Pets</h2>
  
    <div class="container mx-auto">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        <!-- Image 1 -->
        <div class="max-w-full">
          <img src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 1" class="w-full h-auto">
        </div>
    
        <!-- Image 2 -->
        <div class="max-w-full">
          <img src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 2" class="w-full h-auto">
        </div>
    
        <!-- Image 3 -->
        <div class="max-w-full">
          <img src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 3" class="w-full h-auto">
        </div>
    
        <!-- Image 4 -->
        <div class="max-w-full">
          <img src="https://images.unsplash.com/photo-1647535681834-1dafbca7afd9?q=80&w=2896&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 4" class="w-full h-auto">
        </div>
    
       </div>
    </div>      
  
        
  </section>
  
  <section class="pt-10 pb-10">
    <h2 class="text-2xl font-bold pb-5">Connect with pet owners</h2>
  
    <div class="container mx-auto">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        <!-- Image 1 -->
        <div class="max-w-full">
          <img src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 1" class="w-full h-auto">
        </div>
    
        <!-- Image 2 -->
        <div class="max-w-full">
          <img src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 2" class="w-full h-auto">
        </div>
    
        <!-- Image 3 -->
        <div class="max-w-full">
          <img src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 3" class="w-full h-auto">
        </div>
    
        <!-- Image 4 -->
        <div class="max-w-full">
          <img src="https://plus.unsplash.com/premium_photo-1696623776734-4d0c9f49294e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Image 4" class="w-full h-auto">
        </div>
    
       </div>
    </div>      
  
        
  </section>
</div>