import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Card from '@/components/Card'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/card',
      name: 'Card',
      component: Card
    }
  ]
})
