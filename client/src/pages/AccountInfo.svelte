<script>
  import Layout from "../components/Layout.svelte";
  import { IconHome, IconArrowLeft } from "@tabler/icons-svelte";
  import { link, push, pop } from "svelte-spa-router";
  import active from "svelte-spa-router/active";
  import { POST } from "../helpers/http";
  import user from "../stores/userStore";
  import { localStorageCurrentUserUpdate } from "../helpers/localStorage";
  import toast from 'svelte-french-toast';

  const handleSubmit = async () => {
    try {
      console.log($user);
      const payload = JSON.stringify({
        petName: $user.user.petName,
        ownerName: $user.user.ownerName,
        petPhotoUrl: $user.user.petPhotoUrl,
        ownerPhotoUrl: $user.user.ownerPhotoUrl,
      });
      
      const url = `/api/users/${$user.user.key}`
      const [status, data] = await POST(url, payload);

      if (status === 200) {
        localStorageCurrentUserUpdate($user);
        toast.success("Account information updated!");
      } else {
        toast.error("There was an error updating your account information");
      }
    } catch (err) {
      console.log(err);
      toast.error("There was an error updating your account information");
    }
  };
</script>

<Layout>
  <div>
    <h1 class=" mb-6 text-xl font-bold text-[#00000]">
      <span class="flex items-center gap-2">
        <span on:click={() => pop()} class="cursor-pointer"
          ><IconArrowLeft /></span
        > Account Information
      </span>
    </h1>
    <form
      on:submit|preventDefault={handleSubmit}
      class="flex flex-col gap-3 py-5"
    >
      <fieldset class="flex flex-col gap-3 py-5">
        <legend class="text text-center font-bold text-[#f48c25]"
          >Pet Information</legend
        >
        <label for="username" class="text-sm font-bold">Pet Name:</label>
        <input
          bind:value={$user.user.petName}
          placeholder="Pet Name"
          type="text"
          id="petName"
          name="petName"
          class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
        />

        <label for="username" class="text-sm font-bold">Pet Photo Url:</label>
        <input
          bind:value={$user.user.petPhotoUrl}
          placeholder="Pet Photo URL"
          type="url"
          id="petPhotoUrl"
          name="petPhotoUrl"
          class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
        />
      </fieldset>

      <fieldset class="flex flex-col gap-3 py-5">
        <legend class="text text-center font-bold text-[#f48c25]"
          >Owner Information</legend
        >
        <label for="username" class="text-sm font-bold">Owner Name:</label>
        <input
          bind:value={$user.user.ownerName}
          placeholder="Owner Name"
          type="text"
          id="ownerName"
          name="ownerName"
          class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
        />

        <label for="username" class="text-sm font-bold">Owner Photo Url:</label>
        <input
          bind:value={$user.user.ownerPhotoUrl}
          placeholder="Owner Photo URL"
          type="url"
          id="ownerPhotoUrl"
          name="ownerPhotoUrl"
          class="rounded-xl border-2 border-transparent bg-[#f5efe8] p-3 placeholder-[#a7825c] outline-none focus:border-[#f48c25]"
        />
      </fieldset>

      <button
        type="submit"
        class="rounded-xl bg-[#f48c25] px-6 py-3 text-sm font-bold text-[#1e1911]"
        >Save</button
      >
    </form>
  </div>
</Layout>
