<template>
  <div class="input-field">
    <label>{{ title }}</label>
    <input :type="inputType" ref="inputField" />
  </div>
</template>

<script>
export default {
  name: 'InputField',
  props: {
    title: String,
    inputType: String
  },
  methods: {
    getInputValue() {
      return this.$refs.inputField.value;
    }
  }
};
</script>

<style scoped>
.input-field {
  display: flex;
  flex-direction: column;
  margin: 15px 0;
  font-family: Arial, sans-serif;
}

label {
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 5px;
  color: #333;
}

input {
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
  transition: border 0.3s ease, box-shadow 0.3s ease;
}

input:focus {
  border-color: #007bff;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.3);
}

input:hover {
  border-color: #0056b3;
}
</style>
