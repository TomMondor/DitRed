<template>
	<div class="main-container">
		<div class="login-container">
			<div class="header">Login</div>
			<div class="sub-header">
				Don't have an account yet?
				<span class="signup" onclick="window.location.href='/#/signup';"
					>Sign up</span
				>
			</div>
			<div class="inputs-container">
				<div class="input-container">
					<div class="input-text">Username</div>
					<input type="text" id="username-input" class="custom-input" />
				</div>
				<div class="input-container">
					<div class="input-text">Password</div>
					<input type="password" id="password-input" class="custom-input" />
				</div>
			</div>
			<button class="login-button" @click="login">LOGIN</button>
		</div>
	</div>
</template>

<script>
import { login } from "../api/loginAPI.js";
import Cookies from "js-cookie";

export default {
	name: "Login",
	components: {},
	mounted() {},
	data: () => {
		return {};
	},
	methods: {
		async login() {
			const username = document.getElementById("username-input").value;
			const password = document.getElementById("password-input").value;
			const loginResponse = await login(username, password);
			const loginToken = loginResponse["token"];
			const userId = loginResponse["user_id"];

			Cookies.set("userId", userId, {
				SameSite: "Strict",
			});

			Cookies.set("loginToken", loginToken, {
				SameSite: "Strict",
			});

			window.location.href = "/#/";
		},
	},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Varela+Round&display=swap");

.main-container {
	position: absolute;
	display: flex;
	justify-content: center;
	align-items: center;

	height: 100vh;
	width: 100vw;
	top: 0;
}
.login-container {
	display: flex;
	flex-direction: column;
	align-items: center;

	width: 35rem;
	height: fit-content;
	padding: 3rem 0;
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

.signup {
	font-style: italic;
	color: var(--primary);
}

.signup:hover {
	cursor: pointer;
	color: var(--mainwhite);
}

.inputs-container {
	margin: 2.5rem 0;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	gap: 1rem;

	width: 100%;
}

.input-container {
	width: 60%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 0.5rem;
}

.input-text {
	width: 100%;
	text-align: left;
}

.custom-input {
	border: none;
	border-radius: 0.3rem;
	height: 2rem;
	width: 100%;
	padding: 0 1rem;
}

.input-text {
	color: var(--mainwhite);
	font-size: 1.3rem;
}

.login-button {
	font-family: "Varela Round", sans-serif;

	width: 60%;
	height: 2rem;
	border: none;
	border-radius: 0.3rem;
	background-color: var(--primary);
	color: var(--mainwhite);

	font-weight: bold;
}

.login-button:hover {
	cursor: pointer;
	background-color: var(--mainwhite);
	color: var(--primary);
}
</style>
