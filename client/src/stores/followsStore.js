import { writable } from 'svelte/store'
import { fetchCurrentFollows } from '../helpers/localStorage';

const follows = writable(fetchCurrentFollows());

export default follows;