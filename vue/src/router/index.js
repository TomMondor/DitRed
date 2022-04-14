import Vue from "vue";
import Router from "vue-router";
import LoggedUser from "@/pages/LoggedUser";
import Subbed from "@/pages/Subbed";
import User from "@/pages/User";
import Convos from "@/pages/Convos";
import Convo from "@/pages/Convo";
import Subs from "@/pages/Subs";
import Sub from "@/pages/Sub";
import SubPost from "@/pages/SubPost";
import Signup from "@/pages/Signup";
import Login from "@/pages/Login";

Vue.use(Router);

const router = new Router({
	routes: [
		{
			path: "/",
			name: "Subs",
			component: Subs,
		},
		{
			path: "/subbed",
			name: "Subbed",
			component: Subbed,
			meta: { requiresAuth: true },
		},
		{
			path: "/user",
			name: "LoggedUser",
			component: LoggedUser,
			meta: { requiresAuth: true },
		},
		{
			path: "/user/:username",
			name: "User",
			component: User,
		},
		{
			path: "/conversations",
			name: "Convos",
			component: Convos,
			meta: { requiresAuth: true },
		},
		{
			path: "/conversations/:username",
			name: "Convo",
			component: Convo,
			meta: { requiresAuth: true },
		},
		{
			path: "/sub/:subId",
			name: "Sub",
			component: Sub,
		},
		{
			path: "/sub/:subId/sub-post/:subPostId",
			name: "SubPost",
			component: SubPost,
		},
		{
			path: "/signup",
			name: "Signup",
			component: Signup,
		},
		{
			path: "/login",
			name: "Login",
			component: Login,
		},
	],
});

import { validateCookies } from "@/api/loginAPI";

router.beforeEach(async (to, from, next) => {
	if (to.matched.some((record) => record.meta.requiresAuth)) {
		if (await validateCookies()) {
			next();
			return;
		}
		next("/login");
	} else {
		next();
	}
});

export default router;
