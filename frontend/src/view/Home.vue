<template>
    <div >
        <div class="container-fluid">
            <div class="row allContent">
                <div class="col-2 leftBlock " >
                    <div class="stickyLayout" >
                   <div class="row d-flex align-items-center">
                       <div class="col-xl-7 offset-xl-1">
                           <span class="textLeftLayout">Выбрать дату</span>
                       </div>
                       <div class="col-xl-3 d-flex justify-content-end">
                            <img src="../assets/calendar.png" class="imgCalendar">
                       </div>
                   </div>
                   <div class="row">
                       <div class="col-12">
                            <hr>
                       </div>
                   </div>
                   <div class="row d-flex align-items-center">
                        <div class="col-xl-7 offset-xl-1">
                            <span class="textLeftLayout">Друзья</span>
                        </div>
                        <div class="col-xl-3 d-flex justify-content-end">
                            <a href="#/home" @click="isSearch=!isSearch"><img src="../assets/friend_search.png" alt=""></a>
                        </div>
                   </div>
                   <transition name="fade-sForm">  
                        <div v-if="isSearch" class="row d-flex align-items-center search-form">
                            <div class="col-xl-8 ">
                                <input type="text" class="form-control form-control-sm"  name="" id="">
                            </div>
                            <div class="col-xl-4 d-flex justify-content-end">
                                <button class="btn-sm btn-info">Найти</button>
                            </div>
                        </div>
                    </transition>
                    <div v-for="(friend, index) in friends" :key="index" class="row d-flex align-items-center search-form">
                        <div class="col-xl-2 offset-xl-1 ">
                                <img src="../assets/user_.png" alt="">
                        </div>
                        <div class="col-xl-8 d-flex justify-content-">
                            <span class="textListUsers">{{friend}}</span>
                        </div>
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
            searchFriend:'',
            isSearch:false,
            friends: ["Вася Пупкин","Вася Пупкин","Вася Пупкин"]
        }
    },
    methods:{
       
    
    },

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
    border-right: 2px solid rgba(156, 152, 152, 0.329); /* Параметры границы */
    background-color: rgba(247, 185, 229, 0.3);
    padding: 10px; /* Поля вокруг текста */
}
.dateManager{
    background-color: red;
    border: 3px solid black;
    height: 70px;
}
.textLeftLayout{
    font-family: 'Montserrat';
    font-weight: 500;
    font-size: 16px;
}
.textListUsers{
    font-family: 'Montserrat';
    font-weight: 400;
    font-size: 16px;
}
.search-form{
    margin-top:20px;
}
.stickyLayout{
    position:sticky;
    top: 20px;
}
.c{
    background-color: brown;
}

.fade-sForm-enter, .fade-sForm-leave-to{
    opacity: 0;
    transform:translateX(-120px)
}
.fade-sForm-enter-active, .fade-sForm-leave-active{
    transition: all 0.6s ease;
}

</style>
