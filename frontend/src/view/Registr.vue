<template>
    <div class="content">
       <v-notification :messages="statusMsg"></v-notification>
        <div class="container">
            
            <div class="row">
                <div class="col-xl-2  offset-lg-3 offset-md-2  offset-sm-1 offset-1 col-lg-2 col-md-3 col-sm-3 col-4">
                    <img src="../assets/Logo.png" class="logo">
                </div>
                <div class="col-xl-2 col-lg-3 col-sm-3 col-4 main-label">
                    <h1>Регистрация</h1>
                </div>
            </div>
            <div class="row  mt-2">
                <div class="col-lg-4 col-md-6 col-sm-8 col-8 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-group">
                        <label for="login" class="label">Email</label>
                        <input type="email" class="form-control form-control-lg" id="login" v-model="email"  placeholder="Введите email">
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-8 col-8 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-group">
                        <label for="name" class="label">Имя</label>
                        <input type="text" class="form-control form-control-lg" id="name" v-model="name" placeholder="Введите имя">
                    </div>
                </div>
            </div>
             <div class="row">
                 <div class="col-lg-4 col-md-6 col-sm-8 col-8 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-group">
                        <label for="pass" class="label">Пароль</label>
                        <input type="password" class="form-control form-control-lg" id="pass" v-model="pass" placeholder="Введите пароль">
                    </div>
                </div>
            </div>
            <!-- <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-10 col-10 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <transition name="fade">
                        <p >
                            {{statusMsg}}
                        </p>
                    </transition>
                </div>
            </div> -->
            <div class="row mt-4">
                <div class="col-lg-2 col-md-3 col-sm-4 col-4 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-check">
                       <div class="custom-control form-control-lg custom-checkbox">
                            <input type="checkbox" class="custom-control-input" id="customCheck1">
                            <label class="custom-control-label" for="customCheck1">Запомнить</label>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-3 col-sm-6 col-6">
                    <button type="submit" @click=" send(); " class="btn"><span class="text-in-button">Записать</span></button>
                </div>
            </div>
            <!-- <img src="../assets/cardBackground.png" class="img-fluid mx-auto d-block" alt=""> --> 
        </div>
    </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import vNotification from '../components/v-notification'
 
Vue.use(VueAxios, axios)

export default {
    name: "Registr",
    data(){
        return{
            name: "",
            email: "",
            pass: "",
            statusMsg: [],
            isError: false,
            statusMessages:[
                {text: "Неверно ввелен логин", id: Date.now().toLocaleString()},
                {text: "Неверно ввелен логин", id: Date.now().toLocaleString()},
                {text: "Неверно ввелен логин", id: Date.now().toLocaleString()},
            ]
        }
    },
    components:{
        vNotification 
    },
    methods: {
        addStatusMsg(listMes, status="error"){
            for (var i = 0; i < listMes.length; i++)
                setTimeout(this.addMess,500*i,listMes,i,status)
        },
        addMess(listMes, i, status ){
            this.statusMsg.push({text: listMes[i], status: status, id: Date.now().toLocaleString()});
        },
        send(){
            axios.post("http://127.0.0.1:5000/registr",{
                name: this.name,
                email: this.email,
                pass: this.pass
            })
            .then((response) =>{
                if (response.data.status == "success"){
                    this.addStatusMsg(["Регистрация успешна!"], "success")
                    setTimeout(()=>this.$router.push('/login'),5000)
                    this.isError = false
                }
                else{
                    this.isError = true
                    this.addStatusMsg(response.data.errorMsg)
                }
            }).catch(() => {
                this.isError = true
                this.addStatusMsg(["Соединение с сервером не установлено"])
            })
        },
    }
}
</script>

<style scoped>
    .content{
        background: linear-gradient(-45deg, rgba(175, 8, 108, 0.45),rgba(189, 28, 100, 0.47),rgba(223, 79, 79, 0.5));
    }
    .container{
        padding-top: 180px; /*  туть */
        padding-bottom:150px;
        background-image: url(../assets/cardBackground.png);
        background-size: 580px; /*и  туть */
        background-repeat: no-repeat;
        background-position: center;
        background-position-y: center;
        height: 950px;
        
        
    }
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
        opacity: 0;
    }
    
    h1{
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        font-size: 32px;
        color: black;
        text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        margin-top:10px;
    }
    .logo{
        height: 80px;
    }
    .label{
        font-family: 'Montserrat', sans-serif;
        font-weight: medium;
        font-size: 24px;
        color: black;
    }
    .main-label{
        display: flex;
        justify-content: center;
    }
    .custom-control-label{
        font-family: 'Montserrat', sans-serif;
        font-weight: medium;
        font-size: 14px;
        color: black;
    }
    .custom-control-label::before, 
    .custom-control-label::after {
    top: -.1rem;
    width: 1.25rem;
    height: 1.25rem;
    }
    .btn{
        background: linear-gradient(-35deg, rgba(220, 62, 72, 1) , rgba(214, 69, 139, 1));
        width: 170px; 
        height: 60px;
        border-radius: 25px;
        box-shadow: 0px 4px 35px rgba(217, 65, 98, 0.54);
    }
    .form-check{
        top:10px;
    }
    .text-in-button{
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        font-size: 24px;
        color: white;
    }
    .btn:hover{
        box-shadow: 2px 5px 60px rgba(217, 65, 98, 0.75);
        background: linear-gradient(-35deg, rgba(220, 62, 72, 0.9) , rgba(214, 69, 139, 0.9));
    }
    .btn:active{
        box-shadow: 0px 0px 35px rgba(217, 65, 98, 0.54);  
        background: linear-gradient(-35deg, rgba(220, 62, 72, 0.8) , rgba(214, 69, 139, 0.8));
    }
    .mt-6{
        margin-top: 65px;
    }
    @media (max-width: 767px) {
        .container{
            padding-top: 190px;
            background-size: 540px;
        }
        .main-label{
            justify-content: start;
        }
    }
    @media (max-width: 575px) {
        .container{
            padding-top: 200px;
            background-size: 500px;
        }
        .mt-5{
            margin-top: 20px !important;
        }
        .mt-3{
            margin-top: 5px !important;
        }
        .mt-6{
            margin-top: 20px;
        }
        .btn{
            width: 140px; 
            height: 50px; 
        }
        .text-in-button{
            font-size: 20px;
        }
    }
</style>