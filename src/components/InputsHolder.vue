<template>
  <div class="inputs-holder">
    <div class="inputs-container">
      <div v-for="(field, index) in localFields" :key="index">
        <InputField :type="field.type" :value="field.value" :label="field.label" @update="updateField(index, $event)" />
      </div>
    </div>
    <button @click="calculate" class="calculate-button">Calculate</button>
    <LineChart v-if="showGraph" :data="graphData" />
  </div>
</template>

<script>
import InputField from './InputField.vue';
import LineChart from './LineChart.vue';

export default {
  props: {
    fields: {
      type: Array,
      required: true,
    },
  },
  components: {
    InputField,
    LineChart,
  },
  data() {
    return {
      localFields: JSON.parse(JSON.stringify(this.fields)),
      showGraph: false,
      graphData: [],
    };
  },
  methods: {
    updateField(index, value) {
      this.localFields[index].value = Number(value);
      this.$emit('update:fields', this.localFields);
      this.updateGraphData();
    },
    calculate() {
      this.graphData = this.localFields.map((field) => field.value);
      this.showGraph = true;
    },
    updateGraphData() {
      if (this.showGraph) {
        this.graphData = this.localFields.map((field) => field.value);
      }
    },
  },
  watch: {
    fields: {
      handler(newFields) {
        this.localFields = JSON.parse(JSON.stringify(newFields));
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.inputs-holder {
  background: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

.inputs-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  /* Space between inputs */
  justify-content: flex-start;
}

.calculate-button {
  display: inline-block;
  background-color: #3498db;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  padding: 12px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, box-shadow 0.3s;
  margin-top: 20px;
}

.calculate-button:hover {
  background-color: #2980b9;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
}

.calculate-button:active {
  background-color: #1f618d;
}
</style>
