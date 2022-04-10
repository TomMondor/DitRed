<template>
	<div class="container">
		<img
			src="../../../public/DitRed-logo.png"
			class="ditred-logo"
			alt="ditred-logo"
		/>
		<div class="name">{{ name }}</div>
		<div class="info">
			<div>Score: <span class="score">XXXX</span></div>
			<div v-if="timestamp != undefined">
				Member since:
				<span class="timestamp">{{ timestamp.slice(5, 16) }}</span>
			</div>
		</div>
		<div class="bio">
			<h1>BIO</h1>
			{{ bio }}
		</div>
	</div>
</template>

<script>
export default {
	name: "UserCard",
	props: ["name", "timestamp", "bio"],
};
</script>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 30vw;
	height: fit-content;
	padding: 2rem;

	background-color: var(--background);

	border-radius: 1rem;

	color: var(--mainwhite);
}

@media screen and (max-width: 1100px) {
	.container {
		width: 50vw;
	}
}

.ditred-logo {
	width: 10vw;
	height: 10vw;
}

.name {
	font-size: 3rem;
	font-weight: bold;
	color: orange;
}

.info {
	display: flex;
	gap: 1rem;
}

.score {
	color: orangered;
}

.timestamp {
	color: orange;
}

.bio {
	font-size: 1rem;
	color: var(--mainwhite);
}
</style>
