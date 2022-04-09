<template>
    <div class="comment-level">
        <!-- TODO add option to reply (emit event? -> sucks because recursive components) -->
        <div class="comment">
            <div class="display-column">
                <div class="display-row">
                    <div
                        class="comment-header display-row"
                        v-if="commentData.timestamp != undefined"
                    >
                        <Score :isSmall="true" :score="score" />
                        u/{{ commentData.creator_name }} |
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
                :userId="userId"
                :postId="postId"
                :subId="subId"
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
        userId: String,
        postId: String,
        subId: String,
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
        this.$on("upvote", this.upvote);
        this.$on("downvote", this.downvote);
        this.commentData = this.commentsData[this.commentId];
        this.score = this.commentData.score;
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
