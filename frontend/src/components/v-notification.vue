
<template>
  <div class="v-notification">
    <transition-group name="slide-fade" class="block-list">
    <div 
      class="content-block "
      v-for="message in messages"
      :key="message.id"
      :class="message.status"
    >
      <span calss="textMsg">{{message.text}}</span>
      <i class="material-icons">{{message.status == "error" ? "error" : "info" }}</i>

    </div>
    </transition-group >

  </div>
</template>

<script>
  export default {
    name:'v-notification',
    props:{
      status:{
        type:String,
        default: function(){
          return "error"
        }
      },
      messages:{
        type: Array,
        default: function(){
          return []
        }
      }
    },
    methods:{
      deleteMessage: function(){
        let vm = this;
        if (this.messages.length){
          setTimeout(() => {
            vm.messages.splice(0, 1)
          },6000)
        }
      }
    },
    watch:{
      messages(){
        this.deleteMessage()
      } 
      
    },
    mounted(){
      this.deleteMessage();
    }
  }
  
</script>

<style>
  .v-notification{
    position: fixed;
    top:80px;
    right: 16px;
    z-index: 12;
  }
  .content-block{
      padding: 16px;
      border-radius: 4px;
      color: 000;
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 50px;
      margin-bottom: 16px;
  }
  .error{
    background: rgb(240, 68, 76);
  }
  .success{
    background: rgb(0, 161, 40);
  }
  
  .textMsg{
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
  }
  .block-list{
    display: flex;
    flex-direction: column-reverse;
  }
  

    .slide-fade-enter {
      transform: translateX(120px);
      opacity: 0;
    }
    .slide-fade-enter-active {
      transition: all .6s ease;
    }
    .slide-fade-enter-to {
      opacity: 1;
    }
    .slide-fade-leave {
      
      opacity: 1;
    }
    .slide-fade-leave-active {
      transition: all .6s ease
    }
    .slide-fade-leave-to {
      
      transform: translateX(120px);
      opacity: 0;
    }
    .slide-fade-move {
      transition: all .6s ease;
    }
</style>
