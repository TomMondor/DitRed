import Vue from "vue";
import Router from "vue-router";
import User from "@/pages/User";
import Convos from "@/pages/Convos";
import Convo from "@/pages/Convo";
import Subs from "@/pages/Subs";
import Sub from "@/pages/Sub";
import SubPost from "@/pages/SubPost";
import Signup from "@/pages/Signup";
import Login from "@/pages/Login";

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
            path: "/conversations/:userId",
            name: "Convo",
            component: Convo,
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
