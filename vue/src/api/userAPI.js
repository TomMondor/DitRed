const BASE_URL = "http://localhost:5000"; //TODO put the right PORT

export const getAllUsers = async function () {
    const response = await fetch(`${BASE_URL}/users`);

    if (response.status != 200) {
        throw new Error("An error occured while fetching users data.");
    }

    const jsonResponse = await response.json();
    return jsonResponse; //TODO extract data if necessary
};

export const getUser = async function (userId) {
    const response = await fetch(`${BASE_URL}/users/${userId}`);

    if (response.status != 200) {
        throw new Error("An error occured while fetching the user's data.");
    }

    const jsonResponse = await response.json();
    return jsonResponse; //TODO extract data if necessary
};

export const createUser = async function (username, password, email, bio, age) {
    const response = await fetch(`${BASE_URL}/users`, {
        method: "post",
        body: JSON.stringify({
            username: username,
            password: password,
            email: email,
            bio: bio,
            age: age,
        }),
        headers: new Headers({
            "Content-Type": "application/json",
        }),
    });

    if (response.status != 201) {
        throw new Error("Could not create user.");
    }
};

export const createWallPost = async function (ownUserId, wallPostContent) {
    const response = await fetch(`${BASE_URL}/users/${userId}`, {
        method: "post",
        body: JSON.stringify({
            wallPostContent: wallPostContent,
        }),
        headers: new Headers({
            "Content-Type": "application/json", //TODO needs the token
        }),
    });

    if (response.status != 201) {
        throw new Error("Could not create wall post.");
    }
};
