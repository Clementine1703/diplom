import {createRouter, createWebHashHistory} from "vue-router";

import authorizationForm from "@/components/AuthorizationForm";

export default createRouter({
    history: createWebHashHistory(),
    routes:[
        {
            path: '/',
            name: 'main',
            component: authorizationForm,
        }
    ]
})