import { createRouter, createWebHistory } from "vue-router"
const Rule=()=> import('./components/Rule.vue')

const routes=[
    {
        path:'/rule',
        component: Rule,
    },
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router