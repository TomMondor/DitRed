<template>
	<div>
		<UserSelector @userSelected="redirectToUserPage" />
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
			<CreateWallPost :userId="userId" @refresh="getUserData" />
			<WallPostCard
				v-for="(wallPost, index) in wallPosts"
				:key="wallPost[0] + index"
				:content="wallPost[0]"
			/>
		</div>
	</div>
</template>

<script>
import { getUser } from "../api/userAPI.js";
import WallPostCard from "../components/user/WallPostCard.vue";
import UserCard from "../components/user/UserCard.vue";
import CreateWallPost from "../components/user/CreateWallPost.vue";
import UserSelector from "../components/common/UserSelector.vue";
import Cookies from "js-cookie";

export default {
	name: "LoggedUser",
	components: {
		WallPostCard,
		UserCard,
		CreateWallPost,
		UserSelector,
	},
	mounted() {
		this.getUserData();
	},
	data: () => {
		return {
			userData: {},
			wallPosts: [],
			userId: Cookies.get("userId"),
		};
	},
	methods: {
		async getUserData() {
			const data = await getUser(this.userId);
			this.userData = data[this.userId];
			this.wallPosts = [...this.userData.wallPosts];
			this.wallPosts.reverse();
		},
		redirectToUserPage(user) {
			this.$router.push("/user/" + user);
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
