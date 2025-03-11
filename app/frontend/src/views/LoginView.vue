<template>
    <div>
        <LoginItem>
            <div class="input-group">
            <label>Username:</label>
            <textarea v-model="credentials.username" placeholder="Enter username"></textarea>
            </div>
        </LoginItem>

        <LoginItem>
            <div class="input-group">
            <label>Password:</label>
            <<textarea v-model="credentials.password" placeholder="Enter password"></textarea>
            </div>
        </LoginItem>
        <LoginItem>
            <button class="submit-button" @click="submitLogin">Submit</button>
        </LoginItem>
    </div>
</template>

<script>
import LoginItem from '/components/ComponentItem.vue'
import { ref } from 'vue';
export default {
    components: {
        LoginItem,
  },
    setup () {
        const credentials = ref({
            username: '',
            password: ''
            })
        const message = ref('');   

        const submitLogin = async () => {
            if (!recipe.value.username || !recipe.value.password) {
                alert('Please fill in all required fields before submitting.');
                return;
            }
            
            try {
                const response = await fetch(import.meta.env.VITE_API_BASE_URL+"/login", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    
                    body: JSON.stringify(recipe.value),
                });       
                if (response.status == 200) {
                    message.value = response.statusText;
                    alert(message.value );
                    resetForm();
                }
                else {
                    message.value = response.statusText;
                    alert(message.value);
                }
            }
            catch (error) {
                console.error('Error:', error);
                message.value = 'Failed to connect to server!';
                alert(message.value);
            }
        };

        return {credentials,message,submitLogin}
    }
}
</script>

<style scoped>
.input-group {
  margin-bottom: 1rem;
}
.message {
  margin-top: 1rem;
  font-weight: bold;
  color: #4caf50;
}
.submit-button {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>