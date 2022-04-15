<template>
	<div class="container">
		<div class="timestamp">{{ formattedTimestamp }}</div>
		<div
			class="bubble-container"
			:class="[isFromLoggedUser ? 'left-bubble' : 'right-bubble']"
		>
			{{ message }}
		</div>
	</div>
</template>

<script>
export default {
	name: "ConvoBubble",
	props: ["message", "timestamp", "isFromLoggedUser"],
	data: () => {
		return {
			formattedTimestamp: "",
		};
	},
	mounted() {
		this.formatTimestamp();
	},
	methods: {
		formatTimestamp() {
			this.formattedTimestamp = this.timestamp.slice(5, 22);
			if (this.formattedTimestamp.startsWith("0")) {
				this.formattedTimestamp = this.formattedTimestamp.slice(1);
			}
		},
	},
};
</script>

<style scoped>
.container {
	display: flex;
	flex-direction: column;
	align-items: flex-end;
	width: 100%;
	height: fit-content;

	background-color: #0e0b0b;
}

.bubble-container {
	display: flex;
	flex-direction: column;
	align-items: flex-end;
	width: fit-content;
	max-width: 80vw;
	height: fit-content;
	padding: 0.75rem 1rem 0.75rem 1rem;
	border-radius: 1rem;

	color: var(--mainwhite);
}

.left-bubble {
	align-self: flex-start;
	background-color: var(--backgroundlighter);
}

.right-bubble {
	align-self: flex-end;
	background-color: var(--background);
}

.timestamp {
	color: var(--mainwhite);
	font-size: smaller;
	align-self: center;
}
</style>
