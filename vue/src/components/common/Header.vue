<template>
    <div class="hp-header">
        <div class="hp-logo-container">
            <img
                src="../../../public/DitRed-logo.png"
                class="hp-ditred-logo"
                alt="ditred-logo"
            />
            <div class="hp-ditred-text">ditred</div>
        </div>
        <div class="hp-display-links">
            <router-link to="/"
                ><font-awesome-icon
                    class="hp-header-icon"
                    icon="fa-solid fa-list-ul"
            /></router-link>
            <router-link to="/subbed"
                ><font-awesome-icon
                    class="hp-header-icon"
                    icon="fa-solid fa-list-ul"
            /></router-link>
            <router-link to="/user"
                ><font-awesome-icon
                    class="hp-header-icon"
                    icon="fa-solid fa-user"
            /></router-link>
            <router-link to="/conversations"
                ><font-awesome-icon
                    class="hp-header-icon"
                    icon="fa-solid fa-comment-dots"
            /></router-link>
        </div>
        <div class="hp-login-container">
            <router-link v-if="!connected" to="/login" class="hp-login">
                <div>Login</div>
                <font-awesome-icon icon="fa-solid fa-right-to-bracket" />
            </router-link>
            <div v-else class="hp-login" @click="signout">
                <div>Sign out</div>
                <font-awesome-icon icon="fa-solid fa-right-from-bracket" />
            </div>
        </div>
    </div>
</template>

<script>
import Cookies from "js-cookie";
import { validateCookies } from "@/api/loginAPI";

export default {
    name: "Header",
    data() {
        return {
            connected: false,
            key: 0,
        };
    },
    async mounted() {
        if (await validateCookies()) {
            this.connected = true;
        } else {
            this.connected = false;
        }

        this.$root.$on("logged-in", () => {
            this.connected = true;
        });
    },
    methods: {
        signout() {
            Cookies.remove("userId");
            Cookies.remove("token");
            this.connected = false;
            window.location = "/";
        },
    },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

.hp-display-links {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.hp-header {
    display: flex;
    align-items: center;
    gap: 2vw;

    position: sticky;
    top: 0;
    left: 0;
    width: 100%;

    height: 3.5rem;

    background-color: var(--background);

    z-index: 1000;
}

.hp-header-icon {
    height: 1.3rem;
    color: var(--mainwhite);
}

.hp-header-icon:hover {
    color: var(--primary);
}

.hp-logo-container {
    margin-left: 1vw;
    display: flex;
    gap: 0.3rem;
    align-items: center;
    color: var(--mainwhite);

    height: 100%;
}

.hp-ditred-text {
    font-family: "Varela Round", sans-serif;
    font-size: 1.3rem;
    font-weight: bold;
}

.hp-ditred-logo {
    height: 2rem;
}

.hp-login-container {
    flex: 1;
    display: flex;
    justify-content: right;
}

.hp-login {
    text-decoration: none;
    width: fit-content;

    font-family: "Varela Round", sans-serif;
    font-size: 1.3rem;
    font-weight: bold;
    color: var(--mainwhite);

    display: flex;
    align-items: center;
    gap: 0.4rem;

    margin-right: 1rem;
}

.hp-login:hover {
    cursor: pointer;
    color: var(--primary);
}
</style>
