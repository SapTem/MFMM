import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import VueAxios from 'vue-axios';
import router from '../router/index'


Vue.use(Vuex);
Vue.use(VueAxios, axios);


export const store = new Vuex.Store({
  state: {
    isLoading : false,
    isAuth : false,
    notification: {
      statusMessages : [],
      status : null
    },
    tocken : null
  },
  getters: {
    IS_AUTH : state => {
      return state.isAuth;
    },

    STATUS_MSG : state => {
      return state.notification;
    },

    IS_LOADING : state => {
      return state.isLoading
    }
  },
  mutations: {
    SET_AUTH : (state, payload) => {
      state.isAuth = payload;
    },
    
    SET_STASTUS_MSG : (state, payload) => {
      state.notification.statusMessages = payload.msg;
      state.notification.status = payload.status;
    },

    SET_TOCKEN : (state, payload) => {
      state.tocken = payload;
    },

    SET_LOADING : (state, payload) => {
      state.isLoading = payload;
    },

  },
  actions: {
    REGISTR : async (context, payload) => {
      context.commit("SET_LOADING", true)
      
      await axios.post("http://127.0.0.1:5000/registr",payload)
      .then((response) =>{
        if (response.data.status == "success"){
          context.commit("SET_STASTUS_MSG", {
            msg : response.data.errorMsg, 
            status : response.data.status
          })
          setTimeout(() => router.push('/login'),2000)
        }
        else{
          context.commit("SET_STASTUS_MSG", {
            msg : response.data.errorMsg, 
            status : response.data.status
          })
        }
      })
      .catch(() => {
        context.commit("SET_STASTUS_MSG", {
          msg : ["Соединение с сервером не установлено"], 
          status : "error"
        })
      })

      context.commit("SET_LOADING", false)  
      
    }
  },
});