<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png" />
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
import SubPostCard from "./components/SubPostCard.vue";

export default {
    name: "App",
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

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin-top: 60px;
}
</style>
