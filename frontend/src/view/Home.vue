<template>
    <div>
    <button @click="isAuth()">sdfdfsdfsdfs</button>
    <div v-show="isAuthorization">Пососиddddddddddddddddddddd</div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
// import { axios } from 'vue/types/umd'

Vue.use(VueAxios, axios)
export default {
    name:"Home",
    data(){
        return{
            isAuthorization: false
        }
    },
    methods:{
        isAuth(){
            axios.get("http://127.0.0.1:5000/isAuth")
            .then((response) => {
                if (response.data.isAuth == true){
                    this.isAuthorization = true
                }else{
                  this.isAuthorization = false 
                }
            }).catch(() => {
                this.isAuthorization = false
            })
        }
    },
    created(){
        this.isAuth();
    }
}
</script>

<style>

</style>