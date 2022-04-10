<template>
	<div>
		<div v-if="isFormOpen" class="container">
			<div class="input-container">
				<div class="input-text">Your post</div>
				<textarea
					v-model="wallPostContent"
					class="custom-text-area"
					spellcheck="false"
				/>
			</div>
			<div class="buttons-row">
				<button class="cancel-button" @click="toggleFormVisibility">
					CANCEL</button
				><button class="create-button" @click="createPost">POST</button>
			</div>
		</div>
		<div
			v-else
			class="create-post-button container"
			@click="toggleFormVisibility"
		>
			Post something on your wall
		</div>
	</div>
</template>

<script>
import { createWallPost } from "../../api/userAPI.js";
export default {
	name: "CreateWallPost",
	props: { userId: String },
	components: {},
	data: () => {
		return { isFormOpen: false, wallPostContent: "" };
	},
	mounted() {},
	methods: {
		toggleFormVisibility() {
			this.isFormOpen = !this.isFormOpen;
		},
		async createPost() {
			this.wallPostContent = this.wallPostContent.trim();
			if (this.wallPostContent.length == 0) {
				this.$toast.open({
					message: "Wall post must not be empty",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			}
			await createWallPost(this.userId, this.wallPostContent);
			this.toggleFormVisibility();
			this.wallPostContent = "";
			this.$emit("refresh");
		},
	},
};
</script>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 1rem;

	width: 50vw;
	height: fit-content;
	padding: 1rem;
	border-radius: 1rem;

	background-color: #222222;
	color: grey;
}

@media screen and (max-width: 1100px) {
	.container {
		width: 80vw;
	}
}

.create-post-button {
	text-align: center;
	color: white;
	cursor: pointer;
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
	font-size: 1.3rem;
}

.custom-text-area {
	border: none;
	border-radius: 0.3rem;
	height: 4rem;
	width: 100%;
	padding: 0 1rem;
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
