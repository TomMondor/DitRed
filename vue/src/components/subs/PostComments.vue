<template>
	<div class="comments-outer-container">
		<div class="comments-inner-container">
			<CreateCommentAtRoot
				v-if="connected"
				@refresh="refresh"
				:userId="userId"
				:postId="postId"
				:subId="subId"
			/>
			<PostComment
				v-for="child in Object.keys(commentsTree)"
				:key="child"
				:commentId="child"
				:commentsData="commentsData"
				:subTree="commentsTree[child]"
				:userId="userId"
				:postId="postId"
				:subId="subId"
				@refresh="refresh"
			/>
		</div>
	</div>
</template>

<script>
import PostComment from "./PostComment.vue";
import CreateCommentAtRoot from "./CreateCommentAtRoot.vue";
import { validateCookies } from "../../api/loginAPI.js";

export default {
	name: "PostComments",
	props: {
		commentsData: Object,
		userId: String,
		postId: String,
		subId: String,
	},
	components: {
		PostComment,
		CreateCommentAtRoot,
	},
	data: () => {
		return {
			commentsTree: {},
			connected: false,
		};
	},
	async mounted() {
		this.buildCommentsTree();

		if (await validateCookies()) {
			this.connected = true;
		} else {
			this.connected = false;
		}
	},
	methods: {
		buildCommentsTree() {
			// lister les ids de comments du + grand au + petit
			let commentIds = Object.keys(this.commentsData).sort(function (a, b) {
				return b - a;
			});

			// créer l'arbre de base
			this.commentsTree = {};
			for (let commentId of commentIds) {
				this.commentsTree[commentId] = {};
			}

			// déplacer les noeuds de l'arbre dans leur parent
			for (let commentId of commentIds) {
				let parent = this.commentsData[commentId].answers_to;
				if (parent != null) {
					let children = this.commentsTree[commentId];
					delete this.commentsTree[commentId];
					this.commentsTree[parent][commentId] = children;
				}
			}
		},
		refresh() {
			this.$emit("refresh");
		},
	},
};
</script>

<style scoped>
.comments-inner-container {
	display: flex;
	flex-direction: column;
	gap: 0.75rem;
}
.comments-outer-container {
	display: flex;
	flex-direction: column;
	width: 50vw;
	height: fit-content;
	border-radius: 1rem;
	padding: 4rem 1rem 1rem 1rem;
	margin-top: -3rem;
	margin-bottom: 5rem;

	background-color: rgb(73, 73, 73);
	color: white;
}

@media screen and (max-width: 1100px) {
	.comments-outer-container {
		width: 80vw;
	}
}
</style>
