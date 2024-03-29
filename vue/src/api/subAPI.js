const BASE_URL = "http://localhost:5000";

export const getSubs = async function () {
	const response = await fetch(`${BASE_URL}/subs`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching subs.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const getSub = async function (subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub's data.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const getSubPosts = async function (subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub's posts.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const getSubPost = async function (subId, postId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts/${postId}`);

	if (response.status != 200) {
		throw new Error("An error occured while fetching the sub post.");
	}

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const createSub = async function (userId, subName, subDescription) {
	const response = await fetch(`${BASE_URL}/subs`, {
		method: "post",
		credentials: "include",
		body: JSON.stringify({
			name: subName,
			description: subDescription,
			creator_id: userId,
		}),
		headers: new Headers({
			"Content-Type": "application/json",
		}),
	});

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const updateSub = async function (
	userId,
	subId,
	subName,
	subDescription
) {
	const response = await fetch(`${BASE_URL}/subs/${subId}`, {
		method: "put",
		credentials: "include",
		body: JSON.stringify({
			name: subName,
			description: subDescription,
			creator_id: userId,
		}),
		headers: new Headers({
			"Content-Type": "application/json",
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not update sub.");
	}
	const jsonResponse = await response.json();
	return jsonResponse;
};

export const subscribe = async function (userId, subId) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/subscribe`, {
		method: "post",
		credentials: "include",
		body: JSON.stringify({
			user_id: userId,
		}),
		headers: new Headers({
			"Content-Type": "application/json",
		}),
	});

	if (response.status != 201) {
		throw new Error("Could not subscribe.");
	}
};

export const createSubPost = async function (
	userId,
	subId,
	postTitle,
	postContent
) {
	const response = await fetch(`${BASE_URL}/subs/${subId}/posts`, {
		method: "post",
		credentials: "include",
		body: JSON.stringify({
			title: postTitle,
			content: postContent,
			creator_id: userId,
		}),
		headers: new Headers({
			"Content-Type": "application/json",
		}),
	});

	const jsonResponse = await response.json();
	return jsonResponse;
};

export const voteOnSubPost = async function (userId, subId, postId, vote) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/vote`,
		{
			method: "post",
			credentials: "include",
			body: JSON.stringify({
				voter_id: userId,
				vote: vote,
			}),
			headers: new Headers({
				"Content-Type": "application/json",
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not vote on sub post.");
	}
};

export const createSubPostComment = async function (
	userId,
	subId,
	postId,
	comment
) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments`,
		{
			method: "post",
			credentials: "include",
			body: JSON.stringify({
				user_id: userId,
				comment: comment,
			}),
			headers: new Headers({
				"Content-Type": "application/json",
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not create sub post comment.");
	}
};

export const createSubPostCommentAnswer = async function (
	userId,
	subId,
	postId,
	comment,
	answeredCommentId
) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments/${answeredCommentId}`,
		{
			method: "post",
			credentials: "include",
			body: JSON.stringify({
				user_id: userId,
				comment: comment,
			}),
			headers: new Headers({
				"Content-Type": "application/json",
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not create sub post comment.");
	}
};

export const voteOnSubPostComment = async function (
	userId,
	subId,
	postId,
	commentId,
	vote
) {
	const response = await fetch(
		`${BASE_URL}/subs/${subId}/posts/${postId}/comments/${commentId}/vote`,
		{
			method: "post",
			credentials: "include",
			body: JSON.stringify({
				voter_id: userId,
				vote: vote,
			}),
			headers: new Headers({
				"Content-Type": "application/json",
			}),
		}
	);

	if (response.status != 201) {
		throw new Error("Could not vote on sub post comment.");
	}
};
