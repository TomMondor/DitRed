<template>
	<div class="header">
		<div class="display-links">
			<router-link to="/">Subs</router-link>
			<router-link to="/user">User</router-link>
			<router-link to="/conversations">Conversations</router-link>
			<router-link to="/sub">Sub</router-link>
			<router-link to="/sub-post">SubPost</router-link>
		</div>
	</div>
</template>

<script>
export default {
	name: "Header",
};
</script>

<style>
.display-links {
	border-bottom-width: 5px;
	border-bottom-style: solid;
	border-bottom-color: black;
	display: flex;
	align-items: center;
	gap: 10px;
	height: 60px;
}
.header {
	position: absolute;
	top: 0;
	left: 0;
	width: 100vw;
}
</style>
