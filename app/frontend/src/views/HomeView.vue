<script>
import FindRecipe from "@/components/FindRecipe.vue";
import DisplayRecipe from "@/components/DisplayRecipe.vue";
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

export default {
  components: {
    FindRecipe,
    DisplayRecipe,
  },
  setup() {
    const selectedRecipe = ref(null);
    const router = useRouter();

    // Function to set the selected recipe from FindRecipe.vue
    const handleRecipeSelect = (recipe) => {
      selectedRecipe.value = recipe;
      router.push(`/${recipe._id}`);
    }

    // Function to close pop up windouw and reseting URL
    const closePopUp = () => {
      selectedRecipe.value = null;
      router.push("/");
    }

    //TODO: open by changing url with recipe id
 

    return {
      selectedRecipe,
      handleRecipeSelect,
      closePopUp,
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
    <DisplayRecipe v-if="selectedRecipe" :recipe="selectedRecipe" @close="closePopUp"/>
  </div>
</template>

<style scoped>
.home-container {
  text-align: center;
  padding: 20px;
}
</style>