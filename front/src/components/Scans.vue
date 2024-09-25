<template>
  <div>
    <ul>
      <li
        v-for="scan in scans"
        :key="scan"
        @click="selectScan(scan.id)"
        class="scan-item"
      >
        <span>id: {{ scan.id }}</span>
        <span>start: {{ scan.start }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Scans",
  props: {
    scans: Array, // List of scan names passed as props
  },
  methods: {
    selectScan(scanId) {
      // Emit the selected scan to the parent
      this.$emit("scan-selected", scanId);
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

span {
  white-space: nowrap;
}

.scan-item {
  padding: 10px;
  cursor: pointer;
  margin-bottom: 5px;
  border: 1px solid #ddd;
  display: flex;
  flex-direction: column;

}

.scan-item:hover {
  background-color: #e6e6e6;
}
</style>
