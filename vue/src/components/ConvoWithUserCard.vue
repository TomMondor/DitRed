<template>
	<router-link
		:to="{ name: 'Convo', params: { userId: this.userId } }"
		class="router-link"
	>
		<div class="convo-container">
			<img
				src="../../public/DitRed-logo.png"
				class="ditred-logo"
				alt="ditred-logo"
			/>
			<div class="username">{{ username }}</div>
		</div>
	</router-link>
</template>

<script>
export default {
	name: "ConvoWithUserCard",
	props: ["userId", "username"],
	methods: {
		async redirectToConvo() {
			this.$router.push("/conversations/" + this.userId);
		},
	},
};
</script>

<style scoped>
.router-link {
	text-decoration: none;
}

.convo-container {
	display: flex;
	flex-direction: row;
	width: 50vw;
	height: fit-content;
	padding: 2rem;

	align-items: center;
	justify-content: center;
	gap: 2rem;

	background-color: var(--background);

	border-radius: 3rem;

	color: var(--mainwhite);
}

.convo-container:hover {
	background-color: var(--primary);
	cursor: pointer;
}

.ditred-logo {
	width: 10vh;
	height: 10vh;
}

.username {
	font-size: 3rem;
	font-weight: bold;
	flex-grow: 1;
	flex-wrap: wrap;
	word-break: break-all;
	text-align: center;
}
</style>
