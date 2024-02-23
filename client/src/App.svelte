<script>
  import Home from "./pages/Home.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import Login from "./pages/Login.svelte";
  import Settings from "./pages/Settings.svelte";
  import Feed from "./pages/Feed.svelte";
  import AccountInfo from "./pages/AccountInfo.svelte";
  import Header from "./components/Header.svelte";
  import Router from "svelte-spa-router";
  import active from "svelte-spa-router/active";
</script>

<Header />

<div class="container mx-auto px-4 sm:px-10 md:px-12">
  <Router
    routes={{
      "/": Home,
      "/login": Login,
      "/settings": Settings,
      "/feed": Feed,
      "/account-info": AccountInfo,
      "*": NotFound,
    }}
  />
</div>
