<template>
    <div>
        <div id="test" class="convo-container">
            <h1 class="convo-header">Convo:</h1>
            <convo-bubble
                v-for="(messageData, messageId) in convoData"
                :key="messageId"
                :message="messageData['content']"
                :timestamp="messageData['timestamp']"
                :class="[
                    messageData['sender_id'] == userId
                        ? 'left-bubble'
                        : 'right-bubble',
                ]"
            />
        </div>
        <div id="message-form" class="write-message">
            <input
                id="message-input"
                class="write-message-textarea"
                v-model="message"
                placeholder="Write a message..."
                @keydown.enter="sendMessage"
            />
            <button class="write-message-button" @click="sendMessage">
                Send
            </button>
        </div>
    </div>
</template>

<script>
import { getConvo } from "../api/convoAPI.js";
import { createMessage } from "../api/convoAPI.js";
import ConvoBubble from "../components/ConvoBubble.vue";

const { v4: uuidv4 } = require("uuid");
const io = require("socket.io-client");

export default {
    name: "Convos",
    components: { ConvoBubble },
    mounted() {
        this.getUserId();
        this.getConvoData();
        this.setUpPrivateMessageSocket();
        this.setUpReceiveMessages();
        console.log(document.getElementById("test").scrollHeight);
        document.getElementById("test").scrollTop =
            document.getElementById("test").scrollHeight;
    },
    data: () => {
        return {
            convoData: {},
            myUserId: 17, //TODO get real value
            message: "",
        };
    },
    methods: {
        async getConvoData() {
            this.convoData = await getConvo(this.myUserId, this.userId);
        },
        async getUserId() {
            this.userId = this.$router.currentRoute.params.userId;
        },
        sendMessage() {
            if (this.message) {
                this.private_socket.emit("private_message", {
                    user_id: this.userId,
                    message: this.message,
                });
                this.createNewMessageItem(this.message, this.myUserId);
                createMessage(this.myUserId, this.userId, this.message);
            }
            this.message = "";
        },
        setUpPrivateMessageSocket() {
            this.private_socket = io("http://localhost:5000/private");
            this.private_socket.emit("user_id", this.myUserId);
        },
        setUpReceiveMessages() {
            this.private_socket.on("new_private_message", function (message) {
                this.createNewMessageItem(message, this.userId);
            });
        },
        createNewMessageItem(message, userId) {
            const messageId = uuidv4();
            const messageData = {
                content: message,
                sender_id: userId,
                timestamp: new Date().toLocaleString(),
            };
            this.convoData[messageId] = messageData;
        },
    },
};
</script>

<style scoped>
.convo-header {
    color: var(--mainwhite);
}

.convo-container {
    width: 90vw;
    height: fit-content;
    margin: 0 auto;
    margin-top: 5rem;
    margin-bottom: 7rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.left-bubble {
    align-self: flex-start;
    background-color: var(--backgroundlighter);
}

.right-bubble {
    align-self: flex-end;
    background-color: var(--background);
}

.write-message {
    width: 90vw;
    margin: 0 auto;
    margin-top: 2rem;
    margin-bottom: 2rem;
    display: flex;
    gap: 2rem;
}

.write-message-textarea {
    border: none;
    border-radius: 1rem;
    width: 80%;
    display: flex;
    height: fit-content;
    padding-left: 1rem;
    padding-top: 1rem;

    font-size: 1.3rem;
}

.write-message-button {
}
</style>
