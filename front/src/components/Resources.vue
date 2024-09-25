<template>
    <div>
      <table class="table">
        <thead>
          <tr>
            <th>Scan</th>
            <th>URN</th>
            <th>Type</th>
            <th>Data</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="resource in resources" :key="resource.id">
            <td>{{ resource.scan_id }}</td>
            <td>{{ resource.urn }}</td>
            <td>{{ resource.type }}</td>
            <td>{{ resource.data }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Resources',
    props: {
      resources: Array, // Filtered resources passed as props
    },
  };
  </script>
  
  <style scoped>resources
  .table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .table th, .table td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  
  .table th {
    text-align: left;
  }
  </style>
  