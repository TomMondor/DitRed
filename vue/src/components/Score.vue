<template>
	<div class="score-container">
		<font-awesome-icon icon="fa-solid fa-arrow-up" class="arrow arrow-up" />
		<div class="score-text" :class="[score < 0 ? 'center-when-neg' : '']">
			{{ score }}
		</div>
		<font-awesome-icon icon="fa-solid fa-arrow-down" class="arrow arrow-down" />
	</div>
</template>

<script>
export default {
	name: "Score",
	props: ["score"],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.score-container {
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
	width: fit-content;
	height: fit-content;
	padding: 1rem;

	justify-content: center;
}

.score-text {
	color: white;
	text-align: center;
}

.center-when-neg {
	text-align: left;
}

.arrow {
	color: grey;
	height: 1.5rem;
	width: 1.5rem;
}

.arrow:hover {
	cursor: pointer;
}

.arrow-down:hover {
	color: darkblue;
}

.arrow-up:hover {
	color: red;
}
</style>
