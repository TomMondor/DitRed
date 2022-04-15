<template>
	<div>
		<div class="container">
			<div class="input-container">
				<textarea
					v-model="commentContent"
					class="custom-text-area"
					spellcheck="false"
					placeholder="What are your thoughts?"
				/>
			</div>
			<div class="buttons-row">
				<button class="cancel-button" @click="toggleFormVisibility">
					CANCEL</button
				><button class="create-button" @click="createComment">REPLY</button>
			</div>
		</div>
	</div>
</template>

<script>
import { createSubPostCommentAnswer } from "../../api/subAPI.js";
export default {
	name: "CreateComment",
	props: {
		userId: String,
		postId: String,
		subId: String,
		parentCommentId: String,
	},
	components: {},
	data: () => {
		return {
			commentContent: "",
		};
	},
	mounted() {},
	methods: {
		async createComment() {
			this.commentContent = this.commentContent.trim();
			if (this.commentContent.length == 0) {
				this.$toast.open({
					message: "Comment must not be empty",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			} else if (this.commentContent.length > 3000) {
				this.$toast.open({
					message: "Comment is too long",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			} else {
				await createSubPostCommentAnswer(
					Number(this.userId),
					Number(this.subId),
					Number(this.postId),
					this.commentContent,
					Number(this.parentCommentId)
				);
				this.$emit("refresh");
				this.commentContent = "";
				this.toggleFormVisibility();
			}
		},
		toggleFormVisibility() {
			this.$emit("toggleFormVisibility");
		},
	},
};
</script>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
}

.input-container {
	width: 60%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 0.5rem;
}

.input-text {
	width: 100%;
	text-align: left;
	color: var(--mainwhite);
	font-size: 1rem;
}

.custom-input {
	border: none;
	border-radius: 0.3rem;
	height: 2rem;
	width: 100%;
	padding: 0 1rem;
}

.custom-text-area {
	border: none;
	border-radius: 0.3rem;
	height: 4rem;
	width: 100%;
	padding: 0 1rem;
	background-color: var(--background);
	color: var(--mainwhite);
}

.buttons-row {
	width: 60%;
	display: flex;
	flex-direction: row;
	gap: 0.5rem;
}

.create-button {
	font-family: "Varela Round", sans-serif;

	width: 60%;
	height: 2rem;
	border: none;
	border-radius: 0.3rem;
	background-color: var(--primary);
	color: var(--mainwhite);

	font-weight: bold;
}

.create-button:hover {
	cursor: pointer;
	background-color: var(--mainwhite);
	color: var(--primary);
}

.cancel-button {
	font-family: "Varela Round", sans-serif;

	width: 60%;
	height: 2rem;
	border: none;
	border-radius: 0.3rem;
	background-color: var(--secondary);
	color: black;

	font-weight: bold;
}

.cancel-button:hover {
	cursor: pointer;
	background-color: var(--mainwhite);
	color: var(--primary);
}
</style>
