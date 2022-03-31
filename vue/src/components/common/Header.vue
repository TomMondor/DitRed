<template>
    <div class="header">
        <div class="logo-container">
            <img
                src="../../../public/DitRed-logo.png"
                class="ditred-logo"
                alt="ditred-logo"
            />
            <div class="ditred-text">ditred</div>
        </div>
        <div class="display-links">
            <router-link to="/"
                ><font-awesome-icon
                    class="header-icon"
                    icon="fa-solid fa-list-ul"
            /></router-link>
            <router-link to="/user"
                ><font-awesome-icon class="header-icon" icon="fa-solid fa-user"
            /></router-link>
            <router-link to="/conversations"
                ><font-awesome-icon
                    class="header-icon"
                    icon="fa-solid fa-comment-dots"
            /></router-link>
            <router-link to="/sub"
                ><font-awesome-icon
                    class="header-icon"
                    icon="fa-solid fa-users"
            /></router-link>
            <router-link to="/sub-post"
                ><font-awesome-icon
                    class="header-icon"
                    icon="fa-solid fa-chalkboard-user"
            /></router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "Header",
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

.display-links {
    display: flex;
    align-items: center;
    gap: 1rem;
}
.header {
    display: flex;
    align-items: center;
    gap: 2vw;

    position: sticky;
    top: 0;
    left: 0;
    width: 100%;

    height: 3.5rem;

    background-color: var(--background);
}

.header-icon {
    height: 1.3rem;
    color: var(--mainwhite);
}

.header-icon:hover {
    color: var(--primary);
}

.logo-container {
    margin-left: 1vw;
    display: flex;
    gap: 0.3rem;
    align-items: center;
    color: var(--mainwhite);

    height: 100%;
}

.ditred-text {
    font-family: "Varela Round", sans-serif;
    font-size: 1.3rem;
    font-weight: bold;
}

.ditred-logo {
    height: 2rem;
}
</style>
