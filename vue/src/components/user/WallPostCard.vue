<template>
	<div class="container">
		{{ content }}
	</div>
</template>

<script>
export default {
	name: "WallPostCard",
	props: ["content"],
};
</script>

<style scoped>
.container {
	display: flex;
	width: 50vw;
	height: fit-content;
	padding: 2rem;

	background-color: var(--background);

	border-radius: 1rem;

	color: var(--mainwhite);
}

@media screen and (max-width: 1100px) {
	.container {
		width: 80vw;
	}
}
</style>
