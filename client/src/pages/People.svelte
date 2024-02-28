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
  let peopleList = [];
  let loadingPeople = false;
  let creatingPost = false;

  onMount(() => {
    if (!$user) {
      return;
    }

    loadPeople();
  });

  const loadPeople = async () => {
    try {
      let url = "/api/users";
      loadingPeople = true;

      const [status, data] = await GET(url);

      if (status === 200) {
        peopleList = [...data.users];
        loadingPeople = false;
      } else {
        alert("ERROR loading people");
      }
    } catch (err) {
      console.log(err);
      loadingPeople = false;
      alert(err);
    }
  };
</script>

<Layout>
  <div class="flex items-center justify-between bg-gray-50 p-6">
    <h1 class="text-xl font-bold text-[#00000]">People</h1>
    <div>
      <form>
        <input
          class="bg-white-100 rounded-md border border-gray-300 px-6 py-3"
          type="search"
          placeholder="Search here"
        />
      </form>
    </div>
  </div>
  <div class="grid-cols mt-5 grid gap-4 md:grid-cols-2">
    {#each peopleList as person}
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
            <h1 class="text-xl font-bold text-[#00000]">{person.ownerName}</h1>
            <p class="text-sm text-gray-400">{person.petName}</p>
          </div>
          <button class="mt-2 rounded-full bg-blue-600 px-4 py-2 text-white"
            >Follow</button
          >
        </div>
        <img
          class="absolute left-5 top-[50%] h-[100px] w-[100px] translate-y-[-50%] rounded-full border border-4 border-white"
          src={person.ownerPhotoUrl}
          alt="profile"
        />
      </div>
    {/each}
  </div>
</Layout>
