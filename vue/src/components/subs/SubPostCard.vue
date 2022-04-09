<template>
    <div
        class="container"
        :class="[isALink ? 'cursor-pointer' : '']"
        @click="redirectToSubPostPage"
    >
        <Score :score="score" @upvote="upvote" @downvote="downvote" />
        <div class="post-container">
            <div class="post-overhead">
                <div class="sub-name">r/{{ subName }}</div>
                <div>Posted by u/{{ postCreator }}</div>
                <div v-if="timestamp != undefined">
                    On {{ timestamp.slice(4, 16) }}
                </div>
            </div>
            <div class="title">{{ title }}</div>
            <div class="content">{{ content }}</div>
            <div class="comments">
                <font-awesome-icon icon="fa-solid fa-message" />
                <div v-if="comments_count == 1">
                    {{ comments_count }} comment
                </div>
                <div v-else>{{ comments_count }} comments</div>
            </div>
        </div>
    </div>
</template>

<script>
import Score from "../Score.vue";
import { voteOnSubPost } from "../../api/subAPI.js";

export default {
    name: "SubPostCard",
    components: {
        Score,
    },
    props: [
        "postId",
        "subId",
        "subName",
        "postCreator",
        "timestamp",
        "title",
        "content",
        "score",
        "comments_count",
        "isALink",
        "userId",
    ],
    methods: {
        redirectToSubPostPage() {
            if (this.isALink) {
                this.$router.push(`/sub/${this.subId}/sub-post/${this.postId}`);
            }
        },
        async upvote() {
            try {
                await voteOnSubPost(
                    parseInt(this.userId),
                    this.subId,
                    this.postId,
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
                    message: "You have already voted on this post.",
                    type: "error",
                    position: "top-right",
                    duration: 5000,
                    dismissible: true,
                });
            }
        },
        async downvote() {
            try {
                await voteOnSubPost(
                    parseInt(this.userId),
                    this.subId,
                    this.postId,
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
                    message: "You have already voted on this post.",
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
.container {
    display: flex;
    width: 50vw;
    height: fit-content;

    background-color: #222222;

    border-radius: 1rem;

    color: grey;
}

@media screen and (max-width: 1100px) {
    .container {
        width: 80vw;
    }
}

.post-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    padding: 1rem;
}

.post-overhead {
    display: flex;
    gap: 1rem;
}

.sub-name {
    color: white;
}

.title {
    color: white;
    font-size: 1.5rem;
}

.content {
    color: white;
    background-color: rgb(73, 73, 73);

    display: flex;
    flex: 1;
    padding: 1rem;
    border-radius: 1rem;
}

.comments {
    display: flex;
    gap: 1rem;
    width: fit-content;
    padding: 0.5rem;
    border-radius: 0.4rem;

    align-items: center;

    font-size: 0.85rem;
}

.comments:hover {
    background: rgba(255, 255, 255, 0.8);
    cursor: pointer;
}

.cursor-pointer {
    cursor: pointer;
}
</style>
