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
  let title = "";
  let content = "";
  let photoUrl = "";
  let posts = [];

  onMount(() => {
    loadPosts();
  });

  const loadPosts = async () => {
    try {
      const [status, data] = await GET(`/api/users/${$user.user.key}/posts`);
      if (status === 200) {
        debugger;
        posts = data.posts;
      } else {
        alert("ERROR");
      }
    } catch (err) {
      alert(err);
    }
  };

  const handlePostSubmit = async () => {
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
        alert("OK posted!");
      } else {
        alert("ERROR");
      }
    } catch (err) {
      alert(err);
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
          Create Post</button
        >
      </div>
    </form>
  </div>

  <div ruler class="mb-10 mt-10 h-[1px] bg-[#f2f2f2]"></div>

  <!-- Posts -->
  <div class="flex flex-col gap-4">
    {#each posts as post}
      <div class="flex flex-col gap-2 rounded-xl bg-gray-50 p-6 mb-10">
        <h2 class="text-xl font-bold text-[#00000]">{post.title}</h2>
        <p class="text-gray-500">{post.content}</p>
        <img
          src={post.photoUrl}
          alt={post.title}
          class="h-64 w-[50%] rounded-xl object-cover"
        />
        <div class="flex items-center gap-2">
        <span class="rounded-full text-white p-2 bg-red-500">
          <IconThumbUpFilled size="20" />
        </span>  
        <span class="rounded-full text-white p-2 bg-blue-500">
          <IconHeartFilled size="20" />
        </span>
        <span class="flex gap-2">
          <IconMessageCircle /> 22 Comments
        </span>
        </div>
      </div>
    {/each}
  </div></Layout
>
