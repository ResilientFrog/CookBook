<script>
import { ref } from "vue";

export default {
  emits: ["recipe-selected"], // Define event

  setup(_, { emit }) {
    const searchQuery = ref("");
    const searchResults = ref([]);
    const message = ref("");
    const loading = ref(false);

    // Function to fetch recipes
    const fetchRecipes = async () => {
      if (!searchQuery.value) {
        searchResults.value = [];
        return;
      }

      loading.value = true;
      try {
        const response = await fetch("http://127.0.0.1:8000/recipes", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) throw new Error("Error retrieving recipes!");

        const data = await response.json();
        searchResults.value = data.recipes.filter((recipe) =>
          recipe.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        );

        message.value = searchResults.value.length ? "" : "No recipes found!";
      } catch (error) {
        console.error("Error:", error);
        message.value = "Failed to connect to the server!";
      } finally {
        loading.value = false;
      }
    };

    // Emit event when a recipe is selected
    const selectRecipe = (recipe) => {
      emit("recipe-selected", recipe); // Send selected recipe to HomeView
    };

    return {
      searchQuery,
      searchResults,
      message,
      loading,
      fetchRecipes,
      selectRecipe,
    };
  },
};
</script>

<template>
  <div class="search-container">
    <label>Search Recipes:</label>
    <input type="text" v-model="searchQuery" @input="fetchRecipes" />

    <p v-if="loading">Loading...</p>
    <ul v-if="searchResults.length">
      <li v-for="(recipe, index) in searchResults" :key="index" @click="selectRecipe(recipe)">
        {{ recipe.name }}
      </li>
    </ul>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

