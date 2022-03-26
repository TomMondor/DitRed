<template>
	<div>User {{ userData.username }} User</div>
</template>

<script>
import { getUser } from "../api/userAPI.js";

export default {
	name: "User",
	mounted() {
		this.getUserData();
	},
	data: () => {
		return {
			userData: {},
			userId: 17, //TODO get real value
		};
	},
	methods: {
		async getUserData() {
			this.userData = await getUser(this.userId);
		},
	},
};
</script>

<style></style>
