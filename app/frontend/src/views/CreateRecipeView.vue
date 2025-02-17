<script>
import CreateRecipe from '@/components/CreateRecipe.vue'; // If `RecipeItem` is a reusable component

export default {
  components: {
    CreateRecipe,
  },
};
</script>

<template>
  <div>
    <h1>Create a New Recipe</h1>
    <CreateRecipe />
  </div>
</template>
