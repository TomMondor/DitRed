<template>
	<div>
		<h1 class="sub-header">Subbed</h1>
		<div class="subposts-section">
			<SubPostCard
				v-for="(post, index) in postsData"
				:key="index"
				:postId="Number(index)"
				:subId="post.sub_id"
				:subName="post.sub_name"
				:postCreator="post.creator_name"
				:timestamp="post.timestamp"
				:title="post.title"
				:content="post.content"
				:score="post.score"
				:comments_count="post.comments_count"
				:isALink="true"
				:userId="userId"
			/>
		</div>
	</div>
</template>

<script>
import SubPostCard from "../components/subs/SubPostCard.vue";
import { getSubbedPosts } from "../api/subbedAPI.js";
import Cookies from "js-cookie";

export default {
	name: "Subbed",
	components: {
		SubPostCard,
	},
	mounted() {
		this.getpostsData();
	},
	data: () => {
		return {
			userId: Cookies.get("userId"),
			postsData: {},
		};
	},
	methods: {
		async getpostsData() {
			this.postsData = await getSubbedPosts(this.userId);
		},
	},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

.sub-header {
	display: flex;
	width: 100%;
	height: fit-content;
	padding-top: 2rem;
	color: white;
	font-family: "Varela Round", sans-serif;
	font-size: 2rem;
	justify-content: center;
}

.subposts-section {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 100%;
	height: fit-content;
	padding-top: 4rem;
	padding-bottom: 4rem;
	gap: 4rem;
}
</style>
