import { createRouter, createWebHistory } from 'vue-router';
import CreateRecipeView from '@/views/CreateRecipeView.vue';
import HomeView from '@/views/HomeView.vue';

const routes = [

  { path: '/CreateRecipe', name: 'CreateRecipe', component: CreateRecipeView },
  { path: '/', name: 'Home', component: HomeView },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
