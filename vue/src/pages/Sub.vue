<template>
    <div>
        <div class="sub-header">
            <h1 class="text-orange">r/{{ subData.name }}</h1>
            <div>{{ subData.description }}</div>
            <div class="display-row">
                <div class="text-orange">
                    {{ subData.subscribers_count }} subscribers
                </div>
                <div v-if="subData.timestamp != undefined">
                    Created on {{ subData.timestamp.slice(4, 16) }} by u/{{
                        subData.creator_name
                    }}
                </div>
            </div>
        </div>
        <!-- TODO ajouter l'option de créer un Sub Post -->
        <div class="subposts-section">
            <SubPostCard
                v-for="(subPost, index) in subPostsData"
                :key="index"
                :postId="Number(index)"
                :subId="subId"
                :subName="subData.name"
                :postCreator="subPost.creator_name"
                :timestamp="subPost.timestamp"
                :title="subPost.title"
                :content="subPost.content"
                :score="subPost.score"
                :comments_count="subPost.comments_count"
                :isALink="true"
                :userId="userId"
            />
        </div>
    </div>
</template>

<script>
import SubPostCard from "../components/subs/SubPostCard.vue";
import { getSubPosts, getSub } from "../api/subAPI.js";
import Cookies from "js-cookie";

export default {
    name: "Sub",
    components: {
        SubPostCard,
    },
    mounted() {
        this.getSubId();
        this.getSubData();
    },
    data: () => {
        return {
            userId: Cookies.get("userId"),
            subId: "",
            subData: {},
            subPostsData: {},
        };
    },
    methods: {
        getSubId() {
            this.subId = this.$router.currentRoute.params.subId;
        },
        async getSubData() {
            const subData = await getSub(this.subId);
            this.subData = subData[this.subId];
            this.subPostsData = await getSubPosts(this.subId);
        },
    },
};
</script>

<style scoped>
.sub-header {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: fit-content;
    padding: 1rem;
    gap: 1rem;
    background-color: rgb(73, 73, 73);
    color: white;
}
.text-orange {
    color: orange;
}

.display-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
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
