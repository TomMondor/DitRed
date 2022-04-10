<template>
	<div class="subs-container">
		<h1 class="subs-header">Subs</h1>
		<CreateSub v-if="connected" :userId="userId" @refresh="getSubsData" />
		<div v-for="(sub, index) in subsData" :key="index + refresh">
			<SubCard :subData="sub" :subId="Number(index)" />
		</div>
	</div>
</template>

<script>
import { getSubs } from "../api/subAPI.js";
import SubCard from "../components/subs/SubCard.vue";
import CreateSub from "../components/subs/CreateSub.vue";
import Cookies from "js-cookie";
import { validateCookies } from "../api/loginAPI.js";

export default {
	name: "Subs",
	components: { SubCard, CreateSub },
	data: () => {
		return {
			subsData: {},
			userId: Cookies.get("userId"),
			refresh: false,
			connected: false,
		};
	},
	async mounted() {
		this.getSubsData();

		if (await validateCookies()) {
			this.connected = true;
		} else {
			this.connected = false;
		}
	},
	methods: {
		async getSubsData() {
			this.subsData = await getSubs();
		},
	},
};
</script>

<style scoped>
.subs-header {
	color: var(--mainwhite);
}
.subs-container {
	margin-top: 5rem;
	margin-bottom: 7rem;
	display: flex;
	flex-direction: column;
	gap: 2rem;
	align-items: center;
}
</style>
