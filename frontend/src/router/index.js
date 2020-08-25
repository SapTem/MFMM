import Vue from 'vue'
import VueRouter from 'vue-router'

import StartHeader from '../layouts/StartHeader.vue'
import Start from '../view/Start.vue'
import SingIn from '../view/SingIn.vue'
import Registr from '../view/Registr.vue'
import HomeHeader from '../layouts/HomeHeader.vue'
import Home from '../view/Home.vue'


Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        component: StartHeader,
        children:[
            {
                path: '',
                name: 'start',
                component: Start
            },
            {
                path: 'login',
                name: 'login',
                component: SingIn
            },
            {
                path: 'registr',
                name: 'registr',
                component: Registr
            }
        ]
    },
    {
        path:'/home',
        component: HomeHeader,
        children:[
            {
                path: '',
                name: 'home',
                component: Home
            }
        ]
    }
]

const router = new VueRouter({
    routes
})

export default router