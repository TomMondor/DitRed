<template>
    <div class="container">
        <div>{{ timestamp }}</div>
        <div>{{ message }}</div>
    </div>
</template>

<script>
export default {
    name: "ConvoBubble",
    props: ["message", "timestamp"],
};
</script>

<style scoped>
.container {
    display: flex;
    width: fit-content;
    max-width: 80vw;
    height: fit-content;
    padding: 2rem;

    border-radius: 1rem;

    color: var(--mainwhite);
}
</style>
