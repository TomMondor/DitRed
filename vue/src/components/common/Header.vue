<template>
	<div class="hp-header">
		<div class="hp-logo-container">
			<img
				src="../../../public/DitRed-logo.png"
				class="hp-ditred-logo"
				alt="ditred-logo"
			/>
			<div class="hp-ditred-text">ditred</div>
		</div>
		<div class="hp-display-links">
			<router-link to="/"
				><font-awesome-icon class="hp-header-icon" icon="fa-solid fa-list-ul"
			/></router-link>
			<router-link to="/user"
				><font-awesome-icon class="hp-header-icon" icon="fa-solid fa-user"
			/></router-link>
			<router-link to="/conversations"
				><font-awesome-icon
					class="hp-header-icon"
					icon="fa-solid fa-comment-dots"
			/></router-link>
			<router-link to="/sub-post"
				><font-awesome-icon
					class="hp-header-icon"
					icon="fa-solid fa-chalkboard-user"
			/></router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: "Header",
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

.hp-display-links {
	display: flex;
	align-items: center;
	gap: 1rem;
}
.hp-header {
	display: flex;
	align-items: center;
	gap: 2vw;

	position: sticky;
	top: 0;
	left: 0;
	width: 100%;

	height: 3.5rem;

	background-color: var(--background);

	z-index: 1000;
}

.hp-header-icon {
	height: 1.3rem;
	color: var(--mainwhite);
}

.hp-header-icon:hover {
	color: var(--primary);
}

.hp-logo-container {
	margin-left: 1vw;
	display: flex;
	gap: 0.3rem;
	align-items: center;
	color: var(--mainwhite);

	height: 100%;
}

.hp-ditred-text {
	font-family: "Varela Round", sans-serif;
	font-size: 1.3rem;
	font-weight: bold;
}

.hp-ditred-logo {
	height: 2rem;
}
</style>
