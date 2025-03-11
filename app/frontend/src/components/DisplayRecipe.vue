<script>
export default {
  props: {
    recipe: Object, // Receives the selected recipe
  },
  emits: ["close"],
};
</script>

<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>{{ recipe.name }}</h2>
      <p><strong>Ingredients:</strong></p>
      <ul>
        <li v-for="(ingredient, index) in recipe.ingredients" :key="index">
          {{ ingredient }}
        </li>
      </ul>
      <p><strong>Instructions:</strong></p>
      <p>{{ recipe.instructions }}</p>
    </div>
  </div>
</template>

<style scoped>

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* Dark semi-transparent overlay */
  display: flex;
  justify-content: center;
  align-items: center;
}
/*pop up window*/
.modal-content {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40vw;
  height: 80vh;
  background: white;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 2px 2px 2px 2px rgba(0, 0, 0, 0.5);
}
</style>
