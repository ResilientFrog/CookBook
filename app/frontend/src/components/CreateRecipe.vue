<script>
import { ref } from 'vue';
import RecipeItem from './RecipeItem.vue';

export default {
  components: {
    RecipeItem,
  },
  setup() {
    const recipe = ref({
      name: '',
      description: '',
      calories: null,
      num_of_servings: null,
      ingredients: [],
    });

    const message = ref('');

    const addIngredient = () => {
      recipe.value.ingredients.push('');
    };

    const removeIngredient = (index) => {
      recipe.value.ingredients.splice(index, 1);
    };

    const submitRecipe = async () => {
      if (!recipe.value.name || !recipe.value.description || !recipe.value.ingredients.length) {
        alert('Please fill in all required fields before submitting.');
        return;
      }

      try {
        const response = await fetch('../../src/server/api/createRecipe', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(recipe.value),
        });

        if (response.status === 'success') {
          message.value = response.message;
          alert(message.value);
          resetForm();
        } else {
          message.value = response.message;
          alert(message.value);
        }
      } catch (error) {
        console.error('Error:', error);
        message.value = 'Failed to connect to server!';
        alert(message.value);
      }
    };

    const resetForm = () => {
      recipe.value = {
        name: '',
        description: '',
        calories: null,
        num_of_servings: null,
        ingredients: [],
      };
    };

    return {
      recipe,
      addIngredient,
      removeIngredient,
      submitRecipe,
      message,
    };
  },
};
</script>

<template>
  <RecipeItem>
    <template #heading>Create Recipe</template>
    <div class="input-group">
      <label>Recipe Name:</label>
      <input type="text" v-model="recipe.name" placeholder="Enter recipe name" />
    </div>
  </RecipeItem>

  <RecipeItem>
    <div class="input-group">
      <label>Description:</label>
      <textarea v-model="recipe.description" placeholder="Enter description"></textarea>
    </div>
  </RecipeItem>

  <RecipeItem>
    <div class="input-group">
      <label>Calories:</label>
      <input type="number" v-model="recipe.calories" />
    </div>
  </RecipeItem>

  <RecipeItem>
    <div class="input-group">
      <label>Servings:</label>
      <input type="number" v-model="recipe.num_of_servings" />
    </div>
  </RecipeItem>

  <RecipeItem>
    <div class="input-group">
      <label>Ingredients:</label>
      <div v-for="(ingredient, index) in recipe.ingredients" :key="index" class="ingredient-item">
        <input type="text" v-model="recipe.ingredients[index]" placeholder="Enter ingredient" />
        <button @click="removeIngredient(index)">❌</button>
      </div>
      <button @click="addIngredient()">➕ Add Ingredient</button>
    </div>
  </RecipeItem>

  <RecipeItem>
    <button class="submit-button" @click="submitRecipe">✅ Submit Recipe</button>
  </RecipeItem>

  <p v-if="message" class="message">{{ message }}</p>
</template>

<style scoped>
.input-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input,
textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.ingredient-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.5rem;
}

.ingredient-item input {
  flex-grow: 1;
  margin-right: 0.5rem;
}

.submit-button {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #45a049;
}

.message {
  margin-top: 1rem;
  font-weight: bold;
  color: #4caf50;
}
</style>
