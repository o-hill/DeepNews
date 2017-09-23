import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    }
  ]
})
