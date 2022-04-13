<template>
	<div>
		<div class="sub-container" @click="redirectToSubPage">
			<div class="display-row">
				<span class="sub-name">r/{{ subData.name }}</span>
				<span
					class="subscribe-button"
					v-if="userId != undefined"
					@click.stop="subscribe"
					>Subscribe</span
				>
			</div>
			<div class="sub-description">{{ subData.description }}</div>
			<div class="display-row">
				<div v-if="subData != undefined && subData.subscribers_count > 1">
					{{ subData.subscribers_count }} subscribers
				</div>
				<div v-else>{{ subData.subscribers_count }} subscriber</div>
				<div>
					Created on {{ subData.timestamp.slice(5, 16) }} by u/{{
						subData.creator_name
					}}
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
			try {
				await subscribe(this.userId, this.subId);
				this.$toast.open({
					message: "You are now subscribed to this sub!",
					type: "success",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			} catch (error) {
				this.$toast.open({
					message: "You are already subscribed to this sub.",
					type: "error",
					position: "top-right",
					duration: 5000,
					dismissible: true,
				});
			}
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
	gap: 1rem;

	width: 50vw;
	height: fit-content;
	padding: 1rem;
	border-radius: 1rem;
	cursor: pointer;

	background-color: #222222;
	color: grey;
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
