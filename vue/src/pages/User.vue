<template>
	<div>
		<UserSelector :key="username" @userSelected="redirectToUserPage" />
		<div class="user-card-container">
			<UserCard
				:name="userData.username"
				:timestamp="userData.memberSince"
				:bio="userData.bio"
			/>
		</div>

		<div class="wall-posts-container">
			<h1
				v-if="userData.wallPosts != undefined && userData.wallPosts.length > 0"
				class="wallposts-header"
			>
				Wallposts
			</h1>
			<h1 v-else class="wallposts-header">No wallposts yet</h1>
			<WallPostCard
				v-for="wallPost in userData.wallPosts"
				:key="wallPost[0]"
				:content="wallPost[0]"
			/>
		</div>
	</div>
</template>

<script>
import { getUserByUsername } from "../api/userAPI.js";
import WallPostCard from "../components/user/WallPostCard.vue";
import UserCard from "../components/user/UserCard.vue";
import UserSelector from "../components/common/UserSelector.vue";

export default {
	name: "User",
	components: {
		WallPostCard,
		UserCard,
		UserSelector,
	},
	mounted() {
		this.getUsername();
		this.getUserData();
	},
	data: () => {
		return {
			userData: {},
			userId: "",
			username: "",
		};
	},
	methods: {
		getUsername() {
			this.username = this.$router.currentRoute.params.username;
		},
		async getUserData() {
			const data = await getUserByUsername(this.username);
			this.userId = Object.keys(data)[0];
			this.userData = data[this.userId];
		},
		redirectToUserPage(user) {
			this.$router.push("/user/" + user);
		},
	},
	watch: {
		"$route.path": function (newRoute, oldRoute) {
			this.getUsername();
			this.getUserData();
		},
	},
};
</script>

<style>
.user-card-container {
	margin-top: 5rem;
	display: flex;
	justify-content: center;
}

.wallposts-header {
	color: orange;

	background-color: var(--background);
	border-radius: 2rem;
	padding: 0.7rem;
}

.wall-posts-container {
	margin-top: 2rem;

	display: flex;
	flex-direction: column;
	gap: 1rem;
	padding: 1rem;

	align-items: center;
}
</style>
