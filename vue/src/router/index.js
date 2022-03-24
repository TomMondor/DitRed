import Vue from "vue";
import Router from "vue-router";
import User from "@/pages/User";
import Convos from "@/pages/Convos";
import Subs from "@/pages/Subs";
import Sub from "@/pages/Sub";
import SubPost from "@/pages/SubPost";

Vue.use(Router);

export default new Router({
	routes: [
		{
			path: "/",
			name: "Subs",
			component: Subs,
		},
		{
			path: "/user",
			name: "User",
			component: User,
		},
		{
			path: "/conversations",
			name: "Convos",
			component: Convos,
		},
		{
			path: "/sub",
			name: "Sub",
			component: Sub,
		},
		{
			path: "/sub-post",
			name: "SubPost",
			component: SubPost,
		},
	],
});
