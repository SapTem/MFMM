<template>
    <div class="content">
        <div class="container">
            <div class="row">

                <div class="col-xl-6 col-lg-7  col-md-10 mx-auto offer-design">
                    <h1 >
                        Мои друзья - моя мативация.
                    </h1>
                    <p class="top-left-text">
                        Вдохновляйся результатими близких и бей личные рекорды вместе с нашим сервисом.
                    </p>
                    <a type="button" class="btn" href="#/login">
                        <span class="text-btn-top-left text-cenrer">Начать использовать</span>
                    </a>
                </div>

                <div class="col-xl-6 col-lg-5 ">
                    <h2 class="d-flex justify-content-center">Будь продуктивнее!</h2>
                    <img src="../assets/todo_list.png" class="img-fluid mx-auto d-block todo-list-img" alt="">
                </div>

                <div class="col-lg-6 col-md-8 col-sm-11 mx-auto m_b">
                    <h2>Используй время по максимуму!</h2>
                    <img src="../assets/graphic.png" class="img-fluid mx-auto d-block graphic-img" alt="">
                </div>

                <div class="col-lg-6 col-md-8 col-sm-10 mx-auto m_b">
                    <h2>Делись своими достижениями с друзьями!</h2>
                    <img src="../assets/friends.png" alt="" class="mg-fluid mx-auto d-block friend-img">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .content{
        background: linear-gradient(-45deg, rgba(175, 8, 108, 0.45),rgba(189, 28, 100, 0.47),rgba(223, 79, 79, 0.5));
        padding-bottom: 20px;
    }
    h1{
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        font-size: 32px;
        text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.38);
    }
    h2{
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        font-size: 24px;
        
    }
    .top-left-text{
        font-family: 'Montserrat', sans-serif;
        font-weight: medium;
        font-size: 24px;
        width: 400px;
        margin-top: 20px;
        padding-bottom: 13px;
        line-height:35px;
        display: inline-block;
    }
    .container{
        padding-top:70px;
    }
    .text-btn-top-left{
        font-family: "Monserrat", sans-serif;
        font-size: 32px;
        font-weight: bold;
        color: white; 
    }
    .btn{
        background: linear-gradient(-35deg, rgba(220, 62, 72, 1) , rgba(214, 69, 139, 1));
        width: 370px; 
        height: 85px;
        border-radius: 25px;
        box-shadow: 0px 4px 35px rgba(217, 65, 98, 0.54);  
    }
    .btn:hover{
        box-shadow: 2px 5px 60px rgba(217, 65, 98, 0.75);
        background: linear-gradient(-35deg, rgba(220, 62, 72, 0.9) , rgba(214, 69, 139, 0.9));
    }
    .btn:active{
        box-shadow: 0px 0px 35px rgba(217, 65, 98, 0.54);  
        background: linear-gradient(-35deg, rgba(220, 62, 72, 0.8) , rgba(214, 69, 139, 0.8));
    }
    .graphic-img{
        height:  300px;
    }
    .todo-list-img{
        height:  450px;
    }
    .friend-img{
       height:  300px;
    }
    a{
       margin:0;
       padding: 12px;
    }
    @media (max-width: 991px) {
        .offer-design{
            margin-bottom: 20px;
            text-align: center;
            margin-bottom: 100px;
        }   
        .m_b{
            margin-bottom: 50px;
        }
    }
</style>