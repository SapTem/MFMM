import Vue from 'vue'
import VueRouter from 'vue-router'

import Header from '../layouts/AppLayout.vue'
import Start from '../view/Start.vue'
import SingIn from '../view/SingIn.vue'
import Registr from '../view/Registr.vue'


Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        component: Header,
        children:[
            {
                path: '/',
                name: 'start',
                component: Start
            },
            {
                path: '/login',
                name: 'login',
                component: SingIn
            },
            {
                path: '/registr',
                name: 'registr',
                component: Registr
            }
        ]
    }
]

const router = new VueRouter({
    routes
})

export default router