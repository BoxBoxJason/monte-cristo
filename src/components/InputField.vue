<template>
  <div class="input-field">
    <label v-if="label" :for="id">{{ label }}</label>
    <input
      :type="type"
      :value="value"
      :id="id"
      @input="handleInput"
    />
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    value: {
      type: [String, Number, Boolean],
      default: '',
    },
  },
  methods: {
    handleInput(event) {
      this.$emit('update', { id: this.id, value: event.target.value });
    },
  },
};
</script>

<style scoped>
.input-field {
  display: flex;
  flex-direction: column;
  width: 150px;
  font-family: 'Roboto', sans-serif;
}

.input-field label {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 5px;
  color: #2c3e50;
}

.input-field input {
  font-size: 14px;
  padding: 8px;
  border: 1px solid #dcdcdc;
  border-radius: 5px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.input-field input:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
}
</style>
