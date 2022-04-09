<template>
    <div :class="[isSmall ? 'score-container-small' : 'score-container']">
        <font-awesome-icon
            icon="fa-solid fa-arrow-up"
            class="arrow-up"
            :class="[isSmall ? 'arrow-small' : 'arrow']"
            @click.stop="upvote"
        />
        <div class="score-text" :class="[score < 0 ? 'center-when-neg' : '']">
            {{ score }}
        </div>
        <font-awesome-icon
            icon="fa-solid fa-arrow-down"
            class="arrow-down"
            :class="[isSmall ? 'arrow-small' : 'arrow']"
            @click.stop="downvote"
        />
    </div>
</template>

<script>
export default {
    name: "Score",
    props: ["score", "isSmall"],
    methods: {
        upvote() {
            this.$emit("upvote");
        },
        downvote() {
            this.$emit("downvote");
        },
    },
};
</script>

<style scoped>
.score-container {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    width: fit-content;
    height: fit-content;
    padding: 1rem;

    justify-content: center;
}

.score-container-small {
    display: flex;
    flex-direction: row;
    gap: 0.5rem;
    width: fit-content;
    height: fit-content;
    justify-content: center;
}

.score-text {
    color: white;
    text-align: center;
}

.center-when-neg {
    text-align: left;
}

.arrow {
    color: grey;
    height: 1.5rem;
    width: 1.5rem;
}

.arrow-small {
    color: grey;
    height: 1rem;
    width: 1rem;
}

.arrow:hover {
    cursor: pointer;
}

.arrow-down:hover {
    color: darkblue;
}

.arrow-up:hover {
    color: red;
}
</style>
