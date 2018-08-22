import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store/store'
import * as types from '@/store/types'

import Start from '@/components/Start'
import Exam from '@/components/Exam'
Vue.use(Router)

if(window.localStorage.getItem('token')){
    store.commit(types.TESTING, window.localStorage.getItem('token'))
}

const router = new Router({
  routes: [
    {
      path: '/start',
      name: 'Start',
      component: Start
    },
    {
      path: '/exam',
      name: 'Exam',
      component: Exam
    },
    {
      path: '*',
      redirect: '/start'
    }
  ]
});


router.beforeEach((to, from, next) => {
    if (to.matched.some(r => r.meta.requireAuth)) {
        if(store.state.token){
            next();
        }else{
            next({
                path: '/'
            });
        }
    } else{
        next();
    }
})
export default router;