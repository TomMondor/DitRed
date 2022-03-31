<template>
    <div class="test">Signup!</div>
</template>

<script>
import { getUser } from "../api/userAPI.js";
import WallPostCard from "../components/WallPostCard.vue";
import UserCard from "../components/UserCard.vue";

export default {
    name: "Signup",
    components: {},
    mounted() {},
    data: () => {
        return {};
    },
    methods: {},
};
</script>

<style scoped>
.test {
    color: aqua;
}
</style>
