<template>
	<div>
		<div v-if="isSelectorOpen" class="selection-container">
			<div>
				<input
					v-focus
					autocomplete="off"
					spellcheck="false"
					class="username-textarea"
					v-model="potentialUsername"
					placeholder="Select a user..."
					@focusout="toggleSelectorVisibility"
				/>
			</div>
			<div class="suggestions-section">
				<div
					class="name-suggestion"
					v-for="username of correspondingUsernames"
					:key="username"
					@mousedown="selectUsername(username)"
				>
					{{ username }}
				</div>
			</div>
		</div>
		<div v-if="isSelectorOpen" class="arrow-right"></div>
		<div
			v-if="!isSelectorOpen"
			class="selection-icon-container"
			@click="toggleSelectorVisibility"
		>
			<font-awesome-icon
				icon="fa-solid fa-magnifying-glass"
				class="selection-icon"
			/>
		</div>
		<div :key="isSelectorOpen" v-else class="selection-icon-container">
			<font-awesome-icon
				icon="fa-solid fa-magnifying-glass"
				class="selection-icon"
			/>
		</div>
	</div>
</template>

<script>
import { searchUsers } from "../../api/userAPI";

export default {
	name: "UserSelector",
	props: {},
	components: {},
	data: () => {
		return {
			isSelectorOpen: false,
			potentialUsername: "",
			correspondingUsernames: [],
			awaitingSearch: false,
		};
	},
	mounted() {},
	methods: {
		selectUsername(user) {
			this.$emit("userSelected", user);
		},
		async validateUsername() {
			this.correspondingUsernames = await searchUsers(this.potentialUsername);
		},
		toggleSelectorVisibility() {
			this.isSelectorOpen = !this.isSelectorOpen;
		},
	},
	directives: {
		focus: {
			inserted: function (el) {
				el.focus();
			},
		},
	},
	watch: {
		potentialUsername: function (newValue) {
			if (!this.awaitingSearch) {
				setTimeout(() => {
					this.validateUsername();
					this.awaitingSearch = false;
				}, 500);
			}
			this.awaitingSearch = true;
		},
	},
};
</script>

<style scoped>
.selection-container {
	position: absolute;
	top: 83px;
	right: 90px;
	width: 300px;
	max-width: 70vw;
	border-radius: 1rem;
	border: 5px solid rgb(73, 73, 73);
	background-color: rgb(73, 73, 73);
	padding-bottom: 0.5rem;
	z-index: 1;
}

.arrow-right {
	position: absolute;
	top: 87px;
	right: 80px;
	width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-bottom: 25px solid transparent;

	border-left: 30px solid rgb(73, 73, 73);
}

.selection-icon-container {
	position: absolute;
	top: 80px;
	right: 20px;
	cursor: pointer;
	color: orangered;
	background-color: rgb(73, 73, 73);
	width: fit-content;
	padding: 15px;
	border-radius: 100%;
}

.username-textarea {
	border: none;
	width: 100%;
	display: flex;
	height: fit-content;
	padding: 0.5rem;
	font-size: 1.3rem;
	border-radius: 1rem 1rem 0 0;
	background-color: rgb(73, 73, 73);
	color: orange;
}

.suggestions-section {
	height: fit-content;
	max-height: 35vh;
	overflow-y: scroll;
	display: flex;
	flex-direction: column;
}

.suggestions-section::-webkit-scrollbar {
	width: 7px;
	height: 8px;
}
.suggestions-section::-webkit-scrollbar-thumb {
	background-color: var(--background);
	border-radius: 10px;
}

.suggestions-section::-webkit-scrollbar-thumb:hover {
	background-color: black;
}

.name-suggestion {
	padding: 0.5rem 0rem 0.5rem 1rem;
	font-weight: bold;
	color: orange;
	font-size: 1.2rem;
}
.name-suggestion:hover {
	background-color: #0e0b0b;
	cursor: pointer;
}

.selection-icon {
	width: 2rem;
	height: 2rem;
}
</style>
