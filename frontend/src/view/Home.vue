<template>
    <div>
        <div class="container-fluid">
            <div class="row allContent">
                <div class="col-2 leftBlock ">
                   <div class="row">
                       <div class="col-3 ">
                           <img src="../assets/calendar.png" class="imgCalendar">
                       </div>
                       <div class="col-3 offset-1 d-flex align-self-center">
                           Предстоящие
                       </div>
                   </div>
                </div>
                <div class="col-10">
                    <div class="row dateManager">

                    </div>
                </div>
            </div>
        </div>
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
            // isAuthorization: false
        }
    },
    methods:{
        // isAuth(){
        //     axios.get("http://127.0.0.1:5000/isAuth")
        //     .then((response) => {
        //         if (response.data.isAuth == true){
        //             this.isAuthorization = true
        //         }else{
        //           this.isAuthorization = false 
        //         }
        //     }).catch(() => {
        //         this.isAuthorization = false
        //     })
        // }
    },
    // created(){
    //     this.isAuth();
    // }
}
</script>

<style scoped>
.allContent{
    background: linear-gradient(45deg,rgba(233, 146, 146, 0.47),rgba(241, 20, 166, 0.44)) ;
    height: 950px;
}
.imgCalendar{
    height: 40px;
}
.leftBlock{
    border-right: 2px solid black; /* Параметры границы */
    background: #fc3; /* Цвет фона */
    padding: 10px; /* Поля вокруг текста */
}
.dateManager{
    background-color: red;
    border: 3px solid black;
    height: 70px;
}
.c{
    background-color: brown;
}
</style>
