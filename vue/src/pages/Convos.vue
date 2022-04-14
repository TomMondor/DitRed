<template>
	<div class="main-container">
		<UserSelector @userSelected="startNewConvo" />
		<h1 class="convos-header">Conversations with:</h1>
		<div v-if="this.areThereConvos" :key="refresh" class="convos-container">
			<ConvoWithUserCard
				v-for="(otherUserUsername, userId) in convosData"
				:key="otherUserUsername + refresh"
				:username="otherUserUsername"
				:userId="userId"
			/>
		</div>
		<div v-else class="no-convo">You have no conversation.</div>
	</div>
</template>

<script>
import { getConvos } from "../api/convoAPI.js";
import { getUserByUsername } from "../api/userAPI.js";
import ConvoWithUserCard from "../components/ConvoWithUserCard.vue";
import UserSelector from "../components/common/UserSelector.vue";
import Cookies from "js-cookie";

export default {
	name: "Convos",
	components: { ConvoWithUserCard, UserSelector },
	mounted() {
		this.getConvosData();
	},
	data: () => {
		return {
			convosData: {},
			refresh: false,
			userId: Cookies.get("userId"),
			areThereConvos: false,
		};
	},
	methods: {
		async getConvosData() {
			this.convosData = await getConvos(this.userId);
			this.areThereConvos = Object.keys(this.convosData).length > 0;
		},
		async startNewConvo(otherUserUsername) {
			this.$router.push("conversations/" + otherUserUsername);
		},
	},
};
</script>

<style scoped>
.convos-header {
	color: var(--mainwhite);
}

.main-container {
	margin-top: 5rem;
	margin-bottom: 7rem;
	display: flex;
	flex-direction: column;
	gap: 2rem;
	align-items: center;
}

.convos-container {
	height: fit-content;
	width: fit-content;
	display: flex;
	flex-direction: column;
	gap: 2rem;
	align-items: center;
}

.no-convo {
	color: var(--primary);
	font-size: 4rem;
	font-weight: bold;
	text-align: center;
}
</style>
