<script>
  import Layout from "../components/Layout.svelte";
  import {
    IconThumbUpFilled,
    IconHeartFilled,
    IconMessageCircle,
  } from "@tabler/icons-svelte";
  import toast from "svelte-french-toast";
  import follows from "../stores/followsStore";
  import { POST, GET } from "../helpers/http";
  import user from "../stores/userStore";
  import { onMount } from "svelte";
  import { loadFollows } from "../helpers/utilities";
  
  
  let title = "";
  let content = "";
  let photoUrl = "";
  let posts = [];
  let peopleList = [];
  let usernameSearch = "";
  let loadingPeople = false;
  let creatingPost = false;
  let followLoading = false;

  onMount(async () => {
    if (!$user) {
      return;
    }
    
    if (!$follows.length){
      await loadFollows()
    }
    
    loadPeople();
  });

  const loadPeople = async () => {
    try {
      let url;
      if (usernameSearch.length > 0) {
        url = `/api/users?username=${usernameSearch}`;
      } else {
        url = "/api/users";
      }
      loadingPeople = true;

      const [status, data] = await GET(url);

      if (status === 200) {
        peopleList = [...data.users];
        loadingPeople = false;
      } else {
        toast.error("There was an error finding people. Please try again.");
      }
    } catch (err) {
      console.log(err);
      loadingPeople = false;
      toast.error("There was an error finding people. Please try again.");
    }
    
  };

  let searchTimeout;
  const debounceSearch = (e) => {
    // 2 seconds debounce cancel previous request
    if (searchTimeout) {
      clearTimeout(searchTimeout);
    }
    searchTimeout = setTimeout(() => {
      usernameSearch = e.target.value;
      loadPeople();
    }, 1000);
  };

  const handleFollow = async (person) => {
    followLoading = true;
    try {
      const payload = JSON.stringify({
        followerId: $user.user.key,
        followeeId: person.key,
      });
      const [status, data] = await POST("/api/follow", payload);

      if (status === 200) {
        $follows = [...$follows, person.key];
        toast.success("You are now following " + person.ownerName);
      } else {
        toast.error("There was an error following " + person.ownerName);
      }
    } catch (err) {
      console.log(err);
      toast.error("There was an error following " + person.ownerName);
    }
    followLoading = false;
  };
</script>

<Layout>
  <div class="flex items-center justify-between bg-gray-50 p-6">
    <h1 class="text-xl font-bold text-[#00000]">People</h1>
    <div>
      <input
        on:input={debounceSearch}
        class="bg-white-100 rounded-md border border-gray-300 px-6 py-3"
        type="search"
        placeholder="Search here"
      />
    </div>
  </div>
  {#if loadingPeople}
    <div class="flex items-center justify-center bg-gray-50 p-10">
      Loading...
    </div>
  {:else}
    <div class="grid-cols mt-5 grid gap-4 md:grid-cols-2">
      {#each peopleList as person}
        {#if person.key !== $user.user.key}
          <div class="relative flex h-[200px] flex-col">
            <img
              class="h-[50%] w-full object-cover"
              src="https://images.unsplash.com/photo-1508108712903-49b7ef9b1df8?q=10&w=400"
              alt="bg"
            />
            <div
              class="flex h-[50%] w-full items-start justify-between bg-gray-50 py-3 pl-[120px] pr-5"
            >
              <div>
                <h1 class="text-xl font-bold text-[#00000]">
                  {person.ownerName}
                </h1>
                <p class="text-sm text-gray-400">@{person.username}</p>
              </div>
              {#if $follows.includes(person.key)}
                <div
                  class="mt-2 rounded-full bg-green-100 px-4 py-2 text-green-600"
                  >Following</div>
              {:else}
              <button
                disabled={followLoading}
                on:click={() => handleFollow(person)}
                class="mt-2 rounded-full bg-blue-600 px-4 py-2 text-white disabled:opacity-50 disabled:cursor-not-allowed"
                >Follow</button
              >
              {/if}
              
            </div>
            <img
              class="absolute left-5 top-[50%] h-[100px] w-[100px] translate-y-[-50%] rounded-full border border-4 border-white"
              src={person.ownerPhotoUrl}
              alt="profile"
            />
          </div>
        {/if}
      {/each}
    </div>
  {/if}
</Layout>
