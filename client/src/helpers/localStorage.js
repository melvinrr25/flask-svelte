const CURRENT_USER = 'currentUser';

export function localStorageCurrentUserUpdate(attrs) {
  try{
    const currentUser = fetchCurrentUser() || {}

    for(const [key, value] of Object.entries(attrs)){
      currentUser[key] = value;
    }

    localStorage.setItem(CURRENT_USER, JSON.stringify(currentUser));
  } catch (e) {
    console.error("localStorageCurrentUserUpdate", e);
  }
}

export function fetchCurrentUser() {
  try {
    return JSON.parse(localStorage.getItem(CURRENT_USER));
  }
  catch (e) {
    console.error("fetchCurrentUser", e);
    return null;
  }
}

export function removeCurrentUser() {
  return localStorage.removeItem(CURRENT_USER);
}
