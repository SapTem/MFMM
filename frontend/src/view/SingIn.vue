<template>
    <div class="content">
        <div class="container">
            
            <div class="row">
                <div class="col-xl-2  offset-lg-3 offset-md-2  offset-sm-1 offset-1 col-lg-2 col-md-3 col-sm-4 col-4">
                    <img src="../assets/Logo.png" class="logo">
                </div>
                <div class="col-md-2 col-sm-3 col-4 main-label">
                    <h1>Вход</h1>
                </div>
            </div>
            <div class="row  mt-5">
                <div class="col-lg-4 col-md-6 col-sm-8 col-8 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-group">
                        <label for="login" class="label">Логин</label>
                        <input type="email" class="form-control form-control-lg" id="login" v-model="email"  placeholder="Введите логин">
                    </div>
                </div>
            </div>
             <div class="row  mt-3">
                 <div class="col-lg-4 col-md-6 col-sm-8 col-8 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-group">
                        <label for="pass" class="label">Пароль</label>
                        <input type="password" class="form-control form-control-lg" v-model="pass" id="pass" placeholder="Введите пароль">
                    </div>
                </div>
            </div>
            <div class="row mt-6">
                <div class="col-lg-2 col-md-3 col-sm-4 col-4 offset-lg-4 offset-md-3 offset-sm-2 offset-2">
                    <div class="form-check">
                       <div class="custom-control form-control-lg custom-checkbox">
                            <input type="checkbox" class="custom-control-input" id="customCheck1">
                            <label class="custom-control-label" for="customCheck1">Запомнить</label>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-3 col-sm-6 col-6">
                    <button type="submit" class="btn" @click="send"><span class="text-in-button">Войти</span></button>
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
 
Vue.use(VueAxios, axios)

export default {
    name: "login",
    data(){
        return{
            email: "",
            pass: ""
            
        }
    },
    methods: {
        send(){
            axios.post("http://127.0.0.1:5000/login",{
                email: this.email,
                pass: this.pass
            })
            .then((response) =>{
                if (response.data.status == "success"){
                    localStorage.setItem("access_tocken",response.data.access_tocken)
                    this.$router.push('/home')
                }
                else{
                    alert(response.data.status)
                    alert(response.data.errorMsg)
                }

            }).catch(() => {
                alert("пизда")
            })
        }   
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
            padding-top: 230px;
            background-size: 470px;
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
    }
</style>