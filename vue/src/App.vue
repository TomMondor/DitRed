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
:root {
    background-color: #0e0b0b;
}
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --primary: orangered;
    --secondary: grey;
    --background: #222222;
    --backgroundlighter: rgb(63, 62, 62);
    --mainwhite: #ffffff;
}
</style>
