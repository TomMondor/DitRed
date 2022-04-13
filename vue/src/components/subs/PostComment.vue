<template>
	<div class="comment-level">
		<div class="comment">
			<div class="display-column">
				<div class="display-row">
					<div
						class="comment-header display-row"
						v-if="commentData.timestamp != undefined"
					>
						<Score :isSmall="true" :score="score" />
						<div
							class="comment-button"
							v-if="connected"
							@click="toggleFormVisibility"
						>
							<font-awesome-icon icon="fa-solid fa-message" />Reply
						</div>
						u/{{ commentData.creator_name }} |
						{{ commentData.timestamp.slice(4, 16) }}
					</div>
				</div>
				<div>{{ commentData.comment }}</div>
			</div>
		</div>
		<CreateComment
			v-if="isFormOpen"
			class="comment-level comment-box"
			@toggleFormVisibility="toggleFormVisibility"
			@refresh="refresh"
			:parentCommentId="commentId"
			:userId="userId"
			:postId="postId"
			:subId="subId"
		/>
		<div v-if="Object.keys(subTree).length > 0" class="answers">
			<PostComment
				v-for="child in Object.keys(subTree)"
				:key="child"
				:commentId="child"
				:commentsData="commentsData"
				:subTree="subTree[child]"
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
import CreateComment from "./CreateComment.vue";
import Score from "../Score.vue";
import { voteOnSubPostComment } from "../../api/subAPI.js";
import { validateCookies } from "../../api/loginAPI.js";

export default {
	name: "PostComment",
	props: {
		commentId: String,
		commentsData: Object,
		subTree: Object,
		userId: String,
		postId: String,
		subId: String,
	},
	components: {
		PostComment,
		CreateComment,
		Score,
	},
	data: () => {
		return {
			commentData: {},
			score: 0,
			isFormOpen: false,
			connected: false,
		};
	},
	async mounted() {
		this.$on("upvote", this.upvote);
		this.$on("downvote", this.downvote);
		this.commentData = this.commentsData[this.commentId];
		this.score = this.commentData.score;

		if (await validateCookies()) {
			this.connected = true;
		} else {
			this.connected = false;
		}
	},
	methods: {
		async upvote() {
			try {
				await voteOnSubPostComment(
					parseInt(this.userId),
					this.subId,
					this.postId,
					this.commentId,
					"upvote"
				);
				this.score++;
				this.$toast.open({
					message: "Upvoted!",
					type: "success",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			} catch (error) {
				this.$toast.open({
					message: "You have already voted on this comment.",
					type: "error",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			}
		},
		async downvote() {
			try {
				await voteOnSubPostComment(
					parseInt(this.userId),
					this.subId,
					this.postId,
					this.commentId,
					"downvote"
				);
				this.score--;
				this.$toast.open({
					message: "Downvoted!",
					type: "success",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			} catch (error) {
				this.$toast.open({
					message: "You have already voted on this comment.",
					type: "error",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			}
		},
		toggleFormVisibility() {
			this.isFormOpen = !this.isFormOpen;
		},
		refresh() {
			this.$emit("refresh");
		},
	},
};
</script>

<style scoped>
.comment-level {
	display: flex;
	flex-direction: column;
	border-left: 2px solid white;
	gap: 0.75rem;
}

.comment-box {
	margin-left: 1rem;
	padding-left: 0.5rem;
}

.comment {
	padding-left: 0.5rem;
}

.answers {
	display: flex;
	flex-direction: column;
	margin-left: 1rem;
	gap: 0.5rem;
}

.display-row {
	display: flex;
	flex-direction: row;
}

.display-column {
	display: flex;
	flex-direction: column;
	gap: 0.25rem;
}

.comment-header {
	color: orange;
	gap: 0.5rem;
}

.comment-button {
	cursor: pointer;
	display: flex;
	gap: 0.25rem;
	width: fit-content;
	padding: 0.25rem;
	margin-top: -0.25rem;
	border-radius: 0.4rem;
	align-items: center;
	font-size: 1rem;
}

.comment-button:hover {
	background: rgba(255, 255, 255, 0.8);
	color: black;
}
</style>
