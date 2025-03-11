import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import { h } from 'vue'

const routes = [

  { path: '/CreateRecipe', 
    name: 'CreateRecipe', 
    component : () => import('@/views/CreateRecipeView.vue')
  },
  { path: '/',
    name: 'Home', 
    component: HomeView 
  },{
    //wild card: :id
    path: '/:id',
    name: 'single-project',
    props: true,
    component: HomeView 
  },
  {
    path: '/:catchAll(.*)*',
    name: 'NotFound',
    component : h('p',{style:'color: black;'},'404 Not Found')
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
