<template>
	<div class="selection-box">TEST</div>
</template>

<script>
export default {
	name: "UserSelector",
	props: {},
	components: {},
	data: () => {
		return {};
	},
	mounted() {},
	methods: {
		selectUser(user) {
			this.$emit("userSelected", user);
		},
	},
};
</script>

<style scoped>
.selection-box {
	position: absolute;
	top: 60px;
	right: 30px;
	background-color: white;
}
</style>
