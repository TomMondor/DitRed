<template>
    <div>
        <div class="user-card-container">
            <user-card
                :name="userData.username"
                :timestamp="userData.memberSince"
                :bio="userData.bio"
            />
        </div>

        <div class="wall-posts-container">
            <h1 class="wallposts-header">Wallposts</h1>
            <wall-post-card
                v-for="wallPost in userData.wallPosts"
                :key="wallPost[0]"
                :content="wallPost[0]"
            />
        </div>
    </div>
</template>

<script>
import { getUser } from "../api/userAPI.js";
import WallPostCard from "../components/WallPostCard.vue";
import UserCard from "../components/UserCard.vue";

export default {
    name: "User",
    components: {
        WallPostCard,
        UserCard,
    },
    mounted() {
        this.getUserData();
    },
    data: () => {
        return {
            userData: {},
            userId: 17, //TODO get real value
        };
    },
    methods: {
        async getUserData() {
            const data = await getUser(this.userId);
            this.userData = data[this.userId];
        },
    },
};
</script>

<style>
.user-card-container {
    margin-top: 5rem;
    display: flex;
    justify-content: center;
}

.wallposts-header {
    color: orange;

    background-color: var(--background);
    border-radius: 2rem;
    padding: 0.7rem;
}

.wall-posts-container {
    margin-top: 2rem;

    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;

    align-items: center;
}
</style>
