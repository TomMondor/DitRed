<template>
	<div>
		<div v-if="isFormOpen" class="container">
			<div class="input-container">
				<div class="input-text">Sub post title</div>
				<input type="text" v-model="subPostTitle" class="custom-input" />
			</div>
			<div class="input-container">
				<div class="input-text">Sub post content</div>
				<textarea
					v-model="subPostContent"
					class="custom-text-area"
					spellcheck="false"
				/>
			</div>
			<div class="buttons-row">
				<button class="cancel-button" @click="toggleFormVisibility">
					CANCEL</button
				><button class="create-button" @click="createSubPost">POST</button>
			</div>
		</div>
		<div
			v-else
			class="container create-sub-post-button"
			@click="toggleFormVisibility"
		>
			Create post
		</div>
	</div>
</template>

<script>
import { createSubPost } from "../../api/subAPI";
export default {
	name: "CreateSubPost",
	props: { userId: String, subId: String },
	components: {},
	data: () => {
		return {
			isFormOpen: false,
			subPostTitle: "",
			subPostContent: "",
		};
	},
	mounted() {},
	methods: {
		toggleFormVisibility() {
			this.isFormOpen = !this.isFormOpen;
		},
		async createSubPost() {
			this.subPostTitle = this.subPostTitle.trim();
			if (this.subPostTitle.length < 3) {
				this.$toast.open({
					message: "Sub post title must be at least 3 characters long",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			}
			this.subPostContent = this.subPostContent.trim();
			if (this.subPostContent.length == 0) {
				this.$toast.open({
					message: "Sub post content must not be empty",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			}

			//si tout est conforme :
			await createSubPost(
				Number(this.userId),
				Number(this.subId),
				this.subPostTitle,
				this.subPostContent
			);
			this.toggleFormVisibility();
			this.subPostTitle = "";
			this.subPostContent = "";
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
	gap: 0.5rem;
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

.create-sub-post-button {
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
