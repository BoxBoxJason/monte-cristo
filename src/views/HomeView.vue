<template>
  <div class="home-view">
    <h1>Monte-Cristo</h1>
    <InputsHolder :fields="fields" @update:fields="handleFieldsUpdate" graph-name="pie_chart" />
  </div>
</template>

<script>
import InputsHolder from '@/components/InputsHolder.vue';
export default {
  components: {
    InputsHolder,
  },
  data() {
    return {
      fields: [
        { label: 'Input 1', type: 'number', value: 0, id: 'input1' },
        { label: 'Input 2', type: 'number', value: 0, id: 'input2' },
        { label: 'Input 3', type: 'number', value: 0, id: 'input3' },
        { label: 'Input 4', type: 'number', value: 0, id: 'input4' },
        { label: 'Input 5', type: 'number', value: 0, id: 'input5' },
        { label: 'Input 6', type: 'number', value: 0, id: 'input6' },
      ],
    };
  },
  methods: {
    handleFieldsUpdate(updatedFields) {
      console.log('Updated Fields:', updatedFields);
      this.fields = updatedFields;
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-bottom: 20px;
}
</style>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
  margin: 0 auto;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.home-view h1 {
  font-size: 24px;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 20px;
  font-family: 'Roboto', sans-serif;
}
</style>
