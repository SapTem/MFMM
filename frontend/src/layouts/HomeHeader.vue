<template>
    <div class="content">
        <div class="bg">
            <div class="container">
                <div class="row header">
                    <div class="col-xl-2 col-lg-3 col-md-3 col-sm-4 col-4">
                       <a href="#/home"><img src="../assets/LogoHome.png" class="logo"></a>
                    </div>
                    <div class="col-lg-3 col-5 col-sm-4 offset-3 offset-sm-4 offset-xl-7 offset-lg-6 d-flex justify-content-between align-items-center">
                        <a href="#"><img src="../assets/imgAdd.png" alt=""></a>
                        <a href="#"><img src="../assets/imgPurpose.png" alt=""></a>
                        <a href="#"><img src="../assets/imgExit.png" alt=""></a>            
                    </div>
                </div>
            </div>
        </div>
      <router-view></router-view>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.bg{
    background:rgba(215, 155, 216, 0.66);
}
.logo{
    position: absolute;
    height: 66px;
}
.header{
    height:59px;
}

</style>

