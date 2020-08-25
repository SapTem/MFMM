<template>
<div>
    <div class="header">
        <div class="container ">

            <div class="row ">
                <div class="col-xl-2 col-lg-3 col-md-3 col-sm-4 col-4">
                    <a href="/"><img src="../assets/Logo.png" class="logo"></a>
                </div>

                <nav class="col-xl-5 col-lg-2 col-md-3 col-sm-4 col-4 navbar navbar-expand-xl justify-content-start">
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="fa fa-bars"></i>
                    </button>
                    <nav id="navbarNav" class="collapse navbar-collapse">
                        <ul class="menu d-flex justify-content-start navbar-nav">
                            <li class="menu__item" >
                                <a class="nav-link" href="">Возможности</a> 
                            </li>
                            <li class="menu__item">
                                <a class="nav-link" href="">Премиум</a>
                            </li>
                            <li class="menu__item">
                                <a class="nav-link" href="">Преимущества</a>
                            </li>
                            <li class="menu__item ">
                                <a class="nav-link" href="">Ресурсы</a> 
                            </li>
                        </ul>
                    </nav>
                </nav>

                <div class="col-xl-4 col-lg-3 col-md-4 col-sm-4 col-4 ml-auto">
                    <div class="login">
                        <ul class="menu d-flex justify-content-end">
                            <li class="menu__item">
                                <a class="nav-link" href="#/login">Вход</a> 
                            </li>
                            <li class="menu__item">
                                <a class="nav-link nav-link-important" href="#/registr">Регистрация</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>
    </div>
        <router-view/>
        <footer>
        </footer>
    
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .header{
        background-color:rgba(205, 157, 200, 0.54);     
    }
    .logo{
        position: absolute;
        height: 80px;
    }
    .reg{
        right:0;
        position: absolute;
    }
    li{
        display: block;
    }
    .nav-link{
        font-family: 'Montserrat', sans-serif;
        font-weight: normal;
        font-size: 18px;
        color: rgb(97, 95, 95);
    }
    .nav-link:hover{
        color:black
    }
    .nav-link-important{
        color: rgb(237, 52, 52);
    }
    .nav-link-important:hover{
        color: red;
    }
    .menu{
        margin-top:13px;
    }
    .navbar{
        margin: 0;
        padding: 0;
    }
    .navbar-nav{
        padding: 0;
        margin:0;
    }
    .fa-bars{
        font-size:30px;
        color:rgba(82, 61, 42, 1);
    }
    footer{
        height: 40px;
        position: sticky;
        background-color:rgba(205, 157, 200, 0.54);  
    }

    @media (max-width: 575px) {
        .nav-link{
            padding-right: 7px;
            font-size: 16px;
        }
    }
    
</style>