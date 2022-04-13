<template>
	<div>
		<div v-if="isFormOpen" class="sub-container">
			<div class="input-container">
				<div class="input-text">Sub name</div>
				<input type="text" v-model="subName" class="custom-input" />
			</div>
			<div class="input-container">
				<div class="input-text">Sub description</div>
				<textarea
					v-model="subDescription"
					class="custom-text-area"
					spellcheck="false"
				/>
			</div>
			<div class="buttons-row">
				<button class="cancel-button" @click="toggleFormVisibility">
					CANCEL</button
				><button class="create-button" @click="createSub">CREATE SUB</button>
			</div>
		</div>
		<div
			v-else
			class="create-sub-button sub-container"
			@click="toggleFormVisibility"
		>
			Create your own sub
		</div>
	</div>
</template>

<script>
import { createSub, subscribe } from "../../api/subAPI";

export default {
	name: "CreateSub",
	props: { userId: String },
	components: {},
	data: () => {
		return {
			isFormOpen: false,
			subName: "r/",
			subDescription: "",
			createdSubId: null,
		};
	},
	mounted() {},
	methods: {
		toggleFormVisibility() {
			this.isFormOpen = !this.isFormOpen;
		},
		async createSub() {
			this.subName = this.subName.replace("r/", "").trim();
			if (this.subName.length < 3) {
				this.$toast.open({
					message: "Sub name must be at least 3 characters long",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			}
			this.subDescription = this.subDescription.trim();
			if (this.subDescription.length == 0) {
				this.$toast.open({
					message: "Sub description must not be empty",
					type: "error",
					position: "top-right",
					duration: 2000,
					dismissible: true,
				});
				return;
			}

			//si tout est conforme :
			const response = await createSub(
				this.userId,
				this.subName,
				this.subDescription
			);
			this.createdSubId = response["sub_id"];
			this.toggleFormVisibility();
			this.subName = "r/";
			this.subDescription = "";
			this.subscribe();
			this.$emit("refresh");
		},
		async subscribe() {
			try {
				await subscribe(this.userId, this.createdSubId);
				this.$toast.open({
					message: "You are now subscribed to the created sub!",
					type: "success",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			} catch (error) {}
		},
	},
};
</script>

<style scoped>
.sub-container {
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
	.sub-container {
		width: 80vw;
	}
}

.create-sub-button {
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
