const BASE_URL = "http://localhost:5000";

export const getConvos = async function (userId) {
	const response = await fetch(`${BASE_URL}/convo`, {
		method: "get",
		credentials: "include",
		headers: new Headers({
			userId: userId,
		}),
	});

	if (response.status != 200) {
		throw new Error("An error occured while fetching conversations.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const getConvo = async function (myUserId, userId) {
	const response = await fetch(`${BASE_URL}/convo/${userId}`, {
		method: "get",
		credentials: "include",
		headers: new Headers({
			userId: myUserId,
		}),
	});

	if (response.status != 200) {
		throw new Error("An error occured while fetching the conversation.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const createMessage = async function (myUserId, userId, message) {
	const response = await fetch(`${BASE_URL}/convo/${userId}`, {
		method: "post",
		credentials: "include",
		body: JSON.stringify({
			message: message,
		}),
		headers: new Headers({
			"Content-Type": "application/json",
			userId: myUserId,
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not send message.");
	}
};
