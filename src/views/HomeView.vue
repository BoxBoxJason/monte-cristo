<template>
  <div class="home">
    <InputFieldGroup ref="inputGroup">
      <InputField title="First input" input-type="number" />
      <InputField title="Second input" input-type="number" />
      <InputField title="Third input" input-type="number" />
      <InputField title="Fourth input" input-type="number" />
      <InputField title="Fifth input" input-type="number" />
      <InputField title="Sixth input" input-type="number" />
    </InputFieldGroup>

    <button class="submit-inputs" @click="handleCompute">Compute 🔥</button>

    <!-- Render the ECharts line chart -->
    <div v-if="isChartVisible" class="mock-graph">
      <v-chart :option="chartOptions" autoresize />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import InputField from '@/components/InputField.vue';
import InputFieldGroup from '@/components/InputFieldGroup.vue';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { LineChart } from 'echarts/charts';
import { GridComponent, TooltipComponent, TitleComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';

use([
  CanvasRenderer,
  LineChart,
  GridComponent,
  TooltipComponent,
  TitleComponent,
  LegendComponent
]);

export default defineComponent({
  name: 'HomeView',
  components: {
    InputField,
    InputFieldGroup,
    VChart // Register the ECharts component
  },
  data() {
    return {
      isChartVisible: false,
      chartOptions: {
        title: {
          text: 'Mock Data Line Chart'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['Mock Data']
        },
        xAxis: {
          type: 'category',
          data: ['January', 'February', 'March', 'April', 'May']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Mock Data',
            type: 'line',
            data: [10, 5, 30, 25, 45]
          }
        ]
      }
    };
  },
  methods: {
    handleCompute() {
      this.isChartVisible = true;
    }
  }
});
</script>

<style scoped>
.submit-inputs {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-inputs:hover {
  background-color: #2c3e50;
}

.mock-graph {
  margin: 20px auto 0;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 400px;
  max-width: min(800px, 80%);
}
</style>
