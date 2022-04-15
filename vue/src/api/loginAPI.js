import Cookies from "js-cookie";

const BASE_URL = "http://localhost:5000";

export const login = async function (username, password) {
	const response = await fetch(`${BASE_URL}/login`, {
		method: "post",
		body: JSON.stringify({
			username: username,
			password: password,
		}),
		headers: new Headers({
			Accept: "application/json",
			"Content-Type": "application/json",
		}),
	});

	if (response.status != 200) {
		throw new Error("Username/password combination is invalid");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const validateCookies = async function () {
	const userId = Cookies.get("userId");
	const loginToken = Cookies.get("loginToken");

	const response = await fetch(`${BASE_URL}/validate`, {
		method: "get",
		headers: new Headers({
			userId: userId,
			loginToken: loginToken,
		}),
	});

	if (response.status != 200) {
		throw new Error("Could not validate cookies");
	}

	const jsonResponse = await response.json();

	return jsonResponse["valid"];
};
