const BASE_URL = "http://localhost:5000"; //TODO put the right PORT

export const getConvos = async function (userId) {
    const response = await fetch(`${BASE_URL}/convo`, {
        method: "get",
        headers: new Headers({
            user_id: userId, //TODO needs the token (remove userId input when done)
        }),
    });

    if (response.status != 200) {
        throw new Error("An error occured while fetching conversations.");
    }

    const jsonResponse = await response.json();
    return jsonResponse; //TODO extract data if necessary
};

export const getConvo = async function (myUserId, userId) {
    const response = await fetch(`${BASE_URL}/convo/${userId}`, {
        method: "get",
        headers: new Headers({
            user_id: myUserId, //TODO needs the token (remove myUserId input when done)
        }),
    });

    if (response.status != 200) {
        throw new Error("An error occured while fetching the conversation.");
    }

    const jsonResponse = await response.json();
    return jsonResponse; //TODO extract data if necessary
};

export const createMessage = async function (userId, message) {
    const response = await fetch(`${BASE_URL}/convo/${userId}`, {
        method: "post",
        body: JSON.stringify({
            message: message,
        }),
        headers: new Headers({
            "Content-Type": "application/json", //TODO needs the token
        }),
    });

    if (response.status != 201) {
        throw new Error("Could not send message.");
    }
};
