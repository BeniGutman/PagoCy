<template>
  <div class="parent-container">
    <div class="nav-list">
      <Scans :scans="scans" @scan-selected="updateSelectedScan" />
    </div>
    <div class="table-container">
      <Resources :resources="resources" />
    </div>
  </div>
</template>

<script>
import Scans from "./components/Scans.vue";
import Resources from "./components/Resources.vue";
import { ScanService, ResourceService } from "./common/api.service";

export default {
  name: 'App',
  components: {
    Scans,
    Resources,
  },
  async created() {
    this.scans = await ScanService.getAll();
  },
  data() {
    return {
      scans: [],
      resources: [],
      selectedScanId: null, // Track the selected scan
    };
  },
  methods: {
    async updateSelectedScan(scanId) {
      // Update the selected scan based on user's click
      if (scanId === this.selectedScanId) {
        return;
      }
      this.selectedScanId = scanId;
      this.resources = await ResourceService.getAllForScanId(scanId);
    },
  },
};
</script>

<style scoped>
.parent-container {
  display: flex;
  height: 100vh;
  width: 1300px;
}

.nav-list {
  width: 20%;
  padding: 20px;
}

.table-container {
  width: 80%;
  padding: 20px;
}
</style>
