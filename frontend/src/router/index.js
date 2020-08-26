import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import StartHeader from '../layouts/StartHeader.vue'
import Start from '../view/Start.vue'
import SingIn from '../view/SingIn.vue'
import Registr from '../view/Registr.vue'
import HomeHeader from '../layouts/HomeHeader.vue'
import Home from '../view/Home.vue'

Vue.use(VueAxios, axios)
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
        beforeEnter: isAuth,
        children:[
            {
                path: '',
                name: 'home',
                component: Home
            }
        ]
    }
]

function isAuth(to, from, next){
    axios.post("http://127.0.0.1:5000/isAuth",{
        "access_tocken": localStorage.getItem("access_tocken")
        })
        .then((response) => {
            if (response.data.status == "Auth"){
                next()
            }else{
                next("/")
            }
        }).catch(() => {
            next("/")
        })
}

const router = new VueRouter({
    routes
})

export default router