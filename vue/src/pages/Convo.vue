<template>
	<div>
		<div :key="convoBubblesKey" class="convo-container">
			<h1 class="convo-header">Convo:</h1>
			<convo-bubble
				v-for="(messageData, messageId) in convoData"
				:key="messageId"
				:message="messageData['content']"
				:timestamp="messageData['timestamp']"
				:class="[
					messageData['sender_id'] == userId ? 'left-bubble' : 'right-bubble',
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
				autocomplete="off"
			/>
			<div class="write-message-button">
				<font-awesome-icon
					class="send-icon"
					icon="fa-solid fa-paper-plane"
					@click="sendMessage"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import { getConvo } from "../api/convoAPI.js";
import { createMessage } from "../api/convoAPI.js";
import ConvoBubble from "../components/ConvoBubble.vue";
import Cookies from "js-cookie";

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
	},
	data: () => {
		return {
			convoData: {},
			myUserId: Cookies.get("userId"),
			message: "",
			convoBubblesKey: 0,
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
					myUserId: this.myUserId,
					userId: this.userId,
					message: this.message,
				});
				this.createNewMessageItem(this.message, this.userId, this.myUserId);
				createMessage(this.myUserId, this.userId, this.message);
			}
			this.message = "";
		},
		setUpPrivateMessageSocket() {
			this.private_socket = io("http://localhost:5000/private");
			this.private_socket.emit("user_id", this.myUserId);
		},
		setUpReceiveMessages() {
			this.private_socket.on("new_private_message", (payload) => {
				if (Object.keys(payload)[0] == this.userId) {
					this.createNewMessageItem(
						payload[this.userId],
						this.myUserId,
						this.userId
					);
				}
			});
		},
		createNewMessageItem(message, receiverId, senderId) {
			const messageId = uuidv4();
			const messageData = {
				content: message,
				receiver_id: receiverId,
				sender_id: senderId,
				timestamp: new Date().toLocaleString(),
			};
			this.convoData[messageId] = messageData;
			this.forceUpdate();
			window.scrollTo(0, document.body.scrollHeight);
		},
		forceUpdate() {
			this.convoBubblesKey++;
		},
	},
};
</script>

<style scoped>
.convo-header {
	color: var(--mainwhite);
	background-color: #0e0b0b;
	position: fixed;
	top: 3.5rem;
	left: 0;
	width: 100%;

	height: 4rem;
	padding-top: 1.5rem;
	padding-left: 0.5rem;
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
	padding: 1rem;

	font-size: 1.3rem;
}

.write-message-button {
	display: flex;
	justify-content: center;
	align-items: center;
	color: var(--background);
	width: 3.5rem;
	height: 3.5rem;
	background-color: var(--mainwhite);
	border-radius: 50%;
}

.write-message-button:hover {
	cursor: pointer;
	color: var(--primary);
}

.send-icon {
	margin-left: -10%;
	width: 60%;
	height: 60%;
}
</style>
