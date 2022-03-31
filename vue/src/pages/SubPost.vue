<template>
    <div class="subposts-container">
        SubPost SubPost SubPost
        <sub-post-card
            :subName="subName"
            :postCreator="postCreator"
            :timestamp="timestamp"
            :title="title"
            :content="content"
            :score="score"
            :comments_count="comments_count"
        />
    </div>
</template>

<script>
import SubPostCard from "../components/SubPostCard.vue";

export default {
    name: "SubPost",
    components: {
        SubPostCard,
    },
    data: () => {
        return {
            subName: "Memes",
            postCreator: "Nocturnal",
            timestamp: "2015-03-26 11:46:40",
            title: "Tempor exercitation reprehenderit nostrud commodo aliquip nulla minim",
            content:
                "Nisi commodo veniam ad ex do, id commodo irure et sed minim deserunt sunt. Aute quis exercitation sed voluptate.",
            score: "123",
            comments_count: "8",
        };
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
</style>
