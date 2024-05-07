import { createRouter, createWebHistory } from "vue-router"
const Rule=()=> import('./components/Rule.vue')
const Judge=()=> import('./components/Judge.vue')

const routes=[
    {
        path:'/rule',
        component: Rule,
    },
    {
        path:'/judge',
        component: Judge,
    },
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router