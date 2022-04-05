<template>
	<div class="subposts-container">
		<SubPostCard
			:postId="postId"
			:subId="subId"
			:subName="subName"
			:postCreator="subPostData.creator_name"
			:timestamp="subPostData.timestamp"
			:title="subPostData.title"
			:content="subPostData.content"
			:score="subPostData.score"
			:comments_count="subPostData.comments_count"
			:isALink="false"
			class="subpost-card"
		/>
		<PostComments
			v-if="subPostData.comments != undefined"
			:commentsData="subPostData.comments"
		/>
	</div>
</template>

<script>
import SubPostCard from "../components/subs/SubPostCard.vue";
import PostComments from "../components/subs/PostComments.vue";
import { getSubPost, getSub } from "../api/subAPI.js";

export default {
	name: "SubPost",
	components: {
		SubPostCard,
		PostComments,
	},
	mounted() {
		this.getIdsFromURL();
		this.getSubData();
		this.getSubPostData();
	},
	data: () => {
		return {
			subName: "",
			subId: "",
			postId: "",
			subPostData: {},
		};
	},
	methods: {
		getIdsFromURL() {
			this.postId = this.$router.currentRoute.params.subPostId;
			this.subId = this.$router.currentRoute.params.subId;
		},
		async getSubPostData() {
			this.subPostData = await getSubPost(this.subId, this.postId);
		},
		async getSubData() {
			let subData = await getSub(this.subId);
			subData = subData[this.subId];
			this.subName = subData.name;
		},
	},
};
</script>

<style scoped>
.subposts-container {
	margin-top: 5rem;
	display: flex;
	flex-direction: column;
	align-items: center;

	color: var(--mainwhite);
}

.subpost-card {
	z-index: 1;
}
</style>
