<template>
	<div>
		<div>{{ userData.username }}</div>
		<div>{{ userData.email }}</div>
		<div>{{ userData.age }}</div>
		<div>Bio : {{ userData.bio }}</div>
		<div style="padding-top: 10px">Wallposts :</div>
		<div v-for="wallPost in userData.wallPosts" :key="wallPost[0]">
			<div style="padding-top: 10px">Wall post : {{ wallPost[0] }}</div>
		</div>
	</div>
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
			const data = await getUser(this.userId);
			this.userData = data[this.userId];
		},
	},
};
</script>

<style></style>
