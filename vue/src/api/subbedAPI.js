const BASE_URL = "http://localhost:5000";

export const getSubbedPosts = async function (userId) {
	const response = await fetch(`${BASE_URL}/subbed`, {
		method: "get",
		credentials: "include",
		headers: new Headers({
			userId: userId,
		}),
	});

	if (response.status != 200) {
		throw new Error("An error occured while fetching the subbed posts.");
	}

	const jsonResponse = await response.json();
	return jsonResponse; //TODO extract data if necessary
};
