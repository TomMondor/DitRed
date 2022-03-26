<template>
    <div class="container">
        <score :score="score" />
        <div class="post-container">
            <div class="post-overhead">
                <div class="sub-name">r/{{ subName }}</div>
                <div>Posted by u/{{ postCreator }}</div>
                <div>On {{ timestamp }}</div>
            </div>
            <div class="title">{{ title }}</div>
            <div class="content">{{ content }}</div>
            <div class="comments">
                <font-awesome-icon icon="fa-solid fa-message" />
                <div>{{ comments_count }} comments</div>
            </div>
        </div>
    </div>
</template>

<script>
import Score from "../components/Score.vue";

export default {
    name: "SubPostCard",
    components: {
        Score,
    },
    props: [
        "subName",
        "postCreator",
        "timestamp",
        "title",
        "content",
        "score",
        "comments_count",
    ],
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
</style>
