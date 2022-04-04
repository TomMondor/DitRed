<template>
	<div class="subs-container">
		<h1 class="subs-header">Subs</h1>
		<!-- TODO ajouter l'option de créer un Sub -->
		<div v-for="(sub, index) in subsData" :key="index">
			<SubCard :subData="sub" :subId="Number(index)" />
		</div>
	</div>
</template>

<script>
import { getSubs } from "../api/subAPI.js";
import SubCard from "../components/subs/SubCard.vue";

export default {
	name: "Subs",
	components: { SubCard },
	data: () => {
		return {
			subsData: {},
		};
	},
	mounted() {
		this.getSubsData();
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
