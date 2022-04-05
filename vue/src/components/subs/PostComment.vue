<template>
	<div class="comment-level">
		<div class="comment">
			<div class="display-column">
				<div class="display-row">
					<div
						class="comment-header display-row"
						v-if="commentData.timestamp != undefined"
					>
						<Score
							:isSmall="true"
							:score="score"
							@upvote="upvote"
							@downvote="downvote"
						/>
						{{ commentData.creator_name }} |
						{{ commentData.timestamp.slice(4, 16) }}
					</div>
				</div>
				<div>{{ commentData.comment }}</div>
			</div>
		</div>
		<div v-if="Object.keys(subTree).length > 0" class="answers">
			<PostComment
				v-for="child in Object.keys(subTree)"
				:key="child"
				:commentId="child"
				:commentsData="commentsData"
				:subTree="subTree[child]"
			/>
		</div>
	</div>
</template>

<script>
import PostComment from "./PostComment.vue";
import Score from "../Score.vue";
import { voteOnSubPostComment } from "../../api/subAPI.js";

export default {
	name: "PostComment",
	props: {
		commentId: String,
		commentsData: Object,
		subTree: Object,
	},
	components: {
		PostComment,
		Score,
	},
	data: () => {
		return {
			commentData: {},
			score: 0,
		};
	},
	mounted() {
		this.commentData = this.commentsData[this.commentId];
		this.score = this.commentData.score;
	},
	methods: {
		async upvote() {
			//TODO call api await voteOnSubPostComment()
			//if success
			//this.score++;
		},
		async downvote() {
			//TODO call api await voteOnSubPostComment()
			//if success
			//this.score--;
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
</style>
