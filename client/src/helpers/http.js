import { constants } from "../helpers/constants";
import { fetchCurrentUser } from "../helpers/localStorage";

async function genericRequest(url, method, body) {

  try {
    const requestOptions = {
      method: method,
      headers: { "Content-Type": "application/json" },
    };
    // add body to request if it exists
    if (body) {
      requestOptions.body = body;
    }

    // add token to headers if it exists
    if (fetchCurrentUser()) {
      const userFromLocalStorage = fetchCurrentUser();
      requestOptions.headers["Authorization"] =userFromLocalStorage.accessToken;
    }

    const response = await fetch(`${constants.HOST}${url}`, requestOptions);
    const data = await response.json();

    return [response.status, data];
  } catch (e) {
    console.error(">>> HTTP " + method, e);
    return [500, { message: "Internal Server Error" }];
  }
}

export async function POST(url, body) {
  return await genericRequest(url, "POST", body);
}

export async function PATCH(url, body) {
  return await genericRequest(url, "PATCH", body);
}

export async function DELETE(url) {
  return await genericRequest(url, "DELETE", null);
}

export async function GET(url) {
  return await genericRequest(url, "GET", null);
}
