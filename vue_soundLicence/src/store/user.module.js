const state = {
    is_loggedIn : false,
    defaultUser :'Login',
    currentUser : '',
};
  
const mutations =  {
    replaceAccountName(state, name) {
      state.currentUser = name;
    },
    loggInUser(state)
    {
        state.is_loggedIn=true;
    }
  };
const actions ={
    async switchUser(context, name){
        await context.commit('replaceAccountName',name);
    },
    async loggIn(context, name){
        await context.commit('loggInUser');
        await context.commit('replaceAccountName',name);
    }
}
export default {
    state,
    actions,
    mutations
}