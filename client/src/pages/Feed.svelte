<script>
  import Layout from "../components/Layout.svelte";
  import {
    IconThumbUpFilled,
    IconHeartFilled,
    IconMessageCircle,
  } from "@tabler/icons-svelte";
  import { POST, GET } from "../helpers/http";
  import user from "../stores/userStore";
  import { onMount } from "svelte";
  import toast from 'svelte-french-toast';
  
  let title = "";
  let content = "";
  let photoUrl = "";
  let posts = [];
  let loadingPosts = false;
  let creatingPost = false;

  onMount(() => {
    if(!$user){ return }
    
    loadPosts();
  });

  const loadPosts = async (lastPost) => {
    try {
      let url;
      loadingPosts = true;
      console.log($user);
      if(lastPost) {
        url = `/api/posts?last=${lastPost}` 
      }else {
        url = `/api/posts`
      }
      
      const [status, data] = await GET(url)
      
      if (status === 200) {
        posts = [...posts, ...data.posts];
        loadingPosts = false;
      } else {
        loadingPosts = false;
        toast.error("There was an error loading posts");
      }
    } catch (err) {
      console.log(err);
      loadingPosts = false;
      toast.error("There was an error loading posts");
    }
  };

  const handlePostSubmit = async () => {
    if (!title || !content || !photoUrl) {
      return toast.error("Please fill out all fields");
    }
    
    creatingPost = true;
    
    try {
      console.log($user);
      const [status, data] = await POST(
        `/api/users/${$user.user.key}/posts`,
        JSON.stringify({
          title,
          content,
          photoUrl,
        }),
      );

      if (status === 200) {
        creatingPost = false;
        title = "";
        content = "";
        photoUrl = "";
        toast.success("Post created!");
      } else {
        toast.error("There was an error creating your post");
      }
    } catch (err) {
      creatingPost = false;
      toast.error("There was an error creating your post");
    }
  };
</script>

<Layout>
  <div class="">
    <h1 class="pb-5 text-xl font-bold text-[#00000]">Create Post</h1>
    <form on:submit|preventDefault={handlePostSubmit}>
      <div class="flex flex-row gap-4">
        <div class="grow">
          <label for="title" class="mb-2 block text-sm font-bold text-gray-700">
            Title
          </label>
          <input
            bind:value={title}
            type="text"
            id="title"
            class="w-full rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
            placeholder="Enter title"
          />

          <label
            for="title"
            class="mb-2 mt-4 block text-sm font-bold text-gray-700"
          >
            Photo URL
          </label>
          <input
            bind:value={photoUrl}
            type="text"
            id="title"
            class="w-full rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
            placeholder="Enter URL"
          />
        </div>
        <div class="grow">
          <label
            for="content"
            class="mb-2 block text-sm font-bold text-gray-700"
          >
            Content
          </label>
          <textarea
            bind:value={content}
            rows="5"
            id="content"
            class="w-full rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
            placeholder="Enter content"
          ></textarea>
        </div>
      </div>
      <div class="mt-2 flex justify-end">
        <button type="submit" class="rounded bg-blue-500 px-4 py-2 text-white">
        {#if creatingPost}
          Creating Post...
        {:else}
          Create Post 
        {/if}  
        
        </button
        >
      </div>
    </form>
  </div>

  <div ruler class="mb-10 mt-10 h-[1px] bg-[#f2f2f2]"></div>

  <!-- Posts -->
  <div class="flex flex-col gap-4">
    {#each posts as post}
      <div class="mb-10 flex flex-col gap-2 bg-gray-50 p-6 shadow">
        <h2 class="flex items-center gap-2 pb-4">
          <span class="text-sm text-gray-500">
            <img
              src={post.user.ownerPhotoUrl}
              alt={post.user.ownerName}
              class="h-8 w-8 rounded-full object-cover"
            />
          </span>
          <span class="text-sm font-bold text-[#00000]"
            >{post.user.ownerName}</span
          >
        </h2>
        <h3 class="text-sm font-bold text-gray-500">{post.title}</h3>
        <p class="text-wrap text-sm text-gray-500">{post.content}</p>
        <img
          src={post.photoUrl}
          alt={post.title}
          class="h-64 w-[50%] rounded-xl object-cover"
        />
        <div class="flex items-center gap-2">
          <span class="cursor-pointer rounded-full bg-red-500 p-2 text-white">
            <IconHeartFilled size="20" />
          </span>
          <span class="cursor-pointer rounded-full bg-blue-500 p-2 text-white">
            <IconThumbUpFilled size="20" />
          </span>
          <span class="flex gap-2">
            <IconMessageCircle /> 22 Comments
          </span>
        </div>
      </div>
    {/each}
  </div>
  {#if posts.length > 0}
    <div class="text-center">
      <button 
        disabled={loadingPosts}
        on:click={() => loadPosts(posts[posts.length - 1].key)}
        class="rounded bg-blue-500 disabled:opacity-50 px-4 py-2 text-white">
        {#if loadingPosts }
          Loading...
        {:else}
          Load More
        {/if}
      </button>
    </div>
  {/if}
  
</Layout>
