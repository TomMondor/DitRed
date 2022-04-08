<template>
	<div class="convos-container">
		<UserSelector @userSelected="startNewConvo" />
		<h1 class="convos-header">Conversations with:</h1>
		<ConvoWithUserCard
			v-for="(otherUserUsername, userId) in convosData"
			:key="otherUserUsername + refresh"
			:username="otherUserUsername"
			:userId="userId"
		/>
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
		};
	},
	methods: {
		async getConvosData() {
			this.convosData = await getConvos(this.userId);
		},
		async startNewConvo(otherUserUsername) {
			const data = await getUserByUsername(otherUserUsername);
			const userId = Object.keys(data)[0];
			this.convosData[userId] = otherUserUsername;
			this.refresh = !this.refresh;
		},
	},
};
</script>

<style>
.convos-header {
	color: var(--mainwhite);
}

.convos-container {
	margin-top: 5rem;
	margin-bottom: 7rem;
	display: flex;
	flex-direction: column;
	gap: 2rem;
	align-items: center;
}
</style>
