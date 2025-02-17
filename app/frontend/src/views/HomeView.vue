<script>
import FindRecipe from "@/components/FindRecipe.vue";
import DisplayRecipe from "@/components/DisplayRecipe.vue"; // Import DisplayRecipe component

import { ref } from "vue";

export default {
  components: {
    FindRecipe,
    DisplayRecipe, // Register DisplayRecipe
  },
  setup() {
    const selectedRecipe = ref(null); // Store the selected recipe

    // Function to set the selected recipe from FindRecipe.vue
    const handleRecipeSelect = (recipe) => {
      selectedRecipe.value = recipe;
    };

    return {
      selectedRecipe,
      handleRecipeSelect,
    };
  },
};
</script>

<template>
  <div class="home-container">
    <h1>Welcome to the Recipe Finder</h1>
    
    <!-- FindRecipe handles search -->
    <FindRecipe @recipe-selected="handleRecipeSelect" />

    <!-- DisplayRecipe shows the selected recipe -->
    <DisplayRecipe v-if="selectedRecipe" :recipe="selectedRecipe" />
  </div>
</template>

<style scoped>
.home-container {
  text-align: center;
  padding: 20px;
}
</style>
