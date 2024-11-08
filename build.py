# 本代码由AI生成

# Python script to generate `GeneratedButtons.vue` file

# Define a set of button text and corresponding links
data = {
    "Game 1": "https://game1.com",
    "Movie 1": "https://movie1.com",
    "Game 2": "https://game2.com",
    "Movie 2": "https://movie2.com",
    # You can add more game or movie names as needed...
}

# Generate the content of the Vue component file
vue_component_content = """
<template>
  <div class="app-container">
    <div class="buttons-container">
      <button
        v-for="(link, text) in links"
        :key="text"
        @click="goToLink(link)"
        class="button"
      >
        {{ text }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: {
"""

# Dynamically add each button text and link to the `links` object
for text, link in data.items():
    vue_component_content += f'        "{text}": "{link}",\n'

# End the Vue instance and add the click and navigation method
vue_component_content += """
      }
    };
  },
  methods: {
    goToLink(link) {
      window.location.href = link;
    }
  }
};
</script>

<style scoped>
/* Center the entire page */
.app-container {
  position: relative;
  overflow: hidden;
  background-color: #f5e8e4; /* Light beige/pink background */
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px; /* Add padding to avoid button overflow on hover */
  box-sizing: border-box;
}

/* Button container styles */
.buttons-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 50px 0;
}

/* Button styles */
.button {
  padding: 15px 25px;
  font-size: 18px;
  cursor: pointer;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 12px;
  text-transform: uppercase;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s, transform 0.2s;
}

/* Hover effect for buttons */
.button:hover {
  background-color: #218838;
  transform: scale(1.03); /* Control hover scale to avoid overflow */
}
</style>
"""

# Write the generated content to `GeneratedButtons.vue`
output_file_path = "vue-project/src/components/GeneratedButtons.vue"
with open(output_file_path, "w") as file:
    file.write(vue_component_content)

print(f"Vue component file generated: {output_file_path}")