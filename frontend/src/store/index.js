import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    isAuth : false,
    statusMessages : [],
    tocken : null
  },
  getters: {
    IS_AUTH : state => {
      return state.isAuth;
    },

    STATUS_MSG : state => {
      return state.statusMessages;
    }
  },
  mutations: {
    SET_AUTH : (state, payload) => {
      state.isAuth = payload;
    },
    
    SET_STASTUS_MSG : (state, payload) => {
      state.statusMessages = payload;
    },

    SET_TOCKEN : (state, payload) => {
      state.tocken = payload;
    }
  },
  actions: {
    
  },
});