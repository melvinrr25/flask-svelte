import { writable } from 'svelte/store'
import { fetchCurrentUser } from '../helpers/localStorage';

const user = writable(fetchCurrentUser());

export default user;