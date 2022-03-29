<template>
    <div>
        <div class="convo-container">
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
        <div class="write-message">
            <textarea
                class="write-message-textarea"
                v-model="message"
                placeholder="Write a message..."
                @keydown.enter="sendMessage"
            ></textarea>
            <button class="write-message-button" @click="sendMessage">
                Send
            </button>
        </div>
    </div>
</template>

<script>
import { getConvo } from "../api/convoAPI.js";
import ConvoBubble from "../components/ConvoBubble.vue";

export default {
    name: "Convos",
    components: { ConvoBubble },
    mounted() {
        this.getConvoData();
    },
    data: () => {
        return {
            convoData: {},
            myUserId: 17, //TODO get real value
            userId: 1, //TODO get real value
        };
    },
    methods: {
        async getConvoData() {
            this.convoData = await getConvo(this.myUserId, this.userId);
        },
    },
};
</script>

<style>
.convo-header {
    color: var(--mainwhite);
}

.convo-container {
    width: 90vw;
    margin: 0 auto;
    margin-top: 7rem;
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
