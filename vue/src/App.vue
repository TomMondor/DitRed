<template>
    <div id="app">
        <Header />
        <router-view />
    </div>
</template>

<script>
import Header from "./components/common/Header.vue";

export default {
    name: "App",
    components: {
        Header,
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin-top: 70px;
}

:root {
    --primary: orangered;
    --secondary: grey;
    --background: #222222;
    --mainwhite: #ffffff;
}
</style>
