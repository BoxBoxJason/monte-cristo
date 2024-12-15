<template>
  <div class="inputs-holder">
    <div class="inputs-container">
      <div v-for="field in localFields" :key="field.id">
        <InputField :id="field.id" :type="field.type" :value="field.value" :label="field.label" @update="updateField" />
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
    graphName: {
      type: String,
      required: true,
    },
  },
  components: {
    InputField,
    LineChart,
  },
  data() {
    return {
      // Convert fields to an object indexed by id for easier access
      localFields: this.fields.reduce((acc, field) => {
        acc[field.id] = { ...field };
        return acc;
      }, {}),
      showGraph: false,
      graphData: {},
    };
  },
  methods: {
    updateField({ id, value }) {
      if (this.localFields[id]) {
        this.localFields[id].value = Number(value);
        this.$emit(
          'update:fields',
          Object.values(this.localFields) // Emit as an array to preserve original structure
        );
        this.updateGraphData();
      }
    },
    calculate() {
      // Convert the localFields object into query parameters
      const requestParams = Object.keys(this.localFields).reduce((acc, id) => {
        acc[id] = this.localFields[id].value;
        return acc;
      }, {});
      const queryString = new URLSearchParams(requestParams).toString(); // Create a query string

      // Use query string in the GET request
      fetch(`http://localhost:8000/graph/${this.graphName}?${queryString}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => {
          this.graphData = data;
          this.showGraph = true;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    updateGraphData() {
      this.graphData = Object.keys(this.localFields).reduce((acc, id) => {
        acc[id] = this.localFields[id].value;
        return acc;
      }, {});
    },
  },
  watch: {
    fields: {
      handler(newFields) {
        this.localFields = newFields.reduce((acc, field) => {
          acc[field.id] = { ...field };
          return acc;
        }, {});
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
