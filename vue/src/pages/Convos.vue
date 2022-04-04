<template>
    <div class="convos-container">
        <h1 class="convos-header">Conversations with:</h1>
        <convo-with-user-card
            v-for="(otherUserUsername, userId) in convosData"
            :key="otherUserUsername"
            :username="otherUserUsername"
            :userId="userId"
        />
    </div>
</template>

<script>
import { getConvos } from "../api/convoAPI.js";
import ConvoWithUserCard from "../components/ConvoWithUserCard.vue";
import Cookies from "js-cookie";

export default {
    name: "Convos",
    components: { ConvoWithUserCard },
    mounted() {
        this.getConvosData();
    },
    data: () => {
        return {
            convosData: {},
            userId: Cookies.get("userId"),
        };
    },
    methods: {
        async getConvosData() {
            this.convosData = await getConvos(this.userId);
        },
    },
};
</script>

<style>
.convos-header {
    color: var(--mainwhite);
}

.convos-container {
    margin-top: 5rem;
    margin-bottom: 7rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    align-items: center;
}
</style>
