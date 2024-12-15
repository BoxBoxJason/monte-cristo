<template>
  <div ref="chart" style="width: 100%; height: 400px;"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
  watch: {
    data: {
      handler() {
        this.renderChart();
      },
      deep: true,
    },
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chart);
    this.renderChart();
  },
  methods: {
    renderChart() {
      this.chart.setOption(this.data);
    },
  },
};
</script>
