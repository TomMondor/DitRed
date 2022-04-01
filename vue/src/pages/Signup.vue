<template>
    <div class="main-container">
        <div class="signup-container">
            <div class="header">Sign up</div>
            <div class="sub-header">
                Already have an account? <span class="login">Log in</span>
            </div>
            <div class="inputs-text-container">
                <div class="text-container">
                    <div class="input-text">Username:</div>
                    <div class="input-text">Password:</div>
                </div>
                <div class="inputs-container">
                    <input type="text" class="custom-input" />
                    <input type="password" class="custom-input" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
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
.main-container {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;

    height: 100vh;
    width: 100vw;
    top: 0;
}
.signup-container {
    display: flex;
    flex-direction: column;
    align-items: center;

    width: 50vw;
    height: fit-content;
    padding: 5rem 0;
    background-color: var(--background);
    border-radius: 2rem;
}

.header {
    font-size: 3rem;
    font-weight: bold;
    color: var(--mainwhite);
}

.sub-header {
    font-size: 1.1rem;
    color: var(--mainwhite);
}

.login {
    font-style: italic;
    color: var(--primary);
}

.login:hover {
    cursor: pointer;
    color: var(--mainwhite);
}

.inputs-text-container {
    margin-top: 4rem;
    display: flex;
    align-items: center;
    gap: 1rem;

    width: 100%;
}

.inputs-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
}

.text-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 4px solid hotpink;
    gap: 1rem;
}

.custom-input {
    border: none;
    border-radius: 0.3rem;
    height: 1.5rem;
    width: 50%;
}

.input-text {
    color: var(--mainwhite);
    font-size: 1.3rem;
}
</style>
