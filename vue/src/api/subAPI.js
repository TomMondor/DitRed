const BASE_URL = "http://localhost:5000"; //TODO put the right PORT

export const getSubs = async function () {
	const response = await fetch(`${BASE_URL}/subs`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching subs.");
	}

	const jsonResponse = await response.json();
	return jsonResponse; //TODO extract data if necessary
};

export const getSub = async function (subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub's data.");
	}

	const jsonResponse = await response.json();
	return jsonResponse; //TODO extract data if necessary
};

export const getSubPosts = async function (subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub's posts.");
	}

	const jsonResponse = await response.json();
	return jsonResponse; //TODO extract data if necessary
};

export const getSubPost = async function (subId, postId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts/${postId}`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub post.");
	}

	const jsonResponse = await response.json();
	return jsonResponse; //TODO extract data if necessary
};

export const createSub = async function (subName, subDescription) {
	const response = await fetch(`${BASE_URL}/subs`, {
		method: "post",
		body: JSON.stringify({
			subName: subName,
			subDescription: subDescription,
		}),
		headers: new Headers({
			"Content-Type": "application/json", //TODO needs the token
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not create sub.");
	}
};

export const updateSub = async function (subId, subName, subDescription) {
	const response = await fetch(`${BASE_URL}/subs/${subId}`, {
		method: "post", // TODO PUT ?
		body: JSON.stringify({
			subName: subName,
			subDescription: subDescription,
		}),
		headers: new Headers({
			"Content-Type": "application/json", //TODO needs the token
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not update sub.");
	}
};

export const subscribe = async function (subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/subscribe`, {
		method: "post",
		headers: new Headers({
			//TODO needs the token
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not subscribe.");
	}
};

export const createSubPost = async function (subId, postTitle, postContent) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts`, {
		method: "post",
		body: JSON.stringify({
			postTitle: postTitle,
			postContent: postContent,
		}),
		headers: new Headers({
			"Content-Type": "application/json", //TODO needs the token
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not create sub post.");
	}
};

export const voteOnSubPost = async function (subId, postId, vote) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts${postId}/vote`,
		{
			method: "post",
			body: JSON.stringify({
				vote: vote,
			}),
			headers: new Headers({
				"Content-Type": "application/json", //TODO needs the token
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not vote on sub post.");
	}
};

export const createSubPostComment = async function (subId, postId, comment) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments`,
		{
			method: "post",
			body: JSON.stringify({
				comment: comment,
			}),
			headers: new Headers({
				"Content-Type": "application/json", //TODO needs the token
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not create sub post comment.");
	}
};

export const createSubPostCommentAnswer = async function (
	subId,
	postId,
	comment,
	answeredCommentId
) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments/${answeredCommentId}`,
		{
			method: "post",
			body: JSON.stringify({
				comment: comment,
			}),
			headers: new Headers({
				"Content-Type": "application/json", //TODO needs the token
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not create sub post comment.");
	}
};

export const voteOnSubPostComment = async function (
	subId,
	postId,
	commentId,
	vote
) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments/${commentId}/vote`,
		{
			method: "post",
			body: JSON.stringify({
				vote: vote,
			}),
			headers: new Headers({
				"Content-Type": "application/json", //TODO needs the token
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not vote on sub post comment.");
	}
};
