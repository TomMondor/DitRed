<template>
	<div>
		<div class="sub-container">
			<div class="display-row">
				<span class="sub-name" @click="redirectToSubPage"
					>r/{{ subData.name }}</span
				>
				<span
					class="subscribe-button"
					v-if="userId != undefined"
					@click="subscribe"
					>Subscribe</span
				>
			</div>
			<div class="sub-description">{{ subData.description }}</div>
			<div class="display-row">
				<div>{{ subData.subscribers_count }} subscribers</div>
				<div>
					Created on {{ subData.timestamp.slice(5, 16) }} by
					{{ subData.creator_name }}
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { subscribe } from "../../api/subAPI";
import Cookies from "js-cookie";

export default {
	name: "SubCard",
	props: {
		subData: Object,
		subId: Number,
	},
	data: () => {
		return {
			userId: Cookies.get("userId"),
		};
	},
	mounted() {},
	methods: {
		async subscribe() {
			await subscribe(this.subId);
			//TODO vérifier si fonctionne quand le call d'api sera fait dans le b-e
		},
		redirectToSubPage() {
			this.$router.push("/sub/" + this.subId);
		},
	},
};
</script>

<style scoped>
.sub-container {
	display: flex;
	flex-direction: column;
	width: 50vw;
	height: fit-content;
	padding: 1rem;
	gap: 1rem;

	background-color: #222222;
	color: grey;
	border-radius: 1rem;
}

@media screen and (max-width: 1100px) {
	.sub-container {
		width: 80vw;
	}
}

.display-row {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: flex-start;
}

.sub-name {
	color: white;
	font-size: 1.5rem;
	cursor: pointer;
}

.subscribe-button {
	padding: 0.5rem;
	border-radius: 1rem;
	background-color: orange;
	color: black;
	font-weight: bold;
}

.subscribe-button:hover {
	background-color: orangered;
	cursor: pointer;
}

.sub-description {
	border-radius: 1rem;
	background-color: rgb(73, 73, 73);
	color: white;
	padding: 1rem;
}
</style>
