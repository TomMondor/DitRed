import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueToast from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import specific icons */
import { faArrowDown } from "@fortawesome/free-solid-svg-icons";
import { faArrowUp } from "@fortawesome/free-solid-svg-icons";
import { faMessage } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { faCommentDots } from "@fortawesome/free-solid-svg-icons";
import { faChalkboardUser } from "@fortawesome/free-solid-svg-icons";
import { faUsers } from "@fortawesome/free-solid-svg-icons";
import { faListUl } from "@fortawesome/free-solid-svg-icons";
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons";
import { faRightFromBracket } from "@fortawesome/free-solid-svg-icons";
import { faRightToBracket } from "@fortawesome/free-solid-svg-icons";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { faHeart } from "@fortawesome/free-solid-svg-icons";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* add icons to the library */
library.add(faArrowDown);
library.add(faArrowUp);
library.add(faMessage);
library.add(faUser);
library.add(faCommentDots);
library.add(faChalkboardUser);
library.add(faUsers);
library.add(faListUl);
library.add(faPaperPlane);
library.add(faRightFromBracket);
library.add(faRightToBracket);
library.add(faMagnifyingGlass);
library.add(faHeart);

Vue.use(VueToast);

/* add font awesome icon component */
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
	render: (h) => h(App),
	router,
}).$mount("#app");
