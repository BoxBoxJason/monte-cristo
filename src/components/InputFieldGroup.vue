<template>
  <div class="input-field-group">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'InputFieldGroup',
  data() {
    return {
      inputFields: []
    };
  },
  provide() {
    return {
      registerInputField: this.registerInputField
    };
  },
  methods: {
    registerInputField(field) {
      if (field && !this.inputFields.includes(field)) {
        this.inputFields.push(field);
      }
    },
    getInputsValue() {
      // Collect input values from registered InputField components
      return this.inputFields.map(field => field.getInputValue());
    }
  }
};
</script>

<style scoped>
.input-field-group {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  max-width: 60%;
  margin: 0 auto;
}
</style>
