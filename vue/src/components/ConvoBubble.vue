<template>
    <div class="container">
        <div class="timestamp">{{ formattedTimestamp }}</div>
        <div
            class="bubble-container"
            :class="[isFromLoggedUser ? 'left-bubble' : 'right-bubble']"
            :id="timestamp"
        ></div>
    </div>
</template>

<script>
export default {
    name: "ConvoBubble",
    props: ["message", "timestamp", "isFromLoggedUser"],
    data: () => {
        return {
            formattedTimestamp: "",
            formattedMessage: null,
        };
    },
    mounted() {
        this.formatTimestamp();
        this.formatMessage();
    },
    methods: {
        formatTimestamp() {
            this.formattedTimestamp = this.timestamp.slice(5, 22);
            if (this.formattedTimestamp.startsWith("0")) {
                this.formattedTimestamp = this.formattedTimestamp.slice(1);
            }
        },
        formatMessage() {
            this.formattedMessage = this.message.replace(/\n/g, "<br>"); //jsp si fonctionne, notre input permet pas les enter je pense
            this.formattedMessage = formatText(
                this.formattedMessage,
                "*",
                "<strong>",
                "</strong>"
            );
            this.formattedMessage = formatText(
                this.formattedMessage,
                "_",
                "<em>",
                "</em>"
            );
            this.formattedMessage = formatText(
                this.formattedMessage,
                "~",
                "<strike>",
                "</strike>"
            );
            this.formattedMessage = formatText(
                this.formattedMessage,
                "`",
                '<span style="font-family: monospace;white-space: pre-wrap;font-size: 16px;">',
                "</span>"
            );

            document.getElementById(this.timestamp).innerHTML =
                this.formattedMessage;
        },
    },
};

function formatText(text, toReplace, htmlFrontTag, htmlBackTag) {
    // test string : bonjour *ceci* est un _test_ pour voir si ça ~marche~ avec des `tags html`
    // bug : ceci est un test _<strong>testTestTest</strong>_ merci bonsoir
    // -> le gras va s'appliquer, alors que sur messenger on voit les balises <strong>... danger possible?
    let formattedText = text;
    //fonctionne juste si on donne un seul caractère à remplacer (toReplace)
    let symbolCount = (text.match(new RegExp(`[${toReplace}]`, "g")) || [])
        .length;
    while (symbolCount >= 2) {
        const startIndex = formattedText.indexOf(toReplace);
        const endIndex = formattedText.indexOf(toReplace, startIndex + 1);
        formattedText =
            formattedText.slice(0, startIndex) +
            ` ${htmlFrontTag}` +
            formattedText.slice(startIndex + 1, endIndex) +
            `${htmlBackTag} ` +
            formattedText.slice(endIndex + 1);
        symbolCount -= 2;
    }
    return formattedText;
}
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
