import toast from "svelte-french-toast";
import follows from "../stores/followsStore";
import user from "../stores/userStore";
import { GET } from "./http";

let $user;

user.subscribe((value) => {
  $user = value;
});

export function getParameterByName(name, url = window.location.href) {
  name = name.replace(/[\[\]]/g, '\\$&');
  var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)')
  var results = regex.exec(url);
  
  if (!results) return null;
  if (!results[2]) return '';

  return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

export async function loadFollows () {
  try {
    const [status, data] = await GET(`/api/follows/${$user.user.key}`);
    if (status === 200) {
      follows.set(data.followees.map((f) => f.followeeId));
    } else {
      toast.error("There was an error loading your follows. Please try again.");
    }
  } catch (err) {
    console.log(err);
    toast.error("There was an error loading your follows. Please try again.");
  }
};